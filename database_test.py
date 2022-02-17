# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:04:00 2021

@author: yiplf
"""


import pyodbc
import pandas as pd
import sqlalchemy as sa

"""
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-4QJ7B1K\SQLEXPRESS;'
                      'Database=telco;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
"""

def write():
    cursor.execute("INSERT INTO [telco].[dbo].[telcom]\
                   (customerID) VALUES('0000-XXXXX')")
    conn.commit()

def delete():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM [telco].[dbo].[telcom]\
                   WHERE customerID = '0000-XXXXX'")
    conn.commit()
    
def read():
    id_list =[]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM [telco].[dbo].[telcom]\
                   WHERE customerID = '0000-XXXXX'")
    for row in cursor:
        id_list.append(row[0])
    return id_list          
    conn.commit()

def search():
    query = "SELECT * FROM [telco].[dbo].[telcom]\
            WHERE customerID = '7590-VHVEG'"
    data = pd.read_sql(query,conn)
    return data

#write()
#delete()
#read()
def append():
    pass