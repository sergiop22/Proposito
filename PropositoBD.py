#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error

def sql_connection():

    try:
        base = sqlite3.connect('Proposito.db')

        return base

    except Error:
        print(Error)

def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO Proposito(cifrado, descifrado) VALUES(?, ?)', entities)
    
    con.commit()

def sql_fetch(con, entitie):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT descifrado FROM Proposito WHERE cifrado=?', (entitie,))

    rows = cursorObj.fetchall()

    return rows