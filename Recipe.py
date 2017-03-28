# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:04:25 2016

@author: zach
"""
from Measurement import Measurement
import os

class Recipe:    
    
   
        
    def __init__(self, name, OD, ID, wall, concent, oval):
        self.Name = name
        self.outerDiameter = OD
        self.innerDiameter = ID
        self.Wall = wall
        self.Concentricity = concent
        self.Ovality = oval
        
    def getOD(self):
        return self.outerDiameter
        
    def setOD(self, newOD):
        self.outerDiameter = newOD
        
    def getID(self):
        return self.innerDiameter
        
    def setID(self, newID):
        self.innerDiameter = newID
        
    def getWall(self):
        return self.Wall
    
    def setWall(self, newWall):
        self.Wall = newWall
        
    def getConc(self):
        return self.Concentricity
    
    def setConc(self, newConc):
        self.Concentricity = newConc
        
    def getOvality(self):
        return self.Ovality
    
    def setOvality(self, newOval):
        self.Ovality = newOval
        
    def printRecipe(self):         
         # Print the recipe in a controlled manner
        print("") 
    def readRecipe(self):
        # Read a file and construct the recipe from the contents
        print("")
    def writeRecipe(self,out_file_name,x):
    
        if x == 0:
            os.remove(out_file_name)
        try:
            out_file = open(out_file_name, 'a');
            out_file.write( self.Name +"\n")
            out_file.write( self.outerDiameter +"\n")
            out_file.write( self.innerDiameter +"\n")
            out_file.write( self.Wall +"\n")
            out_file.write( self.Concentricity +"\n")
            out_file.write( self.Ovality +"\n")
            
        except:
            print("File open did not work")
        out_file.close()
        
         
    
        