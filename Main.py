# A Python Program to digitilize the character sheets of DnD characters

# Copyright 2024 MDH-Developments
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

# Imports
import PySimpleGUI as sg

# All the stuff inside your window.
# make sure each line in the gui is spaced by one gap in the code

sg.theme('DarkGrey3')

layout = [  [sg.Text('Player Name:'), sg.InputText(size=11), sg.Text('Race:'), sg.InputText(size=10),
             sg.Text('Class:'),
             sg.InputText(size=10), sg.Text('Lv'), sg.InputText(size=3)],

            [sg.Text('Strength'), sg.InputText(size=3), sg.Text('Max Hp'), sg.InputText(size=3),
             sg.Text('Current Hp'),
             sg.InputText(size=3), sg.Text('Amour Class'), sg.InputText(size=3),sg.Text('Init'),
             sg.InputText(size=3),sg.Text('Speed'), sg.InputText(size=3),],

            [sg.Text('Dexterity'), sg.InputText(size=6), sg.Text('Weapon Attacks'), sg.Text('Bonus To Attack'),
             sg.Text('Damage'), sg.Text('Skills')],

            [sg.Text('Constitution'), sg.InputText(size=3), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Checkbox("Acrobatics", key="-CHECKBOX-", enable_events=True)],



            [sg.Text('Inteligence'), sg.InputText(size=4), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Checkbox("Animal Handling", key="-CHECKBOX1-", enable_events=True)],

            [sg.Text('Wisdom'), sg.InputText(size=6), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Checkbox("Arcana", key="-CHECKBOX2-", enable_events=True)],

            [sg.Text('Charisma'), sg.InputText(size=5), sg.InputText(size=15), sg.InputText(size=13),
             sg.InputText(size=8), sg.Checkbox("Deception", key="-CHECKBOX3-", enable_events=True)],

            [sg.Text('Hit Dices'), sg.Text('Max'), sg.InputText(size=5), sg.Text('Current'),
             sg.InputText(size=5)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15), sg.Text('Saving Throws'),
             sg.Text('Gold'), sg.InputText(size=5),
             sg.Push(), sg.Checkbox("History", key="-CHECKBOX4-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Strength", key="-CHECKBOX17-", enable_events=True),
             sg.Text('Silver'), sg.InputText(size=5), sg.Push(),
             sg.Checkbox("Insight", key="-CHECKBOX5-", enable_events=True)],

            [sg.Text('abilities'), sg.InputText(size=15), sg.InputText(size=15),
             sg.Checkbox("Dexterity", key="-CHECKBOX18-", enable_events=True),
             sg.Text('Copper'), sg.InputText(size=5), sg.Push(),
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
             sg.InputText(size=3) , sg.Push(),
             sg.Checkbox("Performance", key="-CHECKBOX11-", enable_events=True)],

            [sg.Push(), sg.Text('Inventory'), sg.Push(),
             sg.Checkbox("Persuasion", key="-CHECKBOX12-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=15),sg.InputText(size=15), sg.InputText(size=15),
             sg.Push(), sg.Checkbox("Religion", key="-CHECKBOX13-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=15),sg.InputText(size=15), sg.InputText(size=15),
             sg.Push(), sg.Checkbox("Slight of Hand", key="-CHECKBOX14-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=15),sg.InputText(size=15), sg.InputText(size=15),
             sg.Push(), sg.Checkbox("Stealth", key="-CHECKBOX15-", enable_events=True)],

            [sg.InputText(size=15), sg.InputText(size=15),sg.InputText(size=15), sg.InputText(size=15),
             sg.Push(), sg.Checkbox("Survival", key="-CHECKBOX16-", enable_events=True)],


            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Digital Character Sheet V0.0.2', layout, size=(600, 700))

# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


window.close()