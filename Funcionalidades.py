from InterfazGrafica import (frame_inicio, 
                             frame_libros, 
                             frame_usuarios, 
                             entry_autor, 
                             entry_correo, 
                             entry_titulo, 
                             entry_usuario,
                             opcion_categoria,
                             categorias,
                             text_resultado, 
                             frame_Consulta)
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