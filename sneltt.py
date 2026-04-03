# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:05:24 2026

@author: User
"""

import math
import turtle


n1=float(input("Choisir un indice optique pour le milieu 1"))
n2=float(input("Choisir un indice optique pour le milieux 2"))
ai_deg=float(input("choisir un angle d'incidence"))
ai_rad=math.radians(ai_deg)

ar_rad=math.asin((n1*math.sin(ai_rad))/(n2))
print("angle de réfraction :",math.degrees(ar_rad))


#le rayon part de 200,200

#on va chercher les coordoennés 
if ai_rad==90:
    turtle.penup()
    turtle.colormode(255)
    turtle.setposition(300,400)
    turtle.pendown()
    turtle.goto(300,0)
    turtle.penup()
    turtle.setposition(200,200)
    turtle.pendown()
    turtle.goto(300,200)
    turtle.goto(600,200)
    
    
if ai_rad <90:
    turtle.penup()
    turtle.colormode(255)
    turtle.setposition(300,400)
    turtle.pendown()
    turtle.goto(300,0)
    turtle.penup()
    turtle.setposition(200,200)
    cy1=math.tan(ai_rad)*100
    print(cy1)
    turtle.pendown()
    turtle.goto(300,200+cy1)
    cy=math.tan(ar_rad)*300
    turtle.goto(600,200+cy1+cy)
    turtle.penup()
    turtle.setposition(200,200)
    turtle.pendown()
    turtle.goto(300,200-cy1)
    cy=math.tan(ar_rad)*300
    turtle.goto(600,200-cy1-cy)
    
if ai_rad>90:
    print("no")
    