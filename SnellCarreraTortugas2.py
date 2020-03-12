# -*- coding: utf-8 -*-

"""
Created on Wed Feb 12 17:49:09 2020

@author: fer
"""

import turtle 
from numpy import sin, tan, arctan, radians, degrees
import tkinter #crear dialogos

### DEFINICIONES DE NÚMEROS MÁGICOS: DISTANCIAS, ANGULOS, PUNTOS,...
# PREGUNTAMOS EL INDICE DE REFRACCIÓN DE LA ARENA (POR SIMPLICIDAD, N_AGUA=1)
parent = tkinter.Tk()
parent.overrideredirect(1) # para que no desaparezca
parent.withdraw() # ???? Hide the window as we do not want to see this one
simpledialog=tkinter.simpledialog
n = simpledialog.askfloat('Fijar índice de refracción', '¿Qué índice de refracción quieres fijar para la arena?', initialvalue=2, minvalue=1.0, maxvalue=1000.0, parent=parent)
#Coordenadas de meta y salida
meta=[330,-330]
salida=[-340,340]
X=meta[0]-salida[0] #distancia recorrida en X (en ambos medios)
Y1,Y2=330,340 #distancia recorrida en Y en cada medio
posicion_y_podio=320 #coordenada y del podio
#angulos (respecto al eje x [complementarios al angulo respecto a la normal]) de partida y colores de las tortugas a,b,c,d,e:
angulos=[-45,-55,-65,-75,-85] #en orden inverso por usar la función pop() 
colores=['purple','#7FFFD4','green','#FFFF00','red'] #en orden inverso por usar la función pop()     
#hacemos una copia de los ángulos de cada tortuga (esta vez sin invertir y RESPECTO A LA NORMAL) para los cálculos post-animación dirigidos a comprobar la ley de snell
angulos_normal=[90-abs(angulo) for angulo in angulos] #pasamos a angulos respecto a la normal
angulos_normal.reverse() #los ordenamos segun posicion de las tortugas
tortugas_nombres=['roja','amarilla','verde','azul','morada'] #nombres de las tortugas












### DIBUJAMOS EL ENTORNO


#zona beige arriba y zona azul abajo

#pintamos el mar
turtle_window = turtle.Screen() 
turtle.setup()
t=turtle.Turtle() #t dibuja nuestro entorno
t.hideturtle()

t.pencolor("blue")
t.fillcolor('blue')
t.pensize(5)
t.begin_fill()

t.goto(-350, 0)
t.goto(350, 0)
t.goto(350, -350)
t.goto(-350, -350)
t.goto(-350, 0)
t.end_fill()

#pintamos la playa
t.pencolor("#FFA500")
t.fillcolor('#FFA500')
t.pensize(5)
t.begin_fill()

t.goto(-350, 0)
t.goto(350, 0)
t.goto(350, 350)
t.goto(-350, 350)
t.goto(-350, 0)
t.end_fill()

#dibujamos la meta
t.hideturtle()
t.penup()
t.goto([330,-360])
t.color('white')
style = ('Courier', 40, 'bold')
t.write('X', font=style, align='center')

#escribimos el índice de refracción de la tierra (y del agua, aunque no se pueda modificar)
#indice agua
t.goto([195,-45])
style = ('Courier', 25, 'bold')
t.write('n2 = 1.0',font=style)

#indice tierra
t.goto([195,-5])
t.color('black')
t.write('n1 = '+ str(n),font=style)

#Creamos las nuevas tortugas y las metemos en una lista
a,b,c,d,e=turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
tortugas=[a,b,c,d,e]
for tortuga in tortugas: tortuga.hideturtle() 

#llevamos las tortugas a la salida (pasando por meta, para dejar dibujada su trayectoria) y las orientamos
for tortuga in tortugas:
    tortuga.penup()
    tortuga.shape('turtle')
    tortuga.showturtle()
    tortuga.color(colores.pop())
    tortuga.pensize(3)
    tortuga.turtlesize(1, 1, 2.4)
    tortuga.goto(meta)
    tortuga.pendown()
    angulo=angulos.pop()
    tortuga.goto(-340-340/tan(radians(angulo)),0)
    tortuga.goto(salida)
    tortuga.setheading(angulo)

# Usuario, empezamos la carrera?
messagebox=tkinter.messagebox
info = messagebox.showinfo('Carrera de tortugas', '¿Empezamos la carrera?', parent=parent)


## EMPIEZA LA CARRERA


#configuramos la velocidad de la animacion y el tamaño del trazo
for tortuga in tortugas:
  tortuga.pensize(10)
  tortuga.speed(5)

#a correr
tortugas_tierra=tortugas[:]
tortugas_agua=[]

while tortugas_agua!=[] or tortugas_tierra!=[]:
  for tortuga in tortugas_tierra:
    tortuga.forward(1)
  for tortuga in tortugas_agua:
    tortuga.forward(n)
  
  #cuando las tortugas llegan al agua, giran:
  posiciones_y_tierra=[tortugalenta.ycor() for tortugalenta in tortugas_tierra]
  tortuga_llega_agua=[numero_tortuga for numero_tortuga in range(len(tortugas_tierra)) if posiciones_y_tierra[numero_tortuga]<0.01]
  if tortuga_llega_agua!=[]:
    tortu_que_gira=tortugas_tierra[tortuga_llega_agua[0]]
    tortu_que_gira.setheading(tortu_que_gira.towards(330,-330))    
    #quitamos la tortuga de la lista de las que estan en tierra y la añadimos a las que estan en mar
    tortugas_agua.append(tortugas_tierra.pop(tortuga_llega_agua[0]))


  #las tortugas ganadoras dejan de avanzar
  posiciones_y_agua=[tortugarapida.ycor() for tortugarapida in tortugas_agua]
  tortuga_gana=[numero_tortuga for numero_tortuga in range(len(tortugas_agua)) if posiciones_y_agua[numero_tortuga]-meta[1]<.01]
  if tortuga_gana!=[]:
    tortu_que_gana=tortugas_agua[tortuga_gana[0]]
    
    tortu_que_gana.penup()
    tortu_que_gana.goto(320,posicion_y_podio)
    tortu_que_gana.turtlesize(3, 3, 7.5)
    tortu_que_gana.stamp()
    posicion_y_podio=posicion_y_podio-30
    
    tortu_que_gana.stamp   
    #quitamos la tortuga de la lista de las que estan en mar
    tortugas_agua.pop(tortuga_gana[0])

# Usuario, cerramos la ventana?
messagebox=tkinter.messagebox
info = messagebox.showinfo('Carrera de tortugas', '¡Carrera finalizada!', parent=parent)

turtle.bye()
#COMPROBAMOS QUE GANA LA QUE MÁS SE ACERCA A LA LEY DE SNELL
for angulo_inc in angulos_normal:
    X1=Y1*tan(radians(angulo_inc)) #distancia recorrida en x en el medio 1
    angulo_ref=round(degrees(arctan((X-X1)/Y2)),1) #redondeamos a los decimales
    nombre=tortugas_nombres.pop(0)
    print('\n\nLa tortuga {} incide en el agua con un ángulo de {}º respecto a la normal, y se dirige a la meta desde el agua con un ángulo de {}º respecto a la normal.'.format(nombre,angulo_inc,angulo_ref))
    print('\nPara la tortuga {}: n1 * sen(angulo_inc) = {}  y  n2 * sen(angulo_ref) = {}'.format(nombre,round(n*sin(radians(angulo_inc)),2),round(sin(radians(angulo_ref)),2)))

