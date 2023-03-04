#Copyright 2021, Morgan Purkis, All rights reserved.

#IMPORTS
from PIL import Image, ImageDraw

#SCRIPT
runScript = 1
while runScript == 1:
    
    #INPUTS
    imageName = input("Input image filename ... ")
    processedName = input("Input filename for processed image ... ")
    processType = int(input("Choose type: 1 for edge demonstration, "))

    #VARIABLES
    img = Image.open(imageName)  
    imgY = img.size[1]
    imgX = img.size[0]
    pixelRGB = img.load()
    pixelEdge = {}
    differencesR = []
    differencesG = []
    differencesB = []
    averageR = 0
    averageG = 0
    averageB = 0

    #EDGE ASSIGNMENT ALONG X AXIS
    for y in range(imgY):
        for x in range(imgX):
            try:
                pixelRGB[x+1,y]
            except:
                None
            else:
                if pixelRGB[x,y][0] >= pixelRGB[x+1,y][0]:
                    differencesR.append(pixelRGB[x,y][0] - pixelRGB[x+1,y][0])
                else:
                    differencesR.append(pixelRGB[x+1,y][0] - pixelRGB[x,y][0])
                if pixelRGB[x,y][1] >= pixelRGB[x+1,y][1]:
                    differencesG.append(pixelRGB[x,y][1] - pixelRGB[x+1,y][1])
                else:
                    differencesG.append(pixelRGB[x+1,y][1] - pixelRGB[x,y][1])
                if pixelRGB[x,y][2] >= pixelRGB[x+1,y][2]:
                    differencesB.append(pixelRGB[x,y][2] - pixelRGB[x+1,y][2])
                else:
                    differencesB.append(pixelRGB[x+1,y][2] - pixelRGB[x,y][2])
        averageR = sum(differencesR)/imgX
        averageG = sum(differencesG)/imgX
        averageB = sum(differencesB)/imgX 
        for x in range(imgX):
            try:
                pixelRGB[x+1,y]
            except:
                None
            else:
                if averageR < differencesR[x] and averageG < differencesG[x] and averageB < differencesB[x]:
                    pixelEdge[str(x + 1) + "," + str(y)] = 1
        differencesR = []
        differencesG = []
        differencesB = []

    #EDGE ASSIGNMENT ALONG Y AXIS
    for x in range(imgX):
        for y in range(imgY):
            try:
                pixelRGB[x,y+1]
            except:
                None
            else:
                if pixelRGB[x,y][0] >= pixelRGB[x,y+1][0]:
                    differencesR.append(pixelRGB[x,y][0] - pixelRGB[x,y+1][0])
                else:
                    differencesR.append(pixelRGB[x,y+1][0] - pixelRGB[x,y][0]) 
                if pixelRGB[x,y][1] >= pixelRGB[x,y+1][1]:
                    differencesG.append(pixelRGB[x,y][1] - pixelRGB[x,y+1][1])
                else:
                    differencesG.append(pixelRGB[x,y+1][1] - pixelRGB[x,y][1]) 
                if pixelRGB[x,y][2] >= pixelRGB[x,y+1][2]:
                    differencesB.append(pixelRGB[x,y][2] - pixelRGB[x,y+1][2])
                else:
                    differencesB.append(pixelRGB[x,y+1][2] - pixelRGB[x,y][2]) 
        averageR = sum(differencesR)/imgY
        averageG = sum(differencesG)/imgY
        averageB = sum(differencesB)/imgY
        for y in range(imgY):
            try:
                pixelRGB[x,y+1]
            except:
                None
            else:
                if averageR < differencesR[y] and averageG < differencesG[y] and averageB < differencesB[y]:
                    pixelEdge[str(x) + "," + str(y + 1)] = 1
        differencesR = []
        differencesG = []
        differencesB = []

    #OUTPUT
    if processType == 1:
        newimg = Image.new("RGB", (img.size[0], img.size[1]), color = "white")
        for y in range(imgY):
            for x in range(imgX):
                try:
                    pixelEdge[str(x) + "," + str(y)]
                except:
                    None
                else:
                    if pixelEdge[str(x) + "," + str(y)] == 1:
                        newimg.putpixel((x,y),(0,0,0,255))
        newimg.save(processedName)







        
