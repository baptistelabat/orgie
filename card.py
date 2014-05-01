# -*- coding: utf-8 -*-
import math
from SimpleCV import Image, Camera
from numpy import argmax, arange
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 1234
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
cam = Camera(0)
toDisplay = True
toBroadcast = True


  
if toBroadcast:
    from SimpleCV import JpegStreamer
    js = JpegStreamer()
    print "Broadcasting at ", js.url()
    
class Track:
    def __init__(self, topLeftCornerX=0, topLeftCornerY=0, width=0, height=0):
        self.topLeftCornerX = topLeftCornerX
        self.topLeftCornerY = topLeftCornerY
        self.width = width
        self.height = height
        
track1 = Track(0, 50, 100, 150)
track2 = Track(110, 50, 100,150)
track3 = Track(220, 55, 100, 150)
tracks = [track1, track2, track3]

if toDisplay:
  from SimpleCV import Display
  disp = Display((640*2, 480))
while True:
    img = cam.getImage()
    if toDisplay or toBroadcast:
        imgDisplay = img
    img.save("box.jpg")
    img = img.stretch(80, 140).medianFilter().binarize().gaussianBlur(sigmaX =11, sigmaY=11).stretch(50, 255)
    
    track_counter = 0
    for track in tracks:
        track_counter +=1
        track_img = img.crop(track.topLeftCornerX, track.topLeftCornerY, track.width, track.height)
        ana = track_img 
        if toDisplay or toBroadcast:
            imgDisplay = imgDisplay.sideBySide(ana)
            imgDisplay = ana
        counter = 0
        for i_time in arange(0, ana.height, ana.height/32.0):
            counter+=1
            i_time = int(round(i_time))
            l = ana.getHorzScanline(i_time)[:,1]
            i_max = argmax(l)
            MESSAGE = str(track_counter) + "," + str(counter) + "," + str(i_max*1.0/ana.width)
            print MESSAGE
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            if i_max!=0:
                ana.drawCircle((i_max, i_time), 5, color = (255, 0, 0), thickness = -1)
    if toDisplay:
        imgDisplay.save(disp)
    if toBroadcast:
        imgDisplay.save(js)

