import PySimpleGUI as psg
layout = [
   [psg.Text('Enter a num: '), psg.Input(key='-FIRST-')],
   [psg.Text('Enter a num: '), psg.Input(key='-SECOND-')],
   [psg.Text('Result : '), psg.Text(key='-OUT-')],
   [psg.Button("Add", key='-ADD-'), psg.Button("Sub", key='- SUB-'), psg.Exit()],
]
window = psg.Window('Calculator', layout)
while True:
   event, values = window.read()
   print(event, values)

   if event == "-ADD-":
      result = int(values['-FIRST-']) + int(values['-SECOND-'])

   if event == "-SUB-":
      result = int(values['-FIRST-']) - int(values['-SECOND-'])

   window['-OUT-'].update(result)

   if event == psg.WIN_CLOSED or event == 'Exit':
      break
window.close()