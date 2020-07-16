 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
    
class CellTypesTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget_layout_long = {'width': '20%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.parent_name = Text(value='None',placeholder='Type something',description='Parent:',disabled=True)

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['default'] = 'default'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_type_parent_dict['default'] = 'None'


        self.cell_def_vboxes = []

        self.bnd_filenames = [None]*1

        self.cfg_filenames = [None]*1
        #  >>>>>>>>>>>>>>>>> <cell_definition> = default
        #  ------------------------- 
        div_row1 = Button(description='phenotype:cycle (model: advanced_Ki67_cycle_model; code=0)', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float0 = FloatText(value='1e30', step='100000000000000000000000000000', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float0, units_btn, ]
        box0 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float1 = FloatText(value='1e30', step='100000000000000000000000000000', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float1, units_btn, ]
        box1 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float2 = FloatText(value='0.006666667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float2, units_btn, ]
        box2 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float3 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float3, units_btn, ]
        box3 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float4 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float4, units_btn, ]
        box4 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row3 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float5 = FloatText(value='0.3', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float5, units_btn]
        box5 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float6 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float6, units_btn]
        box6 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float7 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float7, units_btn]
        box7 = Box(children=row, layout=box_layout)
        self.bool0 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool1 = Checkbox(description='use_2D', value=False,layout=name_button_layout)
        #  ------------------------- 
        div_row4 = Button(description='phenotype:intracellular (maboss)', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'
        bnd_filename = Button(description='bnd_filename', disabled=True, layout=name_button_layout)
        bnd_filename.style.button_color = 'lightgreen'
        self.bnd_filenames[0] = Text(value='../data/boolean_network/CCM_mod4_1.bnd', style=style, layout=widget_layout)
        row = [bnd_filename, self.bnd_filenames[0]]
        box8 = Box(children=row, layout=box_layout)
        cfg_filename = Button(description='cfg_filename', disabled=True, layout=name_button_layout)
        cfg_filename.style.button_color = 'tan'
        self.cfg_filenames[0] = Text(value='../data/boolean_network/CCM_mod4_1.cfg', style=style, layout=widget_layout)
        row = [cfg_filename, self.cfg_filenames[0]]
        box9 = Box(children=row, layout=box_layout)
        time_step = Button(description='time_step', disabled=True, layout=name_button_layout)
        time_step.style.button_color = 'lightgreen'
        self.float8 = FloatText(value='12', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [time_step, self.float8, units_btn]
        box10 = Box(children=row, layout=box_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width':'30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='Single', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float9 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        time_step = [name_btn, self.float9, units_btn, ]
        box11 = Box(children=time_step, layout=box_layout)

        intracellular_mutations = Button(description='mutations', disabled=True, layout={'width':'30%'})
        intracellular_mutations.style.button_color = '#ffde6b'
        name_btn = Button(description='GF', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float10 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [name_btn, self.float10, units_btn, ]
        box12 = Box(children=time_step, layout=box_layout)

        name_btn = Button(description='Glucose', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float11 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        time_step = [name_btn, self.float11, units_btn, ]
        box13 = Box(children=time_step, layout=box_layout)


#      ================== <custom_data>, if present ==================

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, box2, div_row2, death_model1,box3, death_model2,box4, div_row3, box5,box6,box7,self.bool0,self.bool1,div_row4, box8,box9,box10,intracellular_initial_values,box11, intracellular_mutations,box12, box13,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)



        row = [time_step, self.float8, units_btn]
        box13 = Box(children=time_step, layout=box_layout)


        self.tab = VBox([
          self.cell_type_parent_row, 
self.cell_def_vbox0,         ])
        self.display_cell_type_default()

    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            self.parent_name.value = self.cell_type_parent_dict[change['new']]
            idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected].layout.display = 'contents'   # vs. 'contents'


    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[0].layout.display = 'contents'


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (advanced_Ki67_cycle_model)
        self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float1.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float2.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        # ---------  death 
        self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        # ---------  motility 
        self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        # ---------  intracellular
        self.bnd_filenames[0].value = str(uep.find('.//cell_definition[1]//phenotype//intracellular//bnd_filename').text)
        self.cfg_filenames[0].value = str(uep.find('.//cell_definition[1]//phenotype//intracellular//cfg_filename').text)
        self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//intracellular//time_step').text)
        self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values//initial_value[1]').text)
        self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//intracellular//mutations//mutation[1]').text)
        self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//intracellular//mutations//mutation[2]').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (advanced_Ki67_cycle_model)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float0.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float1.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float2.value)
        # ---------  death 
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text = str(self.float3.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text = str(self.float4.value)
        # ---------  motility 
        uep.find('.//cell_definition[1]//phenotype//motility//speed').text = str(self.float5.value)
        uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text = str(self.float6.value)
        uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text = str(self.float7.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text = str(self.bool0.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text = str(self.bool1.value)
        # ---------  intracellular
        uep.find('.//cell_definition[1]//phenotype//intracellular//bnd_filename').text = str(self.bnd_filenames[0].value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//cfg_filename').text = str(self.cfg_filenames[0].value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//time_step').text = str(self.float8.value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values//initial_value[1]').text = str(self.float9.value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//mutations//mutation[1]').text = str(self.float10.value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//mutations//mutation[2]').text = str(self.float11.value)
