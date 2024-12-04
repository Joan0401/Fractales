import tkinter as tk # Para crear la interfaz
from tkinter import messagebox # Para ventanas emergentes
from Fractales import * # Archivo donde estan las clases de los fractales

cantidad_iteraciones = 0


def cerrar_ventana(): #Función para cerrar la interfaz (con confirmación del usuario)
    if messagebox.askokcancel("Cerrar el programa", "¿Estás seguro de que quieres cerrar el programa?"):
        turtle.bye()
        root.destroy()

def config_Dragon():
    global cantidad_iteraciones
    cantidad_iteraciones = 0
    for widget in root.winfo_children():
        widget.destroy()

    def validar_entrada():
        try:
            valor = int(entrada.get())
            if 1 <= valor <= 10:
                cantidad_iteraciones = valor

                #Crear la instancia de curva del dragon
                curva_dragon = CurvaDelDragon(cantidad_iteraciones, longitud_de_linea=10)

                #Llama al metodo para dibujar
                curva_dragon.dibujar()

            else:
                messagebox.showwarning("Entrada inválida", "Ingrese un número entre 1 y 10.")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Ingrese un número válido.")
    
    cantidad = tk.Label(root, text="Ingrese la cantidad de iteraciones\n El rango para este fractal es: 1 - 10 ", font=("Lato", 30), bg='lawn green')
    cantidad.place(x=150, y=50)
    entrada= tk.Entry(root, width= 25)
    entrada.place(x=400, y=300)
    boton = tk.Button(root, text='Aceptar', font=("Lato", 16), command=validar_entrada, bg='medium sea green')
    boton.place(x=430, y=420)
    atras = tk.Button(root, text="Atrás", font=("Lato", 16), command=opciones, bg='medium sea green')
    atras.place(x=800, y=475)
    

def config_Flecha():
    global cantidad_iteraciones
    cantidad_iteraciones = 0
    for widget in root.winfo_children():
        widget.destroy()

    def validar_entrada():
        try:
            valor = int(entrada.get())
            if 1 <= valor <= 11:
                cantidad_iteraciones = valor

                #Crear la instancia de la curva de flecha de Sierpinski
                flecha_sierpinski = CurvaPuntaFlechaSierpinski(cantidad_iteraciones, longitud_segmento=3, grosor_linea=2)

                #Llama al metodo para dibujar
                flecha_sierpinski.dibujar_fractal()

            else:
                messagebox.showwarning("Entrada inválida", "Ingrese un número entre 1 y 11.")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Ingrese un número válido.")
    
    cantidad = tk.Label(root, text="Ingrese la cantidad de iteraciones\n El rango para este fractal es: 1 - 11 ", font=("Lato", 30), bg='lawn green')
    cantidad.place(x=150, y=50)
    entrada= tk.Entry(root, width= 25)
    entrada.place(x=400, y=300)
    boton = tk.Button(root, text='Aceptar', font=("Lato", 16), command=validar_entrada, bg='medium sea green')
    boton.place(x=430, y=420)
    atras = tk.Button(root, text="Atrás", font=("Lato", 16), command=opciones, bg='medium sea green')
    atras.place(x=800, y=475)


def config_Levy():
    global cantidad_iteraciones
    cantidad_iteraciones = 0
    for widget in root.winfo_children():
        widget.destroy()

    def validar_entrada():
        try:
            valor = int(entrada.get())
            if 1 <= valor <= 13:
                cantidad_iteraciones = valor

                #Crear la instancia de curva de la curva de levy c
                curva_levy_c = CurvaLevyC(cantidad_iteraciones, longitud_segmento=5, grosor_linea=2)

                #Llama al metodo para dibujar
                curva_levy_c.dibujar_fractal()

            else:
                messagebox.showwarning("Entrada inválida", "Ingrese un número entre 1 y 13.")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Ingrese un número válido.")
    
    cantidad = tk.Label(root, text="Ingrese la cantidad de iteraciones\n El rango para este fractal es: 1 - 13 ", font=("Lato", 30), bg='lawn green')
    cantidad.place(x=150, y=50)
    entrada= tk.Entry(root, width= 25)
    entrada.place(x=400, y=300)
    boton = tk.Button(root, text='Aceptar', font=("Lato", 16), command=validar_entrada, bg='medium sea green')
    boton.place(x=430, y=420)
    atras = tk.Button(root, text="Atrás", font=("Lato", 16), command=opciones, bg='medium sea green')
    atras.place(x=800, y=475)


def config_Alfombra():
    global cantidad_iteraciones
    cantidad_iteraciones = 0
    for widget in root.winfo_children():
        widget.destroy()

    def validar_entrada():
        try:
            valor = int(entrada.get())
            if 1 <= valor <= 4:
                cantidad_iteraciones = valor

                #Crear la instancia de la alfombra de Sierpinski
                alfombra = AlfombraDeSierpinski(nivel=cantidad_iteraciones)

                #Llama al metodo para dibujar
                alfombra.dibujar()

            else:
                messagebox.showwarning("Entrada inválida", "Ingrese un número entre 1 y 4.")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Ingrese un número válido.")
    
    cantidad = tk.Label(root, text="Ingrese la cantidad de iteraciones\n El rango para este fractal es: 1 - 4 ", font=("Lato", 30), bg='lawn green')
    cantidad.place(x=150, y=50)
    entrada= tk.Entry(root, width= 25)
    entrada.place(x=400, y=300)
    boton = tk.Button(root, text='Aceptar', font=("Lato", 16), command=validar_entrada, bg='medium sea green')
    boton.place(x=430, y=420)
    atras = tk.Button(root, text="Atrás", font=("Lato", 16), command=opciones, bg='medium sea green')
    atras.place(x=800, y=475)


def config_Salchicha():
    global cantidad_iteraciones
    cantidad_iteraciones = 0
    for widget in root.winfo_children():
        widget.destroy()

    def validar_entrada():
        try:
            valor = int(entrada.get())
            if 1 <= valor <= 4:
                cantidad_iteraciones = valor

                #Crear la instancia de la salchicha de Minkowski
                salchicha = SalchichaDeMinkowski(iteracion=cantidad_iteraciones)

                #Crea la lista de giros
                salchicha.generar_l_system()
                
                #Llama al metodo para dibujar
                salchicha.dibujar_l_system()

                salchicha.reset()

            else:
                messagebox.showwarning("Entrada inválida", "Ingrese un número entre 1 y 4.")
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Ingrese un número válido.")
    
    cantidad = tk.Label(root, text="Ingrese la cantidad de iteraciones\n El rango para este fractal es: 1 - 4 ", font=("Lato", 30), bg='lawn green')
    cantidad.place(x=150, y=50)
    entrada= tk.Entry(root, width= 25)
    entrada.place(x=400, y=300)
    boton = tk.Button(root, text='Aceptar', font=("Lato", 16), command=validar_entrada, bg='medium sea green')
    boton.place(x=430, y=420)
    atras = tk.Button(root, text="Atrás", font=("Lato", 16), command=opciones, bg='medium sea green')
    atras.place(x=800, y=475)


def opciones():
    for widget in root.winfo_children():
        widget.destroy()

    opcion = tk.Label(root, text="Escoge uno de los fractales", font=("Lato", 30), bg='lawn green')
    opcion.place(x=200, y=50)

    curvaDragon = tk.Button(root, text="Curva del Dragón", font=("Lato", 16), command=config_Dragon, bg='medium sea green')
    curvaDragon.place(x=50, y=230)

    flechaSierpinski = tk.Button(root, text="Punta de flecha Sierpinski", font=("Lato", 16), command=config_Flecha, bg='medium sea green')
    flechaSierpinski.place(x=315, y=230)

    levyC = tk.Button(root, text="Curva de Levy C", font=("Lato", 16), command=config_Levy, bg='medium sea green')
    levyC.place(x=650, y=230)

    alfombraSierpinski = tk.Button(root, text="Alfombra de Sierpinski", font=("Lato", 16), command=config_Alfombra, bg='medium sea green')
    alfombraSierpinski.place(x=135, y=325)

    salchichaMinkowski = tk.Button(root, text="Salchicha de Minkowski", font=("Lato", 16), command=config_Salchicha, bg='medium sea green')
    salchichaMinkowski.place(x=500, y=325)

    atras = tk.Button(root, text="Atrás", font=("Lato", 16), command=crear_menu_principal, bg='medium sea green')
    atras.place(x=800, y=475)


def crear_menu_principal():
    for widget in root.winfo_children():
        widget.destroy()

    nombre = tk.Label(root, text="Fractales con Sistemas L", font=("Lato", 48), bg='lawn green')
    nombre.place(x=100, y=125)

    entrar = tk.Button(root, text="Entrar", font=("Lato", 24), command=opciones, bg='medium sea green')
    entrar.place(x=400, y=320)

    cerrar = tk.Button(root, text="Cerrar", font=("Lato", 16), command=cerrar_ventana, bg='firebrick3')
    cerrar.place(x=800, y=475)

root = tk.Tk()
root.title('Fractales')
root.geometry('900x550')
root.configure(bg='lawn green')

crear_menu_principal()

root.mainloop()

