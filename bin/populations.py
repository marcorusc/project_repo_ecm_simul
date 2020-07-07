# substrates  Tab

import os, math
from pathlib import Path
from ipywidgets import Layout, Label, Text, Checkbox, Button, BoundedIntText, HBox, VBox, Box, \
    FloatText, Dropdown, interactive
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle, Ellipse, Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.colors as mplc
from collections import deque
import numpy as np
import scipy.io
import xml.etree.ElementTree as ET  # https://docs.python.org/2/library/xml.etree.elementtree.html
import glob
import platform
import zipfile
from debug import debug_view 
import warnings

hublib_flag = True
if platform.system() != 'Windows':
    try:
#        print("Trying to import hublib.ui")
        from hublib.ui import Download
    except:
        hublib_flag = False
else:
    hublib_flag = False

#warnings.warn(message, mplDeprecation, stacklevel=1)
warnings.filterwarnings("ignore")

class PopulationsTab(object):

    def __init__(self):
        
        self.output_dir = '.'
        # self.output_dir = 'tmpdir'

        self.figsize_width_substrate = 15.0  # allow extra for colormap
        self.figsize_height_substrate = 8
        self.figsize_width_svg = 12.0
        self.figsize_height_svg = 12.0

        # self.fig = plt.figure(figsize=(7.2,6))  # this strange figsize results in a ~square contour plot

        self.first_time = True
        self.modulo = 1

        self.use_defaults = True

        self.svg_delta_t = 1
        self.substrate_delta_t = 1
        self.svg_frame = 1
        self.substrate_frame = 1

        self.customized_output_freq = False
        self.therapy_activation_time = 1000000
        self.max_svg_frame_pre_therapy = 1000000
        self.max_substrate_frame_pre_therapy = 1000000

        self.svg_xmin = 0

        # Probably don't want to hardwire these if we allow changing the domain size
        # self.svg_xrange = 2000
        # self.xmin = -1000.
        # self.xmax = 1000.
        # self.ymin = -1000.
        # self.ymax = 1000.
        # self.x_range = 2000.
        # self.y_range = 2000.

        self.show_nucleus = False
        self.show_edge = True

        # initial value
        self.field_index = 4
        # self.field_index = self.mcds_field.value + 4

        self.skip_cb = False

        # define dummy size of mesh (set in the tool's primary module)
        self.numx = 0
        self.numy = 0

        self.title_str = ''

        tab_height = '1200px'
        tab_height = '500px'
        constWidth = '180px'
        constWidth2 = '150px'
        tab_layout = Layout(width='900px',   # border='2px solid black',
                            height=tab_height, ) #overflow_y='scroll')

        max_frames = 0   
        # self.mcds_plot = interactive(self.plot_substrate, frame=(0, max_frames), continuous_update=False)  
        # self.i_plot = interactive(self.plot_plots, frame=(0, max_frames), continuous_update=False)  
        self.pop_plot = interactive(self.plot_celltypes, frame=(0,max_frames), continuous_update=False)
       
       
        self.max_frames = BoundedIntText(
            min=0, max=99999, value=max_frames,
            description='Max',
            layout=Layout(width='160px'),
#            layout=Layout(flex='1 1 auto', width='auto'),  #Layout(width='160px'),
        )
        self.max_frames.observe(self.update_max_frames)

       
        help_label = Label('select slider: drag or left/right arrows')
        
        self.tab = VBox([self.max_frames, self.pop_plot])
            # self.tab = VBox([controls_box, self.debug_str, self.i_plot, download_row])
        

    def update_max_frames(self,_b):
        self.pop_plot.children[0].max = self.max_frames.value
    
    def update(self, rdir=''):
        # with debug_view:
        #     print("substrates: update rdir=", rdir)        
        # print("substrates: update rdir=", rdir)        

        if rdir:
            self.output_dir = rdir
            
        all_files = sorted(glob.glob(os.path.join(self.output_dir, 'snapshot*.svg')))
        if len(all_files) > 0:
            last_file = all_files[-1]
            self.max_frames.value = int(last_file[-12:-4])  # assumes naming scheme: "snapshot%08d.svg"

    def plot_celltypes(self, frame=None):

        if frame <= 0:
            return
        self.title_str = ''

        
        # if (self.substrates_toggle.value):
        # if (True):
        self.pop_counts = {}
        
        self.fig = plt.figure(figsize=(self.figsize_width_substrate, self.figsize_height_substrate))

        
        for i in range(0, frame):
            fname = "output%08d_cells_physicell.mat" % i
            full_fname = os.path.join(self.output_dir, fname)
            
            if not os.path.isfile(full_fname):
                print("Once output files are generated, click the slider.")  # No:  output00000000_microenvironment0.mat
                return

            info_dict = {}
            scipy.io.loadmat(full_fname, info_dict)

            M = info_dict['cells'][5, :].astype(int)

            unique, counts = np.unique(M, return_counts=True)
            pop_size = dict(zip(unique, counts))
            
            for key, value in pop_size.items():
    
                if key not in self.pop_counts.keys():
                    if i == 0:
                        self.pop_counts[key] = [value]
                    else:
                        self.pop_counts[key] = [0]*i + [value]
                    
                else:
                    self.pop_counts[key].append(value)
                     
        config_file = "config.xml"
    
        cell_lines = {}
        if os.path.isfile(config_file):
            
            try:
                tree = ET.parse(config_file)
            except:
                print("Cannot parse",config_file, "- check it's XML syntax.")
                return

            root = tree.getroot()
            uep = root.find('.//cell_definitions')  # find unique entry point (uep) 
            for child in uep.findall('cell_definition'):
                cell_lines[int(child.attrib["ID"])] = child.attrib["name"]
                    # print(child.attrib['name'])

        ax = self.fig.add_subplot(111)
        t_data = []
        t_names = []
        for t_id, name in cell_lines.items():
            if t_id in self.pop_counts.keys():
                t_data.append(self.pop_counts[t_id])
                t_names.append(name)
                    # t_data = [value for value in self.pop_counts.values()]
        ax.stackplot(range(0, frame), t_data , labels=t_names)
        ax.legend(labels=t_names, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

