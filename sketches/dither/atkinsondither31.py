import os

import random

import time

import PIL 





# Schamlos von https://github.com/tgray/hyperdither kopiert und für NodeBox angepasst

def dither(graustufenArray, breite, hoehe, schwelle=127):



    # eine liste genauso gross wie das zu konvertierende Bild

    fehlerBuffer = [ 0 ] * len(graustufenArray)



    fehlerAchtel = 0



    for y in xrange(hoehe):

        for x in xrange(breite):

            offset = y * breite + x

            pixelWert = fehlerBuffer[offset] + graustufenArray[offset]



            # Fehler ausrechnen und Pixel setzen

            if pixelWert >= schwelle:

                # weiß

                fehlerAchtel = (pixelWert - 255) / 8

                # x,y

                graustufenArray[offset] = 255

            else:

                # schwarz

                fehlerAchtel = pixelWert / 8

                # x,y

                graustufenArray[offset] = 1



            # 1/8 Fehler auf 6 umliegende Pixel verteilen

            if x + 1 < breite:

                # x+1, y

                fehlerBuffer[offset+1] += fehlerAchtel

                if x + 2 < breite:

                    # x+2, y

                    fehlerBuffer[offset+2] += fehlerAchtel

            if y + 1 < hoehe:

                # x-1, y+1

                fehlerBuffer[offset+breite-1] += fehlerAchtel

                # x, y+1

                fehlerBuffer[offset+breite] += fehlerAchtel

                if y + 2< hoehe:

                    # x, y+2

                    fehlerBuffer[offset+breite+breite] += fehlerAchtel

                if x + 1 < breite:

                    # x+1, y+1

                    fehlerBuffer[offset+breite+1] += fehlerAchtel

    del fehlerBuffer

    return str(graustufenArray)





def atkinsondither( imagefilepath ):

    img = PIL.Image.open( imagefilepath ).convert('L')

    w, h = img.size

    gray = bytearray( img.tobytes() )

    bw = dither(gray, w, h, schwelle=127)

    out = PIL.Image.frombytes('L', (w,h), bw)

    # name = "atkinsondither_" + datestring(nocolons=True) + '.png'
    name = "atkinsondither_" + datestring(nocolons=True) + '.gif'

    # out.convert('1').save(name, format="PNG")
    out.convert('1').save(name, format="GIF")

    return os.path.abspath(name)





# aktivieren für wiederholbare zufalls folge

# random.seed(0)



# waehle ein zufälliges Desktop Bild

# filetuples = imagefiles( "/Library/Desktop Pictures", False )

filetuples = imagefiles("~/git/nodebox1/sketches/dither/images", False)

images = []

for t in filetuples:

    path, filesize, lastmodified, mode, islink = t

    w,h = imagesize( path )

    images.append( path )

img = choice( images )



# konvertiere. liefert Pfad

starttime = time.time()

hypercardized = atkinsondither( img ) 

stoptime = time.time()



# canvas der Bildgrösse anpassen

w,h = imagesize( hypercardized )

size(w,h)



# plaziere Bild

image(hypercardized, 0,0)





# stats



print "IN:", img

# print "OUT:", hypercardized

print "SIZE:", w, h

print "TIME: %.4f" % ( round(stoptime - starttime, 3) )

print

