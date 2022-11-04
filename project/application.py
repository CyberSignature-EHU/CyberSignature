import pickle
from kivy.config import Config
from kivy.uix.popup import Popup

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '670')
Config.set('input', 'mouse', 'mouse, multitouch_on_demand')

from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

from kivy.graphics import *

import pandas as pd
import time
import math
import os.path
from datetime import datetime
import json
from sklearn.naive_bayes import GaussianNB

Window.clearcolor = (1, 1, 1, 1)


class CyberSignatureApp(App):

    def build(self):
        return GUI()


class GUI(Widget):
    # identifies test user
    user_ID = 0
    with open('false_data\\User0001.json', 'r') as file:
        raw_false = json.load(file)
    # list for storing keyboard events and mouse events
    user_details = {
        'ID': 'CDID0001',
        'Provider': 'Discover',
        'Name': 'Mrs Ellie Miller',
        'Card Number': '4422891459068728',
        'CVC': '646',
        'Expiry': '09/23'
    }

    data = {
        'details': {
            'ID': user_details['ID'],
            'Provider': user_details['Provider'],
            'Name': user_details['Name'],
            'Card Number': user_details['Card Number'],
            'CVC': user_details['CVC'],
            'Expiry': user_details['Expiry']
        },
        'true_data': {
            'test_1': {},
            'test_2': {},
            'test_3': {},
            'test_4': {},
            'test_5': {},
            'test_6': {},
            'test_7': {},
            'test_8': {},
            'test_9': {},
            'test_10': {}
        },
        'false_data': {
            'test_11': raw_false['false_data']['test_1'],
            'test_12': raw_false['false_data']['test_2'],
            'test_13': raw_false['false_data']['test_3'],
            'test_14': raw_false['false_data']['test_4'],
            'test_15': raw_false['false_data']['test_5'],
            'test_16': raw_false['false_data']['test_6'],
            'test_17': raw_false['false_data']['test_7'],
            'test_18': raw_false['false_data']['test_8'],
            'test_19': raw_false['false_data']['test_9'],
            'test_20': raw_false['false_data']['test_10']
        }
    }
    # declares classifier that will be used
    clf = GaussianNB()
    columns = ['dwell_max', 'dwell_avg', 'dwell_min', 'flight_max', 'flight_avg', 'flight_min', 'PR_max', 'PR_avg',
               'PR_min', 'PP_max', 'PP_avg', 'PP_min', 'RR_max', 'RR_avg', 'RR_min', 'UD_rate', 'UD_present',
               'UU_rate', 'UU_present', 'caps_rate', 'caps_present', 'error_rate', 'error_present',
               'in_bounds_rate', 'in_bounds_present', 'actual_traj_min', 'actual_traj_avg', 'actual_traj_max',
               'ideal_traj_min', 'ideal_traj_avg', 'ideal_traj_max', 'traj_diff_min', 'traj_diff_avg',
               'traj_diff_max']
    df = pd.DataFrame(columns=columns)

    test_count = 1
    # initiates the variables for storing user behaviour
    inbound = False
    focus = 'Null'
    box_checked = False
    box_value = None
    box_name = None

    visa_down = False
    mc_down = False
    disc_down = False
    jcb_down = False

    name_valid = False
    num_valid = False
    cvc_valid = False
    exp_m_valid = False
    exp_y_valid = False

    movement_ID = 1

    false_enter_count = 0

    previous_epoch = time.time()

    filename = ''

    def __init__(self, **kwargs):
        # INITIALISES NECESSARY VARIABLES
        self.existing_model = False
        self.k_events = []
        self.m_events = []
        self.temp_events = []
        super().__init__(**kwargs)
        # DECLARES ALL THE WIDGETS THAT WILL BE USED IN THE APPLICATION
        with self.canvas:
            Color(0, 0, 0, 1)
            Line(points=[50, 45, 50, 450], width=1)
            Line(points=[50, 450, 465, 450], width=1)
            Line(points=[465, 450, 465, 45], width=1)
            Line(points=[465, 45, 50, 45])
            self.line = Line(pos=200)
            self.line_colour = Color(1, 0, 0, 1)

        self.ehu_logo = Image(source='ehu_logo.png', pos=(580, 500), size=(200, 200))
        self.cs_logo = Image(source='cs_logo.png', pos=(50, 500), size=(200, 200))

        self.test_count_text = 'Training data entered: ' + str(self.test_count) + '/10'
        self.test_count_label = Label(text=self.test_count_text, pos=(160, 450), size=(30, 30), font_size=20,
                                      color=[0, 0, 0, 1])

        self.card_type_label = Label(text='Card Type:', pos=(70, 370), font_size=18, color=[0, 0, 0, .5])
        self.visa_label = Label(text='Visa', pos=(75, 380), size=(30, 30), font_size=15, color=[0, 0, 0, .5])
        self.visa_checkbox = CheckBox(group='card_type', pos=(40, 325), color=(0, 0, 0, 1))
        self.mc_label = Label(text='MasterCard', pos=(185, 380), size=(30, 30), font_size=15, color=[0, 0, 0, .5])
        self.mc_checkbox = CheckBox(group='card_type', pos=(150, 325), color=(0, 0, 0, 1))
        self.disc_label = Label(text='Discover', pos=(295, 380), size=(30, 30), font_size=15, color=[0, 0, 0, .5])
        self.disc_checkbox = CheckBox(group='card_type', pos=(260, 325), color=(0, 0, 0, 1))
        self.jcb_label = Label(text='JCB', pos=(405, 380), size=(30, 30), font_size=15, color=[0, 0, 0, .5])
        self.jcb_checkbox = CheckBox(group='card_type', pos=(370, 325), color=(0, 0, 0, 1))

        self.name_label = Label(text='Name:', pos=(55, 275), font_size=18,
                                color=[0, 0, 0, .5])
        self.name_input = TextInput(size=(360, 35), pos=(75, 275), font_size=20, write_tab=False, multiline=False)

        self.num_label = Label(text='Number:', pos=(62, 175), font_size=18,
                               color=[0, 0, 0, .5])
        self.num_input = TextInput(size=(360, 35), pos=(75, 175), font_size=20, write_tab=False, multiline=False,
                                   input_filter='int')

        self.cvc_label = Label(text='CVC:', pos=(47, 75), font_size=18, color=[0, 0, 0, .5])
        self.cvc_input = TextInput(size=(47, 35), pos=(75, 75), font_size=20, write_tab=False, multiline=False,
                                   input_filter='int')

        self.exp_label = Label(text='Expiry:', pos=(168, 75), font_size=18, color=[0, 0, 0, .5])
        self.exp_m_input = TextInput(size=(35, 35), pos=(190, 75), font_size=20, write_tab=False, multiline=False,
                                     input_filter='int')
        self.exp_y_input = TextInput(size=(35, 35), pos=(230, 75), font_size=20, write_tab=False, multiline=False,
                                     input_filter='int')

        self.enter_button = Button(text='Enter', size=(100, 50), pos=(335, 70))
        self.reset_button = Button(text='Reset', size=(100, 50), pos=(500, 50), disabled=False)
        self.delete_button = Button(text='Delete Model', size=(100, 50), pos=(610, 50), disabled=True)
        self.save_button = Button(text='Save Model', size=(100, 50), pos=(720, 50), disabled=True, halign='center')

        self.error_label = Label(text="[i]* Please enter valid details[/i]", markup=True, pos=(300, 8),
                                 font_size=18,
                                 color=[1, 0, 0, 0])

        self.instructions_label = Label(text='[u][b]INSTRUCTIONS[/b][/u]'
                                             '\nFill in the form with the card'
                                             '\ndetails given above 10 times to'
                                             '\ntrain the model.'
                                             '\nOnce the model has been trained,'
                                             '\nyou can test the model, and save'
                                             '\nit as a .SAV file.',
                                        pos=(585, 160), font_size=18, markup=True, color=[0, 0, 0, 1])

        self.given_card = 'Card Type: ' + GUI.user_details['Provider']
        self.given_name = 'Name: ' + GUI.user_details['Name']
        self.given_num = str(GUI.user_details['Card Number'])
        self.given_num = 'Number: ' + self.given_num[:4] + '-' + self.given_num[4:8] + '-' + self.given_num[8:12] + '-' \
                         + self.given_num[12:]
        self.given_cvc = 'CVC: ' + str(GUI.user_details['CVC'])
        self.given_exp = 'Expiry: ' + str(GUI.user_details['Expiry'])
        self.given_details = Label(text='[u][b]CARD DETAILS[/b][/u]'
                                        '\n' + self.given_card +
                                        '\n' + self.given_name +
                                        '\n' + self.given_num +
                                        '\n' + self.given_cvc +
                                        '\n' + self.given_exp,
                                   pos=(610, 370), size=(30, 30), font_size=18, markup=True, color=[0, 0, 0, 1])

        # CHECKS IF THERE IS A SAVED MODEL PRESENT, AND LOADS MODEL IF THERE IS ONE
        if os.path.isfile('saved_models\\test_model.sav'):
            self.test_count_text = 'Enter data to test existing model'
            self.test_count_label.text = self.test_count_text
            self.test_count_label.pos = (180, 450)
            self.clf = pickle.load(open('saved_models\\test_model.sav', 'rb'))
            self.delete_button.disabled = False
            self.existing_model = True
            self.name_input.text = ''
            self.num_input.text = ''
            self.cvc_input.text = ''
            self.exp_m_input.text = ''
            self.exp_y_input.text = ''
            self.visa_checkbox.active = False
            self.mc_checkbox.active = False
            self.disc_checkbox.active = False
            self.jcb_checkbox.active = False
            self.box_value = None
            self.box_name = None
            self.visa_label.color = [0, 0, 0, .5]
            self.visa_down = False
            self.mc_label.color = [0, 0, 0, .5]
            self.mc_down = False
            self.disc_label.color = [0, 0, 0, .5]
            self.disc_down = False
            self.jcb_label.color = [0, 0, 0, .5]
            self.jcb_down = False
            self.error_label.color = [0, 0, 0, 0]
            self.movement_ID = 1
            self.previous_epoch = time.time()
            self.test_count = 11

        # ADDS THE DECLARED WIDGETS ONTO THE APPLICATION WINDOW
        GUI.add_widget(self, self.cs_logo)
        GUI.add_widget(self, self.ehu_logo)

        GUI.add_widget(self, self.test_count_label)

        GUI.add_widget(self, self.card_type_label)
        GUI.add_widget(self, self.visa_label)
        GUI.add_widget(self, self.visa_checkbox)
        GUI.add_widget(self, self.mc_label)
        GUI.add_widget(self, self.mc_checkbox)
        GUI.add_widget(self, self.disc_label)
        GUI.add_widget(self, self.disc_checkbox)
        GUI.add_widget(self, self.jcb_label)
        GUI.add_widget(self, self.jcb_checkbox)
        GUI.add_widget(self, self.name_label)
        GUI.add_widget(self, self.name_input)

        GUI.add_widget(self, self.num_label)
        GUI.add_widget(self, self.num_input)

        GUI.add_widget(self, self.cvc_label)
        GUI.add_widget(self, self.cvc_input)

        GUI.add_widget(self, self.exp_label)
        GUI.add_widget(self, self.exp_m_input)
        GUI.add_widget(self, self.exp_y_input)

        GUI.add_widget(self, self.enter_button)
        GUI.add_widget(self, self.save_button)
        GUI.add_widget(self, self.delete_button)
        GUI.add_widget(self, self.reset_button)
        GUI.add_widget(self, self.error_label)

        GUI.add_widget(self, self.instructions_label)
        GUI.add_widget(self, self.given_details)

        # ATTACHES WIDGETS TO RELEVANT FUNCTIONS
        self.name_input.bind(text=self.on_text_name)
        self.num_input.bind(text=self.on_text_num)
        self.cvc_input.bind(text=self.on_text_cvc)
        self.exp_m_input.bind(text=self.on_text_exp_m)
        self.exp_y_input.bind(text=self.on_text_exp_y)

        self.name_input.bind(focus=self.on_focus_name)
        self.num_input.bind(focus=self.on_focus_num)
        self.cvc_input.bind(focus=self.on_focus_cvc)
        self.exp_m_input.bind(focus=self.on_focus_exp_m)
        self.exp_y_input.bind(focus=self.on_focus_exp_y)

        self.enter_button.bind(on_press=self.enter_callback)
        self.reset_button.bind(on_press=self.reset_callback)
        self.save_button.bind(on_press=self.save_callback)
        self.delete_button.bind(on_press=self.delete_callback)

        self.visa_checkbox.bind(on_press=self.on_checkbox)
        self.visa_checkbox.bind(on_press=self.on_visa)
        self.mc_checkbox.bind(on_press=self.on_checkbox)
        self.mc_checkbox.bind(on_press=self.on_mastercard)
        self.disc_checkbox.bind(on_press=self.on_checkbox)
        self.disc_checkbox.bind(on_press=self.on_discover)
        self.jcb_checkbox.bind(on_press=self.on_checkbox)
        self.jcb_checkbox.bind(on_press=self.on_jcb)

        self.popup_false = Popup(title='Negative Authentication',
                                 content=Label(text='Model classifies as different user.'),
                                 size=(300, 150), pos=(100, 100), size_hint=(None, None))
        self.popup_true = Popup(title='Positive Authentication', content=Label(text='Model classifies as same user.'),
                                size=(300, 150), pos=(100, 100), size_hint=(None, None))

        self.popup_training = Popup(title='Model Trained', content=Label(text='Model successfully trained.'
                                                                              '\nEnter further details to test model.'),
                                    size=(300, 150), pos=(100, 100), size_hint=(None, None))

        self.popup_save = Popup(title='Saved Model', content=Label(text='Model saved as:'
                                                                        '\n"' + self.filename + '"'),
                                size=(300, 150), pos=(100, 100), size_hint=(None, None))

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_key_down)
        self._keyboard.bind(on_key_up=self.on_key_up)

        Window.bind(mouse_pos=self.mouse_pos)
        Window.bind(on_touch_down=self.on_press)
        Window.bind(on_touch_up=self.on_release)

    # KEYBOARD FUNCTIONS
    def on_focus_name(self, value, instance):  # When name textbox is in focus
        if instance:
            GUI.focus = 'Name'
        else:
            GUI.focus = 'Null'

        if GUI.name_valid:
            GUI.inbound = False
        else:
            GUI.inbound = True

    def on_focus_num(self, value, instance):  # When the number text box is in focus
        if instance:
            GUI.focus = 'Card No'
        else:
            GUI.focus = 'Null'

        if GUI.num_valid:
            GUI.inbound = False
        else:
            GUI.inbound = True

    def on_focus_cvc(self, value, instance):  # When the cvc textbox is in focus
        if instance:
            GUI.focus = 'CVC'
        else:
            GUI.focus = 'Null'

        if GUI.cvc_valid:
            GUI.inbound = False
        else:
            GUI.inbound = True

    def on_focus_exp_m(self, value, instance):  # When the expiry month text box is in focus
        if instance:
            GUI.focus = 'Exp m'
        else:
            GUI.focus = 'Null'

        if GUI.exp_m_valid:
            GUI.inbound = False
        else:
            GUI.inbound = True

    def on_focus_exp_y(self, value, instance):  # When the expiry year textbox is in focus
        if instance:
            GUI.focus = 'Exp y'
        else:
            GUI.focus = 'Null'

        if GUI.exp_y_valid:
            GUI.inbound = False
        else:
            GUI.inbound = True

    def on_checkbox(self, value):  # When any checkbox for the vard type is checked
        if not self.box_checked:
            self.box_value = value
            self.box_checked = True
            self.visa_label.color = [0, 0, 0, 1]
            self.mc_label.color = [0, 0, 0, 1]
            self.disc_label.color = [0, 0, 0, 1]
            self.jcb_label.color = [0, 0, 0, 1]
            self.card_type_label.color = [0, 0, 0, 1]
        elif self.box_checked and self.box_value == value:
            self.box_checked = False
            self.box_value = None
            self.visa_label.color = [0, 0, 0, .5]
            self.mc_label.color = [0, 0, 0, .5]
            self.disc_label.color = [0, 0, 0, .5]
            self.jcb_label.color = [0, 0, 0, .5]
            self.card_type_label.color = [0, 0, 0, .5]
        elif self.box_checked and self.box_value != value:
            self.box_value = value
            self.box_checked = True
            self.visa_label.color = [0, 0, 0, 1]
            self.mc_label.color = [0, 0, 0, 1]
            self.disc_label.color = [0, 0, 0, 1]
            self.jcb_label.color = [0, 0, 0, 1]
            self.card_type_label.color = [0, 0, 0, 1]

    def on_visa(self, value):  # When the Visa checkbox is checked
        if not self.visa_down:
            self.box_name = 'Visa'
            self.visa_down = True
            # print(self.box_name)
        else:
            self.box_name = None
            self.visa_down = False
            # print(self.box_name)

    def on_mastercard(self, value):  # When the Mastercard checkbox is checked
        if not self.mc_down:
            self.box_name = 'MasterCard'
            self.mc_down = True
            # print(self.box_name)
        else:
            self.box_name = None
            self.mc_down = False
            # print(self.box_name)

    def on_discover(self, value):  # When the Discover checkbox is checked
        if not self.disc_down:
            self.box_name = 'Discover'
            self.disc_down = True
            # print(self.box_name)
        else:
            self.box_name = None
            self.disc_down = False
            # print(self.box_name)

    def on_jcb(self, value):  # When the JCB checkbox is checked
        if not self.jcb_down:
            self.box_name = 'JCB'
            self.jcb_down = True
            # print(self.box_name)
        else:
            self.box_name = None
            self.jcb_down = False
            # print(self.box_name)

    def on_text_name(self, instance, value):  # When a character is typed in the name text box
        if 4 < len(value) < 22:
            GUI.name_valid = True
            self.name_label.color = [0, 0, 0, 1]
            GUI.inbound = True
        elif len(value) > 22:
            self.name_input.text = value[:len(value) - 1]
            GUI.inbound = False
        else:
            GUI.name_valid = False
            self.name_label.color = [0, 0, 0, .5]

    def on_text_num(self, instance, value):  # When a character is typed in the number text box
        if len(value) == 16:
            GUI.inbound = False
            GUI.num_valid = True
            self.num_label.color = [0, 0, 0, 1]
        elif len(value) > 16:
            GUI.inbound = False
            self.num_input.text = value[:len(value) - 1]
        else:
            GUI.inbound = True
            GUI.num_valid = False
            self.num_label.color = [0, 0, 0, .5]

    def on_text_cvc(self, instance, value):  # When a character is typed in the cvc text box
        if len(value) == 3:
            GUI.inbound = False
            GUI.cvc_valid = True
            self.cvc_label.color = [0, 0, 0, 1]
        elif len(value) > 3:
            GUI.inbound = False
            self.cvc_input.text = value[:len(value) - 1]
        else:
            GUI.inbound = True
            GUI.cvc_valid = False
            self.cvc_label.color = [0, 0, 0, .5]

    def on_text_exp_m(self, instance, value):  # When a character is typed in the month expiry text box
        if len(value) == 2:
            GUI.inbound = False
            GUI.exp_m_valid = True
        elif len(value) > 2:
            GUI.inbound = False
            self.exp_m_input.text = value[:len(value) - 1]
        else:
            GUI.inbound = True
            GUI.exp_m_valid = False
        if GUI.exp_m_valid and GUI.exp_y_valid:
            self.exp_label.color = [0, 0, 0, 1]
        else:
            self.exp_label.color = [0, 0, 0, .5]

    def on_text_exp_y(self, instance, value):  # When a character is typed in the year expiry text box
        if len(value) == 2:
            GUI.inbound = False
            GUI.exp_y_valid = True
        elif len(value) > 2:
            GUI.inbound = False
            self.exp_y_input.text = value[:len(value) - 1]
        else:
            GUI.inbound = True
            GUI.exp_y_valid = False
        if GUI.exp_m_valid and GUI.exp_y_valid:
            self.exp_label.color = [0, 0, 0, 1]
        else:
            self.exp_label.color = [0, 0, 0, .5]

    def enter_callback(self, value):  # When the enter button is pressed
        if self.box_checked and GUI.name_valid and GUI.num_valid and GUI.cvc_valid and GUI.exp_m_valid and GUI.exp_y_valid:
            # valid entries
            if self.box_name == self.user_details['Provider'] and self.name_input.text.lower() == self.user_details[
                'Name'].lower() and self.num_input.text == str(
                self.user_details['Card Number']) and self.cvc_input.text == str(self.user_details['CVC']) and \
                    self.user_details['Expiry'].replace('/', '') == self.exp_m_input.text + self.exp_y_input.text:
                # print('correct details')
                if self.test_count <= 10:
                    # Empty input boxes
                    self.name_input.text = ''
                    self.num_input.text = ''
                    self.cvc_input.text = ''
                    self.exp_m_input.text = ''
                    self.exp_y_input.text = ''
                    self.visa_checkbox.active = False
                    self.mc_checkbox.active = False
                    self.disc_checkbox.active = False
                    self.jcb_checkbox.active = False
                    self.box_value = None
                    self.box_name = None
                    self.visa_label.color = [0, 0, 0, .5]
                    self.visa_down = False
                    self.mc_label.color = [0, 0, 0, .5]
                    self.mc_down = False
                    self.disc_label.color = [0, 0, 0, .5]
                    self.disc_down = False
                    self.jcb_label.color = [0, 0, 0, .5]
                    self.jcb_down = False
                    self.error_label.color = [0, 0, 0, 0]
                    self.movement_ID = 1
                    self.previous_epoch = time.time()
                    # Record the test data
                    false_enters = {'false_enters': self.false_enter_count}
                    self.m_events.append(false_enters)
                    test_data = {
                        # 'test_' + str(self.test_count): {
                        'key_events': self.k_events,
                        'mouse_events': self.m_events
                    }
                    temp_data = {
                        'temp_events': self.temp_events
                    }
                    self.data['true_data']['test_' + str(self.test_count)].update(test_data)
                    print('test count label update')
                    self.false_enter_count = 0
                    self.test_count_text = 'Training data entered: ' + str(self.test_count + 1) + '/10'
                    self.test_count_label.text = self.test_count_text
                    if self.test_count == 10:
                        df_count = 0
                        self.popup_training.open()
                        for i in range(1, 11):
                            print('row', i)
                            temp_row = self.feature_engineering(self.data['true_data']['test_' + str(i)])
                            self.df = pd.concat([self.df, temp_row], axis=0)
                            df_count += 1
                        for i in range(11, 21):
                            print('row', i)
                            temp_row = self.feature_engineering(self.data['false_data']['test_' + str(i)])
                            self.df = pd.concat([self.df, temp_row], axis=0)
                            df_count += 1
                        print(self.df)
                        X = self.df
                        y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        self.clf.fit(X, y)
                        self.test_count += 1
                        self.test_count_text = 'Enter data to test trained model'
                        self.test_count_label.text = self.test_count_text
                        self.test_count_label.pos = (180, 450)
                        self.save_button.disabled = False

                    self.k_events = []
                    self.m_events = []
                    self.temp_events = []
                    print('test count:', self.test_count)
                    self.test_count += 1

                elif 10 < self.test_count:
                    # Empty input boxes
                    false_enters = {'false_enters': self.false_enter_count}
                    self.m_events.append(false_enters)
                    self.test_data = {
                        'key_events': self.k_events,
                        'mouse_events': self.m_events
                    }
                    test_df = self.feature_engineering(self.test_data)
                    self.classifier_predict(test_df)
                    self.name_input.text = ''
                    self.num_input.text = ''
                    self.cvc_input.text = ''
                    self.exp_m_input.text = ''
                    self.exp_y_input.text = ''
                    self.visa_checkbox.active = False
                    self.mc_checkbox.active = False
                    self.disc_checkbox.active = False
                    self.jcb_checkbox.active = False
                    self.box_value = None
                    self.box_name = None
                    self.visa_label.color = [0, 0, 0, .5]
                    self.visa_down = False
                    self.mc_label.color = [0, 0, 0, .5]
                    self.mc_down = False
                    self.disc_label.color = [0, 0, 0, .5]
                    self.disc_down = False
                    self.jcb_label.color = [0, 0, 0, .5]
                    self.jcb_down = False
                    self.error_label.color = [0, 0, 0, 0]
                    self.movement_ID = 1
                    self.previous_epoch = time.time()
                    # Record the test data
                    false_enters = {'false_enters': self.false_enter_count}
                    self.m_events.append(false_enters)

                    self.k_events.clear()
                    self.m_events.clear()
                    # get new details

                    self.false_enter_count = 0

                    self.test_count += 1

            else:
                self.false_enter_count += 1
                if self.box_name != self.user_details['Provider']:
                    self.visa_label.color = [1, 0, 0, 1]
                    self.mc_label.color = [1, 0, 0, 1]
                    self.disc_label.color = [1, 0, 0, 1]
                    self.jcb_label.color = [1, 0, 0, 1]
                    self.card_type_label.color = [1, 0, 0, 1]
                    self.error_label.color = [1, 0, 0, 1]
                    self.error_label.text = '[i]* Details not recognised[/i]'
                if self.name_input.text.lower() != self.user_details['Name'].lower():
                    self.name_label.color = [1, 0, 0, 1]
                    self.error_label.color = [1, 0, 0, 1]
                    self.error_label.text = '[i]* Details not recognised[/i]'
                if self.num_input.text != str(self.user_details['Card Number']):
                    self.num_label.color = [1, 0, 0, 1]
                    self.error_label.color = [1, 0, 0, 1]
                    self.error_label.text = '[i]* Details not recognised[/i]'
                if self.cvc_input.text != str(self.user_details['CVC']):
                    self.cvc_label.color = [1, 0, 0, 1]
                    self.error_label.color = [1, 0, 0, 1]
                    self.error_label.text = '[i]* Details not recognised[/i]'
                if self.user_details['Expiry'].replace('/', '') != self.exp_m_input.text + self.exp_y_input.text:
                    self.exp_label.color = [1, 0, 0, 1]
                    self.error_label.color = [1, 0, 0, 1]
                    self.error_label.text = '[i]* Details not recognised[/i]'
        else:
            self.error_label.color = [1, 0, 0, 1]
            self.error_label.text = '[i]* Enter valid details[/i]'
            self.false_enter_count += 1
            # self.error_label.text = 'Enter valid details'
            # self.error_label.color = [1, 0, 0, 1]

    def reset_callback(self, value):  # When the reset button is pressed
        self.name_input.text = ''
        self.num_input.text = ''
        self.cvc_input.text = ''
        self.exp_m_input.text = ''
        self.exp_y_input.text = ''
        self.visa_checkbox.active = False
        self.mc_checkbox.active = False
        self.disc_checkbox.active = False
        self.jcb_checkbox.active = False
        self.box_value = None
        self.box_name = None
        self.visa_label.color = [0, 0, 0, .5]
        self.visa_down = False
        self.mc_label.color = [0, 0, 0, .5]
        self.mc_down = False
        self.disc_label.color = [0, 0, 0, .5]
        self.disc_down = False
        self.jcb_label.color = [0, 0, 0, .5]
        self.jcb_down = False
        self.error_label.color = [0, 0, 0, 0]
        self.movement_ID = 1
        self.previous_epoch = time.time()
        if self.existing_model:
            self.test_count_text = 'Enter data to test existing model'
            self.test_count_label.pos = (180, 450)
            self.test_count = 11

        else:
            self.test_count = 1
            self.test_count_text = 'Training data entered: ' + str(self.test_count) + '/10'
            self.test_count_label.text = self.test_count_text
            self.test_count_label.pos = (160, 450)
            for i in self.data['true_data']:
                self.data['true_data'][i] = {}
            if os.path.isfile('saved_models\\test_model.sav'):
                self.delete_button.disabled = False
            else:
                self.delete_button.disabled = True

    def save_callback(self, value):  # When the save button is pressed
        self.filename = 'test_model.sav'
        self.popup_save.content = Label(text='Model saved')
        self.popup_save.open()
        pickle.dump(self.clf, open('saved_models\\' + self.filename, 'wb'))
        self.save_button.disabled = True
        self.existing_model = True
        self.delete_button.disabled = False

    def delete_callback(self, value):  # When the delete callback is pressed
        try:
            self.test_count = 1
            self.test_count_text = 'Training data entered: ' + str(self.test_count) + '/10'
            self.test_count_label.text = self.test_count_text
            self.test_count_label.pos = (160, 450)
            self.name_input.text = ''
            self.num_input.text = ''
            self.cvc_input.text = ''
            self.exp_m_input.text = ''
            self.exp_y_input.text = ''
            self.visa_checkbox.active = False
            self.mc_checkbox.active = False
            self.disc_checkbox.active = False
            self.jcb_checkbox.active = False
            self.box_value = None
            self.box_name = None
            self.visa_label.color = [0, 0, 0, .5]
            self.visa_down = False
            self.mc_label.color = [0, 0, 0, .5]
            self.mc_down = False
            self.disc_label.color = [0, 0, 0, .5]
            self.disc_down = False
            self.jcb_label.color = [0, 0, 0, .5]
            self.jcb_down = False
            self.error_label.color = [0, 0, 0, 0]
            self.movement_ID = 1
            self.previous_epoch = time.time()
            self.delete_button.disabled = True
            for i in self.data['true_data']:
                self.data['true_data'][i] = {}
            self.existing_model = False
            path = 'saved_models//'
            for f in os.listdir(path):
                os.remove(os.path.join(path, f))
        except:
            file = open('saved_models')
            for i in file:
                os.remove(i)

    def _keyboard_closed(self):
        pass

    # EVENTS TAKEN FROM THE USER
    def on_key_down(self, key, keycode, text, modifiers):  # When a key is pressed down
        timestamp = str(datetime.utcnow())
        epoch = str(time.time())
        event = {
            'Key': keycode[1],
            'Event': 'pressed',
            'Input Box': GUI.focus,
            'Text Changed': GUI.inbound,
            'Timestamp': timestamp,
            'Epoch': epoch
        }
        self.k_events.append(event)
        self.temp_events.append(event['Key'])
        # print(keycode[1])
        # print(event)
        return True

    # Executes on key release
    def on_key_up(self, key, keycode):  # When a key is released
        timestamp = str(datetime.utcnow())
        epoch = str(time.time())
        event = {
            'Key': keycode[1],
            'Event': 'released',
            'Input Box': GUI.focus,
            'Text Changed': GUI.inbound,
            'Timestamp': timestamp,
            'Epoch': epoch
        }
        self.k_events.append(event)
        return True

    # executes if mouse moves
    def mouse_pos(self, obj, coor):  # When the mouse position changes
        timestamp = str(datetime.utcnow())
        epoch = time.time()
        if epoch - self.previous_epoch >= 0.5:
            self.movement_ID += 1
        epoch = str(epoch)
        event = {
            'Event': 'movement',
            'Coordinates': coor,
            'Timestamp': timestamp,
            'Epoch': epoch,
            'Movement ID': self.movement_ID
        }
        self.m_events.append(event)
        self.previous_epoch = float(epoch)
        return True

    def on_release(self, instance, touch):  # When the mouse button is released
        timestamp = str(datetime.utcnow())
        epoch = str(time.time())
        action = str(touch.button) + ' release'
        event = [action, touch.pos, timestamp, epoch]
        event = {
            'Event': action,
            'Coordinates': touch.pos,
            'Timestamp': timestamp,
            'Epoch': epoch
        }
        self.m_events.append(event)

    def on_press(self, instance, touch):  # When the mouse button is pressed
        timestamp = str(datetime.utcnow())
        epoch = str(time.time())
        action = str(touch.button) + ' press'
        event = {
            'Event': action,
            'Coordinates': touch.pos,
            'Timestamp': timestamp,
            'Epoch': epoch
        }
        self.m_events.append(event)

    def classifier_predict(self, df):  # Carries out a prediction with the classifier
        prediction = self.clf.predict(df)
        if prediction == 0:
            self.popup_false.open()
        else:
            self.popup_true.open()

    def feature_engineering(self, data):  # Carries out feature engineering with the raw data
        # GENERATES THE K FEATURES
        # NEW CELL
        # print('START')
        # print(' ')
        temp_df = pd.DataFrame(columns=['dwell_time', 'flight_time', 'UD', 'UU', 'PR', 'PP', 'RR', 'caps'
            , 'l_shift', 'r_shift', 'error', 'in_bounds', 'key_press'])
        flight_time = 0
        temp_count = 0
        k_data = data['key_events']
        tabless_k_data = []
        for i in k_data:
            if i['Key'] != 'tab':
                tabless_k_data.append(i)

        first_loop = True

        count = 0

        l_shift = False
        r_shift = False
        error = False
        capslock = False
        prev_key_press = 0
        prev_key_release = 0
        for i in tabless_k_data:
            # print('count:', count)
            if i['Event'] == 'pressed':
                key_key = i['Key']
                key_press_time = i['Epoch']
                key_released = False
                UD = False
                UU = False
                continued_count = 1
                while key_released == False:
                    j = continued_count + count
                    start_row = tabless_k_data[count]
                    next_row = tabless_k_data[j]
                    if next_row['Key'] == key_key and next_row['Event'] == 'released':
                        key_release_time = next_row['Epoch']
                        dwell_time = float(key_release_time) - float(key_press_time)
                        key_released = True
                    elif next_row['Key'] != key_key and next_row['Event'] == 'pressed':
                        UD = True
                        continued_count += 1
                    elif next_row['Key'] != key_key and next_row['Event'] == 'released':
                        UU = True
                        UD = True
                        continued_count += 1
                    else:
                        key_released = True
                        dwell_time = 0
                        key_release_time = start_row['Epoch']

                if key_key == 'shift':
                    l_shift = True
                    r_shift = False
                elif key_key == 'rshift':
                    l_shift = False
                    r_shift = True

                if key_key == 'backspace':
                    error = True
                else:
                    error = False

                if first_loop:
                    PR = 0
                    PP = 0
                    RR = 0
                    first_loop = False
                else:
                    PR = float(key_release_time) - float(prev_key_press)
                    PP = float(key_press_time) - float(prev_key_press)
                    RR = float(key_release_time) - float(prev_key_release)

                in_bounds = i['Text Changed']
                # stores generated variables into dataframe
                temp_df.loc[temp_count] = [dwell_time, flight_time, UD, UU, PR, PP, RR, capslock, l_shift, r_shift,
                                           error, in_bounds,
                                           key_key]
                # sets variables for the next loop
                prev_key_press = key_press_time
                prev_key_release = key_release_time
                temp_count += 1
            if i['Key'] == 'shift' and i['Event'] == 'released':
                l_shift = False
            if i['Key'] == 'rshift' and i['Event'] == 'released':
                r_shift = False
            count += 1
        # NEW CELL
        temp_df2 = pd.DataFrame(columns=['flight_time', 'key_release'])
        temp_count = 0
        k_data = data['key_events']
        #  removes tabs from the data, as tabs do not register releases,
        #  which affects the way the features are calculated
        tabless_k_data = []
        for i in k_data:
            if i['Key'] != 'tab':
                tabless_k_data.append(i)
        count = 0
        flight_time = []
        key_list = []
        for i in tabless_k_data:
            key = i['Key']
            flight_found = False
            if i['Event'] == 'released':
                continued_count = 1
                while not flight_found:
                    j = count + continued_count
                    if j < len(tabless_k_data):
                        next_row = tabless_k_data[j]
                        if next_row['Event'] == 'pressed' and next_row['Key'] != key:
                            flight_time = float(next_row['Epoch']) - float(i['Epoch'])
                            key_list.append(key)
                            temp_df2.loc[temp_count] = [flight_time, key]
                            temp_count += 1
                            flight_found = True
                        continued_count += 1
                    else:
                        flight_found = True
            count += 1

        fh_count = 0
        flight_hold = []
        for j in temp_df2.index:
            flight_hold.append(temp_df2.at[j, 'flight_time'])
        fh_count = 0
        for j in temp_df.index:
            if fh_count < len(flight_hold):
                temp_df.at[j, 'flight_time'] = flight_hold[fh_count]
                fh_count += 1

        true_k_df = temp_df

        # identifies backspaces and tags the keys that were deleted as in_bounds = false
        count = 0
        err_count = 0
        for j in true_k_df.index:
            if true_k_df.at[j, 'key_press'] == 'backspace':
                if err_count == 0:
                    start_err = count
                err_count += 1
            elif true_k_df.at[j, 'key_press'] != 0 and err_count != 0:
                while err_count != 0:
                    loc = start_err - err_count
                    true_k_df.at[loc, 'in_bounds'] = False
                    err_count -= 1
            else:
                err_count = 0
            count += 1

            accepted_char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                  'r', 's', 't', 'u',
                                  'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            count = 0
            for i in true_k_df['key_press']:
                if i == 'backspace':
                    true_k_df.at[count, 'in_bounds'] = False
                elif i == 'capslock':
                    true_k_df.at[count, 'in_bounds'] = False
                    true_k_df.at[count, 'caps'] = True
                elif len(i) == 1 and i not in accepted_char_list:
                    true_k_df.at[count, 'in_bounds'] = False
                count += 1

        # CALCULATE THE M_FEATURES
        true_m_df = pd.DataFrame(columns=['movement_id', 'trajectory', 'ideal_traj',
                                          'traj_difference', 'single_coor'])
        row_count = 0
        m_data = data['mouse_events']
        m_movements = []
        for i in m_data[:len(m_data) - 1]:
            if i['Event'] == 'movement':
                m_movements.append(i)

        movement_coor_dict = {}
        for i in m_movements:
            movement_coor_dict[i['Movement ID']] = []
        for i in m_movements:
            movement_coor_dict[i['Movement ID']].append(i['Coordinates'])

        for i in movement_coor_dict:
            coor_list = movement_coor_dict[i]
            motion_start = False
            if len(coor_list) > 1:
                trajectory_list = []
                if motion_start == True:
                    motion_start = False
                else:
                    count = 0
                    for j in coor_list:
                        trajectory_list.append(self.get_distance(coor_list[count - 1], coor_list[count]))
                        count += 1
                    movement_id = i
                    ideal_traj = self.get_distance(coor_list[0], coor_list[len(coor_list) - 1])
                    trajectory = sum(trajectory_list)
                    traj_difference = trajectory - ideal_traj
                    single_coor = False
            else:
                movement_id = 1
                trajectory_list = [0]
                ideal_traj = 0
                trajectory = 0
                traj_difference = 0
                single_coor = False

            true_m_df.loc[row_count] = [movement_id, trajectory, ideal_traj, traj_difference, single_coor]
            row_count += 1

        true_m_df = true_m_df.sort_values(by=['movement_id'])
        for i in true_m_df['single_coor'].tolist():
            if i == True:
                true_m_df = true_m_df.drop[count]
            count += 1

        # CONVERTING ROWS INTO AGGREGATED ROWS READY FOR MODEL
        ib_df = pd.DataFrame(columns=true_k_df.columns.tolist())
        count = 0
        ib_df_count = 0
        for i in true_k_df['in_bounds'].tolist():
            if i == True:
                ib_df.loc[ib_df_count] = true_k_df.iloc[count]
                ib_df_count += 1
            count += 1
        ib_df = ib_df.drop('key_press', axis=1)

        test_inputs = len(self.user_details['Name']) + 16 + 3 + 4

        count = 0
        index_list = []
        for j in ib_df.index:
            count += 1
            index_list.append(j)
        if count < test_inputs:
            while count != test_inputs:
                impute_count = 0
                impute_list = [0, 0, False, False, 0, 0, 0, False, False, False, False, True]
                ib_df.loc[len(ib_df.index)] = impute_list
                count += 1
                impute_count += 1
        elif count > test_inputs:
            while count != test_inputs:
                loc = index_list.pop(len(index_list) - 1)
                ib_df = ib_df.drop(loc)
                count -= 1

        ib_df = ib_df.reset_index(drop=True)

        columns = ['dwell_max', 'dwell_avg', 'dwell_min', 'flight_max', 'flight_avg', 'flight_min', 'PR_max', 'PR_avg',
                   'PR_min', 'PP_max', 'PP_avg', 'PP_min', 'RR_max', 'RR_avg', 'RR_min', 'UD_rate', 'UD_present',
                   'UU_rate', 'UU_present', 'caps_rate', 'caps_present', 'error_rate', 'error_present',
                   'in_bounds_rate', 'in_bounds_present', 'actual_traj_min', 'actual_traj_avg', 'actual_traj_max',
                   'ideal_traj_min', 'ideal_traj_avg', 'ideal_traj_max', 'traj_diff_min', 'traj_diff_avg',
                   'traj_diff_max']

        df = pd.DataFrame(columns=columns)

        dwell_list = []
        flight_list = []
        PR_list = []
        PP_list = []
        RR_list = []
        UD_list = []
        UU_list = []
        caps_list = []
        error_list = []
        in_bounds_list = []
        l_shift_list = []
        r_shift_list = []
        error_list = []
        traj_list = []
        ideal_t_list = []
        t_diff_list = []

        for j in true_k_df.index:
            dwell_list.append(true_k_df.at[j, 'dwell_time'])
            flight_list.append(true_k_df.at[j, 'flight_time'])
            PR_list.append(true_k_df.at[j, 'PR'])
            PP_list.append(true_k_df.at[j, 'PP'])
            RR_list.append(true_k_df.at[j, 'RR'])
            UD_list.append(true_k_df.at[j, 'UD'])
            UU_list.append(true_k_df.at[j, 'UU'])
            caps_list.append(true_k_df.at[j, 'caps'])
            error_list.append(true_k_df.at[j, 'error'])
            in_bounds_list.append(true_k_df.at[j, 'in_bounds'])
            l_shift_list.append(true_k_df.at[j, 'l_shift'])
            r_shift_list.append(true_k_df.at[j, 'r_shift'])
            error_list.append(true_k_df.at[j, 'error'])

        for j in true_m_df.index:
            traj_list.append(true_m_df.at[j, 'trajectory'])
            ideal_t_list.append(true_m_df.at[j, 'ideal_traj'])
            t_diff_list.append(true_m_df.at[j, 'traj_difference'])

        dwell_list = [j for j in dwell_list if j != 0]
        flight_list = [j for j in flight_list if j != 0]
        PR_list = [j for j in PR_list if j != 0]
        PP_list = [j for j in PP_list if j != 0]
        RR_list = [j for j in RR_list if j != 0]
        traj_list = [j for j in traj_list if j != 0]
        ideal_t_list = [j for j in ideal_t_list if j != 0]
        t_diff_list = [j for j in t_diff_list if j != 0]

        for j in range(0, len(UD_list)):
            if UD_list[j] == True:
                UD_list[j] = 1
            elif UD_list == False:
                UD_list[j] = 0

        for j in range(0, len(UU_list)):
            if UU_list[j] == True:
                UU_list[j] = 1
            elif UU_list[j] == False:
                UU_list[j] = 0

        for j in range(0, len(caps_list)):
            if caps_list[j] == True:
                caps_list[j] = 1
            elif caps_list[j] == False:
                caps_list[j] = 0

        for j in range(0, len(error_list)):
            if error_list[j] == True:
                error_list[j] = 1
            elif error_list[j] == False:
                error_list[j] = 0

        for j in range(0, len(in_bounds_list)):
            if in_bounds_list[j] == True:
                in_bounds_list[j] = 1
            elif in_bounds_list[j] == False:
                in_bounds_list[j] = 0

        for j in range(0, len(l_shift_list)):
            if l_shift_list[j] == True:
                l_shift_list[j] = 1
            elif l_shift_list[j] == False:
                l_shift_list[j] = 0

        for j in range(0, len(r_shift_list)):
            if r_shift_list[j] == True:
                r_shift_list[j] = 1
            elif r_shift_list[j] == False:
                r_shift_list[j] = 0

        for j in range(0, len(error_list)):
            if error_list[j] == True:
                error_list[j] = 1
            elif error_list[j] == False:
                error_list[j] = 0

        dwell_max = max(dwell_list)
        dwell_avg = sum(dwell_list) / len(dwell_list)
        dwell_min = min(dwell_list)

        flight_max = max(flight_list)
        flight_avg = sum(flight_list) / len(flight_list)
        flight_min = min(flight_list)

        PR_max = max(PR_list)
        PR_avg = sum(PR_list) / len(PR_list)
        PR_min = min(PR_list)

        PP_max = max(PP_list)
        PP_avg = sum(PP_list) / len(PP_list)
        PP_min = min(PP_list)

        RR_max = max(RR_list)
        RR_avg = sum(RR_list) / len(RR_list)
        RR_min = min(RR_list)

        UD_rate = sum(UD_list) / len(UD_list)
        if UD_rate > 0:
            UD_present = 1
        else:
            UD_present = 0

        UU_rate = sum(UU_list) / len(UU_list)
        if UU_rate > 0:
            UU_present = 1
        else:
            UU_present = 0

        UU_rate = sum(UU_list) / len(UU_list)
        if UU_rate > 0:
            UU_present = 1
        else:
            UU_present = 0

        UU_rate = sum(UU_list) / len(UU_list)
        if UU_rate > 0:
            UU_present = 1
        else:
            UU_present = 0

        caps_rate = sum(caps_list) / len(caps_list)
        if caps_rate > 0:
            caps_present = 1
        else:
            caps_present = 0

        error_rate = sum(error_list) / len(error_list)
        if error_rate > 0:
            error_present = 1
        else:
            error_present = 0

        in_bounds_rate = sum(in_bounds_list) / len(in_bounds_list)
        if in_bounds_rate > 0:
            in_bounds_present = 1
        else:
            in_bounds_present = 0

        l_shift_rate = sum(l_shift_list) / len(l_shift_list)
        if l_shift_rate > 0:
            l_shift_present = 1
        else:
            l_shift_present = 0

        r_shift_rate = sum(r_shift_list) / len(r_shift_list)
        if r_shift_rate > 0:
            r_shift_present = 1
        else:
            r_shift_present = 0

        traj_max = max(traj_list)
        traj_avg = sum(traj_list) / len(traj_list)
        traj_min = min(traj_list)

        ideal_t_max = max(ideal_t_list)
        ideal_t_avg = sum(ideal_t_list) / len(ideal_t_list)
        ideal_t_min = min(ideal_t_list)

        t_diff_max = max(t_diff_list)
        t_diff_avg = sum(t_diff_list) / len(t_diff_list)
        t_diff_min = min(t_diff_list)

        agg_data = [dwell_max, dwell_avg, dwell_min, flight_max, flight_avg, flight_min, PR_max, PR_avg, PR_min, PP_max,
                    PP_avg,
                    PP_min, RR_max, RR_avg, RR_min, UD_rate, UD_present, UU_rate, UU_present, caps_rate, caps_present,
                    error_rate,
                    error_present, in_bounds_rate, in_bounds_present, traj_max, traj_avg, traj_min, ideal_t_max,
                    ideal_t_avg,
                    ideal_t_min, t_diff_max, t_diff_avg, t_diff_min]

        df.loc[0] = agg_data

        return df

    def get_distance(self, a, b):  # Gets the distance between two pixels on the Window
        distance = math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
        return distance

    def on_stop(self):
        print('method called')


CyberSignatureApp().run()
