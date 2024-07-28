import PySimpleGUI as sg
import os
import shutil
from pathlib import Path


def clearName(pathname: str) -> str:

	f1 = False
	f2 = False
	for i in reversed(range(0, len(pathname))):

		if pathname[i].isdigit():
			break
		if pathname[i] == '.':
			f1 = True
		if f1 == True and pathname[i].isalpha():
			f2 = True

	if f2 == True:
		return pathname[i+1:len(pathname)]
	else: return complex(pathname, i)


def complex(pathname, i):

	while pathname[i].isdigit() and i >= 0:
		i = i - 1
	if i < 0:
		i = 0
		return pathname

	f = True
	while f == True and i >= 0:

		while pathname[i].isspace():# and i >= 0:
			if i == 0:
				i = i+1
				return pathname[i:len(pathname)]
			else: i = i-1

		while (pathname[i].isalpha()) and (i >= 0):
			i = i - 1
		if i < 0:
			i = 0
			return pathname[i:len(pathname)]
		elif (not pathname[i].isspace()) and (not pathname[i].isalpha()):
			i = i+1
			f = False


	return pathname[i:len(pathname)]


def moveRenamedFile(path, subfolder):

	if not os.path.isdir(subfolder):
		os.mkdir(subfolder)

	files = []
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			files.append(f)

	for name in files:
		if name.endswith(".pdf"):
			newname = clearName(name)

			shutil.copyfile(os.path.join(path, name), \
							os.path.join(subfolder, newname) )

			#os.rename(src, dst)




def buttonAct(path, subfolder):
	moveRenamedFile(path, subfolder)



if __name__ == '__main__':

	# All the stuff inside your window.
	btn = sg.Button('Очистка', key='-CLR-')
	readyTxt = sg.Text('Готово!', key='-READYTXT-', visible = False)

	layout = [[sg.Text("В одной папке, где находится программа должна быть папка 'Чертежи_' с pdf файлами.\n Нажмите 'Очистить', чтобы скопировать файлы в папку \"После очистки\" и оставить только буквенное название со счётными числами")],
			  [btn, readyTxt]]

	# Create the Window
	window = sg.Window('Example', layout)

	# Event Loop to process "events" and get the "values" of the inputs
	while True:
		event, values = window.read()

		if event == '-CLR-':
			buttonAct('Чертежи_', os.path.join('Чертежи_', 'После очистки'))
			sg.popup("Готово, закройте программу, чтобы увидеть файлы")

		# if user closes window or clicks cancel
		if event == sg.WIN_CLOSED or event == 'Cancel':
			break


	window.close()
