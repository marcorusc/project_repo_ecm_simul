 
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

        param_name8 = Button(description='ECM_TGFbeta_ratio', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.ECM_TGFbeta_ratio = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='contact_cell_cell_threshold', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.contact_cell_cell_threshold = FloatText(
          value= 0.9 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='homotypic_adhesion_min', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.homotypic_adhesion_min = FloatText(
          value= 0.2 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name11 = Button(description='homotypic_adhesion_max', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.homotypic_adhesion_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='heterotypic_adhesion_min', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.heterotypic_adhesion_min = FloatText(
          value= 0.2 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name13 = Button(description='heterotypic_adhesion_max', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.heterotypic_adhesion_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='ecm_adhesion_min', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.ecm_adhesion_min = FloatText(
          value= 1 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='ecm_adhesion_max', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.ecm_adhesion_max = FloatText(
          value= 2 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='cell_ecm_repulsion', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.cell_ecm_repulsion = FloatText(
          value= 10.0 ,
          step=1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='ecm_degradation', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.ecm_degradation = FloatText(
          value= 0.5 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='cell_radius', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.cell_radius = FloatText(
          value= 8.413 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='max_interaction_factor', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.max_interaction_factor = FloatText(
          value= 1.3 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='config_radius', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.config_radius = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name21 = Button(description='node_to_visualize', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.node_to_visualize = Text(
          value='Cell_cell',
          style=style, layout=widget_layout)

        param_name22 = Button(description='color_function', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.color_function = IntText(
          value=1,
          step=0.1,
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

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.polarity_coefficient, units_button2, desc_button2] 
        row3 = [param_name3, self.persistence, units_button3, desc_button3] 
        row4 = [param_name4, self.motility_amplitude_min, units_button4, desc_button4] 
        row5 = [param_name5, self.motility_amplitude_max, units_button5, desc_button5] 
        row6 = [param_name6, self.mode_motility, units_button6, desc_button6] 
        row7 = [param_name7, self.contact_cell_ECM_threshold, units_button7, desc_button7] 
        row8 = [param_name8, self.ECM_TGFbeta_ratio, units_button8, desc_button8] 
        row9 = [param_name9, self.contact_cell_cell_threshold, units_button9, desc_button9] 
        row10 = [param_name10, self.homotypic_adhesion_min, units_button10, desc_button10] 
        row11 = [param_name11, self.homotypic_adhesion_max, units_button11, desc_button11] 
        row12 = [param_name12, self.heterotypic_adhesion_min, units_button12, desc_button12] 
        row13 = [param_name13, self.heterotypic_adhesion_max, units_button13, desc_button13] 
        row14 = [param_name14, self.ecm_adhesion_min, units_button14, desc_button14] 
        row15 = [param_name15, self.ecm_adhesion_max, units_button15, desc_button15] 
        row16 = [param_name16, self.cell_ecm_repulsion, units_button16, desc_button16] 
        row17 = [param_name17, self.ecm_degradation, units_button17, desc_button17] 
        row18 = [param_name18, self.cell_radius, units_button18, desc_button18] 
        row19 = [param_name19, self.max_interaction_factor, units_button19, desc_button19] 
        row20 = [param_name20, self.config_radius, units_button20, desc_button20] 
        row21 = [param_name21, self.node_to_visualize, units_button21, desc_button21] 
        row22 = [param_name22, self.color_function, units_button22, desc_button22] 

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
        self.ECM_TGFbeta_ratio.value = float(uep.find('.//ECM_TGFbeta_ratio').text)
        self.contact_cell_cell_threshold.value = float(uep.find('.//contact_cell_cell_threshold').text)
        self.homotypic_adhesion_min.value = float(uep.find('.//homotypic_adhesion_min').text)
        self.homotypic_adhesion_max.value = float(uep.find('.//homotypic_adhesion_max').text)
        self.heterotypic_adhesion_min.value = float(uep.find('.//heterotypic_adhesion_min').text)
        self.heterotypic_adhesion_max.value = float(uep.find('.//heterotypic_adhesion_max').text)
        self.ecm_adhesion_min.value = float(uep.find('.//ecm_adhesion_min').text)
        self.ecm_adhesion_max.value = float(uep.find('.//ecm_adhesion_max').text)
        self.cell_ecm_repulsion.value = float(uep.find('.//cell_ecm_repulsion').text)
        self.ecm_degradation.value = float(uep.find('.//ecm_degradation').text)
        self.cell_radius.value = float(uep.find('.//cell_radius').text)
        self.max_interaction_factor.value = float(uep.find('.//max_interaction_factor').text)
        self.config_radius.value = float(uep.find('.//config_radius').text)
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
        uep.find('.//ECM_TGFbeta_ratio').text = str(self.ECM_TGFbeta_ratio.value)
        uep.find('.//contact_cell_cell_threshold').text = str(self.contact_cell_cell_threshold.value)
        uep.find('.//homotypic_adhesion_min').text = str(self.homotypic_adhesion_min.value)
        uep.find('.//homotypic_adhesion_max').text = str(self.homotypic_adhesion_max.value)
        uep.find('.//heterotypic_adhesion_min').text = str(self.heterotypic_adhesion_min.value)
        uep.find('.//heterotypic_adhesion_max').text = str(self.heterotypic_adhesion_max.value)
        uep.find('.//ecm_adhesion_min').text = str(self.ecm_adhesion_min.value)
        uep.find('.//ecm_adhesion_max').text = str(self.ecm_adhesion_max.value)
        uep.find('.//cell_ecm_repulsion').text = str(self.cell_ecm_repulsion.value)
        uep.find('.//ecm_degradation').text = str(self.ecm_degradation.value)
        uep.find('.//cell_radius').text = str(self.cell_radius.value)
        uep.find('.//max_interaction_factor').text = str(self.max_interaction_factor.value)
        uep.find('.//config_radius').text = str(self.config_radius.value)
        uep.find('.//node_to_visualize').text = str(self.node_to_visualize.value)
        uep.find('.//color_function').text = str(self.color_function.value)
