import PySimpleGUI as sg
import os
import json
import requests
import webbrowser
import time
import subprocess

sg.theme('Python')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Path to map folder')],
            [sg.InputText("-FILE_PATH-"),sg.FolderBrowse()],
            [sg.Button('Dump'), sg.Button('View'),sg.Button('Cancel'),sg.Button('Settings')] ]

# Create the Window
window = sg.Window('Osu map save', layout)
# Event Loop to process "events" and get the "values" of the inputs

def settings_window():
    sg.theme('Python')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('PATH FOR DOWNLOAD')],
              [sg.InputText("-FILE_PATH-"), sg.FolderBrowse()],
              [sg.Text('PATH DATA FILE')],
              [sg.InputText("-FILE_PATH-"), sg.FileBrowse()],
              [sg.Button('Save'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Settings', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == "Save":
            download_path = values[0]
    window.close()

data = []
def url_window():
    sg.theme('Python')
    layout = [
        [sg.Text("Map URL (convert.json)")],
        [sg.Listbox(data,size=(70,40))],
        [sg.Button('Path')]
    ]
    window = sg.Window('map', layout)

    while True:
        event, values = window.read()
        if event == 'Path':
            folder()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
    window.close()

def map_dump():
    temp = os.listdir(values[0])
    details = []
    i = 0
    while i < len(temp):
        details.append(temp[i].split(" ")[0])
        i += 1
        print(f"Карта {i}")
    with open('data.json', 'w') as json_file:
        json.dump(details, json_file)
    map_view()


def map_view():
    with open('data.json') as id:
        id_map = json.load(id)
    i = 0
    while i < len(id_map):
        url = f"https://osu.ppy.sh/beatmapsets/{id_map[i]}/download"
        data.append(url)
        with open('convert.json', 'w') as json_file:
            json.dump(data, json_file)
        i += 1

def folder():
    path = os.path.abspath(os.curdir)
    subprocess.Popen(f'explorer /select , {path}\convert.json')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Dump":
        map_dump()
        print('You entered ', values[0])
    if event == "View":
        url_window()
    if event == "Settings":
        settings_window()

window.close()