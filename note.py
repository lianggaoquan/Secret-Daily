from easygui import *
import os
import sys
import time
from myglobal import *
from face import *

def Write(filepath):

	L = list(time.asctime(time.localtime(time.time())).split(' '))
	filename = L[0] + '-' + L[1] + '-' + L[5] + '.bin'
	file = os.path.join(filepath, filename)
		
	if os.path.exists(file):
		encrypt_text = open(file,'rb').read()
		encrypt_text = encrypt_text.decode('unicode-escape').encode('latin-1')
			
		text = decrypt(encrypt_text)
		textbox(text)
			
	else:
		text = textbox()

	encrypt_text = encrypt(text)
		
	with open(file,'w') as f:

		f.write(str(encrypt_text).split("b'")[1].split("'")[0])
		f.close()
		
def Read():
	'''
	use fileopenbox
	'''
	filename = fileopenbox(default='./daily/*.bin')
	encrypt_text = open(filename,'rb').read()
	encrypt_text = encrypt_text.decode('unicode-escape').encode('latin-1')
			
	text = decrypt(encrypt_text)
	msgbox(text)
	
def choose_mode():
	'''
	use choicebox
	'''
	msg = 'choose the operating mode'
	title = 'secret daily'
	choices = ['Read','Write','Quit']
	
	choice = choicebox(msg, title, choices)
	
	if choice == 'Read':
		Read()
	elif choice == 'Write':
		Write(filepath = './daily/')
	else:
		sys.exit(0)
	

def encrypt(text):
	return cipher.encrypt(pad(text))


def decrypt(encrypt_text):
	return cipher.decrypt(encrypt_text)


# Write(filepath = "./daily/")

def identify():
	pic1 = make_photo('./')
	confidence = face_recognition(pic1)
	_continue = is_same_person(confidence)
	
	os.remove(pic1)
	return _continue

def main():
	if identify() == True:
		choose_mode()
	else:
		msgbox('Access Denied !')

if __name__ == '__main__':
	main()