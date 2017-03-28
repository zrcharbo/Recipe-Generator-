# -*- coding: utf-8 -*-
"""
Spyder Editor
    File:        recipeGenerator.py
    Date:        10/07/16
    Author:      Zach Charbonneau, Robert Kadlec
    Course:      CSC 7014
    Instructor:  Nguyen Thai
    
    Descritption : Program isstill under construction, commented is nto complete
    Also naming conventions will be reviewed prior to final release
    of programming for the project.........

"""

# Simple enough, just import everything from tkinter.
#Global import will not work,need to consult instructor
import tkinter as t
import os
from tkinter import Frame, Menu, messagebox
from PIL import Image, ImageTk
from Recipe import Recipe
from Measurement import Measurement
from Rules import Rules

# Here, we are creating our class, RecipeWindow, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class RecipeWindow(Frame):

  global recipe,d,rule,up_tol,low_tol
  rule=[Rules("default",0.0,0.0) for i in range(3)]
  up_tol = [0 for i in range(3)]
  low_tol = [0 for i in range(3)]
  
  
  try:
    inFile = open("rules.txt", 'r')
  except:
    # Read does not create a new file
    print("Specified input file does not exist or some other IO Error.  quitting");
    os._exit(1)
  
  count=0
  for line in inFile:
    if( line != "" ):
      words = line.split()
      try:
        rule[count].setName(words[0])
        rule[count].setUpperTol(words[1])
        rule[count].setLowerTol(words[2])
      except:
        print("Rules file not structured right or some other IO Error.  quitting");
        os._exit(1)
      count=count+1
  inFile.close()
  
  up_tol[0]="BOO"
    
  # Define settings upon initialization. Here you can specify
  def __init__(self, master=None):
        
    # parameters that you want to send through the Frame class. 
    Frame.__init__(self, master)   

    #reference to the master widget, which is the tk window                 
    self.master = master

    #with that, we want to then run init_window, which doesn't yet exist
    self.init_window()

  #Creation of init_window
  def init_window(self):
        
    # a Do Nothing Funciton as a placeholder opens a dialog box
    def donothing():
      filewin = t.Toplevel(root)
      button = t.Button(filewin, text="Do nothing button")
      button.pack()
      
    def openHelpFile():
      os.startfile("helpDoc.pdf")
      
    def aboutDialog():
      t.messagebox.showinfo("About", " The Recipe Value Generator,\nDeveloped November 2016\nVersion 1.0\n\nrkadlec, zcharbeneau")
        
    def loadRecipeWindow():
        
      d=Measurement(0.0,0.0,0.0,0.0,0.0,'false')
      
      def recipeload():
        reciperetrieve=enterE.get()
        print(reciperetrieve)
        try:
          recipe=Recipe(reciperetrieve,d,d,d,d,d)
          recipeString.set(recipe.Name)
          od_nom_var.set(d.getNom())
          od_up_var.set(d.getUppeSpec())
          od_low_var.set(d.getLowerSpec())
          id_nom_var.set(d.getNom())
          id_up_var.set(d.getUppeSpec())
          id_low_var.set(d.getLowerSpec())
          wall_nom_var.set(d.getNom())
          wall_up_var.set(d.getUppeSpec())
          wall_low_var.set(d.getLowerSpec())
          conc_nom_var.set(d.getNom())
          conc_low_var.set(d.getLowerSpec())
          ovality_nom_var.set(d.getNom())
          ovality_up_var.set(d.getUppeSpec())
        except:
          recipeString.set("INVALID NAME")
        w.destroy()
        
      w=t.Toplevel()
      w.geometry("300x160")
      w.title("Load Recipe")
      enterL= t.Label(w, text ="Enter Recipe Name", font=('Times', 20))
      enterL.place(x=35,y=5,width=230,height=30)
      enterE=t.Entry(w)
      enterE.place(x=55,y=50,width=180,height=30)
      loadBtn = t.Button(w, text="LOAD", height=1,width=12,bd=6,font=("Arial", 14, "bold"))
      loadBtn.place(x=65,y=90)
      loadBtn.configure(command=recipeload)
      
    def loadRulesWindow(edit):
        
      measurement_font=("Arial", 8, "bold")
      number_font=("Arial", 10, "bold")
      w=t.Toplevel()
      w.geometry("390x305")
      w.title("View Rules")
      
      def closeWindow():
          w.destroy()
          
      def saveRules():
        i=0
        try:          
          for x in rule:
            if 0 < float(up_tol[i].get()) < 1: rule[i].setUpperTol(up_tol[i].get())
            else: t.messagebox.showinfo("VALUE ERROR","Bad Value Entered, needs\nNeeds to be 0<value<1"); break
            if 0 < float(low_tol[i].get()) < 1: rule[i].setLowerTol(low_tol[i].get())
            else: t.messagebox.showinfo("VALUE ERROR","Bad Value Entered, needs\nNeeds to be 0<value<1"); break
            rule[i].writeRule("Rules.txt",i)
            i=i+1
        except:
          t.messagebox.showinfo("INPUT ERROR","Bad Value Entered, needs\nNeeds to be NUMBER\nbetween 0<value<1")
      
      if edit==0:
        window_state="readonly"        
      else:
        window_state="normal"
        execBtn = t.Button(w, text="SAVE", height=1,width=10,bd=6,font=("Arial", 12, "bold"))
        execBtn.place(x=235,y=8)
        execBtn.configure(command=lambda: saveRules())      
        
      view1_label= t.Label(w, text ="Tolerance is > .0019”", font=('Times', 12))
      view1_label.place(x=16,y=30,width=140,height=30)
      rule1_frame = t.LabelFrame(w,bd=5)
      rule1_frame.place(x=14,y=60,width=360,height=48)
      up_tol[0]=t.StringVar()
      up_tol[0].set(rule[0].upper_tol)
      rule1_label1 = t.Label(rule1_frame, text="Rule 1 -- ", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
      rule1_entry1=t.Entry(rule1_frame,textvariable=up_tol[0],font=number_font, width = 12,bd=4,state=window_state).grid(row=0,column=1)
      rule1_label2= t.Label(rule1_frame, text ="         ", font=('Times', 8),width=8).grid(row=0,column=2)
      low_tol[0]=t.StringVar()
      low_tol[0].set(rule[0].lower_tol)
      rule1_entry2=t.Entry(rule1_frame,textvariable=low_tol[0],font=number_font, width = 12,bd=4,state=window_state).grid(row=0,column=3)
      
      view2_label= t.Label(w, text ="Tolerance is > .0009” but < .002”", font=('Times', 12))
      view2_label.place(x=16,y=110,width=210,height=30)      
      rule2_frame = t.LabelFrame(w,bd=5)
      rule2_frame.place(x=14,y=140,width=360,height=48)
      rule2_label1 = t.Label(rule2_frame, text="Rule 2 -- ", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
      up_tol[1]=t.StringVar()
      up_tol[1].set(rule[1].upper_tol)
      rule2_entry1=t.Entry(rule2_frame,textvariable=up_tol[1],font=number_font, width = 12,bd=4,state=window_state).grid(row=0,column=1)
      rule2_label2= t.Label(rule2_frame, text ="         ", font=('Times', 8),width=8).grid(row=0,column=2)
      low_tol[1]=t.StringVar()
      low_tol[1].set(rule[1].lower_tol)
      rule2_entry2=t.Entry(rule2_frame,textvariable=low_tol[1],font=number_font, width = 12,bd=4,state=window_state).grid(row=0,column=3)
      
      view3_label= t.Label(w, text ="Tolerance is < .001”", font=('Times', 12))
      view3_label.place(x=16,y=190,width=140,height=30)      
      rule3_frame = t.LabelFrame(w,bd=5)
      rule3_frame.place(x=14,y=220,width=360,height=48)
      rule3_label1 = t.Label(rule3_frame, text="Rule 3 -- ", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
      up_tol[2]=t.StringVar()
      up_tol[2].set(rule[2].upper_tol)
      rule3_entry1=t.Entry(rule3_frame,textvariable=up_tol[2],font=number_font, width = 12,bd=4,state=window_state).grid(row=0,column=1)
      rule3_label2= t.Label(rule3_frame, text ="         ", font=('Times', 8),width=8).grid(row=0,column=2)
      low_tol[2]=t.StringVar()
      low_tol[2].set(rule[2].lower_tol)
      rule3_entry2=t.Entry(rule3_frame,textvariable=low_tol[2],font=number_font, width = 12,bd=4,state=window_state).grid(row=0,column=3)
      
      close_Btn = t.Button(w, text="CLOSE", height=1,width=8,bd=5,font=("Arial", 8, "bold"))
      close_Btn.place(x=14,y=270)
      close_Btn.configure(command=closeWindow)
      
      view7L= t.Label(w, text ="Low End Spec Add", font=('Times', 8))
      view7L.place(x=95,y=268,width=140,height=30) 
      view8L= t.Label(w, text ="High End Spec subtract", font=('Times', 8))
      view8L.place(x=230,y=268,width=140,height=30) 
      
      w.resizable(width=False, height=False)
                   
    # changing the title of our master widget      
    self.master.title("Recipe Value Generator")
    self.master.geometry("900x595")

    # allowing the widget to take the full space of the root window
    self.pack(fill='both', expand=1)

    # creating a menu instance
    recipeMenu = Menu(self.master)
    self.master.config(menu=recipeMenu)

    """********************MENU BUILD************************"""
    # create the filemenu object)
    filemenu = Menu(recipeMenu)
    # adds commands to the menu option, calling it exit, and the
    # and a Load option
    filemenu = Menu(recipeMenu, tearoff=20)
    filemenu.add_command(label="Load", command=loadRecipeWindow)        
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=self.client_exit)

    #added "filemenu" to our menu
    recipeMenu.add_cascade(label="File        ", menu=filemenu)

    # create the Rulesmenu object)
    rulesmenu = Menu(recipeMenu, tearoff=20)        
    rulesmenu.add_command(label="Edit", command=lambda: loadRulesWindow(1))
    rulesmenu.add_separator()
    rulesmenu.add_command(label="View", command=lambda: loadRulesWindow(0))
    recipeMenu.add_cascade(label="Rules        ", menu=rulesmenu) 
        
    #create the t.nhelpmenu object and add choices
    helpmenu = Menu(recipeMenu, tearoff=20)
    helpmenu.add_command(label="Help", command=openHelpFile)
    helpmenu.add_command(label="About", command=aboutDialog)
    recipeMenu.add_cascade(label="Help         ", menu=helpmenu)
    """***********END MENU BUILD****************************"""
    
    """Fonts Used in Entry Boxes and Labels"""
    measurement_font=("Arial", 11, "bold")
    entry_font=("Arial", 18, "bold")
    number_font=("Arial", 10, "bold")
    descFont=("Arial", 8, "bold")

    introframe = t.LabelFrame(root,bd=8)
    introframe.place(x=12,y=12,width=540,height=105)    
    introL = t.Label(introframe, text="Enter the nominal and Specification Limits for each "+
    "Of the Measurements. If a measurement is reference Then leaving the"+
    " specification limits blank is adequate.", fg="black", font=("Arial", 14), width=70,
    wraplength=520, anchor=t.NW,bd=10)
    introL.place(x=0,y=0,width=520,height=80)
    
    recipe_frame = t.LabelFrame(root,bd=6)
    recipe_frame.place(x=115,y=120,width=320,height=56)    
    recipeL = t.Label(recipe_frame, text="Recipe Name -- ", fg="black", font=("Arial", 14 ), width=70,
    anchor=t.NW,bd=10)
    recipeL.place(x=0,y=0,width=280,height=40)
    recipeString = t.StringVar()
    recipeE=t.Entry(recipe_frame,textvariable=recipeString,font=entry_font)
    recipeE.place(x=150,y=0,width=150,height=40)
    
    descframe = t.LabelFrame(root,bd=1)
    descframe.place(x=40,y=185,width=510,height=20)
    descL1 = t.Label(descframe, text="Measurement", fg="black", font=descFont, width=18,
    anchor=t.NW,bd=1).grid(row=0,column=0)
    descL2 = t.Label(descframe, text="    Nominal", fg="black", font=descFont, width=16,
    anchor=t.NW,bd=1).grid(row=0,column=1)
    descL3 = t.Label(descframe, text=" Upper Spec", fg="black", font=descFont, width=17,
    anchor=t.NW,bd=1).grid(row=0,column=2)
    descL4 = t.Label(descframe, text="Lower Spec", fg="black", font=descFont, width=15,
    anchor=t.NW,bd=1).grid(row=0,column=3)
    descL5 = t.Label(descframe, text="REF", fg="black", font=descFont, width=6,
    anchor=t.NW,bd=1).grid(row=0,column=4)
    
    od_frame = t.LabelFrame(root,bd=5)
    od_frame.place(x=14,y=215,width=490,height=52)
    od_label=t.Label(od_frame, text="OD          ", fg="black", font=measurement_font, width=12,
    anchor=t.NW,bd=10).grid(row=0)
    od_nom_var = t.StringVar()
    od_entry_nom=t.Entry(od_frame,textvariable=od_nom_var,font=entry_font, width = 8,bd=5).grid(row=0,column=1)
    od_up_var = t.StringVar()
    od_entry_up=t.Entry(od_frame,textvariable=od_up_var,font=entry_font, width = 8,bd=5).grid(row=0,column=2)
    od_low_var = t.StringVar()
    od_entry_low=t.Entry(od_frame,textvariable=od_low_var,font=entry_font, width = 8,bd=5).grid(row=0,column=3)
    od_ref_var = t.IntVar()
    od_check = t.Checkbutton(root, variable=od_ref_var, font=measurement_font, height=1,width=1)
    od_check.place(x=515,y=225)
    
    id_frame = t.LabelFrame(root,bd=5)
    id_frame.place(x=14,y=280,width=490,height=52)
    id_label=t.Label(id_frame, text="ID          ", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
    id_nom_var = t.StringVar()
    id_entry_nom=t.Entry(id_frame,textvariable=id_nom_var,font=entry_font, width = 8,bd=5).grid(row=0,column=1)
    id_up_var = t.StringVar()
    id_entry_up=t.Entry(id_frame,textvariable=id_up_var,font=entry_font, width = 8,bd=5).grid(row=0,column=2)
    id_low_var = t.StringVar()
    id_entry_low=t.Entry(id_frame,textvariable=id_low_var,font=entry_font, width = 8,bd=5).grid(row=0,column=3)
    id_ref_var = t.IntVar()
    id_check = t.Checkbutton(root, variable=id_ref_var, font=measurement_font, height=1,width=1)
    id_check.place(x=515,y=290)
    
    wall_frame = t.LabelFrame(root,bd=5)
    wall_frame.place(x=14,y=345,width=490,height=52)
    wall_label = t.Label(wall_frame, text="WALL        ", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
    wall_nom_var = t.StringVar()
    wall_entry_nom=t.Entry(wall_frame,textvariable=wall_nom_var,font=entry_font, width = 8,bd=5).grid(row=0,column=1)
    wall_up_var = t.StringVar()
    wall_entry_up=t.Entry(wall_frame,textvariable=wall_up_var,font=entry_font, width = 8,bd=5).grid(row=0,column=2)
    wall_low_var = t.StringVar()
    wall_entry_low=t.Entry(wall_frame,textvariable=wall_low_var,font=entry_font, width = 8,bd=5).grid(row=0,column=3)
    wall_var = t.IntVar()
    wall_check = t.Checkbutton(root, variable=wall_var, font=measurement_font, height=1,width=1)
    wall_check.place(x=515,y=355)
    
    conc_frame = t.LabelFrame(root,bd=5)
    conc_frame.place(x=14,y=410,width=490,height=52)
    conc_label = t.Label(conc_frame, text="Concentricity", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
    conc_nom_var=t.StringVar()
    conc_entry_nom=t.Entry(conc_frame,textvariable=conc_nom_var,font=entry_font, width = 8,bd=5).grid(row=0,column=1)
    none_label=t.Label(conc_frame, text="   None  ", fg="black", font=measurement_font, width=11,bd=8).grid(row=0,column=2)
    conc_low_var=t.StringVar()
    conc_entry_low=t.Entry(conc_frame,textvariable=conc_low_var,font=entry_font, width = 8,bd=5).grid(row=0,column=3)
    conc_var = t.IntVar()
    conc_check = t.Checkbutton(root, variable=conc_var, font=measurement_font, height=1,width=1)
    conc_check.place(x=515,y=420)
    
    ovality_frame = t.LabelFrame(root,bd=5)
    ovality_frame.place(x=14,y=475,width=490,height=52)
    ovality_label = t.Label(ovality_frame, text="Ovality     ", fg="black", font=measurement_font, width=12,anchor=t.NW,bd=10).grid(row=0)
    ovality_nom_var=t.StringVar()
    ovality_entry_nom=t.Entry(ovality_frame,textvariable=ovality_nom_var,font=entry_font, width = 8,bd=5).grid(row=0,column=1)
    ovality_up_var=t.StringVar()
    ovality_entry_up=t.Entry(ovality_frame,textvariable=ovality_up_var,font=entry_font, width = 8,bd=5).grid(row=0,column=2)
    none_label=t.Label(ovality_frame, text="  None", fg="black", font=measurement_font, width=11,bd=8).grid(row=0,column=3)
    ovality_var = t.IntVar()
    ovality_check = t.Checkbutton(root, variable=ovality_var, font=measurement_font, height=1,width=1)
    ovality_check.place(x=515,y=485)

    file = Image.open("tubes.gif")
    gif1 = ImageTk.PhotoImage(file)
    root.gif1=gif1
    # Added a canvas for now, not sure if it will be necessary
    ImageCanvas = t.Canvas(self, bg="gray", width=320, height=510,
                             bd=0, offset = "e", highlightthickness=20)
    ImageCanvas.pack(side="right")
    ImageCanvas.create_image(180, 275, anchor = t.CENTER, image = gif1)
    
    execBtn = t.Button(root, text="EXECUTE", height=1,width=20,bd=6,font=("Arial", 14, "bold"))
    execBtn.place(x=150,y=535)   

  # 'self closing function for the filemenu
  def client_exit(self):
        exit()
        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = t.Tk()
root.resizable(width=False, height=False)
#creation of an instance
app = RecipeWindow(root)

#mainloop 
root.mainloop() 