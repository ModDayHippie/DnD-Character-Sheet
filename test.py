import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText('', key='input_height')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == 'Submit':
        height = int(values['input_height'])

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print('You entered ', height)

window.close()