import tkinter as tk
import json

usuario_actual = None

def mostrar_frame(frame):
    for f in [frame_bienvenida, frame_registro, frame_login, frame_principal, frame_libros, frame_consulta]:
        f.pack_forget()
    frame.pack()

def volver_inicio():
    mostrar_frame(frame_principal)

# ---------------------------
# REGISTRO DE USUARIO
# ---------------------------
def registrar_usuario():
    usuario = entry_reg_usuario.get()
    correo = entry_reg_correo.get()
    contraseña = entry_reg_contraseña.get()

    if not usuario or not correo or not contraseña:
        print("Completa todos los campos.")
        return

    nuevo_usuario = {
        "usuario": usuario,
        "correo": correo,
        "contraseña": contraseña
    }

    try:
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    for u in datos:
        if u["usuario"] == usuario:
            print("Usuario ya registrado.")
            return

    datos.append(nuevo_usuario)
    with open("usuarios.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Usuario registrado exitosamente.")
    entry_reg_usuario.delete(0, "end")
    entry_reg_correo.delete(0, "end")
    entry_reg_contraseña.delete(0, "end")
    mostrar_frame(frame_bienvenida)

# ---------------------------
# INICIO DE SESIÓN
# ---------------------------
def iniciar_sesion():
    global usuario_actual
    usuario = entry_login_usuario.get()
    contraseña = entry_login_contraseña.get()

    try:
        with open("usuarios.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    for u in datos:
        if u["usuario"] == usuario and u["contraseña"] == contraseña:
            print("Inicio de sesión exitoso.")
            usuario_actual = usuario
            entry_login_usuario.delete(0, "end")
            entry_login_contraseña.delete(0, "end")
            mostrar_frame(frame_principal)
            return

    print("Credenciales incorrectas.")

# ---------------------------
# GUARDAR LIBRO
# ---------------------------
def guardar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    categoria = opcion_categoria.get()
    disponibilidad = opcion_disponibilidad.get()

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponibilidad": disponibilidad
    }

    try:
        with open("libros.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    datos.append(nuevo_libro)

    with open("libros.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print(f"Libro '{titulo}' guardado.")
    entry_titulo.delete(0, "end")
    entry_autor.delete(0, "end")
    opcion_categoria.set(categorias[0])
    opcion_disponibilidad.set(disponibilidades[0])

# ---------------------------
# CONSULTAR LIBROS
# ---------------------------
def consultar_libros():
    text_resultado.delete("1.0", "end")
    try:
        with open("libros.json", "r") as archivo:
            libros = json.load(archivo)
            if libros:
                for i, libro in enumerate(libros, 1):
                    text_resultado.insert("end", f"{i}. {libro['titulo']} - {libro['autor']} ({libro['categoria']}) - {libro['disponibilidad']}\n")
            else:
                text_resultado.insert("end", "No hay libros registrados.")
    except FileNotFoundError:
        text_resultado.insert("end", "No se encontró la base de libros.")

# ---------------------------
# INTERFAZ PRINCIPAL
# ---------------------------
ventana = tk.Tk()
ventana.geometry("520x550")
ventana.title("------- Gestor de Biblioteca -------")

# ---------------------------
# FRAME BIENVENIDA
# ---------------------------
frame_bienvenida = tk.Frame(ventana)
tk.Label(frame_bienvenida, text="Bienvenido 📚", font=("Arial", 18, "bold")).pack(pady=20)
tk.Button(frame_bienvenida, text="Registrar Usuario", command=lambda: mostrar_frame(frame_registro)).pack(pady=10)
tk.Button(frame_bienvenida, text="Iniciar Sesión", command=lambda: mostrar_frame(frame_login)).pack(pady=10)
frame_bienvenida.pack()

# ---------------------------
# FRAME REGISTRO
# ---------------------------
frame_registro = tk.Frame(ventana)
tk.Label(frame_registro, text="Registrar Usuario", font=("Arial", 16)).pack(pady=10)
tk.Label(frame_registro, text="Usuario:").pack()
entry_reg_usuario = tk.Entry(frame_registro)
entry_reg_usuario.pack()
tk.Label(frame_registro, text="Correo:").pack()
entry_reg_correo = tk.Entry(frame_registro)
entry_reg_correo.pack()
tk.Label(frame_registro, text="Contraseña:").pack()
entry_reg_contraseña = tk.Entry(frame_registro, show="*")
entry_reg_contraseña.pack()
tk.Button(frame_registro, text="Registrar", command=registrar_usuario).pack(pady=10)
tk.Button(frame_registro, text="Volver", command=lambda: mostrar_frame(frame_bienvenida)).pack()

# ---------------------------
# FRAME LOGIN
# ---------------------------
frame_login = tk.Frame(ventana)
tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 16)).pack(pady=10)
tk.Label(frame_login, text="Usuario:").pack()
entry_login_usuario = tk.Entry(frame_login)
entry_login_usuario.pack()
tk.Label(frame_login, text="Contraseña:").pack()
entry_login_contraseña = tk.Entry(frame_login, show="*")
entry_login_contraseña.pack()
tk.Button(frame_login, text="Entrar", command=iniciar_sesion).pack(pady=10)
tk.Button(frame_login, text="Volver", command=lambda: mostrar_frame(frame_bienvenida)).pack()

# ---------------------------
# FRAME PRINCIPAL (DESPUÉS DE LOGIN)
# ---------------------------
frame_principal = tk.Frame(ventana)
tk.Label(frame_principal, text="Panel Principal", font=("Arial", 16)).pack(pady=20)
tk.Button(frame_principal, text="Registrar Libro", command=lambda: mostrar_frame(frame_libros)).pack(pady=10)
tk.Button(frame_principal, text="Consultar Libros", command=lambda: [mostrar_frame(frame_consulta), consultar_libros()]).pack(pady=10)
tk.Button(frame_principal, text="Cerrar Sesión", command=lambda: mostrar_frame(frame_bienvenida)).pack(pady=20)

# ---------------------------
# FRAME REGISTRO LIBROS
# ---------------------------
frame_libros = tk.Frame(ventana)
tk.Label(frame_libros, text="Registrar Libro", font=("Arial", 16)).pack(pady=10)
tk.Label(frame_libros, text="Título:").pack()
entry_titulo = tk.Entry(frame_libros)
entry_titulo.pack()
tk.Label(frame_libros, text="Autor:").pack()
entry_autor = tk.Entry(frame_libros)
entry_autor.pack()
tk.Label(frame_libros, text="Categoría:").pack()
categorias = ["Ciencia ficción", "Romance", "Historia"]
opcion_categoria = tk.StringVar(value=categorias[0])
tk.OptionMenu(frame_libros, opcion_categoria, *categorias).pack()
tk.Label(frame_libros, text="Disponibilidad:").pack()
disponibilidades = ["disponible", "prestado"]
opcion_disponibilidad = tk.StringVar(value=disponibilidades[0])
tk.OptionMenu(frame_libros, opcion_disponibilidad, *disponibilidades).pack()
tk.Button(frame_libros, text="Guardar Libro", command=guardar_libro).pack(pady=10)
tk.Button(frame_libros, text="Volver", command=volver_inicio).pack()

# ---------------------------
# FRAME CONSULTA LIBROS
# ---------------------------
frame_consulta = tk.Frame(ventana)
tk.Label(frame_consulta, text="Consulta de Libros", font=("Arial", 16)).pack(pady=10)
text_resultado = tk.Text(frame_consulta, height=15, width=60)
text_resultado.pack()
tk.Button(frame_consulta, text="Actualizar Lista", command=consultar_libros).pack(pady=5)
tk.Button(frame_consulta, text="Volver", command=volver_inicio).pack(pady=10)

# ---------------------------
# MAIN LOOP
# ---------------------------
ventana.mainloop()

