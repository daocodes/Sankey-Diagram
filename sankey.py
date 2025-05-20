# TITLE: Sankey Diagram

# AUTHOR: Dao Bui

# DATE DUE: 5/16/2025
# DATE SUBMITTED: 5/20/2025

# COURSE TITLE: Python for Scientist

# DESCRIPTION: A project that creates an animated sankey diagram based on a text file with data. It will distribute and show the percentages of values.

#These are some needed imports for my code to work. The math is used for the curves
from graphics import *
from math import sin, pi

import random

#This is the main file where a file is inputted by the user, and then a series of operations to create the sankey diagram will occur.
def main():
    inputFileName = input("Give me the name of the data file:") #Takes the input in 
    print(inputFileName)
    

    infile = open(inputFileName, "r") #Opens the file

    infile.readline()
    title = infile.readline().strip() 
    totalLabel = infile.readline().strip() #This reads in the label and processes it.
    
    fileName = inputFileName.split('.')[0]
    
    
    

    win = GraphWin(title, 900, 900) # Creates the canvas
    
    titleText = Text(Point(450, 50), title)
    titleText.setSize(20)
    titleText.setStyle("bold")
    titleText.draw(win)
    label = Text(Point(40, 450), totalLabel)# Initilizes the title
    label.draw(win)
    dictionary = makeDictionary(infile) #Creates a dictionary with the data given
    drawSankey(win,dictionary)
    fileText = Text(Point(100, 875), "FILE: " + fileName +".txt")
    fileText.draw(win)
    authorText = Text(Point(750, 875), "Designed by: Dao Bui 05/20/25")#Adds the file and the creator names.
    authorText.draw(win)
    
    win.postscript(file = fileName+".ps", colormode = "color")
    win.postscript(file = fileName+".pdf", colormode = "color") #This is to process the image into a ps and pdf file
    #win.getMouse()
    win.close()
    #Closes the system
    
    
    
    


    
#This is a function that creates a dictionary from the input file. It will parse through a series of lines and then spit out a dictionary at the end.
def makeDictionary(infile):
    emptyDict = dict() #Initilizes the dictionary
    currentLine = infile.readline()
    while currentLine:
        currentLinesSplit = currentLine.split(',')
        if len(currentLinesSplit) >= 2:
            emptyDict[currentLinesSplit[0]] = float(currentLinesSplit[1]) #This loop parses through the file and then adds to the dictionary
        currentLine = infile.readline()
    infile.close()
    return emptyDict


    
#This is a function that draws the actual diagram
def drawSankey(win, dictionary):
    colors = [
    (255, 0, 0),        # red
    (255, 192, 203),    # pink
    (255, 165, 0),      # orange
    (0, 128, 0),        # green
    (0, 0, 255),        # blue
    (128, 0, 128),      # purple
    (0, 255, 255),      # cyan
    (0, 128, 128),      # teal
    (255, 255, 0),      # yellow
    (0, 255, 0),        # lime
    (255, 255, 255)     # white
]
    totalFlow = 0
    numberOfDestinations = 0
    for value in dictionary.values():
        totalFlow += value
        numberOfDestinations += 1
#A series of needed calculations in order to calculate the flow per destination
    availablePixels = 600 - (numberOfDestinations - 1) * 10 
    numberOfPixelsPerUnit = availablePixels / totalFlow

    dest_heights = {}
    for key in dictionary:
        dest_heights[key] = dictionary[key] * numberOfPixelsPerUnit

    heightOfSourceBar = totalFlow * numberOfPixelsPerUnit
    total_dest_height = sum(dest_heights.values()) + (numberOfDestinations - 1) * 10

    # Starting Y position
    start_y = (900 - total_dest_height) / 2
    source_y1 = (900 - heightOfSourceBar) / 2

    # Draw source rectangle
    source = Rectangle(Point(100, source_y1), Point(150, source_y1 + heightOfSourceBar))
    source.setFill("white")
    source.setOutline('black')
    source.draw(win)

    # Draw destinations and connectors
    source_current_y = source_y1
    current_y = start_y
    colorCount = 0
    

    for dest, height in dest_heights.items():
        # Draw destination rectangle
        destColor = colors[colorCount]
        dest_rect = Rectangle(Point(700, current_y), Point(800, current_y + height))
        dest_rect.setFill(color_rgb(destColor[0], destColor[1], destColor[2]))
        dest_rect.setOutline('black')
        dest_rect.draw(win)

        # Draw label
        label = Text(Point(850, current_y + height / 2), dest)
        label.draw(win)

        source_color = (225,225,225)
        
        #Initilizes a top and bottom array
        top = []
        bottom = []
        
        
                
        for x in range(148,702):
                
            value = (x-148) / 550
            p = value * pi - pi / 2
            p = (sin(p) + 1) / 2 #Calculates the amount to curve and then creates a top and bottom value
            
            top_y = source_current_y + (current_y - source_current_y) * p
            bottom_y = source_current_y + height + (current_y + height - source_current_y - height) * p
            
            top.append(Point(x, top_y))
            bottom.insert(0, Point(x, bottom_y))
                    
                  
            r = int(source_color[0] + (destColor[0] - source_color[0])*p)
            g = int(source_color[1] + (destColor[1] - source_color[1])*p)
            b = int(source_color[2] + (destColor[2] - source_color[2])*p)
            color = color_rgb(r, g, b) #This is for the gradient
        
            line = Rectangle(Point(x, top_y), Point(x + 1, bottom_y))
            line.setFill(color)
            line.setOutline('')
            line.draw(win)
            
            #This is for the black outline
        polygon_points = top + bottom
        segment_outline = Polygon(polygon_points)
        segment_outline.setOutline("black")
        segment_outline.setWidth(2)
        segment_outline.setFill("")  # Transparent fill
        segment_outline.draw(win)
        
        dest_rect = Rectangle(Point(700, current_y+1), Point(702, current_y + height-1))
        dest_rect.setFill(color_rgb(destColor[0], destColor[1], destColor[2]))
        dest_rect.setOutline('')
        dest_rect.draw(win)
        #Increments after the loop
        source_current_y += height
        current_y += height + 10
        colorCount = colorCount + 1
        
    
    
        
        
       
       #This is to cover up the outline
    source = Rectangle(Point(147, source_y1+.5), Point(150, source_y1 + heightOfSourceBar-.5))
 
    source.setFill("white")
    source.setOutline('')
    source.draw(win)
    
    
    #California_Electricity.txt

                    
            
            
        
        



    
    
    
    
    
    
    
    
        
        
    
    
    
    
    #The main function that is called
main()
