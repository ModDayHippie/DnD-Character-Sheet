# A Python Program to digitilize the character sheets of DnD characters

# 2024 MDH-Developments
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction,
# including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software. THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Item Spreadsheet Source
# https://docs.google.com/spreadsheets/d/10q9-pMNvQZE5T7Zuco4PJsYW-rwES_LfMp0-wUerfyw/edit#gid=0
# Other usefull links
# https://www.reddit.com/r/learnpython/comments/vlnb0c/pysimplegui_window_resizes_when_pandasgui/
# https://pypi.org/project/dnd-character/
# https://www.youtube.com/watch?v=LzCfNanQ_9c

# Imports

import PySimpleGUI as sg
import pandas as pd
from pandasgui import show



def make_armour_win() -> None:
    armour_df = pd.read_csv('Armor.csv')
    armour_df = armour_df.fillna('-')
    sg.popup_scrolled(armour_df, title='Armour', size=(125, 50))

def make_potions_win() -> None:
    Potion_df = pd.read_csv('Potions.csv')
    Potion_df = Potion_df.fillna('-')
    sg.popup_scrolled(Potion_df, title='Potions', size=(125, 50))

def make_Magic_win() -> None:
    Magic_df = pd.read_csv('Magic.csv')
    Magic_df = Magic_df.fillna('-')
    sg.popup_scrolled(Magic_df, title='Magic', size=(125, 50))

def make_Gear_win() -> None:
    Gear_df = pd.read_csv('Gear.csv')
    Gear_df = Gear_df.fillna('-')
    sg.popup_scrolled(Gear_df, title='Gear', size=(125, 50))

def make_Tools_win() -> None:
    Tools_df = pd.read_csv('Tools.csv')
    Tools_df = Tools_df.fillna('-')
    sg.popup_scrolled(Tools_df, title='Tools', size=(125, 50))

def make_Mounts_win() -> None:
    Mounts_df = pd.read_csv('Mount&tack.csv')
    Mounts_df = Mounts_df.fillna('-')
    sg.popup_scrolled(Mounts_df, title='Mounts', size=(125, 50))

EXCEL_FILE1 = 'Items2.ods'
# EXCEL_FILE2 = 'Magic.ods'
df = pd.read_excel(EXCEL_FILE1)
# df2 = pd.read_excel(EXCEL_FILE2)

# keys

# Race = sg.InputText(key='Race', size=10)
# Race = values['-Race-']

# All the stuff inside your window.
# make sure each line in the gui is spaced by one gap in the code

sg.theme('DarkRed1')

layout = [[sg.Text('Player Name:'), sg.InputText(size=11), sg.Text('Race:'), sg.InputText(key='Race', size=10),
             sg.Text('Class:'), sg.InputText(size=10), sg.Text('Lv'), sg.InputText(size=4)],

            [sg.Text('Strength'), sg.InputText(size=3, key='HP'), sg.Text('Max Hp'), sg.InputText(size=3),
             sg.Text('Current Hp'),
             sg.InputText(size=3), sg.Text('Armor Class'), sg.InputText(size=3), sg.Text('Init'),
             sg.InputText(size=3), sg.Text('Speed'), sg.InputText(size=3)],

            [sg.Text('Dexterity'), sg.InputText(size=6), sg.Text('Weapon Attacks'), sg.Text('Bonus To Attack'),
             sg.Text('Damage'), sg.Text('Skills')],

            [sg.Text('Constitution'), sg.InputText(size=3), sg.InputText(key=1, size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Push(), sg.Checkbox("Acrobatics", key="-CHECKBOX-", enable_events=True)],

            [sg.Text('Inteligence'), sg.InputText(size=4), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Push(), sg.Checkbox("Animal Handling", key="-CHECKBOX1-", enable_events=True)],

            [sg.Text('Wisdom'), sg.InputText(size=6), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Push(), sg.Checkbox("Arcana", key="-CHECKBOX2-", enable_events=True)],

            [sg.Text('Charisma'), sg.InputText(size=5), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Push(), sg.Checkbox("Deception", key="-CHECKBOX3-", enable_events=True)],

            [sg.Text('Hit Dices'), sg.Text('Max'), sg.InputText(size=5), sg.Text('Current'),
             sg.InputText(size=5), sg.Text('Gold'), sg.InputText(key='Gold',size=5), sg.Text('Silver'), sg.InputText(key='Silver', size=5),
             sg.Text('Copper'), sg.InputText(key='Copper', size=5)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15), sg.Text('Saving Throws'),
             sg.Text('Plat'), sg.InputText(key='Plat', size=5), sg.Push(),
             sg.Checkbox("History", key="-CHECKBOX4-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Strength", key="-CHECKBOX17-", enable_events=True), sg.Push(),
             sg.Checkbox("Insight", key="-CHECKBOX5-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Dexterity", key="-CHECKBOX18-", enable_events=True), sg.Push(),
             sg.Checkbox("Intimidation", key="-CHECKBOX6-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Constitution", key="-CHECKBOX19-", enable_events=True),
             sg.Push(), sg.Checkbox("Investigation", key="-CHECKBOX7-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Intelegence", key="-CHECKBOX20-", enable_events=True),
             sg.Push(), sg.Checkbox("Medicin", key="-CHECKBOX8-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Wisdom", key="-CHECKBOX21-", enable_events=True),
             sg.Push(), sg.Checkbox("Nature", key="-CHECKBOX9-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Charisma", key="-CHECKBOX22-", enable_events=True),
             sg.Push(), sg.Checkbox("Perception", key="-CHECKBOX10-", enable_events=True)],

            [sg.Text('Death saves passed'), sg.InputText(size=3), sg.Text('Death saves failed'),
             sg.InputText(size=3), sg.Push(),
             sg.Checkbox("Performance", key="-CHECKBOX11-", enable_events=True)],

            [sg.Push(), sg.Text('Inventory'), sg.Push(),
             sg.Checkbox("Persuasion", key="-CHECKBOX12-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=3), sg.InputText(size=15), sg.InputText(size=3),
             sg.InputText(size=15), sg.InputText(size=3), sg.Push(),
             sg.Checkbox("Religion", key="-CHECKBOX13-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=3), sg.InputText(size=15), sg.InputText(size=3),
             sg.InputText(size=15), sg.InputText(size=3),
             sg.Push(), sg.Checkbox("Slight of Hand", key="-CHECKBOX14-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=3), sg.InputText(size=15), sg.InputText(size=3),
             sg.InputText(size=15), sg.InputText(size=3),
             sg.Push(), sg.Checkbox("Stealth", key="-CHECKBOX15-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=3), sg.InputText(size=15), sg.InputText(size=3),
             sg.InputText(size=15), sg.InputText(size=3),
             sg.Push(), sg.Checkbox("Survival", key="-CHECKBOX16-", enable_events=True)],

            [sg.Button('Potions'), sg.Button('Items'), sg.Button('Magic'), sg.Button('Gear'), sg.Button('Save')],

            [sg.Button('Tools'), sg.Button('Armor'), sg.Button('Mounts/Tack'), sg.Button('Undo')]]

# Create the Window

window = sg.Window('Digital Character Sheet V0.3.5', layout, size=(700, 750))
event, values = window.Read()

# Race = (values['-Race-'])

# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()

    if event in 'Items':
        show(df)

    if event in 'Magic':
        make_Magic_win()

    if event in 'Save':
        # print line is for testing
        sg.popup("Currently a WIP")
        break

    if event in 'Potions':
        make_potions_win()

    if event in 'Gear':
        make_Gear_win()

    if event in 'Tools':
        make_Tools_win()

    if event in 'Armor':
        if event == ('Armor'):
            make_armour_win()

    if event in 'Mounts/Tack':
        make_Mounts_win()

    if event in 'Undo':
        sg.popup("Currently a WIP")

# if user closes window or clicks cancel

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()