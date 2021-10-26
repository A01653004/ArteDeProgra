from turtle import *
speed(8)
s = 200



def cuadrado():
    for i in range(4):
        fd(s)
        lt(90)
    
    
def triangulo():
    for k in range(3):
        fd(s)
        lt(120)
    
    

def hexagono():
    for j in range(6):
        fd(s)
        lt(60)
    
def pentagono():
    for j in range(5):
        fd(s)
        lt(72)
    

cuadrado()
triangulo()
done()