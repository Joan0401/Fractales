import turtle
class CurvaDelDragon:
    """
    Constructor de la clase.
    Entradas: iteraciones: Número de iteraciones para generar la curva (int, no negativo). longitud_de_linea: Longitud de cada segmento de línea (int, opcional, por defecto 10).
    Salidas: No retorna valores, pero inicializa la instancia de la clase.
    Restricciones: iteraciones debe ser un entero no negativo. longitud_de_linea debe ser un entero positivo.
    """
    def __init__(self, iteraciones, longitud_de_linea=10):
        self.iteraciones = iteraciones
        self.longitud_de_linea = longitud_de_linea
        self.secuencia = self.generar_secuencia_curva_del_dragon()  # Genera la secuencia de giros
        self.ancho, self.alto = self.calcular_dimensiones()  # Calcula las dimensiones para el dibujo

    def generar_secuencia_curva_del_dragon(self):
        """
        Genera la secuencia de giros para la Curva del Dragón.
        Entradas: Ninguna (utiliza self.iteraciones de la instancia de la clase).
        Salidas: Lista de caracteres ('R' o 'L') que representa la secuencia de giros.
        Restricciones: Ninguna adicional a las del constructor.
        """
        secuencia = []  # Secuencia inicial vacía
        for _ in range(self.iteraciones):
            # Extiende la secuencia actual con un patrón específico
            nueva_secuencia = secuencia + ['R'] + ['L' if turno == 'R' else 'R' for turno in reversed(secuencia)]
            secuencia = nueva_secuencia
        return secuencia
    
    def calcular_dimensiones(self):
        """
        Calcula las dimensiones necesarias para dibujar la curva.
        Entradas: Ninguna (utiliza self.secuencia y self.longitud_de_linea de la instancia de la clase).
        Salidas: Tupla (ancho, alto) con las dimensiones de la curva.
        Restricciones: Ninguna adicional a las del constructor.
        """
        x, y = 0, 0  # Coordenadas iniciales
        max_x, min_x, max_y, min_y = 0, 0, 0, 0  # Valores máximos y mínimos para x y y
        direccion = 0  # Inicialmente apuntando hacia arriba

        for turno in self.secuencia:
            # Actualiza la dirección basada en el turno
            direccion = (direccion + 1) % 4 if turno == 'R' else (direccion - 1) % 4

            # Mueve las coordenadas y actualiza los valores máximos y mínimos
            if direccion == 0:
                y += self.longitud_de_linea
            elif direccion == 1:
                x += self.longitud_de_linea
            elif direccion == 2:
                y -= self.longitud_de_linea
            else:  # dirección == 3
                x -= self.longitud_de_linea

            max_x, min_x = max(max_x, x), min(min_x, x)
            max_y, min_y = max(max_y, y), min(min_y, y)

        # Calcula las diferencias en lugar de ancho y alto
        delta_x = max_x - min_x
        delta_y = max_y - min_y
        return delta_x, delta_y

    def dibujar(self):
        """
        Dibuja la Curva del Dragón.
        Entradas: Ninguna (utiliza self.secuencia, self.ancho, self.alto, y self.longitud_de_linea de la instancia de la clase).
        Salidas: Dibuja la curva en una ventana gráfica.
        Restricciones: Ninguna adicional a las del constructor.
        """
        
        try:
            turtle.speed('fastest')
            turtle.tracer(False)

            inicio_x = -self.ancho // 2
            inicio_y = self.alto // 2
            turtle.penup()
            turtle.goto(inicio_x + self.ancho / 2, inicio_y - self.alto / 2)
            turtle.pendown()

            for turno in self.secuencia:
                turtle.left(90) if turno == 'L' else turtle.right(90)
                turtle.forward(self.longitud_de_linea)

            turtle.update()
            turtle.done()

        except turtle.Terminator:
            pass


class CurvaPuntaFlechaSierpinski:
    def __init__(self, iteraciones, longitud_segmento=3, grosor_linea=2):
        # Constructor de la clase. Inicializa los parámetros del objeto.
        self.iteraciones = iteraciones
        self.longitud_segmento = longitud_segmento
        self.grosor_linea = grosor_linea
        self.axioma = "XF"
        self.reglas = {
            "X": "YF+XF+Y",
            "Y": "XF-YF-X"
        }
        self.lista_comandos = self.generar_lista_comandos()

    def aplicar_regla(self, simbolo):
        # Aplica las reglas de la gramática de la curva de Sierpinski.
        return self.reglas.get(simbolo, simbolo)

    def generar_lista_comandos(self):
        # Genera la lista de comandos iterando sobre las reglas.
        cadena_actual = self.axioma
        for _ in range(self.iteraciones):
            nueva_cadena = ''.join([self.aplicar_regla(simbolo) for simbolo in cadena_actual])
            cadena_actual = nueva_cadena
        return cadena_actual

    def calcular_posicion_inicial(self):
        # Calcula la posición inicial basada en la paridad de las iteraciones.
        # Si la cantidad de iteraciones es impar, coloca el cursor en la esquina inferior izquierda.
        if self.iteraciones % 2 == 1:
            return -350, -250
        # Si la cantidad de iteraciones es par, coloca el cursor en la esquina superior izquierda.
        else:
            return -350, 250

    def dibujar_fractal(self):
        try:
            # Configura la ventana de turtle y dibuja el fractal.
            turtle.setup(width=800, height=600)
            turtle.speed('fastest')
            turtle.tracer(False)
            turtle.width(self.grosor_linea)

            # Establece la posición inicial del cursor.
            turtle.penup()
            turtle.goto(self.calcular_posicion_inicial())
            turtle.pendown()

            # Itera sobre los comandos y realiza las acciones correspondientes.
            for comando in self.lista_comandos:
                if comando == 'F':
                    turtle.forward(self.longitud_segmento)
                elif comando == '+':
                    turtle.left(60)
                elif comando == '-':
                    turtle.right(60)

            # Actualiza la pantalla y finaliza la aplicación turtle.
            turtle.update()
            turtle.done()

        except turtle.Terminator:
            pass



class CurvaLevyC:
    def __init__(self, iteraciones, longitud_segmento, grosor_linea):
        # Inicializa los parámetros del objeto CurvaLevyC
        self.iteraciones = iteraciones
        self.longitud_segmento = longitud_segmento
        self.grosor_linea = grosor_linea
        # Axioma inicial (cadena de inicio)
        self.axioma = "F"
        # Reglas de reemplazo
        self.reglas = {
            "F": "+F--F+"
        }
        # Genera la lista de comandos para el fractal
        self.lista_comandos = self.generar_lista_comandos()

    def aplicar_regla(self, simbolo):
        # Aplica la regla de reemplazo al símbolo dado
        return self.reglas.get(simbolo, simbolo)

    def generar_lista_comandos(self):
        # Genera la lista de comandos para el fractal utilizando las reglas
        cadena_actual = self.axioma
        for _ in range(self.iteraciones):
            nueva_cadena = ''.join([self.aplicar_regla(simbolo) for simbolo in cadena_actual])
            cadena_actual = nueva_cadena

        return cadena_actual

    def dibujar_fractal(self):
        try:
            # Configura la ventana de turtle
            turtle.setup(width=800, height=600)
            turtle.speed('fastest')
            turtle.tracer(False)
            turtle.width(self.grosor_linea)

            # Establece la posición inicial del cursor
            turtle.penup()
            turtle.goto(-150, 150)
            turtle.pendown()

            # Itera sobre los comandos y ejecuta las acciones correspondientes
            for comando in self.lista_comandos:
                if comando == 'F':
                    # Avanza la longitud del segmento
                    turtle.forward(self.longitud_segmento)
                elif comando == '+':
                    # Gira a la derecha
                    turtle.right(45)
                elif comando == '-':
                    # Gira a la izquierda
                    turtle.left(45)

            # Actualiza la ventana de turtle y finaliza
            turtle.update()
            turtle.done()

        except turtle.Terminator:
            pass

class AlfombraDeSierpinski:
    """
    Clase para dibujar una Alfombra de Sierpinski con la biblioteca turtle de Python utilizando un sistema L.    
    Entradas: nivel - profundidad de la recursión para el fractal.    
    Salidas: Una ventana de turtle que muestra el fractal de la Alfombra de Sierpinski.
    Restricciones: El nivel debe ser un número entero no negativo.
    """
    def __init__(self, nivel):
        self.nivel = nivel
        self.axioma = "F+F+F+F"
        self.regla = {"F": "F+F-F-F+F"}

    def aplicar_regla(self, cadena):
        nueva_cadena = ""
        for caracter in cadena:
            nueva_cadena += self.regla.get(caracter, caracter)
        return nueva_cadena

    def generar_secuencia(self):
        secuencia = self.axioma
        for _ in range(self.nivel):
            secuencia = self.aplicar_regla(secuencia)
        return secuencia

    def dibujar(self):
        try:
            secuencia = self.generar_secuencia()
            turtle.speed('fastest')
            turtle.color('red')
            turtle.fillcolor('red')
            turtle.colormode(255)
            turtle.tracer(0, 0)

            # Ajustar posición inicial para empezar en la esquina superior izquierda
            turtle.penup()
            turtle.goto(-200, 200)
            turtle.pendown()

            for comando in secuencia:
                if comando == "F":
                    turtle.forward(5)  # Se puede ajustar la distancia
                elif comando == "+":
                    turtle.right(90)
                elif comando == "-":
                    turtle.left(90)

            turtle.hideturtle()
            turtle.update()
            turtle.done()

        except turtle.Terminator:
            pass


class SalchichaDeMinkowski:
    def __init__(self, iteracion):
        self.iteracion = iteracion
        self.axioma = "F"
        self.reglas = {"F": "F+F-F-F+F"}
        self.pantalla = turtle.Screen()
        self.pantalla.tracer(0, 0)
        self.tortuga = turtle.Turtle()

    def aplicar_reglas(self, cadena):
        nueva_cadena = ""
        for caracter in cadena:
            nueva_cadena += self.reglas.get(caracter, caracter)
        return nueva_cadena

    def generar_l_system(self):
        for _ in range(self.iteracion):
            self.axioma = self.aplicar_reglas(self.axioma)

    def dibujar_l_system(self):
        try:
            self.tortuga.penup()
            self.tortuga.goto(-200, -200)
            self.tortuga.pendown()

            for caracter in self.axioma:
                if caracter == "F":
                    self.tortuga.forward(5)
                elif caracter == "+":
                    self.tortuga.left(90)
                elif caracter == "-":
                    self.tortuga.right(90)

                self.pantalla.update()

            turtle.done()
        except turtle.Terminator:
            pass

    def reset(self):
        self.tortuga.reset()
