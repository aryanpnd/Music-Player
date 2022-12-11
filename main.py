from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import os
from PIL import ImageTk,Image


aryan1 = tk.ThemedTk()
aryan1.get_themes()
aryan1.set_theme("scidmint")
mixer.init()


# background image by PIL
background_main = Image.open(r'images/background_sample.png')
load_background = ImageTk.PhotoImage(background_main)
background1 = Label(aryan1, image = load_background)
background1.place(x=0, y=0)

# geometry and window
aryan1.geometry('500x623')
aryan1.minsize(500,623)
aryan1.maxsize(500,623)
aryan1.title('My Player')
aryan1.iconbitmap(r'images/image.ico')

# windows title
title_main = PhotoImage(file='images/music player title.png')
title_lable = Label(aryan1, image=title_main, bd=0, bg='#000000')
title_lable.pack(pady=20)




# menu bar
def open_files():
    global song_name
    song_name = filedialog.askopenfilename()

def show_info():
        tkinter.messagebox.showinfo('About Music Player',
                                    'This MP3 Player was Developed by\n'
                                    'Aryan using Python\'s Tkinter')

menubar = Menu(aryan1)
filemenu = Menu(menubar, tearoff=0, bg='black')
filemenu.add_command(label="Open", foreground='white', command=open_files)
filemenu.add_command(label="Exit", command=aryan1.destroy, foreground='red')
menubar.add_cascade(label="File", menu=filemenu)

About = Menu(menubar, tearoff=0, bg='black')
About.add_command(label="About...", foreground='blue', command=show_info)
menubar.add_cascade(label="About", menu=About)


# MUSIC ICON
photo = PhotoImage(file='images/music.png')
MP3_image=Button(aryan1, image=photo, bg='#000000', activebackground='#000000'
                 ,command=open_files, bd=0)
MP3_image.pack(pady=20)


# status bar
status_bar = Label(aryan1, text='Welcome To Aryan\'s Music player....,', relief=RIDGE, anchor=W,
                   bg='#F7D76A', bd='0',font='bold')
status_bar.pack(side=BOTTOM, fill=X)


# Displaying song name
display_section_frame = Frame(aryan1, bd=5 ,bg='black')
display_section_frame.pack(pady=20)
display_section = Label(display_section_frame, bg='black', fg='white')
display_section.pack()

def display_song():
    display_section['text'] = os.path.basename(song_name)


# STILL WORKING ON IT : )
# displaying song lenght
# display_section_frame2 = Frame(aryan1, bd=5 ,bg='black')
# display_section_frame2.pack(pady=20)
# display_section2 = Label(display_section_frame2, text='00:00',bg='black', fg='white')
# display_section2.pack()

# def display_song_lenght(): # only working for WAV file
#     display_section2['text'] = os.path.basename(song_name)
#     song_lenght = mixer.sound(song_name)
#     lenght = song_lenght.get_lenght()
#     print(song_lenght)




# making function for buttons

def play_music():
    global paused
    mixer.music.pause()
    if paused:
        mixer.music.unpause()
        status_bar['text'] = 'Status: Playing', os.path.basename(song_name)
        paused = FALSE
    else:
        try:
            mixer.music.load(song_name)
            mixer.music.play()
            status_bar['text'] = 'Status: PAUSED', os.path.basename(song_name)
            # display_song()

        except:
            status_bar['text'] = 'Status: No files are found'
            tkinter.messagebox.showerror('NO FILES ARE FOUND\n',
                                         'Sorry no files are found in queue\n'
                                         'try to select some from file menu\n'
                                         'or click on MUSIC icon to go to files')

def stop_music():
    try:
        mixer.music.load(song_name)
        status_bar['text'] = 'Status: Stopped'
        mixer.music.stop()
    except:
        status_bar['text'] = 'Status: No files are found'
        tkinter.messagebox.showerror('NO FILES ARE FOUND\n',
                                     'Sorry no files are found in queue\n'
                                     'try to select some from file menu\n'
                                     'or click on MUSIC icon to go to files')

paused = FALSE
def pause_music():
        global paused
        paused = True
        mixer.music.pause()
        status_bar['text'] = 'Status: Paused...'


def increase_volume(val):
    vol = float(val)/100
    mixer.music.set_volume(vol)


muted = FALSE
def mutebutton():
    global muted
    if muted:
        mixer.music.set_volume(0.2)
        muting_button.configure(image=photo6)
        muted = FALSE
        volume_slider.set(50)
    else:
        mixer.music.set_volume(0)
        muting_button.configure(image=photo5)
        muted = TRUE


# frames
mediabuttons_frames = Frame(aryan1,  bd='0', bg='#000000')
mediabuttons_frames.pack(pady=20)

volumebuttons_frames = Frame(aryan1, bd='0', bg='#000000')
volumebuttons_frames.config(background='#000000')
volumebuttons_frames.pack(pady=20)


# Media buttons

photo2 = PhotoImage(file='images/play.png')
play_button = Button(mediabuttons_frames, image=photo2, bg='#000000', command=play_music, bd=0,
                      activebackground='#000000')
play_button.pack(side=LEFT, padx=5)


photo3 = PhotoImage(file='images/stop.png')
stop_button = Button(mediabuttons_frames, image=photo3, bg='#000000', command=stop_music, bd=0,
                      activebackground='#000000')
stop_button.pack(side=LEFT, padx=5)


photo4 = PhotoImage(file='images/pause.png')
pause_button = Button(mediabuttons_frames, image=photo4, bg='#000000', command=pause_music,
                      bd=0, activebackground='#000000')
pause_button.pack(side=LEFT, padx=5)


photo5 = PhotoImage(file='images/mute.png')
photo6 = PhotoImage(file='images/unmute.png')
muting_button = Button(volumebuttons_frames, image=photo6, bg='#000000', bd=0,
                      activebackground = '#000000', command=mutebutton)
muting_button.pack(side=LEFT, padx=8)



volume_slider = ttk.Scale(volumebuttons_frames, from_=0, to=100,
                  orient=HORIZONTAL,len=200, command=increase_volume)
volume_slider.set(50)
mixer.music.set_volume(50)
volume_slider.pack(side=BOTTOM)


# copyright statements
copyright_statement_frame = Frame(aryan1, bg='#000000',bd=0)
copyright_statement_frame.pack(pady=20)

def clickme_for_copyright():
    tkinter.messagebox.showinfo('COPYRIGHT',
                                'Copyright © 2020 ARYAN PANDEY\n'
                                'All Rights reserved XD')

copyright_photo = PhotoImage(file='images/copyright.png')
C = Button(copyright_statement_frame,image=copyright_photo, bd=0, command=clickme_for_copyright, bg='#000000'
           , activebackground='#000000')
C.pack()



aryan1.configure()
aryan1.config(menu=menubar)
aryan1.mainloop()