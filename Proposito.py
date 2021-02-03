#!/usr/bin/python
# -*- coding: utf-8 -*-
import PropositoBD as BD
from sqlite3 import Error
import sys
import Cifrado as CF
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Proposito')
root.geometry('250x200')
root.minsize(250,200)

con = BD.sql_connection()

def cifrado():
    final = ""
    #indice = [3,5,8,10,11,15,20]
    text = texto.get()

    for i in text:
        if i in CF.num: 
            pos_letra = CF.num.get(i)
            final+= pos_letra

    label = Label(text=final, fg="red")
    label.place(x=10,y=120) 

    entities = (final, text)
    BD.sql_insert(con, entities)

def contraseña():
    ventana = tk.Toplevel()
    ventana.geometry('150x100')

    contraseña = tk.StringVar()
    decifrar = Entry(ventana, show="*", textvariable= contraseña)
    decifrar.place(x=13,y=20)

    entrar = Button(ventana, text="Entrar",
            command= lambda: descifrado(contraseña))
    entrar.place(x=55,y=50)
    

def descifrado(contraseña):
    if contraseña.get() == CF.contra:
        entitie = (texto.get())
        rows = BD.sql_fetch(con, entitie)

        if rows:
            label = Label(root, text=rows, fg="red")
            label.place(x=20,y=120)
        else:
            root.destroy()
    else:
        root.destroy()

###################### INICIO ################################    
label = Label(text="Ingresar palabra a cifrar")
label.place(x=60,y=10)

texto = tk.StringVar()
ingresar = Entry(textvariable= texto)
ingresar.place(x=63,y=40)

boton = Button(root, text="Crear Cifrado", command=cifrado)
boton.place(x=85, y=75)

descifrar = Button(root, text="Descifrar", command= contraseña)
descifrar.place(x=10,y=170)

quitar = Button(root, text="Quitar", fg="red", command= root.destroy)
quitar.place(x=200,y=170)

root.mainloop()

