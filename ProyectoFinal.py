from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

#PROGRAMA ECHO POR JOAN SEBASTIAN DIMEY FONSECA / SISTEMAS OPERATIVOS
#IMPORTACIONES IMPORTANTES:
#pip install easygui
#pip install tk

#FUNCIONES:
    #***********************************************************************************************************
    #* Nombre Método: open_window
    #* Propósito: abrir una ventana utilizando easygui del explorador de windows
    #* Variables utilizadas: read
    #* Precondición: ser llamada por un boton o dentro de otro metodo
    #* Postcondición: Abrir el explorador de archivos
    #**********************************************************************************************************
def open_window():
    read=easygui.fileopenbox()
    return read

#***********************************************************************************************************
    #* Nombre Método: open_file
    #* Propósito: abrir un archivo seleccionado en el explorador de archivos
    #* Variables utilizadas: string,directorioActual
    #* Precondición: ser llamada por un boton o dentro de otro metodo
    #* Postcondición: Abrir un archivo seleccionado
    #**********************************************************************************************************
def open_file():
    string = open_window()
    try:
        directorioActual=os.path.split(string)
        os.startfile(string)
        print("Archivo abierto exitosamente")
        synchronized(directorioActual[0],directorioActual[1])
    except:
        mb.showinfo('confirmation', "PLEASE SELECT A VALID FILE \n FAILED SYNCHRONIZED FILE !")



#***********************************************************************************************************
    #* Nombre Método: synchronized
    #* Propósito: Syncronizar dos carpetas seleccionadas
    #* Variables utilizadas: carpeta,directorio,destination
    #* Precondición: Haber seleccionado dos carpetas y ser llamada en un boton o otro metodo
    #* Postcondición: Mantener sincronizada dos carpetas
    #**********************************************************************************************************

def synchronized(carpeta,archivo):
    if carpeta==carpetaNormalArreglado:
        delete_dir(carpetaNube)
        directorio= carpetaLocal
        destination=carpetaNube
        shutil.copytree(directorio,destination)
        mb.showinfo('confirmation', "File: "+archivo+" synchronized !")
    elif carpeta==carpetaNubeArreglado:
        delete_dir(carpetaLocal)
        directorio= carpetaNube
        destination=carpetaLocal
        shutil.copytree(directorio,destination)
        mb.showinfo('confirmation', "File "+archivo+"  synchronized !")

#***********************************************************************************************************
    #* Nombre Método: delete_dir
    #* Propósito: Eliminar una carpeta seleccionada
    #* Variables utilizadas: carpeta,directorio
    #* Precondición: Haber seleccionado una carpeta y ser llamada en un boton o metodo
    #* Postcondición: Eliminar la carpeta seleccionada
    #**********************************************************************************************************

def delete_dir(carpeta):
    directorio= carpeta
    if os.path.exists(directorio):
        shutil.rmtree(directorio)
        print("La carpeta a sido eliminada")
    else:
        print("La carpeta no existe")


#***********************************************************************************************************
    #* Nombre Método: select
    #* Propósito: Seleccionar las carpetas y gracias a estas utilizar los metodos para sincronizar las carpetas
    #* despues de abrir un archivo.
    #* Variables utilizadas: opcion,carpetaLocal,carpetaNube,carpetaNormalArreglado,carpetaNubeArreglado
    #* Precondición: Haber seleccionado una carpeta y ser llamada en un boton o metodo
    #* Postcondición: Eliminar la carpeta seleccionada
    #**********************************************************************************************************

def select(opcion):
    global carpetaLocal
    global carpetaNube
    global carpetaNormalArreglado
    global carpetaNubeArreglado
    if opcion==1:
        try:
            carpetaLocal=filedialog.askdirectory()
            carpetaNormalArreglado=os.path.normpath(carpetaLocal)
            Label(root, text="carpeta local: \n"+carpetaNormalArreglado, font=("Helvetica", 8), fg="blue").place(x=50,y=150)
            habilitarBtnAbrir("normal",seleccionarNube)
        except:
            mb.showinfo('confirmation', "Por Favor seleccione una carpeta")
    elif opcion==2:
        try:
            carpetaNube=filedialog.askdirectory()
            carpetaNubeArreglado=os.path.normpath(carpetaNube)
            #delete_dir()
            Label(root, text="carpeta nube: \n"+carpetaNubeArreglado, font=("Helvetica", 8), fg="blue").place(x=50,y=240)
            habilitarBtnAbrir("normal",abrir)
        except:
            mb.showinfo('confirmation', "Por Favor seleccione una carpeta")


#***********************************************************************************************************
    #* Nombre Método: habilitarBtnAbrir
    #* Propósito: Habilitar botones
    #* Variables utilizadas: estado,boton
    #* Precondición: Haber seleccionado un boton y llamarlo en un metodo
    #* Postcondición: Habilitar el boton deseado
    #**********************************************************************************************************

def habilitarBtnAbrir(estado,boton):
    if boton==seleccionarNube:
        seleccionarNube.configure(state=estado)
        seleccionarNube.configure(state=estado)
    elif boton==abrir:
        abrir.configure(state=estado)
        abrir.configure(state=estado)

#INTERFAZ

root = Tk()

root.title('SO PROYECTO FINAL')
root.geometry("400x400")
root.resizable (0,0)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

Label(root, text="SO PROYECTO \n FINAL", font=("Helvetica", 16), fg="blue").place(x=120,y=10)

#BOTONES
seleccionar= Button(root, text="SELECCIONAR \n CARPETA LOCAL",command=lambda:select(1))
seleccionar.place(x=150,y=100)

seleccionarNube= Button(root, text="SELECCIONAR \n CARPETA NUBE",command=lambda:select(2))
seleccionarNube.place(x=155,y=190)
seleccionarNube.configure(state="disabled")


abrir= Button(root, text="ABRIR",command=lambda:open_file())
abrir.place(x=180,y=300)
abrir.configure(state="disabled")


root.mainloop()