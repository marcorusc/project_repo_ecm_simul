 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

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
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='polarity_coefficient', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.polarity_coefficient = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='persistence', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.persistence = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='motility_amplitude_min', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.motility_amplitude_min = FloatText(
          value= 0.1 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='motility_amplitude_max', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.motility_amplitude_max = FloatText(
          value= 0.5 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='mode_motility', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.mode_motility = IntText(
          value= 1 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='contact_cell_ECM_threshold', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.contact_cell_ECM_threshold = FloatText(
          value= 0.5 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='contact_cell_cell_threshold', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.contact_cell_cell_threshold = FloatText(
          value= 0.9 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='homotypic_adhesion_min', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.homotypic_adhesion_min = FloatText(
          value= 0.2 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='homotypic_adhesion_max', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.homotypic_adhesion_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='heterotypic_adhesion_min', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.heterotypic_adhesion_min = FloatText(
          value= 0.2 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='heterotypic_adhesion_max', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.heterotypic_adhesion_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='cell_basement_membrane_repulsion', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.cell_basement_membrane_repulsion = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='cell_basement_membrane_adhesion', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.cell_basement_membrane_adhesion = FloatText(
          value=1.70577155519015,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='ecm_adhesion_min', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.ecm_adhesion_min = IntText(
          value= 1 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='ecm_adhesion_max', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.ecm_adhesion_max = IntText(
          value= 2 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='cell_ecm_repulsion', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.cell_ecm_repulsion = FloatText(
          value= 10.0 ,
          step=1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='ecm_degradation', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.ecm_degradation = IntText(
          value= 5 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='max_interaction_factor', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.max_interaction_factor = FloatText(
          value= 1.3 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='cell_radius', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.cell_radius = FloatText(
          value= 8.413 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='nucleus_radius', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.nucleus_radius = FloatText(
          value= 5.052 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.fluid_fraction = FloatText(
          value= 0.75 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='solid_nuclear', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.solid_nuclear = IntText(
          value= 135 ,
          step=10,
          style=style, layout=widget_layout)

        param_name24 = Button(description='solid_cytoplasmic', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.solid_cytoplasmic = IntText(
          value= 486 ,
          step=10,
          style=style, layout=widget_layout)

        param_name25 = Button(description='protein_threshold', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.protein_threshold = IntText(
          value= 1 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name26 = Button(description='bnd_file', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.bnd_file = Text(
          value='./config/boolean_network/CCM_mod4_1.bnd',
          style=style, layout=widget_layout)

        param_name27 = Button(description='cfg_file', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.cfg_file = Text(
          value='./config/boolean_network/CCM_mod4_1.cfg',
          style=style, layout=widget_layout)

        param_name28 = Button(description='init_cells_filename', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.init_cells_filename = Text(
          value='./config/init.txt',
          style=style, layout=widget_layout)

        param_name29 = Button(description='init_ecm_filename', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.init_ecm_filename = Text(
          value='./config/ecm.txt',
          style=style, layout=widget_layout)

        param_name30 = Button(description='tgfb_threshold', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.tgfb_threshold = FloatText(
          value=1.,
          step=0.1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='membrane_shape', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.membrane_shape = Text(
          value='sphere',
          style=style, layout=widget_layout)

        param_name32 = Button(description='membrane_length', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.membrane_length = FloatText(
          value= 10 ,
          step=1,
          style=style, layout=widget_layout)

        param_name33 = Button(description='node_to_visualize', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.node_to_visualize = Text(
          value='Cell_cell',
          style=style, layout=widget_layout)

        param_name34 = Button(description='color_function', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.color_function = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.polarity_coefficient, units_button2, desc_button2] 
        row3 = [param_name3, self.persistence, units_button3, desc_button3] 
        row4 = [param_name4, self.motility_amplitude_min, units_button4, desc_button4] 
        row5 = [param_name5, self.motility_amplitude_max, units_button5, desc_button5] 
        row6 = [param_name6, self.mode_motility, units_button6, desc_button6] 
        row7 = [param_name7, self.contact_cell_ECM_threshold, units_button7, desc_button7] 
        row8 = [param_name8, self.contact_cell_cell_threshold, units_button8, desc_button8] 
        row9 = [param_name9, self.homotypic_adhesion_min, units_button9, desc_button9] 
        row10 = [param_name10, self.homotypic_adhesion_max, units_button10, desc_button10] 
        row11 = [param_name11, self.heterotypic_adhesion_min, units_button11, desc_button11] 
        row12 = [param_name12, self.heterotypic_adhesion_max, units_button12, desc_button12] 
        row13 = [param_name13, self.cell_basement_membrane_repulsion, units_button13, desc_button13] 
        row14 = [param_name14, self.cell_basement_membrane_adhesion, units_button14, desc_button14] 
        row15 = [param_name15, self.ecm_adhesion_min, units_button15, desc_button15] 
        row16 = [param_name16, self.ecm_adhesion_max, units_button16, desc_button16] 
        row17 = [param_name17, self.cell_ecm_repulsion, units_button17, desc_button17] 
        row18 = [param_name18, self.ecm_degradation, units_button18, desc_button18] 
        row19 = [param_name19, self.max_interaction_factor, units_button19, desc_button19] 
        row20 = [param_name20, self.cell_radius, units_button20, desc_button20] 
        row21 = [param_name21, self.nucleus_radius, units_button21, desc_button21] 
        row22 = [param_name22, self.fluid_fraction, units_button22, desc_button22] 
        row23 = [param_name23, self.solid_nuclear, units_button23, desc_button23] 
        row24 = [param_name24, self.solid_cytoplasmic, units_button24, desc_button24] 
        row25 = [param_name25, self.protein_threshold, units_button25, desc_button25] 
        row26 = [param_name26, self.bnd_file, units_button26, desc_button26] 
        row27 = [param_name27, self.cfg_file, units_button27, desc_button27] 
        row28 = [param_name28, self.init_cells_filename, units_button28, desc_button28] 
        row29 = [param_name29, self.init_ecm_filename, units_button29, desc_button29] 
        row30 = [param_name30, self.tgfb_threshold, units_button30, desc_button30] 
        row31 = [param_name31, self.membrane_shape, units_button31, desc_button31] 
        row32 = [param_name32, self.membrane_length, units_button32, desc_button32] 
        row33 = [param_name33, self.node_to_visualize, units_button33, desc_button33] 
        row34 = [param_name34, self.color_function, units_button34, desc_button34] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.polarity_coefficient.value = float(uep.find('.//polarity_coefficient').text)
        self.persistence.value = float(uep.find('.//persistence').text)
        self.motility_amplitude_min.value = float(uep.find('.//motility_amplitude_min').text)
        self.motility_amplitude_max.value = float(uep.find('.//motility_amplitude_max').text)
        self.mode_motility.value = int(uep.find('.//mode_motility').text)
        self.contact_cell_ECM_threshold.value = float(uep.find('.//contact_cell_ECM_threshold').text)
        self.contact_cell_cell_threshold.value = float(uep.find('.//contact_cell_cell_threshold').text)
        self.homotypic_adhesion_min.value = float(uep.find('.//homotypic_adhesion_min').text)
        self.homotypic_adhesion_max.value = float(uep.find('.//homotypic_adhesion_max').text)
        self.heterotypic_adhesion_min.value = float(uep.find('.//heterotypic_adhesion_min').text)
        self.heterotypic_adhesion_max.value = float(uep.find('.//heterotypic_adhesion_max').text)
        self.cell_basement_membrane_repulsion.value = float(uep.find('.//cell_basement_membrane_repulsion').text)
        self.cell_basement_membrane_adhesion.value = float(uep.find('.//cell_basement_membrane_adhesion').text)
        self.ecm_adhesion_min.value = int(uep.find('.//ecm_adhesion_min').text)
        self.ecm_adhesion_max.value = int(uep.find('.//ecm_adhesion_max').text)
        self.cell_ecm_repulsion.value = float(uep.find('.//cell_ecm_repulsion').text)
        self.ecm_degradation.value = int(uep.find('.//ecm_degradation').text)
        self.max_interaction_factor.value = float(uep.find('.//max_interaction_factor').text)
        self.cell_radius.value = float(uep.find('.//cell_radius').text)
        self.nucleus_radius.value = float(uep.find('.//nucleus_radius').text)
        self.fluid_fraction.value = float(uep.find('.//fluid_fraction').text)
        self.solid_nuclear.value = int(uep.find('.//solid_nuclear').text)
        self.solid_cytoplasmic.value = int(uep.find('.//solid_cytoplasmic').text)
        self.protein_threshold.value = int(uep.find('.//protein_threshold').text)
        self.bnd_file.value = (uep.find('.//bnd_file').text)
        self.cfg_file.value = (uep.find('.//cfg_file').text)
        self.init_cells_filename.value = (uep.find('.//init_cells_filename').text)
        self.init_ecm_filename.value = (uep.find('.//init_ecm_filename').text)
        self.tgfb_threshold.value = float(uep.find('.//tgfb_threshold').text)
        self.membrane_shape.value = (uep.find('.//membrane_shape').text)
        self.membrane_length.value = float(uep.find('.//membrane_length').text)
        self.node_to_visualize.value = (uep.find('.//node_to_visualize').text)
        self.color_function.value = int(uep.find('.//color_function').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//polarity_coefficient').text = str(self.polarity_coefficient.value)
        uep.find('.//persistence').text = str(self.persistence.value)
        uep.find('.//motility_amplitude_min').text = str(self.motility_amplitude_min.value)
        uep.find('.//motility_amplitude_max').text = str(self.motility_amplitude_max.value)
        uep.find('.//mode_motility').text = str(self.mode_motility.value)
        uep.find('.//contact_cell_ECM_threshold').text = str(self.contact_cell_ECM_threshold.value)
        uep.find('.//contact_cell_cell_threshold').text = str(self.contact_cell_cell_threshold.value)
        uep.find('.//homotypic_adhesion_min').text = str(self.homotypic_adhesion_min.value)
        uep.find('.//homotypic_adhesion_max').text = str(self.homotypic_adhesion_max.value)
        uep.find('.//heterotypic_adhesion_min').text = str(self.heterotypic_adhesion_min.value)
        uep.find('.//heterotypic_adhesion_max').text = str(self.heterotypic_adhesion_max.value)
        uep.find('.//cell_basement_membrane_repulsion').text = str(self.cell_basement_membrane_repulsion.value)
        uep.find('.//cell_basement_membrane_adhesion').text = str(self.cell_basement_membrane_adhesion.value)
        uep.find('.//ecm_adhesion_min').text = str(self.ecm_adhesion_min.value)
        uep.find('.//ecm_adhesion_max').text = str(self.ecm_adhesion_max.value)
        uep.find('.//cell_ecm_repulsion').text = str(self.cell_ecm_repulsion.value)
        uep.find('.//ecm_degradation').text = str(self.ecm_degradation.value)
        uep.find('.//max_interaction_factor').text = str(self.max_interaction_factor.value)
        uep.find('.//cell_radius').text = str(self.cell_radius.value)
        uep.find('.//nucleus_radius').text = str(self.nucleus_radius.value)
        uep.find('.//fluid_fraction').text = str(self.fluid_fraction.value)
        uep.find('.//solid_nuclear').text = str(self.solid_nuclear.value)
        uep.find('.//solid_cytoplasmic').text = str(self.solid_cytoplasmic.value)
        uep.find('.//protein_threshold').text = str(self.protein_threshold.value)
        uep.find('.//bnd_file').text = str(self.bnd_file.value)
        uep.find('.//cfg_file').text = str(self.cfg_file.value)
        uep.find('.//init_cells_filename').text = str(self.init_cells_filename.value)
        uep.find('.//init_ecm_filename').text = str(self.init_ecm_filename.value)
        uep.find('.//tgfb_threshold').text = str(self.tgfb_threshold.value)
        uep.find('.//membrane_shape').text = str(self.membrane_shape.value)
        uep.find('.//membrane_length').text = str(self.membrane_length.value)
        uep.find('.//node_to_visualize').text = str(self.node_to_visualize.value)
        uep.find('.//color_function').text = str(self.color_function.value)
