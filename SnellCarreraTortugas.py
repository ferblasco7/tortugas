#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:49:09 2020

@author: buntu
"""

#Funcion para pintar una X con turtle. Fuente: https://stackoverflow.com/questions/43021399/turtle-x-drawing-simplification
import turtle 
from numpy import tan, radians

### INDICE DE REFRACCIÓN DE LA ARENA (POR SIMPLICIDAD, N_AGUA=1)
n=2
###


def letraX(t, length):

    half_length = length / 2
    hypotenuse = (2 * half_length**2)**0.5

    t.pendown()
    t.right(45)
    t.forward(half_length)
    t.left(135)

    t.penup()
    t.forward(hypotenuse)
    t.pendown()

    t.left(135)
    t.forward(length)
    t.right(135)

    t.penup()
    t.forward(hypotenuse)
    t.pendown()

    t.right(135)
    t.forward(half_length)
    t.left(45)
    t.penup()

#Coordenadas de meta y salida
meta=[330,-330]
salida=[-340,340]

#angulos de partida de las tortugas a,b,c,d,e:
angulos=[-85,-75,-65,-55,-45]

turtle.reset()
turtle.clear()

t=turtle.Turtle() #t dibuja nuestro entorno


#zona beige arriba y zona azul abajo

#pintamos el mar
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
t.penup()
t.pencolor('white')
t.goto([330,-330])
letraX(t,30)

#Creamos las nuevas tortugas
a=turtle.Turtle()
a.penup()
a.shape('turtle')
a.color('red')
a.pensize(3)
a.turtlesize(1, 1, 2.4)
a.goto(meta)
a.pendown()
a.goto(-340-340/tan(radians(angulos[0])),0)
a.goto(-340,340)
a.setheading(angulos[0])


b=turtle.Turtle()
b.penup()
b.shape('turtle')
b.color('green')
b.pensize(3)
b.turtlesize(1, 1, 2.4)
b.goto(meta)
b.pendown()
b.goto(-340-340/tan(radians(angulos[1])),0)
b.goto(salida)
b.setheading(angulos[1])


c=turtle.Turtle()
c.penup()
c.shape('turtle')
c.color('pink')
c.pensize(3)
c.turtlesize(1, 1, 2.4)
c.goto(meta)
c.pendown()
c.goto(-340-340/tan(radians(angulos[2])),0)
c.goto(salida)
c.setheading(angulos[2])


d=turtle.Turtle()
d.penup()
d.shape('turtle')
d.color('black')
d.pensize(3)
d.turtlesize(1, 1, 2.4)
d.goto(meta)
d.pendown()
d.goto(-340-340/tan(radians(angulos[3])),0)
d.goto(-340,340)
d.goto(salida)
d.setheading(angulos[3])

e=turtle.Turtle()
e.penup()
e.shape('turtle')
e.color('purple')
e.pensize(3)
e.turtlesize(1, 1, 2.4)
e.goto(meta)
e.pendown()
e.goto(-340-340/tan(radians(angulos[4])),0)
e.goto(salida)
e.setheading(angulos[4])



## EMPIEZA LA CARRERA
tortugas=[a,b,c,d,e]
posicion_y_podio=320

#configuramos la velocidad de la animacion y el tamaño del trazo
for tortuga in tortugas:
  tortuga.pensize(10)
  tortuga.speed(5)

#a correr
tortugas_tierra=tortugas
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

turtle.done()