'''
Created on 7 juil. 2014

@author: fdaligand
'''
import svgwrite
import random
from svgwrite.animate import AnimateTransform

# svg = svgwrite.Drawing('testsvgwritelib.svg',size=(300,300))
# line = svg.line((300,300),(150,300),stroke=svgwrite.rgb(10,10,16,'%'),stroke_width=(2))
# rect = svgwrite.shapes.Rect(insert=(10,10),size=(110,110))
# animate =AnimateTransform("rotate",from_="0 300 300",to="90 300 300",dur="10s",repeatCount="indefinite",begin="0s")
# animate.set_target('transform') 
# line.add(animate)
# svg.add(line)
# svg.save()
def trmintodeg(value):
    return (value*90)/10000
def compte_tour(data,timebase):
    
    svg = svgwrite.Drawing('comptetour.svg',size=(300,300))
    line = svg.line((150,300),(0,300),stroke=svgwrite.rgb(10,10,16,'%'),stroke_width=(2))
    starttime=0
    startdeg=0
    for value in data:
        deg=trmintodeg(value)
        animate = AnimateTransform('rotate',begin=str(starttime)+'s',from_=str(startdeg)+' 150 300', to=str(deg)+' 150 300',dur=str(timebase)+'s')
        animate.set_target('transform')
        line.add(animate)
        starttime += timebase
        startdeg=deg
    svg.add(line)
    svg.save()
data=[]
for x in range(0,30,1):
    data.append(random.randrange(0,15000,100))
    
compte_tour(data,1)
