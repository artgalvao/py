from os import close
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Submit

sg.theme('BluePurple')

layout = [[sg.Text('Nome e Sobrenome :'), sg.Input(key='A')],
            [sg.Text('Data de Nascimento:'), sg.Input(key='B')],      
            [sg.Submit(key='C', button_text='Enviar'), sg.Cancel('Cancelar')]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values['A']    
sg.popup(f"Nome e Sobrenome {values['A']}\nData de Nascimento: {values['B']}")
window.close()