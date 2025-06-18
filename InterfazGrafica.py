import tkinter as tk

#from Funcionalidades import mostrar_frame, guardar_libro, guardar_usuario, volver_inicio, consultar_libros

import json

# ---------------------------
# FUNCIONES PRINCIPALES
# ---------------------------
def mostrar_frame(frame):
    frame_inicio.pack_forget()
    frame_usuarios.pack_forget()
    frame_libros.pack_forget()
    frame_Consulta.pack_forget()
    frame.pack()

def volver_inicio():
    mostrar_frame(frame_inicio)

# ---------------------------
# GUARDAR USUARIO EN JSON
# ---------------------------
def guardar_usuario():
    usuario = entry_usuario.get()
    correo = entry_correo.get()

    nuevo_usuario = {
        "usuario": usuario,
        "correo": correo
    }

    try:
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    datos.append(nuevo_usuario)

    with open("usuarios.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print(f"Usuario '{usuario}' registrado!")
    entry_usuario.delete(0, "end")
    entry_correo.delete(0, "end")

# ---------------------------
# GUARDAR LIBRO EN JSON
# ---------------------------
def guardar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    categoria = opcion_categoria.get()

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria
    }

    try:
        with open("libros.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    datos.append(nuevo_libro)

    with open("libros.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print(f"Libro '{titulo}' guardado correctamente!")
    entry_titulo.delete(0, "end")
    entry_autor.delete(0, "end")
    opcion_categoria.set(categorias[0])

# ---------------------------
# CONSULTAR LIBROS
# ---------------------------
def consultar_libros():
    text_resultado.delete("1.0", "end")  # Limpia el área de texto
    try:
        with open("libros.json", "r") as archivo:
            libros = json.load(archivo)
            if libros:
                for i, libro in enumerate(libros, 1):
                    texto = f"{i}. Título: {libro['titulo']}, Autor: {libro['autor']}, Categoría: {libro['categoria']}\n"
                    text_resultado.insert("end", texto)
            else:
                text_resultado.insert("end", "No hay libros registrados.")
    except FileNotFoundError:
        text_resultado.insert("end", "Archivo de libros no encontrado.")

# ---------------------------
# INTERFAZ PRINCIPAL
# ---------------------------
ventana = tk.Tk() #Abre una ventana
ventana.geometry("500x500") #Dimensiones de la ventana
ventana.title("Gestor de Libros y Usuarios") #Titulo de la ventana

# ---------------------------
# FRAME INICIO
# ---------------------------
frame_inicio = tk.Frame(ventana) #Primer frime para navegación dinámica
label_inicio = tk.Label(frame_inicio, text="Bienvenido al Gestor", font=("Arial", 16, "bold")) #Titulo del frame
label_inicio.pack(pady=20) #Posición en y del frame

btn_usuarios = tk.Button(frame_inicio, text="Registrar Usuario", command=lambda: mostrar_frame(frame_usuarios)) #botoo de registro de usuario en el frame inicial
btn_usuarios.pack(pady=10) #Ubicación boton
btn_libros = tk.Button(frame_inicio, text="Registrar Libro", command=lambda: mostrar_frame(frame_libros)) #Boton de registro e libro en el frame inicial
btn_libros.pack(pady=10) #Ubicación del botón
btn_consultar = tk.Button(frame_inicio, text="Consultar Libro", command=lambda: [mostrar_frame(frame_Consulta), consultar_libros()])
btn_consultar.pack(pady=10)

frame_inicio.pack()

# ---------------------------
# FRAME REGISTRO USUARIOS
# ---------------------------
frame_usuarios = tk.Frame(ventana)

label_usuarios = tk.Label(frame_usuarios, text="Registro de Usuarios \U0001F464", font=("Arial", 16, "bold"))
label_usuarios.pack(pady=10)

label_usuario = tk.Label(frame_usuarios, text="Nombre del usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(frame_usuarios)
entry_usuario.pack()

label_correo = tk.Label(frame_usuarios, text="Correo electrónico:")
label_correo.pack()
entry_correo = tk.Entry(frame_usuarios)
entry_correo.pack()

label_contraseña = tk.Label(frame_usuarios, text="Contraseña:")
label_contraseña.pack()
# No se guarda la contraseña en este ejemplo

btn_guardar_usuario = tk.Button(frame_usuarios, text="Guardar Usuario", command=guardar_usuario)
btn_guardar_usuario.pack(pady=10)

btn_volver1 = tk.Button(frame_usuarios, text="Volver al Inicio", command=volver_inicio)
btn_volver1.pack(pady=10)

# ---------------------------
# FRAME REGISTRO LIBROS
# ---------------------------
frame_libros = tk.Frame(ventana)

label_libros = tk.Label(frame_libros, text="Registro de Libros \U0001F4DA", font=("Arial", 16, "bold"))
label_libros.pack(pady=10)

label_titulo = tk.Label(frame_libros, text="Título del libro:")
label_titulo.pack()
entry_titulo = tk.Entry(frame_libros)
entry_titulo.pack()

label_autor = tk.Label(frame_libros, text="Autor:")
label_autor.pack()
entry_autor = tk.Entry(frame_libros)
entry_autor.pack()

label_categoria = tk.Label(frame_libros, text="Categoría:")
label_categoria.pack()

categorias = ["Ciencia ficción", "Romance", "Historia"]
opcion_categoria = tk.StringVar()
opcion_categoria.set(categorias[0])

menu_categorias = tk.OptionMenu(frame_libros, opcion_categoria, *categorias)
menu_categorias.pack()

btn_guardar_libro = tk.Button(frame_libros, text="Guardar Libro", command=guardar_libro)
btn_guardar_libro.pack(pady=10)

btn_volver2 = tk.Button(frame_libros, text="Volver al Inicio", command=volver_inicio)
btn_volver2.pack(pady=10)

# ---------------------------
# FRAME DE CONSULTA DE LIBROS
# ---------------------------
frame_Consulta = tk.Frame(ventana)

label_consulta = tk.Label(frame_Consulta, text="Consulta de Libros 📚", font=("Arial", 16, "bold"))
label_consulta.pack(pady=10)

text_resultado = tk.Text(frame_Consulta, height=15, width=60)
text_resultado.pack(pady=10)

btn_actualizar = tk.Button(frame_Consulta, text="Actualizar Lista", command=consultar_libros)
btn_actualizar.pack(pady=5)

btn_volver3 = tk.Button(frame_Consulta, text="Volver al Inicio", command=volver_inicio)
btn_volver3.pack(pady=10)

# ---------------------------
# MAIN LOOP
# ---------------------------
ventana.mainloop()
