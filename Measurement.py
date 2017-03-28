# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:26:42 2016

@author: zach
"""  
# This file will contain the measurement class

# Construct a default measurement
class Measurement:
    
        
    
    def __init__(self):
        self.Nominal = 0.0
        self.upperSpec = 0.0
        self.lowerSpec = 0.0
        self.upperWarning = 0.0
        self.lowerWarning = 0.0
        self.referenceBool = False 
    
    def __init__(self, nominal, upperspec, lowerspec, upperwarn, lowerwarn, ref ):
        self.Nominal = nominal
        self.upperSpec = upperspec
        self.lowerSpec = lowerspec
        self.referenceBool = ref
        self.upperWarning = upperwarn
        self.lowerWarning = lowerwarn

    def getNom(self):
        return self.Nominal
        
    def setNom(self, newNom):
        self.Nominal = newNom
        
    def getUppeSpec(self):
        return self.upperSpec
        
    def setUpperSpec(self,newUpperSpec):
        self.upperSpec = newUpperSpec
        
    def getLowerSpec(self):
        return self.lowerSpec
    
    def setLowerSpec(self, newLowerSpec):
        self.lowerSpec = newLowerSpec
        
        # Calculate and return an upper warning value
    def getUpperWarning(self):
        return self.upperWarning
        
        # Calculate and return a lower warning value
    def getLowerWarning(self):
        return self.lowerWarning
        
    def printMeasurement(self):
        # Print the recipe in a controlled manner
        print("")