import PySimpleGUI as sg
import zipfile
import os

def compress_files(files, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

layout = [
    [sg.Text('Select files to compress:')],
    [sg.Input(key='files', enable_events=True), sg.FilesBrowse('Browse')],
    [sg.Text('Output Directory:')],
    [sg.Input(key='folder', enable_events=True), sg.FolderBrowse('Browse')],
    [sg.Button('Compress'), sg.Button('Cancel')]
]

window = sg.Window('File Compressor', layout)

while True:
    event, values = window.read()
    match event:
        case sg.WINDOW_CLOSED, 'Cancel':
            break
        case 'Compress':
            files = values['files'].split(';')
            output_dir = values['folder']
            if not files or not output_dir:
                sg.popup_error('Please select files and specify output directory')
            else:
                output_zip = os.path.join(output_dir, 'compressed_files.zip')
                compress_files(files, output_zip)
                sg.popup('Compression complete!')
        case 'folder':
            output_path = values['folder']
            window['folder'].update(output_path)
        case sg.WIN_CLOSED:
            exit()

window.close()
