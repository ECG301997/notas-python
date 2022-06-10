
import sqlite3
from tkinter import messagebox as MessageBox
from tkinter  import ttk
from tkinter import *
import os
from generateCsv import fileCsv

class qualification :
    db_name = 'notas.db'
   
    def __init__(self,window):
        self.wind = window
        self.wind.title('Notas')
      
        #frame container
        frame = LabelFrame(self.wind,text='Registrar Estudiante')
        frame.grid(row= 0,column=0 ,columnspan=3,pady= 20)        

       #Name input 
        ttk.Label(frame,text='Nombres :').grid(row=1 ,column='0')
        self.name= Entry(frame)
        #con focus nos pone el cursor en nuestro inputd
        self.name.focus()
        self.name.grid(row=1 ,column=1)
        
        #lasName input
        ttk.Label(frame,text='Apellidos : ').grid(row=2 ,column= '0')
        self.apellidos = Entry(frame)
        self.apellidos.grid(row=2,column=1)
        
        #notaUno
        ttk.Label(frame,text='Nota : ').grid(row=3 ,column= '0')
        self.notaUno = Entry(frame)
        self.notaUno.grid(row=3,column=1)
        
        
        #notaDos
        ttk.Label(frame,text='Nota : ').grid(row=4 ,column= '0')
        self.notaDos = Entry(frame)
        self.notaDos.grid(row=4,column=1)
        
        #notaTres
        ttk.Label(frame,text='Nota : ').grid(row=5 ,column= '0')
        self.notaTres = Entry(frame)
        self.notaTres.grid(row=5,column=1)
        
        # button
        buuton = ttk.Button(frame,text='send',command= self.insert_product)
        buuton.grid(row=7,columnspan=2, sticky= W+E)
        
        # buuton2 = ttk.Button(frame,text='generar csv ',command= self.openFile)
        # buuton2.grid(row=8,columnspan=2, sticky= W+E)
        #table
        #creación de tabla
        self.table = ttk.Treeview(height=10,columns=7)        
        #coordenadas para mostrar la tabla
        self.table.grid(row= 4,column=0,columnspan=2)
        #encabezados con el texto centrado
        self.table.heading('#0',text='Nombres',anchor= CENTER)
        self.table.heading('#1',text='Nota Final',anchor=CENTER)
    
     
        
        self.get_products()
      
        
    #conexion db
    def _run_query(Self,query,Parameters=()):
        with sqlite3.connect(Self.db_name) as conn:
            cursor =conn.cursor()
            result =cursor.execute(query,Parameters)
            conn.commit()
            return result
        
    #get products
    def get_products(self):
        
        records =self.table.get_children()
        for elements in records :
            self.table.delete(elements)
        
        query ='SELECT * FROM estudiantes '
        db_rows= self._run_query(query)
        
        for row in db_rows:
            print(row)
            self.table.insert('',0,text=row[1],values=row[2])
            
            
    def validation(self):
        return len(self.name.get()) !=0 and len(self.apellidos.get())  !=0 and len(self.notaUno.get()) !=0  and len(self.notaDos.get()) !=0  and len(self.notaTres.get()) !=0
    
    
    def insert_product(self):
        
        if self.validation():
            
            n1 = float(self.notaUno.get())
            n2=  float(self.notaDos.get())
            n3 = float(self.notaTres.get())
            result = round(((n1*35/100)+(n2*35/100)+(n3*30/100)/3),1)
            if result < 3.0:
                MessageBox.showinfo('','el estudiante no aprobo')
                
            else:
               
                MessageBox.showinfo('','el estudiante aprobo')
                
                query = 'INSERT INTO estudiantes VALUES(NULL,?,?)'
                Parameters =  (self.name.get(),result)
                self._run_query(query,Parameters)
                MessageBox.showinfo('','productos enviados correctamente!!')
                #create csv 
                fileCsv(self.name.get(),self.apellidos.get(),self.notaUno.get(),self.notaDos.get(),self.notaTres.get(),result)
          
        else :
              MessageBox.showerror('','datos requeridos') 
        self.get_products()    
            
        
        

  

       

         
if __name__ == '__main__':
     window =  Tk()
     application = qualification(window)
     window.mainloop()
     window.configure(bg='#49A')