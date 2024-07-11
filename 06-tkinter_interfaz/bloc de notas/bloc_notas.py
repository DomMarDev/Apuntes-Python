# Importamos los módulos necesarios
from tkinter import *
from tkinter import filedialog as FD
from pathlib import Path

# Funcionalidades
ruta = ''
def nuevo():
    global ruta # declaramos la ruta como una variable global
    mensaje.set('Nuevo archivo')
    ruta = '' # para dejar vacía la ruta de nuevo una vez la rescata
    texto.delete(1.0, 'end') # que te borre desde el primer caracter hasta el final
    root.title('Mi bloc de notas')

def abrir():
    global ruta
    mensaje.set('Abrir archivo')
    ruta = FD.askopenfilename(
        initialdir= '.',
        filetypes=(('Archivos de texto', '*.txt'),),
        title= 'Abrir un archivo de texto'
    )

    if ruta != '':
        ruta_path = Path(ruta)
        contenido = ruta_path.read_text()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        root.title(ruta + '- Mi boc de notas')

def guardar():
    global ruta
    mensaje.set('Guardar archivo')
    if ruta != '':
        contenido = texto.get(1.0, 'end-1c')
        ruta_path = Path(ruta)
        ruta_path.write_text(contenido)
        mensaje.set('Archivo guardado correctamente')
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set('Guardar archivo como')
    archivo = FD.asksaveasfilename(
    # archivo = FD.asksaveasfile(
        title= 'Guardar archivo', 
        # mode= 'w',
        defaultextension= '.txt')
    if archivo != None:
        ruta= archivo
        # ruta= archivo.name
        contenido = texto.get(1.0, 'end-1c') # le quitamos un caracter al final para quitar un espacio que pone
        ruta_path= Path(ruta)
        ruta_path.write_text(contenido)
        mensaje.set('Archivo guardado correctamente')
    else:
        mensaje.set('Guardado cancelado')
        ruta = ''


# Configurar la ventana root
root = Tk()
root.title('Bloc de notas')

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label= 'Nuevo', command= nuevo)
filemenu.add_command(label= 'Abrir', command= abrir)
filemenu.add_command(label= 'Guardar', command= guardar)
filemenu.add_command(label= 'Guardar como', command= guardar_como)
filemenu.add_separator()
filemenu.add_command(label= 'Salir', command= root.destroy)
menubar.add_cascade(menu= filemenu, label= 'Archivo')


# Creando caja de texto central
texto = Text(root) # puedes tener texto multilinea con el widget Text
texto.pack(fill= 'both', expand= 1)
texto.config(bd= 0, padx= 5, pady= 5, font= ('Courier', 14))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido al bloc de notas')
monitor = Label(root, textvariable= mensaje, justify= 'right')
monitor.pack(side= 'right')

# Configuramos el menu
root.config(menu= menubar) # El menú está dentro del menubar

# Loop principal
root.mainloop()
