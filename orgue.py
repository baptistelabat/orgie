# -*- coding: utf-8 -*-
import math
from SimpleCV import Image, Color, Display, Camera

cam = Camera()
#imgVelleda = Image('velleda.jpg')
imgVelleda = cam.getImage()
imgVelleda = imgVelleda.resize(100, 100)

toDisplay = False
if toDisplay:
  disp = Display((640, 480))

while True:
    for i_time in range(0, imgVelleda.width) : 
        imgVelleda = cam.getImage().resize(100, 100)
        wb = imgVelleda.hueDistance(color=Color.BLUE).invert().threshold(210)
        # Move a vertical scan line and take blue pixel index
        blue_pix = [i for i in range(len(wb.getVertScanline(i_time))) if wb.getVertScanline(i_time)[i].any()]
        print blue_pix
        # Draw the scan line
        imgVelleda_copy = imgVelleda.copy()
        imgVelleda_copy.drawLine((i_time,0), (i_time, imgVelleda.height), color= Color.RED)
        imgVelleda_copy.drawCircle( ((0.5+math.floor(i_time*8/imgVelleda.width))*imgVelleda.width/8.0, 10), 5, color=Color.RED, thickness = -1)
        # Draw circles at blue point
        for pix in blue_pix:
            imgVelleda_copy.drawCircle((i_time, pix), 5)
        if toDisplay :
          imgVelleda_copy.save(disp)
