# =========================================================DOCUMENTACION INTERNA=======================================================================================================================================================
# -- Objetivo: Implementar el problema de las Torres de Hanoi mediante una simulación gráfica utilizando Canvas, incorporando animaciones y el uso de estructuras tipo stack para la gestión de discos.
# -- Autor: Elmer Juarez
# -- Descipcion: El programa permite visualizar la resolución automática del problema de las Torres de Hanoi. Se emplean pilas (stacks) para representar cada torre y se utilizan animaciones para mostrar el movimiento de los discos (subida, desplazamiento y bajada) dentro de un entorno gráfico.
# -- Lenguaje: Python3
# -- Recursos: Libreria Tkinter
# -- Procesos: Se inicializan tres torres representadas como pilas, donde los discos se almacenan mediante operaciones push y pop. Se aplica un algoritmo recursivo para generar la secuencia de movimientos necesarios para resolver el problema, y posteriormente se animan dichos movimientos en un Canvas.
# -- Historia: Fecha de creacion 27/03/2026
# -- Ajustes pendientes: Implementar control manual del usuario, contador de movimientos y opciones de pausa o ajuste de velocidad.
# ======================================================================================================================================================================================================================================


from tkinter import *
from tkinter import messagebox as mb
import time


# ========================== CLASE TORRE ==========================
class Torre:
    def __init__(self):
        self.pila = []

    def push(self, disco):
        self.pila.append(disco)

    def pop(self):
        if len(self.pila) > 0:
            return self.pila.pop()
        return None


# ========================== CLASE LOGICA ==========================
class TorresHanoi:
    def __init__(self, n):
        self.n = n
        self.torres = [Torre(), Torre(), Torre()]

        i = n
        while i > 0:
            self.torres[0].push(i)
            i -= 1

    def resolver(self, n, origen, auxiliar, destino, movimientos):
        if n == 1:
            movimientos.append((origen, destino))
        else:
            self.resolver(n - 1, origen, destino, auxiliar, movimientos)
            movimientos.append((origen, destino))
            self.resolver(n - 1, auxiliar, origen, destino, movimientos)


# ========================== CLASE GRAFICA ==========================
class HanoiGrafico(Tk):
    def __init__(self):
        super().__init__()
        self.title("Torres de Hanoi")
        self.geometry("1200x700")
        self.config(bg="beige")

        Label(self, text="Número de discos:", font=("Arial", 12, "bold")).pack()

        self.entrada = Entry(self)
        self.entrada.pack()

        Button(self, text="Iniciar", command=self.iniciar, bg="pink").pack()
        Button(self, text="Reiniciar", command=self.reiniciar, bg="lightblue").pack()

        self.canvas = Canvas(self, width=1200, height=600, bg="white")
        self.canvas.pack()

        self.posiciones_x = [150, 600, 1050]

        self.altura_disco = 22
        self.discos_canvas = [[], [], []]

        self.ancho_max_base = 400
        self.ancho_max_disco = 370

        self.base_y = 520
        self.tope_torre = 180

        self.dibujar_torres()

    # ===================== TORRES =====================
    def dibujar_torres(self):
        self.canvas.delete("all")

        i = 0
        while i < 3:
            x = self.posiciones_x[i]

            # base
            self.canvas.create_rectangle(
                x - self.ancho_max_base / 2,
                self.base_y,
                x + self.ancho_max_base / 2,
                self.base_y + 20,
                fill="brown",
            )

            # torre
            self.canvas.create_rectangle(
                x - 6, self.tope_torre, x + 6, self.base_y, fill="black"
            )

            i += 1

    # ===================== INICIAR =====================
    def iniciar(self):
        self.dibujar_torres()

        try:
            n = int(self.entrada.get())
            if n < 1 or n > 10:
                mb.showerror("Error", "Solo entre 1 y 10 discos")
                return
        except ValueError:
            return

        self.juego = TorresHanoi(n)
        self.discos_canvas = [[], [], []]

        factor = self.ancho_max_disco / n

        i = 0
        while i < len(self.juego.torres[0].pila):
            disco = self.juego.torres[0].pila[i]

            ancho = disco * factor
            x = self.posiciones_x[0]
            y = self.base_y - (i * self.altura_disco)

            rect = self.canvas.create_rectangle(
                x - ancho / 2, y - self.altura_disco, x + ancho / 2, y, fill="blue"
            )

            numero_visual = n - disco + 1

            texto = self.canvas.create_text(
                x,
                y - self.altura_disco / 2,
                text=str(numero_visual),
                fill="white",
                font=("Arial", 11, "bold"),
            )

            self.discos_canvas[0].append((rect, texto))
            i += 1

        self.update()

        movimientos = []
        self.juego.resolver(n, 0, 1, 2, movimientos)
        self.animar(movimientos)

    # ===================== REINICIAR =====================
    def reiniciar(self):
        self.canvas.delete("all")
        self.discos_canvas = [[], [], []]
        self.dibujar_torres()

    # ===================== ANIMACION =====================
    def animar(self, movimientos):
        i = 0
        while i < len(movimientos):
            origen, destino = movimientos[i]
            self.mover_disco(origen, destino)
            self.update()
            time.sleep(0.4)
            i += 1

    # ===================== MOVER DISCO =====================
    def mover_disco(self, origen, destino):

        if len(self.juego.torres[origen].pila) == 0:
            return

        if len(self.discos_canvas[origen]) == 0:
            return

        disco = self.juego.torres[origen].pop()
        rect, texto = self.discos_canvas[origen].pop()

        # SUBIR HASTA ARRIBA DEL CANVAS
        while self.canvas.coords(rect)[1] > 80:
            self.canvas.move(rect, 0, -5)
            self.canvas.move(texto, 0, -5)
            self.update()
            time.sleep(0.01)

        coords = self.canvas.coords(rect)
        x_actual = (coords[0] + coords[2]) / 2
        x_destino = self.posiciones_x[destino]

        pasos = 60
        dx = (x_destino - x_actual) / pasos

        # mover horizontal
        i = 0
        while i < pasos:
            self.canvas.move(rect, dx, 0)
            self.canvas.move(texto, dx, 0)
            self.update()
            time.sleep(0.01)
            i += 1

        # bajar
        nivel = len(self.juego.torres[destino].pila)
        y_objetivo = self.base_y - (nivel * self.altura_disco)

        while self.canvas.coords(rect)[3] < y_objetivo:
            self.canvas.move(rect, 0, 5)
            self.canvas.move(texto, 0, 5)
            self.update()
            time.sleep(0.01)

        self.juego.torres[destino].push(disco)
        self.discos_canvas[destino].append((rect, texto))


HanoiGrafico().mainloop()
