# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:22:45 2016

@author: zach
"""
import os
class Rules: 

    def __init__(self, name, upper_tol, lower_tol):
        self.name = name
        self.upper_tol = 0.0
        self.lower_tol = 0.0
        
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
        
    def getUpperTol(self):
        return self.upper_tol
        
    def setUpperTol(self, newUpperTol):
        self.upper_tol = newUpperTol
        
    def getLowerTol(self):
        return self.lower_tol
        
    def setLowerTol(self, newLowerTol):
        self.lower_tol = newLowerTol
        
    def printRule(self):
        # Print the rule in a controlled manner
        print("Print")
        
    def readRule(self):
        # Read a file and construct a rule from the contents
        print("Read")
        
    def writeRule(self,out_file_name,x):
      if x == 0:
        os.remove(out_file_name)
      try:
        out_file = open(out_file_name, 'a');
        out_file.write( self.name + " " + self.upper_tol + " " + self.lower_tol + "\n" )
      except:
        print("OOoops, file open did not work")
      out_file.close()
        

        