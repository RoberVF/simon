import random
import time
from sense_hat import SenseHat
sense= SenseHat()

r= (255,0,0)
g= (0,255,0)
b= (0,0,255)
a= (245,255,50)
n= (0,0,0)
all_colors= [r,g,b,a]
color=[]
nivelActual= 2

arriba= a
izquierda= b
derecha= g
abajo= r

final_result= []

tArriba= "up"
tAbajo= "down"
tDerecha= "right"
tIzquierda= "left"

def primeraTransicion():
  sense.show_message("Simon dice")

def mostrarColor():
  for i in range(0,nivelActual):
    color.append(random.choice(all_colors))
  random.shuffle(color)
  print(color)  
  for i in range(0, nivelActual):
    sense.clear(color[i])
    time.sleep(.7)
    sense.clear()
    time.sleep(.1)
  final_color= [n,n,arriba,arriba,arriba,arriba,n,n,
              n,n,arriba,arriba,arriba,arriba,n,n,
              izquierda,izquierda,n,n,n,n,derecha,derecha,
              izquierda,izquierda,n,n,n,n,derecha,derecha,
              izquierda,izquierda,n,n,n,n,derecha,derecha,
              izquierda,izquierda,n,n,n,n,derecha,derecha,
              n,n,abajo,abajo,abajo,abajo,n,n,
              n,n,abajo,abajo,abajo,abajo,n,n]
  sense.set_pixels(final_color)


def seleccionarColor():
  global nivelActual
  global final_result
  while True:
    for e in sense.stick.get_events():
      
      if(e.direction == tArriba):
        final_result.append(a)
        time.sleep(.05)
        
      elif(e.direction == tDerecha):
        final_result.append(g)
        time.sleep(.05)
        
      elif(e.direction == tAbajo):
        final_result.append(r)
        time.sleep(.05)
        
      elif(e.direction == tIzquierda):
        final_result.append(b)
        time.sleep(.05)
        
      else:
        sense.clear()
        time.sleep(1)
        final_result= []
        nivelActual= 1
        primeraTransicion()
        mostrarColor()
        seleccionarColor()
      
      
      
      if(len(final_result) == nivelActual*2):
        for n in range(0, nivelActual):
          final_result.pop(n)

        if(final_result == color[:nivelActual]):
          sense.show_message("Nivel {}".format(nivelActual + 1), back_colour=[0,255,0])
          final_result= []
          nivelActual += 1
          sense.clear()
          time.sleep(.5)
          mostrarColor()
          seleccionarColor()
        
        else:
          sense.show_message("Derrota {}".format(nivelActual), back_colour=[255,0,0])
          print("Ha llegado hasta el nivel: " + str(nivelActual))
          
          
        
      else: 
        print("Siguiente")


#primeraTransicion()
mostrarColor()
seleccionarColor()