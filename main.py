import os
import pygame
import sys
import fileinput
from tkinter import *
from os import listdir
from tkinter.filedialog import *
from pygame import*
mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
def play():
    global name
    name=listbox.get(ACTIVE)
    file="music/"+str(name)
    mixer.music.load(file)
    mixer.music.play()
    label()

def label():
    global name
    title.configure(text=name)

def stop():
    pygame.mixer.music.stop()

def next_selection():
    file=listbox.curselection()
    next_selection=0
    if len(file)>0:
        last_selection = int(file[-1])
        listbox.selection_clear(file)
        if last_selection < listbox.size() - 1:
            next_selection = last_selection + 1
    listbox.activate(next_selection)
    listbox.selection_set(next_selection)
    play()

def previous_selection():
    file=listbox.curselection()
    previous_selection=0
    if len (file)>0:
        first_selection=int(file[0])
        listbox.selection_clear(file)
        if first_selection < listbox.size()+1:
            previous_selection=first_selection-1
    listbox.activate(previous_selection)
    listbox.selection_set(previous_selection)
    play()
    

def open():
    file=askopenfilename()
    mixer.music.load(file)
    listbox.insert(END,file)
    return mixer.music.load

def directory():
    path=os.listdir("Music")
    music = filter(lambda x: x.endswith('.wav'), path)
    for filename in music:
        listbox.insert(END,filename)

def volume(self):
    n=sca.get()
    pygame.mixer.music.set_volume(n)
    ns=sca.get()
    ns=ns*100
    label=Label(text=(ns,"%"))
    label.grid(row=3,column=3)

root=Tk()

m=Menu(root)
root.config(menu=m)

fm=Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open",command_=open)

playbut=PhotoImage(file="icons/play-button.png")
but=Button(root,image=playbut,relief=FLAT,command=play)
but.grid(row=1,column=1)

pausebut=PhotoImage(file="icons/stop.png")
but1=Button(root,image=pausebut,relief=FLAT,command=stop)
but1.grid(row=1,column=2)

forwardbut=PhotoImage(file="icons/forward.png")
but2=Button(root,image=forwardbut,command=next_selection,relief=FLAT)
but2.grid(row=1,column=3,sticky="w")

backbut=PhotoImage(file="icons/back.png")
but3=Button(root,image=backbut,command=previous_selection,relief=FLAT)
but3.grid(row=1,column=0,sticky="e")

sca=Scale(root,orient=HORIZONTAL,length=100,from_=0,to=1,resolution=0.1, command=volume, showvalue=FALSE)
sca.grid(row=2,column=3)
sca.set(1)

listbox=Listbox(root,height=4,width=60,selectmode=SINGLE)
listbox.grid(row=0,column=0,columnspan=4)

title=Label(root)
title.grid(row=3,column=0,columnspan=3)

directory()
root.mainloop()
pygame.quit()
