import tkinter as tk
from tkinter import *
from tkinter import ttk,PhotoImage
from tkinter import scrolledtext as st
import tkinter.font as tkFont
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import  ttk, scrolledtext
import json
from io import open
import csv
from tkinter.font import Font
from csv import writer, reader
import random
import os.path, time
import os
import webbrowser
import mysql.connector
from mysql.connector.errors import DatabaseError



if os.path.exists("usuario.txt") == True:
        os.remove("usuario.txt")
if os.path.exists("contraseña.txt") == True:
        os.remove("contraseña.txt")


def recuperar():
    user= usuario.get()
    cont= contrasena.get()

    f = open("usuario.txt", "a")
    f.write(user)
    f.close()
    f = open("contraseña.txt", "a")
    f.write(cont)
    f.close()
    raiz.destroy()
   



raiz = Tk()
raiz.title("Ingreso datos BD")
raiz.geometry("300x150")
tk.Label(raiz, text="Usuario").pack()
usuario = tk.Entry(raiz)
usuario.insert(0, "completar")
usuario.bind("<Button-1>", lambda e: usuario.delete(0, tk.END))
usuario.pack()



tk.Label(raiz, text="Contraseña").pack()
contrasena = tk.Entry(raiz)
contrasena.insert(0, "completar")
contrasena.bind("<Button-1>", lambda e: contrasena.delete(0, tk.END))
contrasena.pack()
        
        
tk.Button(raiz, text="Entrar", command= recuperar).pack()

raiz.mainloop()


x = open("usuario.txt")
us=(x.read())
x.close()

y = open("contraseña.txt")
con=(y.read())
y.close()

os.remove("usuario.txt")
os.remove("contraseña.txt")





"""datos de conneccion para todo el programa, cambiar por usuario y password segun corresponda"""




try:
    config = {'user': us,
          'password': con,
          'host': '127.0.0.1',
          'database': 'recetario'}
    
    
    conn = mysql.connector.connect(**config)
    conn.close()
except DatabaseError as err:
    if 'Unknown database' in str(err):
       config = {'user': us,
          'password': con,
          'host': '127.0.0.1'}
       conn = mysql.connector.connect(**config)
       cur = conn.cursor()
       cur.execute("CREATE DATABASE IF NOT EXISTS recetario")
       cur.execute("USE recetario")
       receta = """CREATE table IF NOT EXISTS receta (
           id_recetas tinyint NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY, 
           nombre varchar(100) NOT NULL, 
           ingredientes TINYTEXT NOT NULL, 
           preparacion TEXT NOT NULL
           ) ENGINE=InnoDB;"""
       cur.execute(receta)
       conn.commit()
       cur.close()
       conn.close()
    else:
        print("error de conneccion T_T ", err)
        
config = {'user': us,
          'password': con,
          'host': '127.0.0.1',
          'database': 'recetario'}




class App(tk.Tk):
    def __init__(self, root):
        """ abre una ventana raiz, inicio del programa"""
        #stitulo
        root.title("Mis recetas")
        root['bg'] = '#B28D8E'
        #ventana principal
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.imagen= PhotoImage(file="Imagenes/fondo.gif")
        Label(root,image=self.imagen).place(x=25, y=0)
        icono = tk.PhotoImage(file="Imagenes/favicon.png")
        root.iconphoto(True, icono)

        #botones
        self.img_boton = tk.PhotoImage(file="Imagenes/bt01.gif")
        GButton_976=tk.Button(root)
        GButton_976["activebackground"] = "#0f7d7e"
        GButton_976["activeforeground"] = "#ffffff"
        GButton_976["bg"] = "#a4d9a3"
        GButton_976["image"] = self.img_boton
        GButton_976["compound"]= LEFT
        ft = tkFont.Font(family="Courier", size=20, weight="bold")
        GButton_976["font"] = ft
        GButton_976["fg"] = "#393d49"
        GButton_976["justify"] = "center"
        GButton_976["text"] = "Nueva Receta"
        GButton_976["relief"] = "raised"
        GButton_976.place(x=0,y=90,width=600,height=90)
        GButton_976["command"] = self.crearReceta
        
        self.img_boton2 = tk.PhotoImage(file="Imagenes/bt02.gif")
        GButton_806=tk.Button(root)
        GButton_806["activebackground"] = "#5fb878"
        GButton_806["activeforeground"] = "#ffffff"
        GButton_806["bg"] = "#c6d7a0"
        GButton_806["image"] = self.img_boton2
        GButton_806["compound"]= LEFT
        ft = tkFont.Font(family="Courier", size=16, weight="bold")
        GButton_806["font"] = ft
        GButton_806["fg"] = "#000000"
        GButton_806["justify"] = "center"
        GButton_806["text"] = "Lista de recetas"
        GButton_806.place(x=120,y=220,width=400,height=90)
        GButton_806["command"] = self.listaRecetas

        self.img_boton3 = tk.PhotoImage(file="Imagenes/bt03.gif")
        GButton_418=tk.Button(root)
        GButton_418["activebackground"] = "#fec49b"
        GButton_418["activeforeground"] = "#ffffff"
        GButton_418["bg"] = "#fbdcb0"
        GButton_418["image"] = self.img_boton3
        GButton_418["compound"]= LEFT
        ft = tkFont.Font(family="Courier", size=16, weight="bold")
        GButton_418["font"] = ft
        GButton_418["fg"] = "#000000"
        GButton_418["justify"] = "center"
        GButton_418["text"] = "Receta al azar"
        GButton_418.place(x=120,y=340,width=400,height=90)
        GButton_418["command"] = self.recetaazar
        
    #funciones
    def abrir_lista(self, list):
      """ abre una ventana de lista de recetas"""
      vt2 = tk.Toplevel()
      app2 = Listarecetas(vt2, list)
      vt2.mainloop()

    def crearReceta(self):
      """ abre una ventana de creacion de recetas"""
      vt = tk.Toplevel()
      app2 = CrearReceta(vt)
      vt.mainloop()
    
    def abrir_receta(self, nomb, ingr, prep):
      """ abre una ventana del lector de recetas"""
      vt = tk.Toplevel()
      app2 = Receta(vt, nomb, ingr, prep)
      vt.mainloop()

    def recetaazar(self):
        """ genera un numero al azar, entre la cantidad de recetas almacenadas"""
        """recetar = opencsv()
        azar=random.randint(1, len(recetar)-1)"""
        
   
        conn = mysql.connector.connect(**config)
        
        consulta = """SELECT id_recetas FROM recetario.receta;"""
        cur = conn.cursor()
        cur.execute(consulta)
        resultado = cur.fetchall()
        valor=random.choice(resultado)
        
        s = ''.join(map(str, valor))
        tw=s.replace("',)","")
        azar=int(tw.replace("('",""))
        
        
        self.obtener(azar)
        
        cur.close()
        conn.close()
  
    def formateostr(self, lista):
        s = ''.join(map(str, lista))
        tw=s.replace("',)","")
        no=tw.replace("('","")
        return no

    def obtener(self,numr):
        """obtiene indice de la receta para abrirlo y formatea los ingredientes para presentar""" 
         

        conn = mysql.connector.connect(**config)
        
        consulta = """SELECT nombre, ingredientes, preparacion FROM receta WHERE id_recetas = %s"""
        cur = conn.cursor()
        cur.execute(consulta, (numr,))
        resul = cur.fetchall()
        cur.close()
        conn.close()
        
        nomb=self.formateostr(resul[0][0])
        prep=self.formateostr(resul[0][2])
        ot=self.formateostr(resul[0][1])
        tx = str(ot)
        tw=tx.replace('")',"")
        tt=tw.replace('("',"")
        tu=tt.replace("}","")
        tz=tu.replace("{","")
        ty=tz.replace(",", "\n \n")
        ingr= ty.replace(":", f"    |🄲🄰🄽🅃🄸🄳🄰🄳|》   ")
        self.abrir_receta(nomb, ingr, prep)

    def listaRecetas(self):
        """ importa lista de recetas almacenadas"""
        mostrarlista=opencsv()
        self.abrir_lista(mostrarlista)


class CrearReceta(tk.Toplevel): #crear recetas
    def __init__(self,root):
        """ abre una ventana secundaria de creacion de receta"""
        try:
            os.remove("ingredientes.json")
        except FileNotFoundError:
            pass

        try:
            os.remove("tiempo.txt")
        except FileNotFoundError:
            pass
        

        self.root = root
        #titulo2
        root.title("Nueva Receta uwu")
        #ventana2 ajustes
        root['bg'] = '#B28D8E'
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.transient(app)
        root.focus_set()

        #lavel, entradas, botones
        GLabel_424=tk.Label(self.root)
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GLabel_424["bg"] = "#fbdcb0"
        GLabel_424["font"] = ft
        GLabel_424["fg"] = "#000000"
        GLabel_424["justify"] = "center"
        GLabel_424["text"] = "Ingresar Nombre de la Receta"
        GLabel_424.place(x=0,y=10,width=270,height=30)

        GLineEdit_832=tk.Entry(self.root)
        GLineEdit_832["borderwidth"] = "1px"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GLineEdit_832["font"] = ft
        GLineEdit_832["fg"] = "#333333"
        GLineEdit_832["justify"] = "center"
        GLineEdit_832["text"] = ""
        GLineEdit_832.place(x=30,y=50,width=541,height=58)
        self.nomb=GLineEdit_832
       
        self.img_boton4 = tk.PhotoImage(file="Imagenes/bt04.gif")
        GButton_381=tk.Button(self.root)
        GButton_381["activebackground"] = "#5fb878"
        GButton_381["activeforeground"] = "#ffffff"
        GButton_381["bg"] = "#c6d7a0"
        GButton_381["image"] = self.img_boton4
        GButton_381["compound"]= LEFT
        ft = tkFont.Font(family="Courier", size=16, weight="bold")
        GButton_381["font"] = ft
        GButton_381["fg"] = "#000000"
        GButton_381["justify"] = "center"
        GButton_381["text"] = "Ingresar Ingredientes"
        GButton_381.place(x=30,y=130,width=538,height=80)
        GButton_381["command"] = self.ingresaringrediente

        GButton_400=tk.Button(root)
        GButton_400["bg"] = "#eeeeee"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GButton_400["font"] = ft
        GButton_400["fg"] = "#000000"
        GButton_400["justify"] = "center"
        GButton_400["text"] = " Tabla Medidas "
        GButton_400.place(x=400,y=210,width=150,height=30)
        GButton_400["command"] = self.tablamedidas

        GLabel_507=tk.Label(self.root)
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GLabel_507["bg"] = "#fbdcb0"
        GLabel_507["font"] = ft
        GLabel_507["fg"] = "#000000"
        GLabel_507["justify"] = "center"
        GLabel_507["text"] = "Ingresar Pasos de Preparación"
        GLabel_507.place(x=0,y=250,width=270,height=30)
        
        self.stt=st.ScrolledText(self.root, width=50,height=10)
        self.stt.place(x=30,y=290,width=541,height=148)
        
        GButton_23=tk.Button(self.root)
        GButton_23["activebackground"] = "#0f7d7e"
        GButton_23["activeforeground"] = "#ffffff"
        GButton_23["bg"] = "#a4d9a3"
        ft = tkFont.Font(family="Courier", size=12, weight="bold")
        GButton_23["font"] = ft
        GButton_23["fg"] = "#000000"
        GButton_23["justify"] = "center"
        GButton_23["text"] = "Guardar"
        GButton_23.place(x=100,y=450,width=402,height=30)
        GButton_23["command"] = self.comprobaryGuardar

    def tablamedidas(self):
       """ abre una ventana secundaria para mostrar una tabla de equivalencias de medidas"""
       ventana_secundaria = tk.Toplevel()
       img = PhotoImage(file="Imagenes/tabla.gif")
       Label(ventana_secundaria, image=img).pack()
       ventana_secundaria.mainloop() 

    def ingresaringrediente(self):
        """ importa los ingredientes en diccionario para emparejar, ingrediente=clave, antidad/medida=valor """
        ingredientes = {}
        cantIngredientes = None
    
        while type(cantIngredientes) != int:
            try:
              cantIngredientes = int(tkinter.simpledialog.askstring("Cantidad", "Ingrese la Cantidad de Ingredientes ",initialvalue= 1 ,parent=self.root))
            except ValueError:
                tkinter.messagebox.showerror("Error", "Ingresar Solo Número")
        for i in range(cantIngredientes):
            ingrediente = tkinter.simpledialog.askstring("Ingredientes", "Ingresar Ingrediente (No dejar casilla vacia)", initialvalue="-" ,parent=self.root)
            medida = tkinter.simpledialog.askstring("Cantidad / Medida", """   Ingresar Cantidad y Medida
(ej; pizca, kg, taza, litro, unidades)
    (No dejar casilla vacia)""", initialvalue="-",parent=self.root)
            ingredientes[ingrediente] = medida
        with open("ingredientes.json", "w", encoding="utf-8") as jsonfile:
            json.dump(ingredientes, jsonfile)
        
    def guardar_receta(self):
        """ guarda receta creada"""
        prepa=str(self.stt.get("1.0",tk.END))
        with open('ingredientes.json', 'r', encoding="utf-8") as jsonfile:
            ingre = json.load(jsonfile)

        with open("tiempo.txt","w") as tiemp:
            tiemp.write('')
        ruta="tiempo.txt"
        cree="Creado {}".format(time.strftime("%d-%m-%Y %H:%M:%S", time.strptime(time.ctime(os.path.getctime(ruta)))))
        tpre = tkinter.simpledialog.askstring("Preparación", "Ingresar Tiempo total de Preparación (en Minutos)",initialvalue="--(no especificado)--" ,parent=self.root)
        tcoc = tkinter.simpledialog.askstring("Cocción", "Ingresar Tiempo de Cocción (en Minutos)" ,initialvalue="--(no especificado)--",parent=self.root)
        if tpre=="--(no especificado)--":
            tpref= tpre
        else:
            tpref= "Tiempo de Preparación " + tpre + " Minutos"
        if tcoc=="--(no especificado)--":
            tcocf= tcoc
        else:
            tcocf= "Tiempo de Cocción " + tcoc + " Minutos"
        prepa2=prepa + "\n" + tcocf + "\n" + tpref + "\n" + cree
        
        nomb=str(self.nomb.get())
        
        ingre2 = json.dumps(ingre)
        
        
        conn = mysql.connector.connect(**config)
        
        cursor = conn.cursor()

        ndatos = """INSERT INTO receta(
            nombre, ingredientes, preparacion)
            VALUES (%s, %s, %s);"""
            
        cursor.execute(ndatos, (nomb, ingre2, prepa2))
        conn.commit()
        cursor.close() 
        conn.close()
 
        os.remove("ingredientes.json")
        os.remove("tiempo.txt")
        self.root.destroy()

    def comprobaryGuardar(self):
        """ comprobacion de nombre de receta, para evitar repetidos y evitar datos vacios"""
        comp=self.nomb.get()
        la=opencsv()
        if comp in la:
            tkinter.messagebox.showerror("Error", "Nombre Repetido")
        else:
            if not comp :
                tkinter.messagebox.showerror("Error", "Nombre VACIO")
            else:
                prepa=str(self.stt.get("1.0",tk.END))
                if prepa == "\n" :
                    tkinter.messagebox.showerror("Error", "Preparación VACIA")
                else:
                    verarch=os.path.exists('ingredientes.json')
                    if verarch == FALSE:
                        tkinter.messagebox.showerror("Error", "Ingredientes VACIO")
                    else:
                        self.guardar_receta()


class Receta(tk.Toplevel):
    def __init__(self, root, nomb, ingr, prep):
        """ ventana del lector de recetas"""

        self.nomb=nomb
        self.ingr=ingr
        self.prep=prep
   
        root.title(self.nomb)
        root['bg'] = '#B28D8E'

        width=600
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.imagen= PhotoImage(file="Imagenes/fondo2.gif")
        Label(root,image=self.imagen).place(x=0, y=0)

        label1=tk.Label(root, text = f"  {self.nomb}  ", font = ("Times New Roman", 30), background = "#fbdcb0", foreground = "#B28D8E", wraplength=600,anchor="n")
        label1.grid(column = 0,row = 0)

        label2=tk.Label(root, text = "  Ingredientes  ", font = ("Courier", 20), background = "#fbdcb0", foreground = "#000000")
        label2.grid(column = 0,row = 2)

        text_area = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 56, 
                                      height = 10,
                                      font = ("Times New Roman",
                                              15))
        text_area.grid(column = 0, pady = 10, padx = 10)
        text_area.insert(tk.INSERT, self.ingr)
        text_area.tag_configure("tag_name", justify='center')
        text_area.configure(state ='disabled')
        text_area.tag_add("tag_name", "1.0", "end")
       
        
        label3=tk.Label(root, text = "  Preparación  ", font = ("Courier", 20), background = "#fbdcb0", foreground = "#000000")
        label3.grid(column = 0,row = 4)

        text_area2 = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 70, 
                                      height = 19, 
                                      font = ("Courier",
                                              10))
        text_area2.grid(column = 0, pady = 10, padx = 10)
        text_area2.insert(tk.INSERT, self.prep)
        text_area2.tag_configure("tag_name", justify='left')
        text_area2.configure(state ='disabled')
        text_area2.tag_add("tag_name", "1.0", "end")
        text_area.focus()

        button1=tkinter.Button(root, text=" Ver Imagen(web) ", bg="#a4d9a3", command=self.link_clicked)
        button1.grid(row=6,column=0)

    def link_clicked(self):
        direccion="https://yandex.com/images/search?text="+self.nomb
        webbrowser.open(direccion)

class Listarecetas(tk.Toplevel):

    def __init__(self, root, list):
        """ ventana muestra lista de recetas"""
        self.root = root
        self.list=list
        self.unt=list
        root.title("Lista de Recetas ^_^ ")
        root['bg'] = "#c6d7a0"
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.transient(app)
        root.focus_set()

        self.imagen= PhotoImage(file="Imagenes/fondo3.gif")
        Label(root,image=self.imagen).place(x=5, y=60)

        GLineEdit_981=tk.Entry(root)
        GLineEdit_981["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_981["font"] = ft
        GLineEdit_981["fg"] = "#333333"
        GLineEdit_981["justify"] = "center"
        GLineEdit_981["text"] = "receta a buscar"
        GLineEdit_981.place(x=40,y=10,width=300,height=35)
        self.valbus=GLineEdit_981  # toma valor del entry y lo almacena

        GButton_345=tk.Button(root)
        GButton_345["bg"] = "#fbdcb0"
        ft = tkFont.Font(family='Times',size=12)
        self.img_04 = tk.PhotoImage(file="Imagenes/04.png")
        GButton_345["image"] = self.img_04
        GButton_345["compound"]= LEFT
        GButton_345["font"] = ft
        GButton_345["fg"] = "#000000"
        GButton_345["justify"] = "center"
        GButton_345["text"] = "Buscar Receta"
        GButton_345.place(x=350,y=10,width=220,height=40)
        GButton_345["command"] = self.buscarReceta
        
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL)
        hscrollbar = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        listb = tk.Listbox(self.root, yscrollcommand=scrollbar.set,xscrollcommand=hscrollbar.set, selectmode=tk.SINGLE,font=Font(family="Sans Serif", size=16))
        listb.place(x=100,y=50,width=470,height=370)
        scrollbar.config(command=listb.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        hscrollbar.config(command=listb.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        listb.insert(0, *self.list)
        self.list= listb

        GButton_4421=tk.Button(root)
        GButton_4421["activebackground"] = "#fec49b"
        GButton_4421["activeforeground"] = "#ffffff"
        GButton_4421["bg"] = "#fbdcb0"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        self.img_03 = tk.PhotoImage(file="Imagenes/03.png")
        GButton_4421["image"] = self.img_03
        GButton_4421["compound"]= LEFT
        GButton_4421["font"] = ft
        GButton_4421["fg"] = "#000000"
        GButton_4421["justify"] = "center"
        GButton_4421["text"] = " ABRIR Selección"
        GButton_4421.place(x=20,y=430,width=180,height=40)
        GButton_4421["command"] = self.abrirReceta

        GButton_4003=tk.Button(root)
        GButton_4003["activebackground"] = "#fec49b"
        GButton_4003["activeforeground"] = "#ffffff"
        GButton_4003["bg"] = "#fbdcb0"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        self.img_02 = tk.PhotoImage(file="Imagenes/02.png")
        GButton_4003["image"] = self.img_02
        GButton_4003["compound"]= LEFT
        GButton_4003["font"] = ft
        GButton_4003["fg"] = "#000000"
        GButton_4003["justify"] = "center"
        GButton_4003["text"] = " ELIMINAR Selección"
        GButton_4003.place(x=210,y=430,width=180,height=40)
        GButton_4003["command"] = self.eliminarReceta

        GButton_4008=tk.Button(root)
        GButton_4008["activebackground"] = "#fec49b"
        GButton_4008["activeforeground"] = "#ffffff"
        GButton_4008["bg"] = "#fbdcb0"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        self.img_01 = tk.PhotoImage(file="Imagenes/01.png")
        GButton_4008["image"] = self.img_01
        GButton_4008["compound"]= LEFT
        GButton_4008["font"] = ft
        GButton_4008["fg"] = "#000000"
        GButton_4008["justify"] = "center"
        GButton_4008["text"] = " EDITAR Selección"
        GButton_4008.place(x=400,y=430,width=180,height=40)
        GButton_4008["command"] = self.datosEditar
        
    

    def buscarReceta(self):
        """ busca receta por nombre"""
        """"busqueda y abrir la encontrada"""
        varbus = self.valbus.get()    
        rec = opencsv()
        bandera=0
        
        for i in varbus:
            if i.isalnum() == False:
                if i != " ":
                    tkinter.messagebox.showinfo("No posible","Solo ingresar Letra y/o Numeros")
                    bandera=1
                    break
                  
        if bandera == 0:
           encontrado=[]        
           lisbus=(varbus.lower()).split()
           for e in rec:
               x=e.lower()
               for c in lisbus:
                   if len(c) > 3:
                       if c in x:
                           if not e in encontrado:
                               encontrado.append(e)
                           
        if  encontrado != []:
            self.root.destroy()
            self.abrir_lisNueva(encontrado) 
                
        else:
            tkinter.messagebox.showinfo("Lo Sentimos","Receta No Encontrada")
        
        
    def abrir_lisNueva(self, list):
      """ abre una ventana de lista de recetas"""
      vt2 = tk.Toplevel()
      app2 = Listarecetas(vt2, list)
      vt2.mainloop()

    def formateostr(self, lista):
        s = ''.join(map(str, lista))
        tw=s.replace("',)","")
        no=tw.replace("('","")
        return no
   

    def abrirReceta(self):
        """ importa los datos de la receta seleccionada para el lector de recetas"""
        indices = self.list.curselection()
        rec = self.unt
        
        if indices != (): 
            ind1=str(indices)
            ind2=ind1.replace(',)',"")
            indfor=ind2.replace('(',"")
            indform=int(indfor)
            
            conn = mysql.connector.connect(**config)
        
            consulta = """SELECT nombre, ingredientes, preparacion FROM receta WHERE nombre = %s"""
            cur = conn.cursor()
            cur.execute(consulta, (rec[indform],))
            resul = cur.fetchall()
            cur.close()
            conn.close()
            
            nomb=str(resul[0][0])
            prep=str(resul[0][2])
            ot=self.formateostr(resul[0][1])
            tx = str(ot)
            tw=tx.replace('")',"")
            tt=tw.replace('("',"")
            tu=tt.replace("}","")
            tz=tu.replace("{","")
            ty=tz.replace(",", "\n \n")
            ingr= ty.replace(":", f"    |🄲🄰🄽🅃🄸🄳🄰🄳|》   ")

            self.abrir_receta(nomb, ingr, prep)
        else:
            tkinter.messagebox.showerror("Error", "Ninguna Receta Seleccionada")
        
    def abrir_receta(self, nomb, ingr, prep):
      """ abre ventana lector de receta"""
      vt = tk.Toplevel()
      app2 = Receta(vt, nomb, ingr, prep)
      vt.mainloop()

    def eliminarReceta(self):
        """ elimina receta seleccionada"""
        indices = self.list.curselection()
        if indices != ():
            respuesta=tkinter.messagebox.askyesno("Cuidado", "¿Quiere Borrar la Receta?")
            rec = opencsv()
            
            if respuesta==True:
                ind1=str(indices)
                ind2=ind1.replace(',)',"")
                indfor=ind2.replace('(',"")
                indform=int(indfor)
            
                conn = mysql.connector.connect(**config)
        
                consulta = """DELETE FROM receta WHERE nombre = %s"""
                cur = conn.cursor()
                cur.execute(consulta, (rec[indform],))
                self.list.delete(indices)

                conn.commit()
                cur.close()
                conn.close()

            else:
                pass
        else:
            pass
            
    def datosEditar(self):
        """ importa los datos para edicion de las recetas"""
        indices = self.list.curselection()
        
        if indices != (): 
            self.editarReceta(indices)
        else:
            pass        

    def editarReceta(self, eleg):
        """ abre ventana de edicion de receta"""
        vt = tk.Toplevel()
        app2 = EditarReceta(vt, eleg)
        vt.mainloop()
        

class EditarReceta(tk.Toplevel):
    
    def __init__(self, root, elegida):
        """ ventana de edicion de receta"""
        self.root = root
        self.elegida=elegida
        #titulo2
        root.title("Editar Receta owo")
        #ventana2 ajustes
        root['bg'] = '#B28D8E'
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.transient(app)
        root.focus_set()
        
        rec = opencsv()
        ind1=str(self.elegida)
        ind2=ind1.replace(',)',"")
        indfor=ind2.replace('(',"")
        indform=int(indfor)
            
        conn = mysql.connector.connect(**config)
        
        consulta = """SELECT nombre, ingredientes, preparacion FROM receta WHERE nombre = %s"""
        cur = conn.cursor()
        cur.execute(consulta, (rec[indform],))
        resul = cur.fetchall()
        cur.close()
        conn.close()
            
            
        nomb=str(resul[0][0])
        ingr=str(resul[0][1])
        prep=str(resul[0][2])
        self.nomb = nomb
        self.ingr = ingr
        self.prep = prep


        #lavel, entradas, botones
        GLabel_424=tk.Label(self.root)
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GLabel_424["bg"] = "#fbdcb0"
        GLabel_424["font"] = ft
        GLabel_424["fg"] = "#000000"
        GLabel_424["justify"] = "center"
        GLabel_424["text"] = "Nombre de la Receta"
        GLabel_424.place(x=0,y=10,width=181,height=30)

        GLabel_832=tk.Label(self.root)
        ft = tkFont.Font(family="Courier", size=16, weight="bold")
        GLabel_832["bg"] = "#fbdcb0"
        GLabel_832["font"] = ft
        GLabel_832["fg"] = "#000000"
        GLabel_832["justify"] = "center"
        GLabel_832["text"] = self.nomb
        GLabel_832.place(x=30,y=50,width=541,height=58)

        longtext = """
        Ingresar Ingredientes        
        Nuevamente        
        """
        longtext2 = """
        Conservar Ingredientes        
        Ingresados        
        """

        GButton_81=tk.Button(self.root)
        GButton_81["activebackground"] = "#5fb878"
        GButton_81["activeforeground"] = "#ffffff"
        GButton_81["bg"] = "#c6d7a0"
        GButton_81["compound"]= LEFT
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GButton_81["font"] = ft
        GButton_81["fg"] = "#000000"
        GButton_81["justify"] = "center"
        GButton_81["text"] = longtext
        GButton_81.place(x=40,y=130,width=240,height=80)
        GButton_81["command"] = self.ingresaringrediente

        GButton_381=tk.Button(self.root)
        GButton_381["activebackground"] = "#5fb878"
        GButton_381["activeforeground"] = "#ffffff"
        GButton_381["bg"] = "#c6d7a0"
        GButton_381["compound"]= LEFT
        ft = tkFont.Font(family="Courier", size=10, weight="bold")

        GButton_381["font"] = ft
        GButton_381["fg"] = "#000000"
        GButton_381["justify"] = "center"
        GButton_381["text"] = longtext2
        GButton_381.place(x=320,y=130,width=240,height=80)
        GButton_381["command"] = self.conservaringredientes

        GButton_400=tk.Button(root)
        GButton_400["bg"] = "#eeeeee"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GButton_400["font"] = ft
        GButton_400["fg"] = "#000000"
        GButton_400["justify"] = "center"
        GButton_400["text"] = " Tabla Medidas "
        GButton_400.place(x=400,y=210,width=150,height=30)
        GButton_400["command"] = self.tablamedidas

        GButton_00=tk.Button(root)
        GButton_00["bg"] = "#eeeeee"
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GButton_00["font"] = ft
        GButton_00["fg"] = "#000000"
        GButton_00["justify"] = "center"
        GButton_00["text"] = " Ver Receta "
        GButton_00.place(x=400,y=250,width=150,height=30)
        GButton_00["command"] = self.abrirReceta

        GLabel_507=tk.Label(self.root)
        ft = tkFont.Font(family="Courier", size=10, weight="bold")
        GLabel_507["bg"] = "#fbdcb0"
        GLabel_507["font"] = ft
        GLabel_507["fg"] = "#000000"
        GLabel_507["justify"] = "center"
        GLabel_507["text"] = "Preparación"
        GLabel_507.place(x=0,y=250,width=181,height=30)
        
        self.stt=st.ScrolledText(self.root, width=50,height=10)
        self.stt.place(x=30,y=290,width=541,height=148)
        self.stt.insert("1.0", self.prep)
        
        GButton_23=tk.Button(self.root)
        GButton_23["activebackground"] = "#0f7d7e"
        GButton_23["activeforeground"] = "#ffffff"
        GButton_23["bg"] = "#a4d9a3"
        ft = tkFont.Font(family="Courier", size=12, weight="bold")
        GButton_23["font"] = ft
        GButton_23["fg"] = "#000000"
        GButton_23["justify"] = "center"
        GButton_23["text"] = "Guardar"
        GButton_23.place(x=100,y=450,width=402,height=30)
        GButton_23["command"] = self.comprobaryGuardar


    def tablamedidas(self):
       """ abre una ventana secundaria para mostrar una tabla de equivalencias de medidas"""
       ventana_secundaria = tk.Toplevel()
       img = PhotoImage(file="Imagenes/tabla.gif")
       Label(ventana_secundaria, image=img).pack()
       ventana_secundaria.mainloop() 

    def ingresaringrediente(self):
        """ ingreso nuevo de todos los ingredientes para las recetas"""
        ingredientes = {}
        cantIngredientes = None
    
        while type(cantIngredientes) != int:
            try:
              cantIngredientes = int(tkinter.simpledialog.askstring("Cantidad", "Ingrese la Cantidad de Ingredientes ",initialvalue= 1 ,parent=self.root))
            except ValueError:
                tkinter.messagebox.showerror("Error", "Ingresar Solo Número")
        for i in range(cantIngredientes):
            ingrediente = tkinter.simpledialog.askstring("Ingredientes", "Ingresar Ingrediente (No dejar casilla vacia)", initialvalue="-" ,parent=self.root)
            medida = tkinter.simpledialog.askstring("Cantidad / Medida", """   Ingresar Cantidad y Medida
(ej; pizca, kg, taza, litro, unidades)
    (No dejar casilla vacia)""", initialvalue="-",parent=self.root)
            ingredientes[ingrediente] = medida
        with open("ingredientes.json", "w", encoding="utf-8") as jsonfile:
            json.dump(ingredientes, jsonfile)
        
        
    def conservaringredientes(self):
        """ reutiliza los ingredientes de las recetas"""

        ingredientes=self.ingr
        with open("ingredientes.json", "w", encoding="utf-8") as jsonfile:
            json.dump(ingredientes, jsonfile)


    def comprobaryGuardar(self):
        """ comprobacion evitar datos vacios"""
        prepa=str(self.stt.get("1.0",tk.END))
        if prepa == "\n" :
            tkinter.messagebox.showerror("Error", "Preparación VACIA")
        else:
            verarch=os.path.exists('ingredientes.json')
            if verarch == FALSE:
                tkinter.messagebox.showerror("Error", "Ingredientes VACIO")
            else:
                self.guardar_receta()

    def guardar_receta(self):
        
        """ guarda las recetas editadas"""
        
        nom=self.nomb
        prepa=str(self.stt.get("1.0",tk.END))
        with open('ingredientes.json', 'r', encoding="utf-8") as jsonfile:
            ingre = json.load(jsonfile) 
            
        ingre2 = json.dumps(ingre) 
        
    
        conn = mysql.connector.connect(**config)
        
        cursor = conn.cursor()
        
        consulta = """DELETE FROM receta WHERE nombre = %s"""
        cursor.execute(consulta, (nom,))
        
        conn.commit()
        

        ndatos = """INSERT INTO receta(
            nombre, ingredientes, preparacion)
            VALUES (%s, %s, %s);"""
            
        cursor.execute(ndatos, (nom, ingre2, prepa,))
        conn.commit()
        cursor.close() 
        conn.close()
        
        
        os.remove("ingredientes.json")
        self.root.destroy()

    def abrirReceta(self):
        """ importa los datos de la receta seleccionada para el lector de recetas"""
        ot=self.ingr
        tx = str(ot)
        tw=tx.replace('")',"")
        tt=tw.replace('("',"")
        tu=tt.replace("}","")
        tz=tu.replace("{","")
        ty=tz.replace(",", "\n \n")
        ingr= ty.replace(":", f"    |🄲🄰🄽🅃🄸🄳🄰🄳|》   ")
       
       
       
        self.abrir_receta(self.nomb, ingr, self.prep)

        
    def abrir_receta(self, nomb, ingr, prep):
      """ abre ventana lector de receta"""
      vt = tk.Toplevel()
      app2 = Receta(vt, nomb, ingr, prep)
      vt.mainloop()

def opencsv():
    """ abre el archivo para leer las recetas"""
    
    conn = mysql.connector.connect(**config)
        
    consulta = """SELECT nombre FROM receta"""
    cur = conn.cursor()
    cur.execute(consulta,)
    resul = cur.fetchall()

    cur.close()
    conn.close()

    lista=[]

    for i in resul:
        conv=''.join(i)
        lista.append(conv)
    
    return lista

def writecsv(recetas):
    """ escribe el archivo para guardar las recetas"""
        
    conn = mysql.connector.connect(**config)
        
    cursor = conn.cursor()

    ndatos = """INSERT INTO receta(
            nombre, ingredientes, preparacion)
            VALUES (%s, %s, %s);"""
            
    cursor.execute(ndatos, (recetas[0], recetas[1], recetas[2]))
    conn.commit()
    cursor.close() 
    conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
