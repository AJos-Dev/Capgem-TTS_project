from cProfile import label
from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import speed
from tkinter.filedialog import askopenfilename
from backend import load_voices
from backend import *

#Executed once play button clicked.

language = "english"
gender_of_text = "male"
speed_of_text = "fast"


def ready_to_play():
    global volume
    load_voices()
    volume = slider.get()
    ptt(filename, gender_of_text, speed_of_text, language, volume)


#Put the backend code in here - use all parameters.
def ptt(filename, gender_of_text, speed_of_text, language, volume):
    if gender_of_text == "male":
        gender_of_text = True
    else:
        gender_of_text = False
    text_to_speech(pdf_to_text(filename),language, gender_of_text, speed_of_text, volume)

#Functions that set language, speed and gender.
def english(): 
    global language
    language = "english"

def spanish(): 
    global language
    language = "spanish"

def french(): 
    global language    
    language = "french"
 
def german(): 
    global language 
    language = "german"

def hindi(): 
    global language
    language = "hindi"

def male():
    global gender_of_text
    gender_of_text = "male"

def female():
    global gender_of_text
    gender_of_text = "female"

def fast():
    global speed_of_text
    speed_of_text = "fast"

def medium():
    global speed_of_text
    speed_of_text = "medium"

def slow():
    global speed_of_text
    speed_of_text = "slow"

#File is pulled into variable = filename

def file_select():
    global filename
    filename = askopenfilename()


root = Tk()
menubar = Menu(root)
root.title("PDF to Speech APP")


#Dimensions

window_width = 670
window_height = 250

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

upload = Button(root, bg='Grey', width = 15, command=file_select, text="Upload PDF")
upload.grid(row=3, column =0)

"""
pvmenu = Menu(menubar, tearoff=0)
pvmenu.add_command(label="Upload", command=file_select)
menubar.add_cascade(label="Upload PDF", menu=pvmenu)


Gendermenu = Menu(menubar, tearoff=0)
Gendermenu.add_command(label="Male", command=male)
Gendermenu.add_command(label="Female", command=female)
menubar.add_cascade(label="Gender", menu=Gendermenu)
"""

genderl = tk.Label(root, bg='white', width=20, text='Gender')
genderl.grid(row =0, column=1)
gender = tk.IntVar()
g1 = tk.Checkbutton(root, text='Male',variable=gender, onvalue=0, offvalue=0, command=male)
g1.grid(row=1, column=1)
g2 = tk.Checkbutton(root, text='Female',variable=gender, onvalue=1, offvalue=1, command=female)
g2.grid(row=2, column=1)

"""
fsmenu = Menu(menubar, tearoff=1)
fsmenu.add_command(label="Fast", command=hello)
fsmenu.add_command(label="Medium", command=hello)
fsmenu.add_command(label="Slow", command=hello)
menubar.add_cascade(label="Speed", menu=fsmenu)
"""

speedl = tk.Label(root, bg='white', width=20, text='Speed')
speedl.grid(row=0, column=2)
speed = tk.IntVar()
sf = tk.Checkbutton(root, text='Fast',variable=speed, onvalue=0, offvalue=0, command=fast)
sf.grid(row=1, column=2)
sg = tk.Checkbutton(root, text='Medium',variable=speed, onvalue=1, offvalue=1, command=medium)
sg.grid(row=2, column=2)
ss = tk.Checkbutton(root, text='Slow',variable=speed, onvalue=2, offvalue=2, command=slow)
ss.grid(row=3, column=2)

"""
languagesmenu = Menu(menubar, tearoff=1)
languagesmenu.add_command(label="English", command=english)
languagesmenu.add_command(label="Spanish", command=spanish)
languagesmenu.add_command(label="French", command=french)
languagesmenu.add_command(label="German", command=german)
languagesmenu.add_command(label="Hindi", command=hindi)
menubar.add_cascade(label="Language", menu=languagesmenu)
"""

langl = tk.Label(root, bg='white', width=20, text='Languages')
langl.grid(row=0, column=3)
lang = tk.IntVar()
l_eng = tk.Checkbutton(root, text='English',variable=lang, onvalue=0, offvalue=0, command=english)
l_eng.grid(row=1, column=3)
l_spa = tk.Checkbutton(root, text='Spanish',variable=lang, onvalue=1, offvalue=1, command=spanish)
l_spa.grid(row=2, column=3)
l_fra = tk.Checkbutton(root, text='French',variable=lang, onvalue=2, offvalue=2, command=french)
l_fra.grid(row=3, column=3)
l_ger = tk.Checkbutton(root, text='German',variable=lang, onvalue=3, offvalue=3, command=german)
l_ger.grid(row=4, column=3)
l_hin = tk.Checkbutton(root, text='Hindi',variable=lang, onvalue=4, offvalue=4, command=hindi)
l_hin.grid(row=5, column=3)


volumel = tk.Label(root, bg='white', width=20, text='Volume')
volumel.grid(row=8, column=2)

slider = Scale(
    root,
    from_=0,
    to=100,
    tickinterval=25,
    orient=HORIZONTAL
    
)

slider.set(50)

slider.grid(row=12, column = 2)


play = Button(root, bg='Red', width = 15, command=ready_to_play, text="Play")
play.grid(row=3, column =5)

"""
pvmenu = Menu(menubar, tearoff=1)
pvmenu.add_command(label="Pause", command=hello)
pvmenu.add_command(label="Play", command=hello)
menubar.add_cascade(label="Pause/Play", menu=pvmenu)
"""
root.config(menu=menubar)
root.mainloop()
