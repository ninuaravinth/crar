from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageDraw, ImageFilter
from PIL import Image, ImageDraw
import os.path
import base64
import sys
import cv2
import numpy as np
import mapper
import sys
from base64 import decodestring

import argparse


import math
from objloader_simple import *

import os

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   


def open_file():
   import os
   filepath = askopenfilename(
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
      )
   
   
   window.title(f"CRAR - {filepath}")
   with open(filepath, 'rb') as binary_file:
      binary_file_data = binary_file.read()
      base64_encoded_data = base64.b64encode(binary_file_data)
      base64_message = base64_encoded_data.decode('utf-8')
   a= ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

   filename = os.path.splitext(filepath)
   extension = os.path.splitext(str(filename))[1]
   
   ion="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
   C=str(base64_message)+str(extension)+ion
   print(len(a))
   print(C)
   for i in range (0,243):
      if(C[i]=="A"):
         a[i]="rgb(255,0,0)"
      elif(C[i]=="B"):
         a[i]="rgb(0,255,0)"
      elif(C[i]=="C"):
        a[i]="rgb(0,0,255)"
      elif(C[i]=="D"):
         a[i]="rgb(255,255,0)"
      elif(C[i]=="E"):
         a[i]="rgb(0,255,255)"
      elif(C[i]=="F"):
         a[i]="rgb(255,0,255)"
      elif(C[i]=="G"):
         a[i]="rgb(192,192,192)"
      elif(C[i]=="H"):
         a[i]="rgb(128,128,128)"
      elif(C[i]=="I"):
         a[i]="rgb(128,0,0)"
      elif(C[i]=="J"):
         a[i]="rgb(128,128,0)"
      elif(C[i]=="K"):
         a[i]="rgb(0,128,0)"
      elif(C[i]=="L"):
         a[i]="rgb(128,0,128)"
      elif(C[i]=="M"):
         a[i]="rgb(0,128,128)"
      elif(C[i]=="N"):
         a[i]="rgb(0,0,128)"
      elif(C[i]=="O"):
         a[i]="rgb(255,140,0)" #'''darkorange'''
      elif(C[i]=="P"):
         a[i]="rgb(255,215,0)" #'''gold'''
      elif(C[i]=="Q"):
         a[i]="rgb(85,107,47)" #'''dark olive green'''
      elif(C[i]=="R"):
         a[i]="rgb(173,255,47)" #'''green yellow'''
      elif(C[i]=="S"):
         a[i]="rgb(50,205,50)" #''' lime green'''
      elif(C[i]=="T"):
         a[i]="rgb(0,250,154)" #'''medium spring green'''
      elif(C[i]=="U"):
         a[i]="rgb(47,79,79)" #'''dark slate gray'''
      elif(C[i]=="V"):
         a[i]="rgb(0,206,209)" #'''dark turquoise'''
      elif(C[i]=="W"):
         a[i]="rgb(100,149,237)" #'''corn flower blue'''
      elif(C[i]=="X"):
         a[i]="rgb(0,191,255)" #'''dep sky blue'''
      elif(C[i]=="Y"):
         a[i]="rgb(127,255,212)" #''' aqua marine'''
      elif(C[i]=="Z"):
         a[i]="rgb(0,0,205)" #''' medium blue'''
      elif(C[i]=="a"):
         a[i]="rgb(138,43,226)" #''' blue violet'''
      elif(C[i]=="b"):
         a[i]="rgb(123,104,238)" # ''' medium slate blue'''
      elif(C[i]=="c"):
         a[i]="rgb(148,0,211)"  #'''dark violet'''
      elif(C[i]=="d"):
         a[i]="rgb(139,0,139)"  #''' dark mafneta'''
      elif(C[i]=="e"):
         a[i]="rgb(75,0,130)"  #''' indigo'''
      elif(C[i]=="f"):
         a[i]="rgb(128,0,128)" #''' purple'''
      elif(C[i]=="g"):
         a[i]="rgb(238,130,238)"  #'''violet'''
      elif(C[i]=="h"):
         a[i]="rgb(199,21,133)"  #''' medium violet red'''
      elif(C[i]=="i"):
         a[i]="rgb(250,235,215)"  #''' antique white'''
      elif(C[i]=="j"):
         a[i]="rgb(139,69,19)"   #''' saddle brown'''
      elif(C[i]=="k"):
         a[i]="rgb(210,105,30)" #''' cholate '''
      elif(C[i]=="l"):
         a[i]="rgb(244,164,96)"  #''' sandy brown '''
      elif(C[i]=="m"):
         a[i]="rgb(188,143,143)"  #''' rosy brown'''
      elif(C[i]=="n"):
         a[i]="rgb(176,196,222)"  #''' light steel vlue'''
      elif(C[i]=="o"):
         a[i]="rgb(240,255,240)"  #'''honey dew'''
      elif(C[i]=="p"):
         a[i]="rgb(189,183,107)"  #''' dark khaki'''
      elif(C[i]=="q"):
         a[i]="rgb(34,139,34)"  #''' forest green'''
      elif(C[i]=="r"):
         a[i]="rgb(60,179,113)"  #'' 'medium sea green'''
      elif(C[i]=="s"):
         a[i]="rgb(255,127,80)"  #''' coral'''
      elif(C[i]=="t"):
         a[i]="rgb(255,99,71)"  #''' tomato'''
      elif(C[i]=="u"):
         a[i]="rgb(240,128,128)"  #''' light coral'''
      elif(C[i]=="v"):
         a[i]="rgb(255,160,122)"  #''' light salmon'''
      elif(C[i]=="w"):
         a[i]="rgb(70,130,180)"  #''' steel blue'''
      elif(C[i]=="x"):
         a[i]="rgb(176,224,230)"  #''' powder blue'''
      elif(C[i]=="y"):
         a[i]="rgb(30,144,255)"  #''' doger blue'''
      elif(C[i]=="z"):
         a[i]="rgb(230,230,250)"  #''' lavender'''
      elif(C[i]=="0"):
         a[i]="rgb(255,250,205)" #'''lemon chiffon'''
      elif(C[i]=="1"):
         a[i]="rgb(233,150,122)"  #''' dark salmon '''
      elif(C[i]=="2"):
         a[i]="rgb(255,105,180)" # ''' hot pink'''
      elif(C[i]=="3"):
         a[i]="rgb(205,133,63)"  #''' rosy brown'''
      elif(C[i]=="4"):
         a[i]="rgb(222,184,135)"  #''' burly wood'''
      elif(C[i]=="5"):
         a[i]="rgb(255,228,181)"  #''' mocassin'''
      elif(C[i]=="6"):
         a[i]="rgb(46,139,87)"  #''' sea green'''
      elif(C[i]=="7"):
         a[i]="rgb(60,179,113)"  #''' medium sea green'''
      elif(C[i]=="8"):
         a[i]="rgb(107,142,35)"  #''' dark olive drab'''
      elif(C[i]=="9"):
         a[i]="rgb(205,92,92)"   #''' indian red'''
      elif(C[i]=="+"):
         a[i]="rgb(147,112,219)" #''' medium purple'''
      elif(C[i]=="/"):
         a[i]="rgb(245,222,179)"  #''' wheat'''
      elif(C[i]=="="):
         a[i]="rgb(220,220,220)"  #''' honeydew'''
      elif(C[i]=="."):
         a[i]="rgb(255,250,250)"
      else:
         a[i]="rgb(0,0,0)"
   print(a[4])
   print(a[16])
   im = Image.new('RGB', (160,160), (128, 128, 128))
   draw = ImageDraw.Draw(im)
   draw.rectangle((0, 10, 160, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 160, 10), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 30, 160, 20), fill=a[1], outline=(0, 0, 0))
   draw.rectangle((0, 40, 160, 30), fill=a[2], outline=(0, 0, 0))
   draw.rectangle((0, 50, 160, 40), fill=a[3], outline=(0, 0, 0))
   draw.rectangle((0, 60, 160, 50), fill=a[4], outline=(0, 0, 0))
   draw.rectangle((0, 70, 160, 60), fill=a[0], outline=(0, 0, 0))
   draw.rectangle((0, 80, 160, 70), fill=a[184], outline=(0, 0, 0))
   draw.rectangle((0, 90, 160, 80), fill=a[185], outline=(0, 0, 0))
   draw.rectangle((0, 100, 160, 90), fill=a[186], outline=(0, 0, 0))
   draw.rectangle((0, 110, 160, 100), fill=a[5], outline=(0, 0, 0))
   draw.rectangle((0, 120, 160, 110), fill=a[6], outline=(0, 0, 0))
   draw.rectangle((0, 130, 160, 120), fill=a[7], outline=(0, 0, 0))
   draw.rectangle((0, 140, 160, 130), fill=a[8], outline=(0, 0, 0))
   draw.rectangle((0, 150, 160, 140), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 160, 160, 150), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 10, 150, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 150, 10), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 30, 150, 20), fill=a[9], outline=(0, 0, 0))
   draw.rectangle((0, 40, 150, 30), fill=a[10], outline=(0, 0, 0))
   draw.rectangle((0, 50, 150, 40), fill=a[11], outline=(0, 0, 0))
   draw.rectangle((0, 60, 150, 50), fill=a[12], outline=(0, 0, 0))
   draw.rectangle((0, 70, 150, 60), fill=a[187], outline=(0, 0, 0))
   draw.rectangle((0, 80, 150, 70), fill=a[13], outline=(0, 0, 0))
   draw.rectangle((0, 90, 150, 80), fill=a[14], outline=(0, 0, 0))
   draw.rectangle((0, 100, 150, 90), fill=a[188], outline=(0, 0, 0))
   draw.rectangle((0, 110, 150, 100), fill=a[15], outline=(0, 0, 0))
   draw.rectangle((0, 120, 150, 110), fill=a[16], outline=(0, 0, 0))
   draw.rectangle((0, 130, 150, 120), fill=a[17], outline=(0, 0, 0))
   draw.rectangle((0, 140, 150, 130), fill=a[18], outline=(0, 0, 0))
   draw.rectangle((0, 150, 150, 140), fill=a[19], outline=(0, 0, 0))
   draw.rectangle((0, 160, 150, 150), fill=(0, 0, 0), outline=(0, 0, 0))

   draw.rectangle((0, 10, 140, 0), fill=a[20], outline=(0, 0, 0))
   draw.rectangle((0, 20, 140, 10), fill=a[21], outline=(0, 0, 0))
   draw.rectangle((0, 30, 140, 20), fill=a[22], outline=(0, 0, 0))
   draw.rectangle((0, 40, 140, 30), fill=a[23], outline=(0, 0, 0))
   draw.rectangle((0, 50, 140, 40), fill=a[189], outline=(0, 0, 0))
   draw.rectangle((0, 60, 140, 50), fill=a[190], outline=(0, 0, 0))
   draw.rectangle((0, 70, 140, 60), fill=a[191], outline=(0, 0, 0))
   draw.rectangle((0, 80, 140, 70), fill=a[24], outline=(0, 0, 0))
   draw.rectangle((0, 90, 140, 80), fill=a[25], outline=(0, 0, 0))
   draw.rectangle((0, 100, 140, 90), fill=a[192], outline=(0, 0, 0))
   draw.rectangle((0, 110, 140, 100), fill=a[193], outline=(0, 0, 0))
   draw.rectangle((0, 120, 140, 110), fill=a[194], outline=(0, 0, 0))
   draw.rectangle((0, 130, 140, 120), fill=a[26], outline=(0, 0, 0))
   draw.rectangle((0, 140, 140, 130), fill=a[27], outline=(0, 0, 0))
   draw.rectangle((0, 150, 140, 140), fill=a[28], outline=(0, 0, 0))
   draw.rectangle((0, 160, 140, 150), fill=a[29], outline=(0, 0, 0))

   draw.rectangle((0, 10, 130, 0), fill=a[30], outline=(0, 0, 0))
   draw.rectangle((0, 20, 130, 10), fill=a[31], outline=(0, 0, 0))
   draw.rectangle((0, 30, 130, 20), fill=a[32], outline=(0, 0, 0))
   draw.rectangle((0, 40, 130, 30), fill=a[33], outline=(0, 0, 0))
   draw.rectangle((0, 50, 130, 40), fill=a[195], outline=(0, 0, 0))
   draw.rectangle((0, 60, 130, 50), fill=a[34], outline=(0, 0, 0))
   draw.rectangle((0, 70, 130, 60), fill=a[35], outline=(0, 0, 0))
   draw.rectangle((0, 80, 130, 70), fill=a[36], outline=(0, 0, 0))
   draw.rectangle((0, 90, 130, 80), fill=a[37], outline=(0, 0, 0))
   draw.rectangle((0, 100, 130, 90), fill=a[38], outline=(0, 0, 0))
   draw.rectangle((0, 110, 130, 100), fill=a[39], outline=(0, 0, 0))
   draw.rectangle((0, 120, 130, 110), fill=a[196], outline=(0, 0, 0))
   draw.rectangle((0, 130, 130, 120), fill=a[40], outline=(0, 0, 0))
   draw.rectangle((0, 140, 130, 130), fill=a[41], outline=(0, 0, 0))
   draw.rectangle((0, 150, 130, 140), fill=a[42], outline=(0, 0, 0))
   draw.rectangle((0, 160, 130, 150), fill=a[43], outline=(0, 0, 0))

   draw.rectangle((0, 10, 120, 0), fill=a[44], outline=(0, 0, 0))
   draw.rectangle((0, 20, 120, 10), fill=a[45], outline=(0, 0, 0))
   draw.rectangle((0, 30, 120, 20), fill=a[197], outline=(0, 0, 0))
   draw.rectangle((0, 40, 120, 30), fill=a[198], outline=(0, 0, 0))
   draw.rectangle((0, 50, 120, 40), fill=a[199], outline=(0, 0, 0))
   draw.rectangle((0, 60, 120, 50), fill=a[46], outline=(0, 0, 0))
   draw.rectangle((0, 70, 120, 60), fill=a[47], outline=(0, 0, 0))
   draw.rectangle((0, 80, 120, 70), fill=a[48], outline=(0, 0, 0))
   draw.rectangle((0, 90, 120, 80), fill=a[49], outline=(0, 0, 0))
   draw.rectangle((0, 100, 120, 90), fill=a[50], outline=(0, 0, 0))
   draw.rectangle((0, 110, 120, 100), fill=a[51], outline=(0, 0, 0))
   draw.rectangle((0, 120, 120, 110), fill=a[200], outline=(0, 0, 0))
   draw.rectangle((0, 130, 120, 120), fill=a[201], outline=(0, 0, 0))
   draw.rectangle((0, 140, 120, 130), fill=a[202], outline=(0, 0, 0))
   draw.rectangle((0, 150, 120, 140), fill=a[52], outline=(0, 0, 0))
   draw.rectangle((0, 160, 120, 150), fill=a[53], outline=(0, 0, 0))

   draw.rectangle((0, 10, 110, 0), fill=a[54], outline=(0, 0, 0))
   draw.rectangle((0, 20, 110, 10), fill=a[55], outline=(0, 0, 0))
   draw.rectangle((0, 30, 110, 20), fill=a[203], outline=(0, 0, 0))
   draw.rectangle((0, 40, 110, 30), fill=a[56], outline=(0, 0, 0))
   draw.rectangle((0, 50, 110, 40), fill=a[57], outline=(0, 0, 0))
   draw.rectangle((0, 60, 110, 50), fill=a[58], outline=(0, 0, 0))
   draw.rectangle((0, 70, 110, 60), fill=a[59], outline=(0, 0, 0))
   draw.rectangle((0, 80, 110, 70), fill=a[60], outline=(0, 0, 0))
   draw.rectangle((0, 90, 110, 80), fill=a[61], outline=(0, 0, 0))
   draw.rectangle((0, 100, 110, 90), fill=a[62], outline=(0, 0, 0))
   draw.rectangle((0, 110, 110, 100), fill=a[63], outline=(0, 0, 0))
   draw.rectangle((0, 120, 110, 110), fill=a[64], outline=(0, 0, 0))
   draw.rectangle((0, 130, 110, 120), fill=a[65], outline=(0, 0, 0))
   draw.rectangle((0, 140, 110, 130), fill=a[204], outline=(0, 0, 0))
   draw.rectangle((0, 150, 110, 140), fill=a[66], outline=(0, 0, 0))
   draw.rectangle((0, 160, 110, 150), fill=a[67], outline=(0, 0, 0))

   draw.rectangle((0, 10, 100, 0), fill=a[205], outline=(0, 0, 0))
   draw.rectangle((0, 20, 100, 10), fill=a[206], outline=(0, 0, 0))
   draw.rectangle((0, 30, 100, 20), fill=a[207], outline=(0, 0, 0))
   draw.rectangle((0, 40, 100, 30), fill=a[68], outline=(0, 0, 0))
   draw.rectangle((0, 50, 100, 40), fill=a[69], outline=(0, 0, 0))
   draw.rectangle((0, 60, 100, 50), fill=a[70], outline=(0, 0, 0))
   draw.rectangle((0, 70, 100, 60), fill=a[71], outline=(0, 0, 0))
   draw.rectangle((0, 80, 100, 70), fill=a[72], outline=(0, 0, 0))
   draw.rectangle((0, 90, 100, 80), fill=a[73], outline=(0, 0, 0))
   draw.rectangle((0, 100, 100, 90), fill=a[74], outline=(0, 0, 0))
   draw.rectangle((0, 110, 100, 100), fill=a[75], outline=(0, 0, 0))
   draw.rectangle((0, 120, 100, 110), fill=a[76], outline=(0, 0, 0))
   draw.rectangle((0, 130, 100, 120), fill=a[77], outline=(0, 0, 0))
   draw.rectangle((0, 140, 100, 130), fill=a[208], outline=(0, 0, 0))
   draw.rectangle((0, 150, 100, 140), fill=a[209], outline=(0, 0, 0))
   draw.rectangle((0, 160, 100, 150), fill=a[210], outline=(0, 0, 0))

   draw.rectangle((0, 10, 90, 0), fill=a[211], outline=(0, 0, 0))
   draw.rectangle((0, 20, 90, 10), fill=a[78], outline=(0, 0, 0))
   draw.rectangle((0, 30, 90, 20), fill=a[79], outline=(0, 0, 0))
   draw.rectangle((0, 40, 90, 30), fill=a[80], outline=(0, 0, 0))
   draw.rectangle((0, 50, 90, 40), fill=a[81], outline=(0, 0, 0))
   draw.rectangle((0, 60, 90, 50), fill=a[82], outline=(0, 0, 0))
   draw.rectangle((0, 70, 90, 60), fill=a[83], outline=(0, 0, 0))
   draw.rectangle((0, 80, 90, 70), fill=a[84], outline=(0, 0, 0))
   draw.rectangle((0, 90, 90, 80), fill=a[85], outline=(0, 0, 0))
   draw.rectangle((0, 100, 90, 90), fill=a[86], outline=(0, 0, 0))
   draw.rectangle((0, 110, 90, 100), fill=a[87], outline=(0, 0, 0))
   draw.rectangle((0, 120, 90, 110), fill=a[88], outline=(0, 0, 0))
   draw.rectangle((0, 130, 90, 120), fill=a[89], outline=(0, 0, 0))
   draw.rectangle((0, 140, 90, 130), fill=a[90], outline=(0, 0, 0))
   draw.rectangle((0, 150, 90, 140), fill=a[91], outline=(0, 0, 0))
   draw.rectangle((0, 160, 90, 150), fill=a[212], outline=(0, 0, 0))

   draw.rectangle((0, 10, 80, 0), fill=a[213], outline=(0, 0, 0))
   draw.rectangle((0, 20, 80, 10), fill=a[92], outline=(0, 0, 0))
   draw.rectangle((0, 30, 80, 20), fill=a[93], outline=(0, 0, 0))
   draw.rectangle((0, 40, 80, 30), fill=a[94], outline=(0, 0, 0))
   draw.rectangle((0, 50, 80, 40), fill=a[95], outline=(0, 0, 0))
   draw.rectangle((0, 60, 80, 50), fill=a[96], outline=(0, 0, 0))
   draw.rectangle((0, 70, 80, 60), fill=a[97], outline=(0, 0, 0))
   draw.rectangle((0, 80, 80, 70), fill=a[98], outline=(0, 0, 0))
   draw.rectangle((0, 90, 80, 80), fill=a[99], outline=(0, 0, 0))
   draw.rectangle((0, 100, 80, 90), fill=a[100], outline=(0, 0, 0))
   draw.rectangle((0, 110, 80, 100), fill=a[101], outline=(0, 0, 0))
   draw.rectangle((0, 120, 80, 110), fill=a[102], outline=(0, 0, 0))
   draw.rectangle((0, 130, 80, 120), fill=a[103], outline=(0, 0, 0))
   draw.rectangle((0, 140, 80, 130), fill=a[104], outline=(0, 0, 0))
   draw.rectangle((0, 150, 80, 140), fill=a[105], outline=(0, 0, 0))
   draw.rectangle((0, 160, 80, 150), fill=a[214], outline=(0, 0, 0))

   draw.rectangle((0, 10, 70, 0), fill=a[215], outline=(0, 0, 0))
   draw.rectangle((0, 20, 70, 10), fill=a[216], outline=(0, 0, 0))
   draw.rectangle((0, 30, 70, 20), fill=a[217], outline=(0, 0, 0))
   draw.rectangle((0, 40, 70, 30), fill=a[106], outline=(0, 0, 0))
   draw.rectangle((0, 50, 70, 40), fill=a[107], outline=(0, 0, 0))
   draw.rectangle((0, 60, 70, 50), fill=a[108], outline=(0, 0, 0))
   draw.rectangle((0, 70, 70, 60), fill=a[109], outline=(0, 0, 0))
   draw.rectangle((0, 80, 70, 70), fill=a[110], outline=(0, 0, 0))
   draw.rectangle((0, 90, 70, 80), fill=a[111], outline=(0, 0, 0))
   draw.rectangle((0, 100, 70, 90), fill=a[112], outline=(0, 0, 0))
   draw.rectangle((0, 110, 70, 100), fill=a[113], outline=(0, 0, 0))
   draw.rectangle((0, 120, 70, 110), fill=a[114], outline=(0, 0, 0))
   draw.rectangle((0, 130, 70, 120), fill=a[115], outline=(0, 0, 0))
   draw.rectangle((0, 140, 70, 130), fill=a[218], outline=(0, 0, 0))
   draw.rectangle((0, 150, 70, 140), fill=a[219], outline=(0, 0, 0))
   draw.rectangle((0, 160, 70, 150), fill=a[220], outline=(0, 0, 0))

   draw.rectangle((0, 10, 60, 0), fill=a[116], outline=(0, 0, 0))
   draw.rectangle((0, 20, 60, 10), fill=a[117], outline=(0, 0, 0))
   draw.rectangle((0, 30, 60, 20), fill=a[221], outline=(0, 0, 0))
   draw.rectangle((0, 40, 60, 30), fill=a[118], outline=(0, 0, 0))
   draw.rectangle((0, 50, 60, 40), fill=a[119], outline=(0, 0, 0))
   draw.rectangle((0, 60, 60, 50), fill=a[120], outline=(0, 0, 0))
   draw.rectangle((0, 70, 60, 60), fill=a[121], outline=(0, 0, 0))
   draw.rectangle((0, 80, 60, 70), fill=a[122], outline=(0, 0, 0))
   draw.rectangle((0, 90, 60, 80), fill=a[123], outline=(0, 0, 0))
   draw.rectangle((0, 100, 60, 90), fill=a[124], outline=(0, 0, 0))
   draw.rectangle((0, 110, 60, 100), fill=a[125], outline=(0, 0, 0))
   draw.rectangle((0, 120, 60, 110), fill=a[126], outline=(0, 0, 0))
   draw.rectangle((0, 130, 60, 120), fill=a[127], outline=(0, 0, 0))
   draw.rectangle((0, 140, 60, 130), fill=a[222], outline=(0, 0, 0))
   draw.rectangle((0, 150, 60, 140), fill=a[128], outline=(0, 0, 0))
   draw.rectangle((0, 160, 60, 150), fill=a[129], outline=(0, 0, 0))

   draw.rectangle((0, 10, 50, 0), fill=a[130], outline=(0, 0, 0))
   draw.rectangle((0, 20, 50, 10), fill=a[131], outline=(0, 0, 0))
   draw.rectangle((0, 30, 50, 20), fill=a[223], outline=(0, 0, 0))
   draw.rectangle((0, 40, 50, 30), fill=a[224], outline=(0, 0, 0))
   draw.rectangle((0, 50, 50, 40), fill=a[225], outline=(0, 0, 0))
   draw.rectangle((0, 60, 50, 50), fill=a[132], outline=(0, 0, 0))
   draw.rectangle((0, 70, 50, 60), fill=a[133], outline=(0, 0, 0))
   draw.rectangle((0, 80, 50, 70), fill=a[134], outline=(0, 0, 0))
   draw.rectangle((0, 90, 50, 80), fill=a[135], outline=(0, 0, 0))
   draw.rectangle((0, 100, 50, 90), fill=a[136], outline=(0, 0, 0))
   draw.rectangle((0, 110, 50, 100), fill=a[137], outline=(0, 0, 0))
   draw.rectangle((0, 120, 50, 110), fill=a[226], outline=(0, 0, 0))
   draw.rectangle((0, 130, 50, 120), fill=a[227], outline=(0, 0, 0))
   draw.rectangle((0, 140, 50, 130), fill=a[228], outline=(0, 0, 0))
   draw.rectangle((0, 150, 50, 140), fill=a[138], outline=(0, 0, 0))
   draw.rectangle((0, 160, 50, 150), fill=a[139], outline=(0, 0, 0))

   draw.rectangle((0, 10, 40, 0), fill=a[140], outline=(0, 0, 0))
   draw.rectangle((0, 20, 40, 10), fill=a[141], outline=(0, 0, 0))
   draw.rectangle((0, 30, 40, 20), fill=a[142], outline=(0, 0, 0))
   draw.rectangle((0, 40, 40, 30), fill=a[143], outline=(0, 0, 0))
   draw.rectangle((0, 50, 40, 40), fill=a[229], outline=(0, 0, 0))
   draw.rectangle((0, 60, 40, 50), fill=a[144], outline=(0, 0, 0))
   draw.rectangle((0, 70, 40, 60), fill=a[145], outline=(0, 0, 0))
   draw.rectangle((0, 80, 40, 70), fill=a[146], outline=(0, 0, 0))
   draw.rectangle((0, 90, 40, 80), fill=a[147], outline=(0, 0, 0))
   draw.rectangle((0, 100, 40, 90), fill=a[148], outline=(0, 0, 0))
   draw.rectangle((0, 110, 40, 100), fill=a[149], outline=(0, 0, 0))
   draw.rectangle((0, 120, 40, 110), fill=a[230], outline=(0, 0, 0))
   draw.rectangle((0, 130, 40, 120), fill=a[150], outline=(0, 0, 0))
   draw.rectangle((0, 140, 40, 130), fill=a[151], outline=(0, 0, 0))
   draw.rectangle((0, 150, 40, 140), fill=a[152], outline=(0, 0, 0))
   draw.rectangle((0, 160, 40, 150), fill=a[153], outline=(0, 0, 0))

   draw.rectangle((0, 10, 30, 0), fill=a[154], outline=(0, 0, 0))
   draw.rectangle((0, 20, 30, 10), fill=a[155], outline=(0, 0, 0))
   draw.rectangle((0, 30, 30, 20), fill=a[156], outline=(0, 0, 0))
   draw.rectangle((0, 40, 30, 30), fill=a[157], outline=(0, 0, 0))
   draw.rectangle((0, 50, 30, 40), fill=a[231], outline=(0, 0, 0))
   draw.rectangle((0, 60, 30, 50), fill=a[232], outline=(0, 0, 0))
   draw.rectangle((0, 70, 30, 60), fill=a[233], outline=(0, 0, 0))
   draw.rectangle((0, 80, 30, 70), fill=a[158], outline=(0, 0, 0))
   draw.rectangle((0, 90, 30, 80), fill=a[159], outline=(0, 0, 0))
   draw.rectangle((0, 100, 30, 90), fill=a[234], outline=(0, 0, 0))
   draw.rectangle((0, 110, 30, 100), fill=a[235], outline=(0, 0, 0))
   draw.rectangle((0, 120, 30, 110), fill=a[236], outline=(0, 0, 0))
   draw.rectangle((0, 130, 30, 120), fill=a[160], outline=(0, 0, 0))
   draw.rectangle((0, 140, 30, 130), fill=a[161], outline=(0, 0, 0))
   draw.rectangle((0, 150, 30, 140), fill=a[162], outline=(0, 0, 0))
   draw.rectangle((0, 160, 30, 150), fill=a[163], outline=(0, 0, 0))

   draw.rectangle((0, 10, 20, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 20, 10), fill=a[164], outline=(0, 0, 0))
   draw.rectangle((0, 30, 20, 20), fill=a[165], outline=(0, 0, 0))
   draw.rectangle((0, 40, 20, 30), fill=a[166], outline=(0, 0, 0))
   draw.rectangle((0, 50, 20, 40), fill=a[167], outline=(0, 0, 0))
   draw.rectangle((0, 60, 20, 50), fill=a[168], outline=(0, 0, 0))
   draw.rectangle((0, 70, 20, 60), fill=a[237], outline=(0, 0, 0))
   draw.rectangle((0, 80, 20, 70), fill=a[169], outline=(0, 0, 0))
   draw.rectangle((0, 90, 20, 80), fill=a[170], outline=(0, 0, 0))
   draw.rectangle((0, 100, 20, 90), fill=a[238], outline=(0, 0, 0))
   draw.rectangle((0, 110, 20, 100), fill=a[171], outline=(0, 0, 0))
   draw.rectangle((0, 120, 20, 110), fill=a[172], outline=(0, 0, 0))
   draw.rectangle((0, 130, 20, 120), fill=a[173], outline=(0, 0, 0))
   draw.rectangle((0, 140, 20, 130), fill=a[174], outline=(0, 0, 0))
   draw.rectangle((0, 150, 20, 140), fill=a[175], outline=(0, 0, 0))
   draw.rectangle((0, 160, 20, 150), fill=(0, 0, 0), outline=(0, 0, 0))

   draw.rectangle((0, 10, 10, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 10, 10), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 30, 10, 20), fill=a[176], outline=(0, 0, 0))
   draw.rectangle((0, 40, 10, 30), fill=a[177], outline=(0, 0, 0))
   draw.rectangle((0, 50, 10, 40), fill=a[178], outline=(0, 0, 0))
   draw.rectangle((0, 60, 10, 50), fill=a[179], outline=(0, 0, 0))
   draw.rectangle((0, 70, 10, 60), fill=a[239], outline=(0, 0, 0))
   draw.rectangle((0, 80, 10, 70), fill=a[240], outline=(0, 0, 0))
   draw.rectangle((0, 90, 10, 80), fill=a[241], outline=(0, 0, 0))
   draw.rectangle((0, 100, 10, 90), fill=a[242], outline=(0, 0, 0))
   draw.rectangle((0, 110, 10, 100), fill=a[180], outline=(0, 0, 0))
   draw.rectangle((0, 120, 10, 110), fill=a[181], outline=(0, 0, 0))
   draw.rectangle((0, 130, 10, 120), fill=a[182], outline=(0, 0, 0))
   draw.rectangle((0, 140, 10, 130), fill=a[183], outline=(0, 0, 0))
   draw.rectangle((0, 150, 10, 140), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 160, 10, 150), fill=(0, 0, 0), outline=(0, 0, 0))
   im.save('16x16.png', quality=100)
   im = Image.new('RGB', (200,200), (255, 255, 255))
   draw = ImageDraw.Draw(im)
   draw.rectangle((0, 200, 200, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((10, 10, 190, 190), fill=(255, 255, 255), outline=(255, 255, 255))
   im.save("blank.png",quality =100)
   im2 = Image.open('16x16.png')
   im1 = Image.open('blank.png')
   back_im = im1.copy()
   back_im.paste(im2, (20, 20))
   back_im.save('yno.png', quality=100)
   im = Image.new('RGB', (240,240), (255, 255, 255))
   draw = ImageDraw.Draw(im)
   im.save("blank1.png",quality =100)
   im2 = Image.open('yno.png')
   im1 = Image.open('blank1.png')
   back_im = im1.copy()
   back_im.paste(im2, (20, 20))
   back_im.save('yn161.png', quality=100)


def open_file2():
   filepath = askopenfilename(
      filetypes=[("Text Files", "*.png"), ("All Files", "*.*")]
      )
   
   
   image=cv2.imread(filepath)   #read in the image
   image=cv2.resize(image,(1300,800)) #resizing because opencv does not work well with bigger images
   orig=image.copy()
   gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #RGB To Gray Scal
   '''
cv2.imshow("Title",gray) '''
   blurred=cv2.GaussianBlur(gray,(5,5),0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
   '''
cv2.imshow("Blur",blurred)'''
   edged=cv2.Canny(blurred,30,50)  #30 MinThreshold and 50 is the MaxThreshold
   '''
cv2.imshow("Canny",edged) '''
   contours,hierarchy=cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  #retrieve the contours as a list, with simple apprximation model
   contours=sorted(contours,key=cv2.contourArea,reverse=True)
   #the loop extracts the boundary contours of the page
   for c in contours:
      p=cv2.arcLength(c,True)
      approx=cv2.approxPolyDP(c,0.02*p,True)
      if len(approx)==4:
         target=approx
         break
   approx=mapper.mapp(target) #find endpoints of the sheet
   pts=np.float32([[0,0],[800,0],[800,800],[0,800]])  #map to 800*800 target window
   op=cv2.getPerspectiveTransform(approx,pts)  #get the top or bird eye view effect
   dst=cv2.warpPerspective(orig,op,(800,800))
   cv2.imwrite("IMAGE_NAME.png", dst)
   cv2.imshow("Scanned",dst)
   # creating an image object
   image1=cv2.imread("IMAGE_NAME.png")
   # loading the pixel data of the image'''
   im = Image.open("IMAGE_NAME.png")
   # Creating coordinates of the pixel (x,y)
   C=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
   C[0]= x, y = 700,340
   C[1]= x, y = 700,180
   C[2]= x, y = 700,220
   C[3]= x, y = 700,260
   C[4]= x, y = 700,300
   C[5]= x, y = 700,500
   C[6]= x, y = 700,540
   C[7]= x, y = 700,580
   C[8]= x, y = 700,620
   C[9]= x, y = 660,180
   C[10]= x, y = 660,220
   C[11]= x, y = 660,260
   C[12]= x, y = 660,300
   C[13]= x, y = 660,380
   C[14]= x, y = 660,420
   C[15]= x, y = 660,500
   C[16]= x, y = 660,540
   C[17]= x, y = 660,580
   C[18]= x, y = 660,620
   C[19]= x, y = 660,660
   C[20]= x, y = 620,100
   C[21]= x, y = 620,140
   C[22]= x, y = 620,180
   C[23]= x, y = 620,220
   C[24]= x, y = 620,380
   C[25]= x, y = 620,420
   C[26]= x, y = 620,580
   C[27]= x, y = 620,620
   C[28]= x, y = 620,660
   C[29]= x, y = 620,700
   C[30]= x, y = 580,100
   C[31]= x, y = 580,140
   C[32]= x, y = 580,180
   C[33]= x, y = 580,220
   C[34]= x, y = 580,300
   C[35]= x, y = 580,340
   C[36]= x, y = 580,380
   C[37]= x, y = 580,420
   C[38]= x, y = 580,460
   C[39]= x, y = 580,500
   C[40]= x, y = 580,580
   C[41]= x, y = 580,620
   C[42]= x, y = 580,660
   C[43]= x, y = 580,700
   C[44]= x, y = 540,100
   C[45]= x, y = 540,140
   C[46]= x, y = 540,300
   C[47]= x, y = 540,340
   C[48]= x, y = 540,380
   C[49]= x, y = 540,420
   C[50]= x, y = 540,460
   C[51]= x, y = 540,500
   C[52]= x, y = 540,660
   C[53]= x, y = 540,700
   C[54]= x, y = 500,100
   C[55]= x, y = 500,140
   C[56]= x, y = 500,220
   C[57]= x, y = 500,260
   C[58]= x, y = 500,300
   C[59]= x, y = 500,340
   C[60]= x, y = 500,380
   C[61]= x, y = 500,420
   C[62]= x, y = 500,460
   C[63]= x, y = 500,500
   C[64]= x, y = 500,540
   C[65]= x, y = 500,580
   C[66]= x, y = 500,660
   C[67]= x, y = 500,700
   C[68]= x, y = 460,220
   C[69]= x, y = 460,260
   C[70]= x, y = 460,300
   C[71]= x, y = 460,340
   C[72]= x, y = 460,380
   C[73]= x, y = 460,420
   C[74]= x, y = 460,460
   C[75]= x, y = 460,500
   C[76]= x, y = 460,540
   C[77]= x, y = 460,580
   C[78]= x, y = 420,140
   C[79]= x, y = 420,180
   C[80]= x, y = 420,220
   C[81]= x, y = 420,260
   C[82]= x, y = 420,300
   C[83]= x, y = 420,340
   C[84]= x, y = 420,380
   C[85]= x, y = 420,420
   C[86]= x, y = 420,460
   C[87]= x, y = 420,500
   C[88]= x, y = 420,540
   C[89]= x, y = 420,580
   C[90]= x, y = 420,620
   C[91]= x, y = 420,660
   C[92]= x, y = 380,140
   C[93]= x, y = 380,180
   C[94]= x, y = 380,220
   C[95]= x, y = 380,260
   C[96]= x, y = 380,300
   C[97]= x, y = 380,340
   C[98]= x, y = 380,380
   C[99]= x, y = 380,420
   C[100]= x, y = 380,460
   C[101]= x, y = 380,500
   C[102]= x, y = 380,540
   C[103]= x, y = 380,580
   C[104]= x, y = 380,620
   C[105]= x, y = 380,660
   C[106]= x, y = 340,220
   C[107]= x, y = 340,260
   C[108]= x, y = 340,300
   C[109]= x, y = 340,340
   C[110]= x, y = 340,380
   C[111]= x, y = 340,420
   C[112]= x, y = 340,460
   C[113]= x, y = 340,500
   C[114]= x, y = 340,540
   C[115]= x, y = 340,580
   C[116]= x, y = 300,100
   C[117]= x, y = 300,140
   C[118]= x, y = 300,220
   C[119]= x, y = 300,260
   C[120]= x, y = 300,300
   C[121]= x, y = 300,340
   C[122]= x, y = 300,380
   C[123]= x, y = 300,420
   C[124]= x, y = 300,460
   C[125]= x, y = 300,500
   C[126]= x, y = 300,540
   C[127]= x, y = 300,580
   C[128]= x, y = 300,660
   C[129]= x, y = 300,700
   C[130]= x, y = 260,100
   C[131]= x, y = 260,140
   C[132]= x, y = 260,300
   C[133]= x, y = 260,340
   C[134]= x, y = 260,380
   C[135]= x, y = 260,420
   C[136]= x, y = 260,460
   C[137]= x, y = 260,500
   C[138]= x, y = 260,660
   C[139]= x, y = 260,700
   C[140]= x, y = 220,100
   C[141]= x, y = 220,140
   C[142]= x, y = 220,180
   C[143]= x, y = 220,220
   C[144]= x, y = 220,300
   C[145]= x, y = 220,340
   C[146]= x, y = 220,380
   C[147]= x, y = 220,420
   C[148]= x, y = 220,460
   C[149]= x, y = 220,500
   C[150]= x, y = 220,580
   C[151]= x, y = 220,620
   C[152]= x, y = 220,660
   C[153]= x, y = 220,700
   C[154]= x, y = 180,100
   C[155]= x, y = 180,140
   C[156]= x, y = 180,180
   C[157]= x, y = 180,220
   C[158]= x, y = 180,380
   C[159]= x, y = 180,420
   C[160]= x, y = 180,580
   C[161]= x, y = 180,620
   C[162]= x, y = 180,660
   C[163]= x, y = 180,700
   C[164]= x, y = 140,140
   C[165]= x, y = 140,180
   C[166]= x, y = 140,220
   C[167]= x, y = 140,260
   C[168]= x, y = 140,300
   C[169]= x, y = 140,380
   C[170]= x, y = 140,420
   C[171]= x, y = 140,500
   C[172]= x, y = 140,540
   C[173]= x, y = 140,580
   C[174]= x, y = 140,620
   C[175]= x, y = 140,660
   C[176]= x, y = 100,180
   C[177]= x, y = 100,220
   C[178]= x, y = 100,260
   C[179]= x, y = 100,300
   C[180]= x, y = 100,500
   C[181]= x, y = 100,540
   C[182]= x, y = 100,580
   C[183]= x, y = 100,620
   C[184]= x, y = 700,380
   C[185]= x, y = 700,420
   C[186]= x, y = 700,460
   C[187]= x, y = 660,340
   C[188]= x, y = 660,460
   C[189]= x, y = 620,180
   C[190]= x, y = 620,220
   C[191]= x, y = 620,260
   C[192]= x, y = 620,460
   C[193]= x, y = 620,500
   C[194]= x, y = 620,540
   C[195]= x, y = 580,260
   C[196]= x, y = 580,540
   C[197]= x, y = 540,180
   C[198]= x, y = 540,220
   C[199]= x, y = 540,260
   C[200]= x, y = 540,540
   C[201]= x, y = 540,580
   C[202]= x, y = 540,620
   C[203]= x, y = 500,180
   C[204]= x, y = 500,620
   C[205]= x, y = 460,100
   C[206]= x, y = 460,140
   C[207]= x, y = 460,180
   C[208]= x, y = 460,620
   C[209]= x, y = 460,660
   C[210]= x, y = 460,700
   C[211]= x, y = 420,100
   C[212]= x, y = 420,700
   C[213]= x, y = 380,100
   C[214]= x, y = 380,700
   C[215]= x, y = 340,100
   C[216]= x, y = 340,140
   C[217]= x, y = 340,180
   C[218]= x, y = 340,620
   C[219]= x, y = 340,660
   C[220]= x, y = 340,700
   C[221]= x, y = 300,180
   C[222]= x, y = 300,620
   C[223]= x, y = 260,180
   C[224]= x, y = 260,220
   C[225]= x, y = 260,260
   C[226]= x, y = 260,540
   C[227]= x, y = 260,580
   C[228]= x, y = 260,620
   C[229]= x, y = 220,260
   C[230]= x, y = 220,540
   C[231]= x, y = 180,260
   C[232]= x, y = 180,300
   C[233]= x, y = 180,340
   C[234]= x, y = 180,460
   C[235]= x, y = 180,500
   C[236]= x, y = 180,540
   C[237]= x, y = 140,340
   C[238]= x, y = 140,460
   C[239]= x, y = 120,340
   C[240]= x, y = 120,380
   C[241]= x, y = 120,420
   C[242]= x, y = 120,460
   '''
C[243]= x, y =
C[244]= x, y =
C[245]= x, y =
C[246]= x, y =
C[247]= x, y =
C[248]= x, y =
C[249]= x, y =
C[250]= x, y =
C[251]= x, y =
C[252]= x, y =
C[253]= x, y =
C[254]= x, y =
C[255]= x, y =
C[256]= x, y =
C[257]= x, y =
C[258]= x, y =
C[259]= x, y =
C[259]= x, y =
'''
   # getting pixel value using getpixel() method
   h=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
   h[0]=im.getpixel(C[0])
   h[1]=im.getpixel(C[1])
   h[2]=im.getpixel(C[2])
   h[3]=im.getpixel(C[3])
   h[4]=im.getpixel(C[4])
   h[5]=im.getpixel(C[5])
   h[6]=im.getpixel(C[6])
   h[7]=im.getpixel(C[7])
   h[8]=im.getpixel(C[8])
   h[9]=im.getpixel(C[9])
   h[10]=im.getpixel(C[10])
   h[11]=im.getpixel(C[11])
   h[12]=im.getpixel(C[12])
   h[13]=im.getpixel(C[13])
   h[14]=im.getpixel(C[14])
   h[15]=im.getpixel(C[15])
   h[16]=im.getpixel(C[16])
   h[17]=im.getpixel(C[17])
   h[18]=im.getpixel(C[18])
   h[19]=im.getpixel(C[19])
   h[20]=im.getpixel(C[20])
   h[21]=im.getpixel(C[21])
   h[22]=im.getpixel(C[22])
   h[23]=im.getpixel(C[23])
   h[24]=im.getpixel(C[24])
   h[25]=im.getpixel(C[25])
   h[26]=im.getpixel(C[26])
   h[27]=im.getpixel(C[27])
   h[28]=im.getpixel(C[28])
   h[29]=im.getpixel(C[29])
   h[30]=im.getpixel(C[30])
   h[31]=im.getpixel(C[31])
   h[32]=im.getpixel(C[32])
   h[33]=im.getpixel(C[33])
   h[34]=im.getpixel(C[34])
   h[35]=im.getpixel(C[35])
   h[36]=im.getpixel(C[36])
   h[37]=im.getpixel(C[37])
   h[38]=im.getpixel(C[38])
   h[39]=im.getpixel(C[39])
   h[40]=im.getpixel(C[40])
   h[41]=im.getpixel(C[41])
   h[42]=im.getpixel(C[42])
   h[43]=im.getpixel(C[43])
   h[44]=im.getpixel(C[44])
   h[45]=im.getpixel(C[45])
   h[46]=im.getpixel(C[46])
   h[47]=im.getpixel(C[47])
   h[48]=im.getpixel(C[48])
   h[49]=im.getpixel(C[49])
   h[50]=im.getpixel(C[50])
   h[51]=im.getpixel(C[51])
   h[52]=im.getpixel(C[52])
   h[53]=im.getpixel(C[53])
   h[54]=im.getpixel(C[54])
   h[55]=im.getpixel(C[55])
   h[56]=im.getpixel(C[56])
   h[57]=im.getpixel(C[57])
   h[58]=im.getpixel(C[58])
   h[59]=im.getpixel(C[59])
   h[60]=im.getpixel(C[60])
   h[61]=im.getpixel(C[61])
   h[62]=im.getpixel(C[62])
   h[63]=im.getpixel(C[63])
   h[64]=im.getpixel(C[64])
   h[65]=im.getpixel(C[65])
   h[66]=im.getpixel(C[66])
   h[67]=im.getpixel(C[67])
   h[68]=im.getpixel(C[68])
   h[69]=im.getpixel(C[69])
   h[70]=im.getpixel(C[70])
   h[71]=im.getpixel(C[71])
   h[72]=im.getpixel(C[72])
   h[73]=im.getpixel(C[73])
   h[74]=im.getpixel(C[74])
   h[75]=im.getpixel(C[75])
   h[76]=im.getpixel(C[76])
   h[77]=im.getpixel(C[77])
   h[78]=im.getpixel(C[78])
   h[79]=im.getpixel(C[79])
   h[80]=im.getpixel(C[80])
   h[81]=im.getpixel(C[81])
   h[82]=im.getpixel(C[82])
   h[83]=im.getpixel(C[83])
   h[84]=im.getpixel(C[84])
   h[85]=im.getpixel(C[85])
   h[86]=im.getpixel(C[86])
   h[87]=im.getpixel(C[87])
   h[88]=im.getpixel(C[88])
   h[89]=im.getpixel(C[89])
   h[90]=im.getpixel(C[90])
   h[91]=im.getpixel(C[91])
   h[92]=im.getpixel(C[92])
   h[93]=im.getpixel(C[93])
   h[94]=im.getpixel(C[94])
   h[95]=im.getpixel(C[95])
   h[96]=im.getpixel(C[96])
   h[97]=im.getpixel(C[97])
   h[98]=im.getpixel(C[98])
   h[99]=im.getpixel(C[99])
   h[100]=im.getpixel(C[100])
   h[101]=im.getpixel(C[101])
   h[102]=im.getpixel(C[102])
   h[103]=im.getpixel(C[103])
   h[104]=im.getpixel(C[104])
   h[105]=im.getpixel(C[105])
   h[106]=im.getpixel(C[106])
   h[107]=im.getpixel(C[107])
   h[108]=im.getpixel(C[108])
   h[109]=im.getpixel(C[109])
   h[110]=im.getpixel(C[110])
   h[111]=im.getpixel(C[111])
   h[112]=im.getpixel(C[112])
   h[113]=im.getpixel(C[113])
   h[114]=im.getpixel(C[114])
   h[115]=im.getpixel(C[115])
   h[116]=im.getpixel(C[116])
   h[117]=im.getpixel(C[117])
   h[118]=im.getpixel(C[118])
   h[119]=im.getpixel(C[119])
   h[120]=im.getpixel(C[120])
   h[121]=im.getpixel(C[121])
   h[122]=im.getpixel(C[122])
   h[123]=im.getpixel(C[123])
   h[124]=im.getpixel(C[124])
   h[125]=im.getpixel(C[125])
   h[126]=im.getpixel(C[126])
   h[127]=im.getpixel(C[127])
   h[128]=im.getpixel(C[128])
   h[129]=im.getpixel(C[129])
   h[130]=im.getpixel(C[130])
   h[131]=im.getpixel(C[131])
   h[132]=im.getpixel(C[132])
   h[133]=im.getpixel(C[133])
   h[134]=im.getpixel(C[134])
   h[135]=im.getpixel(C[135])
   h[136]=im.getpixel(C[136])
   h[137]=im.getpixel(C[137])
   h[138]=im.getpixel(C[138])
   h[139]=im.getpixel(C[139])
   h[140]=im.getpixel(C[140])
   h[141]=im.getpixel(C[141])
   h[142]=im.getpixel(C[142])
   h[143]=im.getpixel(C[143])
   h[144]=im.getpixel(C[144])
   h[145]=im.getpixel(C[145])
   h[146]=im.getpixel(C[146])
   h[147]=im.getpixel(C[147])
   h[148]=im.getpixel(C[148])
   h[149]=im.getpixel(C[149])
   h[150]=im.getpixel(C[150])
   h[151]=im.getpixel(C[151])
   h[152]=im.getpixel(C[152])
   h[153]=im.getpixel(C[153])
   h[154]=im.getpixel(C[154])
   h[155]=im.getpixel(C[155])
   h[156]=im.getpixel(C[156])
   h[157]=im.getpixel(C[157])
   h[158]=im.getpixel(C[158])
   h[159]=im.getpixel(C[159])
   h[160]=im.getpixel(C[160])
   h[161]=im.getpixel(C[161])
   h[162]=im.getpixel(C[162])
   h[163]=im.getpixel(C[163])
   h[164]=im.getpixel(C[164])
   h[165]=im.getpixel(C[165])
   h[166]=im.getpixel(C[166])
   h[167]=im.getpixel(C[167])
   h[168]=im.getpixel(C[168])
   h[169]=im.getpixel(C[169])
   h[170]=im.getpixel(C[170])
   h[171]=im.getpixel(C[171])
   h[172]=im.getpixel(C[172])
   h[173]=im.getpixel(C[173])
   h[174]=im.getpixel(C[174])
   h[175]=im.getpixel(C[175])
   h[176]=im.getpixel(C[176])
   h[177]=im.getpixel(C[177])
   h[178]=im.getpixel(C[178])
   h[179]=im.getpixel(C[179])
   h[180]=im.getpixel(C[180])
   h[181]=im.getpixel(C[181])
   h[182]=im.getpixel(C[182])
   h[183]=im.getpixel(C[183])
   h[184]=im.getpixel(C[184])
   h[185]=im.getpixel(C[185])
   h[186]=im.getpixel(C[186])
   h[187]=im.getpixel(C[187])
   h[188]=im.getpixel(C[188])
   h[189]=im.getpixel(C[189])
   h[190]=im.getpixel(C[190])
   h[191]=im.getpixel(C[191])
   h[192]=im.getpixel(C[192])
   h[193]=im.getpixel(C[193])
   h[194]=im.getpixel(C[194])
   h[195]=im.getpixel(C[195])
   h[196]=im.getpixel(C[196])
   h[197]=im.getpixel(C[197])
   h[198]=im.getpixel(C[198])
   h[199]=im.getpixel(C[199])
   h[200]=im.getpixel(C[200])
   h[201]=im.getpixel(C[201])
   h[202]=im.getpixel(C[202])
   h[203]=im.getpixel(C[203])
   h[204]=im.getpixel(C[204])
   h[205]=im.getpixel(C[205])
   h[206]=im.getpixel(C[206])
   h[207]=im.getpixel(C[207])
   h[208]=im.getpixel(C[208])
   h[209]=im.getpixel(C[209])
   h[210]=im.getpixel(C[210])
   h[211]=im.getpixel(C[211])
   h[212]=im.getpixel(C[212])
   h[213]=im.getpixel(C[213])
   h[214]=im.getpixel(C[214])
   h[215]=im.getpixel(C[215])
   h[216]=im.getpixel(C[216])
   h[217]=im.getpixel(C[217])
   h[218]=im.getpixel(C[218])
   h[219]=im.getpixel(C[219])
   h[220]=im.getpixel(C[220])
   h[221]=im.getpixel(C[221])
   h[222]=im.getpixel(C[222])
   h[223]=im.getpixel(C[223])
   h[224]=im.getpixel(C[224])
   h[225]=im.getpixel(C[225])
   h[226]=im.getpixel(C[226])
   h[227]=im.getpixel(C[227])
   h[228]=im.getpixel(C[228])
   h[229]=im.getpixel(C[229])
   h[230]=im.getpixel(C[230])
   h[231]=im.getpixel(C[231])
   h[232]=im.getpixel(C[232])
   h[233]=im.getpixel(C[233])
   h[234]=im.getpixel(C[234])
   h[235]=im.getpixel(C[235])
   h[236]=im.getpixel(C[236])
   h[237]=im.getpixel(C[237])
   h[238]=im.getpixel(C[238])
   h[239]=im.getpixel(C[239])
   h[240]=im.getpixel(C[240])
   h[241]=im.getpixel(C[241])
   h[242]=im.getpixel(C[242])
   '''
print(h[1])
print(h[0])
print(h[1])
print(h[2])
print(h[3])
print(h[4])
print(h[5])
print(h[6])
print(h[7])
print(h[8])
print(h[9])
print(h[10])
print(h[11])
print(h[12])
print(h[13])
print(h[14])
print(h[15])
print(h[16])
print(h[17])
print(h[18])
print(h[19])
print(h[20])
print(h[21])
print(h[22])
print(h[23])
print(h[24])
print(h[25])
print(h[26])
print(h[27])
print(h[28])
print(h[29])
print(h[30])
print(h[31])
print(h[32])
print(h[33])
print(h[34])
print(h[35])
print(h[36])
print(h[37])
print(h[38])
print(h[39])
print(h[40])
print(h[41])
print(h[42])
print(h[43])
print(h[44])
print(h[45])
print(h[46])
print(h[47])
print(h[48])
print(h[49])
print(h[50])
print(h[51])
print(h[52])
print(h[53])
print(h[54])
print(h[55])
print(h[56])
print(h[57])
print(h[58])
print(h[59])
print(h[60])
print(h[61])
print(h[62])
print(h[63])
print(h[64])
print(h[65])
print(h[66])
print(h[67])
print(h[68])
print(h[69])
print(h[70])
print(h[71])
print(h[72])
print(h[73])
print(h[74])
print(h[75])
print(h[76])
print(h[77])
print(h[78])
print(h[79])
print(h[80])
print(h[81])
print(h[82])
print(h[83])
print(h[84])
print(h[85])
print(h[86])
print(h[87])
print(h[88])
print(h[89])
print(h[90])
print(h[91])
print(h[92])
print(h[93])
print(h[94])
print(h[95])
print(h[96])
print(h[97])
print(h[98])
print(h[99])
print(h[100])
print(h[101])
print(h[102])
print(h[103])
print(h[104])
print(h[105])
print(h[106])
print(h[107])
print(h[108])
print(h[109])
print(h[110])
print(h[111])
print(h[112])
print(h[113])
print(h[114])
print(h[115])
print(h[116])
print(h[117])
print(h[118])
print(h[119])
print(h[120])
print(h[121])
print(h[122])
print(h[123])
print(h[124])
print(h[125])
print(h[126])
print(h[127])
print(h[128])
print(h[129])
print(h[130])
print(h[131])
print(h[132])
print(h[133])
print(h[134])
print(h[135])
print(h[136])
print(h[137])
print(h[138])
print(h[139])
print(h[140])
print(h[141])
print(h[142])
print(h[143])
print(h[144])
print(h[145])
print(h[146])
print(h[147])
print(h[148])
print(h[149])
print(h[150])
print(h[151])
print(h[152])
print(h[153])
print(h[154])
print(h[155])
print(h[156])
print(h[157])
print(h[158])
print(h[159])
print(h[160])
print(h[161])
print(h[162])
print(h[163])
print(h[164])
print(h[165])
print(h[166])
print(h[167])
print(h[168])
print(h[169])
print(h[170])
print(h[171])
print(h[172])
print(h[173])
print(h[174])
print(h[175])
print(h[176])
print(h[177])
print(h[178])
print(h[179])
print(h[180])
print(h[181])
print(h[182])
print(h[183])
print(h[184])
print(h[185])
print(h[186])
print(h[187])
print(h[188])
print(h[189])
print(h[190])
print(h[191])
print(h[192])
print(h[193])
print(h[194])
print(h[195])
print(h[196])
print(h[197])
print(h[198])
print(h[199])
print(h[200])
print(h[201])
print(h[202])
print(h[203])
print(h[204])
print(h[205])
print(h[206])
print(h[207])
print(h[208])
print(h[209])
print(h[210])
print(h[211])
print(h[212])
print(h[213])
print(h[214])
print(h[215])
print(h[216])
print(h[217])
print(h[218])
print(h[219])
print(h[220])
print(h[221])
print(h[222])
print(h[223])
print(h[224])
print(h[225])
print(h[226])
print(h[227])
print(h[228])
print(h[229])
print(h[230])
print(h[231])
print(h[232])
print(h[233])
print(h[234])
print(h[235])
print(h[236])
print(h[237])
print(h[238])
print(h[239])
print(h[240])
print(h[241])
print(h[242])
'''
   a=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
   for i in range(0,243):
      if(str(h[i])=="(255, 0, 0)"):
         a[i]="A"
      elif(str(h[i])=="(0, 255, 0)"):
         a[i]="B"
      elif(str(h[i])=="(0, 0, 255)"):
         a[i]="C"
      elif(str(h[i])=="(255, 255, 0)"):
         a[i]="D"
      elif(str(h[i])=="(0, 255, 255)"):
         a[i]="E"
      elif(str(h[i])=="(255, 0, 255)"):
         a[i]="F"
      elif(str(h[i])=="(192, 192, 192)"):
         a[i]="G"
      elif(str(h[i])=="(128, 128, 128)"):
         a[i]="H"
      elif(str(h[i])=="(128, 0, 0)"):
         a[i]="I"
      elif(str(h[i])=="(128, 128, 0)"):
         a[i]="J"
      elif(str(h[i])=="(0, 128, 0)"):
         a[i]="K"
      elif(str(h[i])=="(128, 0, 128)"):
         a[i]="L"
      elif(str(h[i])=="(0, 128, 128)"):
         a[i]="M"
      elif(str(h[i])=="(0, 0, 128)"):
         a[i]="N"
      elif(str(h[i])=="(255, 140, 0)"):
         a[i]="O" #'''darkorange'''
      elif(str(h[i])=="(255, 215, 0)"):
         a[i]="P" #'''gold'''
      elif(str(h[i])=="(85, 107, 47)"):
         a[i]="Q" #'''dark olive green'''
      elif(str(h[i])=="(173, 255, 47)"):
         a[i]="R" #'''green yellow'''
      elif(str(h[i])=="(50, 205, 50)"):
         a[i]="S" #''' lime green'''
      elif(str(h[i])=="(0, 250, 154)"):
         a[i]="T" #'''medium spring green'''
      elif(str(h[i])=="(47, 79, 79)"):
         a[i]="U" #'''dark slate gray'''
      elif(str(h[i])=="(0, 206, 209)"):
         a[i]="V" #'''dark turquoise'''
      elif(str(h[i])=="(100, 149, 237)"):
         a[i]="W" #'''corn flower blue'''
      elif(str(h[i])=="(0, 191, 255)"):
         a[i]="X" #'''dep sky blue'''
      elif(str(h[i])=="(127, 255, 212)"):
         a[i]="Y" #''' aqua marine'''
      elif(str(h[i])=="(0, 0, 205)"):
         a[i]="Z" #''' medium blue'''
      elif(str(h[i])=="(138, 43, 226)"):
         a[i]="a" #''' blue violet'''
      elif(str(h[i])=="(123, 104, 238)"):
         a[i]="b" # ''' medium slate blue'''
      elif(str(h[i])=="(148, 0, 211)"):
         a[i]="c"  #'''dark violet'''
      elif(str(h[i])=="(139, 0, 139)"):
         a[i]="d"  #''' dark mafneta'''
      elif(str(h[i])=="(75, 0, 130)"):
         a[i]="e"  #''' indigo'''
      elif(str(h[i])=="(128, 0, 128)"):
         a[i]="f" #''' purple'''
      elif(str(h[i])=="(238, 130, 238)"):
         a[i]="g"  #'''violet'''
      elif(str(h[i])=="(199, 21, 133)"):
         a[i]="h"  #''' medium violet red'''
      elif(str(h[i])=="(250, 235, 215)"):
         a[i]="i"  #''' antique white'''
      elif(str(h[i])=="(139, 69, 19)"):
         a[i]="j"   #''' saddle brown'''
      elif(str(h[i])=="(210, 105, 30)"):
         a[i]="k" #''' cholate '''
      elif(str(h[i])=="(244, 164, 96)"):
         a[i]="l"  #''' sandy brown '''
      elif(str(h[i])=="(188, 143, 143)"):
         a[i]="m"  #''' rosy brown'''
      elif(str(h[i])=="(176, 196, 222)"):
         a[i]="n"  #''' light steel vlue'''
      elif(str(h[i])=="(240, 255, 240)"):
         a[i]="o"  #'''honey dew'''
      elif(str(h[i])=="(189, 183, 107)"):
         a[i]="p"  #''' dark khaki'''
      elif(str(h[i])=="(34, 139, 34)"):
         a[i]="q"  #''' forest green'''
      elif(str(h[i])=="(60, 179, 113)"):
         a[i]="r"  #'' 'medium sea green'''
      elif(str(h[i])=="(255, 127, 80)"):
         a[i]="s"  #''' coral'''
      elif(str(h[i])=="(255, 99, 71)"):
         a[i]="t"  #''' tomato'''
      elif(str(h[i])=="(240, 128, 128)"):
         a[i]="u"  #''' light coral'''
      elif(str(h[i])=="(255, 160, 122)"):
         a[i]="v"  #''' light salmon'''
      elif(str(h[i])=="(70, 130, 180)"):
         a[i]="w"  #''' steel blue'''
      elif(str(h[i])=="(176, 224, 230)"):
         a[i]="x"  #''' powder blue'''
      elif(str(h[i])=="(30, 144, 255)"):
         a[i]="y"  #''' doger blue'''
      elif(str(h[i])=="(230, 230, 250)"):
         a[i]="z"  #''' lavender'''
      elif(str(h[i])=="(255, 250, 205)"):
         a[i]="0" #'''lemon chiffon'''
      elif(str(h[i])=="(233, 150, 122)"):
         a[i]="1"  #''' dark salmon '''
      elif(str(h[i])=="(255, 105, 180)"):
         a[i]="2" # ''' hot pink'''
      elif(str(h[i])=="(205, 133, 63)"):
         a[i]="3"  #''' rosy brown'''
      elif(str(h[i])=="(222, 184, 135)"):
         a[i]="4"  #''' burly wood'''
      elif(str(h[i])=="(255, 228, 181)"):
         a[i]="5"  #''' mocassin'''
      elif(str(h[i])=="(46, 139, 87)"):
         a[i]="6"  #''' sea green'''
      elif(str(h[i])=="(60, 179, 113)"):
         a[i]="7"  #''' medium sea green'''
      elif(str(h[i])=="(107, 142, 35)"):
         a[i]="8"  #''' dark olive drab'''
      elif(str(h[i])=="(205, 92, 92)"):
         a[i]="9"   #''' indian red'''
      elif(str(h[i])=="(147, 112, 219)"):
         a[i]="+" #''' medium purple'''
      elif(str(h[i])=="(245, 222, 179)"):
         a[i]="/"  #''' wheat'''
      elif(str(h[i])=="(240, 255, 240)"):
         a[i]="="  #''' honeydew'''
      elif(str(h[i])=="(255, 250, 250)"):
         a[i]="."
      else:
         a[i]=""
   print(h)
   print(a)
   def listToString(s):
      # initialize an empty string
      str1 = ""
      #traverse in the string
      for ele in s:
         str1 += ele
      # return string
      return str1 
        
   # Driver code
   f=listToString(a)
   print(listToString(f))
   spl=f.split(".",1)[1]
   minko="cvt"+"."+str(spl)
   sd=f.split(".",1)[0]
   hop=str(sd)
   print (sd)
   file = open('1mn.txt', 'a')
   sys.stdout = file
   print(sd)
   '''
res = bytes(sd, 'utf-8')
print(res)
decoded_string = base64.b64decode(sd)
print(decoded_string )
with open("koki1.rar", "wb") as image_file1:
    image_file1.write(decoded_string);
    '''
   f = open("converted.txt", "r+")
   # absolute file positioning
   f.seek(0)
   # to erase all data
   f.truncate()
   f.close
   '''
   mink="b'"+str(sd)+"'" '''
   # string with encoding 'utf-8'
   file = open('converted.txt', 'w')
   sys.stdout = file
   print(sd)
   file.close()
   '''
   with open('converted.txt', 'r') as f:
      txt = f.read().replace(' ', '')
   with open('converted1.txt', 'w') as f:
      f.write(txt)
    
   '''
   '''
decoded_data=base64.b64decode(mink)
file = open(minko, 'a')
sys.stdout = file

print(sd) 


file.close()
'''
   fin = open(r'converted.txt', "r")
   fout = open(minko, "wb")
   base64.decode(fin, fout)
   fin.close()
   fout.close()

   
def save_file():
   
   """Save the current file as a new file."""
   text = txt_edit.get(1.0, tk.END)
   
   
   a= ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
    ,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']


   
   ion="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
   C=str(text)+ion
   print(len(a))
   print(C)
   for i in range (0,243):
      if(C[i]=="A"):
         a[i]="rgb(255,0,0)"
      elif(C[i]=="B"):
         a[i]="rgb(0,255,0)"
      elif(C[i]=="C"):
        a[i]="rgb(0,0,255)"
      elif(C[i]=="D"):
         a[i]="rgb(255,255,0)"
      elif(C[i]=="E"):
         a[i]="rgb(0,255,255)"
      elif(C[i]=="F"):
         a[i]="rgb(255,0,255)"
      elif(C[i]=="G"):
         a[i]="rgb(192,192,192)"
      elif(C[i]=="H"):
         a[i]="rgb(128,128,128)"
      elif(C[i]=="I"):
         a[i]="rgb(128,0,0)"
      elif(C[i]=="J"):
         a[i]="rgb(128,128,0)"
      elif(C[i]=="K"):
         a[i]="rgb(0,128,0)"
      elif(C[i]=="L"):
         a[i]="rgb(128,0,128)"
      elif(C[i]=="M"):
         a[i]="rgb(0,128,128)"
      elif(C[i]=="N"):
         a[i]="rgb(0,0,128)"
      elif(C[i]=="O"):
         a[i]="rgb(255,140,0)" #'''darkorange'''
      elif(C[i]=="P"):
         a[i]="rgb(255,215,0)" #'''gold'''
      elif(C[i]=="Q"):
         a[i]="rgb(85,107,47)" #'''dark olive green'''
      elif(C[i]=="R"):
         a[i]="rgb(173,255,47)" #'''green yellow'''
      elif(C[i]=="S"):
         a[i]="rgb(50,205,50)" #''' lime green'''
      elif(C[i]=="T"):
         a[i]="rgb(0,250,154)" #'''medium spring green'''
      elif(C[i]=="U"):
         a[i]="rgb(47,79,79)" #'''dark slate gray'''
      elif(C[i]=="V"):
         a[i]="rgb(0,206,209)" #'''dark turquoise'''
      elif(C[i]=="W"):
         a[i]="rgb(100,149,237)" #'''corn flower blue'''
      elif(C[i]=="X"):
         a[i]="rgb(0,191,255)" #'''dep sky blue'''
      elif(C[i]=="Y"):
         a[i]="rgb(127,255,212)" #''' aqua marine'''
      elif(C[i]=="Z"):
         a[i]="rgb(0,0,205)" #''' medium blue'''
      elif(C[i]=="a"):
         a[i]="rgb(138,43,226)" #''' blue violet'''
      elif(C[i]=="b"):
         a[i]="rgb(123,104,238)" # ''' medium slate blue'''
      elif(C[i]=="c"):
         a[i]="rgb(148,0,211)"  #'''dark violet'''
      elif(C[i]=="d"):
         a[i]="rgb(139,0,139)"  #''' dark mafneta'''
      elif(C[i]=="e"):
         a[i]="rgb(75,0,130)"  #''' indigo'''
      elif(C[i]=="f"):
         a[i]="rgb(128,0,128)" #''' purple'''
      elif(C[i]=="g"):
         a[i]="rgb(238,130,238)"  #'''violet'''
      elif(C[i]=="h"):
         a[i]="rgb(199,21,133)"  #''' medium violet red'''
      elif(C[i]=="i"):
         a[i]="rgb(250,235,215)"  #''' antique white'''
      elif(C[i]=="j"):
         a[i]="rgb(139,69,19)"   #''' saddle brown'''
      elif(C[i]=="k"):
         a[i]="rgb(210,105,30)" #''' cholate '''
      elif(C[i]=="l"):
         a[i]="rgb(244,164,96)"  #''' sandy brown '''
      elif(C[i]=="m"):
         a[i]="rgb(188,143,143)"  #''' rosy brown'''
      elif(C[i]=="n"):
         a[i]="rgb(176,196,222)"  #''' light steel vlue'''
      elif(C[i]=="o"):
         a[i]="rgb(240,255,240)"  #'''honey dew'''
      elif(C[i]=="p"):
         a[i]="rgb(189,183,107)"  #''' dark khaki'''
      elif(C[i]=="q"):
         a[i]="rgb(34,139,34)"  #''' forest green'''
      elif(C[i]=="r"):
         a[i]="rgb(60,179,113)"  #'' 'medium sea green'''
      elif(C[i]=="s"):
         a[i]="rgb(255,127,80)"  #''' coral'''
      elif(C[i]=="t"):
         a[i]="rgb(255,99,71)"  #''' tomato'''
      elif(C[i]=="u"):
         a[i]="rgb(240,128,128)"  #''' light coral'''
      elif(C[i]=="v"):
         a[i]="rgb(255,160,122)"  #''' light salmon'''
      elif(C[i]=="w"):
         a[i]="rgb(70,130,180)"  #''' steel blue'''
      elif(C[i]=="x"):
         a[i]="rgb(176,224,230)"  #''' powder blue'''
      elif(C[i]=="y"):
         a[i]="rgb(30,144,255)"  #''' doger blue'''
      elif(C[i]=="z"):
         a[i]="rgb(230,230,250)"  #''' lavender'''
      elif(C[i]=="0"):
         a[i]="rgb(255,250,205)" #'''lemon chiffon'''
      elif(C[i]=="1"):
         a[i]="rgb(233,150,122)"  #''' dark salmon '''
      elif(C[i]=="2"):
         a[i]="rgb(255,105,180)" # ''' hot pink'''
      elif(C[i]=="3"):
         a[i]="rgb(205,133,63)"  #''' rosy brown'''
      elif(C[i]=="4"):
         a[i]="rgb(222,184,135)"  #''' burly wood'''
      elif(C[i]=="5"):
         a[i]="rgb(255,228,181)"  #''' mocassin'''
      elif(C[i]=="6"):
         a[i]="rgb(46,139,87)"  #''' sea green'''
      elif(C[i]=="7"):
         a[i]="rgb(60,179,113)"  #''' medium sea green'''
      elif(C[i]=="8"):
         a[i]="rgb(107,142,35)"  #''' dark olive drab'''
      elif(C[i]=="9"):
         a[i]="rgb(205,92,92)"   #''' indian red'''
      elif(C[i]=="+"):
         a[i]="rgb(147,112,219)" #''' medium purple'''
      elif(C[i]=="/"):
         a[i]="rgb(245,222,179)"  #''' wheat'''
      elif(C[i]=="="):
         a[i]="rgb(220,220,220)"  #''' honeydew'''
      elif(C[i]=="."):
         a[i]="rgb(255,250,250)"
      else:
         a[i]="rgb(0,0,0)"
   print(a[4])
   print(a[16])
   im = Image.new('RGB', (160,160), (128, 128, 128))
   draw = ImageDraw.Draw(im)
   draw.rectangle((0, 10, 160, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 160, 10), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 30, 160, 20), fill=a[1], outline=(0, 0, 0))
   draw.rectangle((0, 40, 160, 30), fill=a[2], outline=(0, 0, 0))
   draw.rectangle((0, 50, 160, 40), fill=a[3], outline=(0, 0, 0))
   draw.rectangle((0, 60, 160, 50), fill=a[4], outline=(0, 0, 0))
   draw.rectangle((0, 70, 160, 60), fill=a[0], outline=(0, 0, 0))
   draw.rectangle((0, 80, 160, 70), fill=a[184], outline=(0, 0, 0))
   draw.rectangle((0, 90, 160, 80), fill=a[185], outline=(0, 0, 0))
   draw.rectangle((0, 100, 160, 90), fill=a[186], outline=(0, 0, 0))
   draw.rectangle((0, 110, 160, 100), fill=a[5], outline=(0, 0, 0))
   draw.rectangle((0, 120, 160, 110), fill=a[6], outline=(0, 0, 0))
   draw.rectangle((0, 130, 160, 120), fill=a[7], outline=(0, 0, 0))
   draw.rectangle((0, 140, 160, 130), fill=a[8], outline=(0, 0, 0))
   draw.rectangle((0, 150, 160, 140), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 160, 160, 150), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 10, 150, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 150, 10), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 30, 150, 20), fill=a[9], outline=(0, 0, 0))
   draw.rectangle((0, 40, 150, 30), fill=a[10], outline=(0, 0, 0))
   draw.rectangle((0, 50, 150, 40), fill=a[11], outline=(0, 0, 0))
   draw.rectangle((0, 60, 150, 50), fill=a[12], outline=(0, 0, 0))
   draw.rectangle((0, 70, 150, 60), fill=a[187], outline=(0, 0, 0))
   draw.rectangle((0, 80, 150, 70), fill=a[13], outline=(0, 0, 0))
   draw.rectangle((0, 90, 150, 80), fill=a[14], outline=(0, 0, 0))
   draw.rectangle((0, 100, 150, 90), fill=a[188], outline=(0, 0, 0))
   draw.rectangle((0, 110, 150, 100), fill=a[15], outline=(0, 0, 0))
   draw.rectangle((0, 120, 150, 110), fill=a[16], outline=(0, 0, 0))
   draw.rectangle((0, 130, 150, 120), fill=a[17], outline=(0, 0, 0))
   draw.rectangle((0, 140, 150, 130), fill=a[18], outline=(0, 0, 0))
   draw.rectangle((0, 150, 150, 140), fill=a[19], outline=(0, 0, 0))
   draw.rectangle((0, 160, 150, 150), fill=(0, 0, 0), outline=(0, 0, 0))

   draw.rectangle((0, 10, 140, 0), fill=a[20], outline=(0, 0, 0))
   draw.rectangle((0, 20, 140, 10), fill=a[21], outline=(0, 0, 0))
   draw.rectangle((0, 30, 140, 20), fill=a[22], outline=(0, 0, 0))
   draw.rectangle((0, 40, 140, 30), fill=a[23], outline=(0, 0, 0))
   draw.rectangle((0, 50, 140, 40), fill=a[189], outline=(0, 0, 0))
   draw.rectangle((0, 60, 140, 50), fill=a[190], outline=(0, 0, 0))
   draw.rectangle((0, 70, 140, 60), fill=a[191], outline=(0, 0, 0))
   draw.rectangle((0, 80, 140, 70), fill=a[24], outline=(0, 0, 0))
   draw.rectangle((0, 90, 140, 80), fill=a[25], outline=(0, 0, 0))
   draw.rectangle((0, 100, 140, 90), fill=a[192], outline=(0, 0, 0))
   draw.rectangle((0, 110, 140, 100), fill=a[193], outline=(0, 0, 0))
   draw.rectangle((0, 120, 140, 110), fill=a[194], outline=(0, 0, 0))
   draw.rectangle((0, 130, 140, 120), fill=a[26], outline=(0, 0, 0))
   draw.rectangle((0, 140, 140, 130), fill=a[27], outline=(0, 0, 0))
   draw.rectangle((0, 150, 140, 140), fill=a[28], outline=(0, 0, 0))
   draw.rectangle((0, 160, 140, 150), fill=a[29], outline=(0, 0, 0))

   draw.rectangle((0, 10, 130, 0), fill=a[30], outline=(0, 0, 0))
   draw.rectangle((0, 20, 130, 10), fill=a[31], outline=(0, 0, 0))
   draw.rectangle((0, 30, 130, 20), fill=a[32], outline=(0, 0, 0))
   draw.rectangle((0, 40, 130, 30), fill=a[33], outline=(0, 0, 0))
   draw.rectangle((0, 50, 130, 40), fill=a[195], outline=(0, 0, 0))
   draw.rectangle((0, 60, 130, 50), fill=a[34], outline=(0, 0, 0))
   draw.rectangle((0, 70, 130, 60), fill=a[35], outline=(0, 0, 0))
   draw.rectangle((0, 80, 130, 70), fill=a[36], outline=(0, 0, 0))
   draw.rectangle((0, 90, 130, 80), fill=a[37], outline=(0, 0, 0))
   draw.rectangle((0, 100, 130, 90), fill=a[38], outline=(0, 0, 0))
   draw.rectangle((0, 110, 130, 100), fill=a[39], outline=(0, 0, 0))
   draw.rectangle((0, 120, 130, 110), fill=a[196], outline=(0, 0, 0))
   draw.rectangle((0, 130, 130, 120), fill=a[40], outline=(0, 0, 0))
   draw.rectangle((0, 140, 130, 130), fill=a[41], outline=(0, 0, 0))
   draw.rectangle((0, 150, 130, 140), fill=a[42], outline=(0, 0, 0))
   draw.rectangle((0, 160, 130, 150), fill=a[43], outline=(0, 0, 0))

   draw.rectangle((0, 10, 120, 0), fill=a[44], outline=(0, 0, 0))
   draw.rectangle((0, 20, 120, 10), fill=a[45], outline=(0, 0, 0))
   draw.rectangle((0, 30, 120, 20), fill=a[197], outline=(0, 0, 0))
   draw.rectangle((0, 40, 120, 30), fill=a[198], outline=(0, 0, 0))
   draw.rectangle((0, 50, 120, 40), fill=a[199], outline=(0, 0, 0))
   draw.rectangle((0, 60, 120, 50), fill=a[46], outline=(0, 0, 0))
   draw.rectangle((0, 70, 120, 60), fill=a[47], outline=(0, 0, 0))
   draw.rectangle((0, 80, 120, 70), fill=a[48], outline=(0, 0, 0))
   draw.rectangle((0, 90, 120, 80), fill=a[49], outline=(0, 0, 0))
   draw.rectangle((0, 100, 120, 90), fill=a[50], outline=(0, 0, 0))
   draw.rectangle((0, 110, 120, 100), fill=a[51], outline=(0, 0, 0))
   draw.rectangle((0, 120, 120, 110), fill=a[200], outline=(0, 0, 0))
   draw.rectangle((0, 130, 120, 120), fill=a[201], outline=(0, 0, 0))
   draw.rectangle((0, 140, 120, 130), fill=a[202], outline=(0, 0, 0))
   draw.rectangle((0, 150, 120, 140), fill=a[52], outline=(0, 0, 0))
   draw.rectangle((0, 160, 120, 150), fill=a[53], outline=(0, 0, 0))

   draw.rectangle((0, 10, 110, 0), fill=a[54], outline=(0, 0, 0))
   draw.rectangle((0, 20, 110, 10), fill=a[55], outline=(0, 0, 0))
   draw.rectangle((0, 30, 110, 20), fill=a[203], outline=(0, 0, 0))
   draw.rectangle((0, 40, 110, 30), fill=a[56], outline=(0, 0, 0))
   draw.rectangle((0, 50, 110, 40), fill=a[57], outline=(0, 0, 0))
   draw.rectangle((0, 60, 110, 50), fill=a[58], outline=(0, 0, 0))
   draw.rectangle((0, 70, 110, 60), fill=a[59], outline=(0, 0, 0))
   draw.rectangle((0, 80, 110, 70), fill=a[60], outline=(0, 0, 0))
   draw.rectangle((0, 90, 110, 80), fill=a[61], outline=(0, 0, 0))
   draw.rectangle((0, 100, 110, 90), fill=a[62], outline=(0, 0, 0))
   draw.rectangle((0, 110, 110, 100), fill=a[63], outline=(0, 0, 0))
   draw.rectangle((0, 120, 110, 110), fill=a[64], outline=(0, 0, 0))
   draw.rectangle((0, 130, 110, 120), fill=a[65], outline=(0, 0, 0))
   draw.rectangle((0, 140, 110, 130), fill=a[204], outline=(0, 0, 0))
   draw.rectangle((0, 150, 110, 140), fill=a[66], outline=(0, 0, 0))
   draw.rectangle((0, 160, 110, 150), fill=a[67], outline=(0, 0, 0))

   draw.rectangle((0, 10, 100, 0), fill=a[205], outline=(0, 0, 0))
   draw.rectangle((0, 20, 100, 10), fill=a[206], outline=(0, 0, 0))
   draw.rectangle((0, 30, 100, 20), fill=a[207], outline=(0, 0, 0))
   draw.rectangle((0, 40, 100, 30), fill=a[68], outline=(0, 0, 0))
   draw.rectangle((0, 50, 100, 40), fill=a[69], outline=(0, 0, 0))
   draw.rectangle((0, 60, 100, 50), fill=a[70], outline=(0, 0, 0))
   draw.rectangle((0, 70, 100, 60), fill=a[71], outline=(0, 0, 0))
   draw.rectangle((0, 80, 100, 70), fill=a[72], outline=(0, 0, 0))
   draw.rectangle((0, 90, 100, 80), fill=a[73], outline=(0, 0, 0))
   draw.rectangle((0, 100, 100, 90), fill=a[74], outline=(0, 0, 0))
   draw.rectangle((0, 110, 100, 100), fill=a[75], outline=(0, 0, 0))
   draw.rectangle((0, 120, 100, 110), fill=a[76], outline=(0, 0, 0))
   draw.rectangle((0, 130, 100, 120), fill=a[77], outline=(0, 0, 0))
   draw.rectangle((0, 140, 100, 130), fill=a[208], outline=(0, 0, 0))
   draw.rectangle((0, 150, 100, 140), fill=a[209], outline=(0, 0, 0))
   draw.rectangle((0, 160, 100, 150), fill=a[210], outline=(0, 0, 0))

   draw.rectangle((0, 10, 90, 0), fill=a[211], outline=(0, 0, 0))
   draw.rectangle((0, 20, 90, 10), fill=a[78], outline=(0, 0, 0))
   draw.rectangle((0, 30, 90, 20), fill=a[79], outline=(0, 0, 0))
   draw.rectangle((0, 40, 90, 30), fill=a[80], outline=(0, 0, 0))
   draw.rectangle((0, 50, 90, 40), fill=a[81], outline=(0, 0, 0))
   draw.rectangle((0, 60, 90, 50), fill=a[82], outline=(0, 0, 0))
   draw.rectangle((0, 70, 90, 60), fill=a[83], outline=(0, 0, 0))
   draw.rectangle((0, 80, 90, 70), fill=a[84], outline=(0, 0, 0))
   draw.rectangle((0, 90, 90, 80), fill=a[85], outline=(0, 0, 0))
   draw.rectangle((0, 100, 90, 90), fill=a[86], outline=(0, 0, 0))
   draw.rectangle((0, 110, 90, 100), fill=a[87], outline=(0, 0, 0))
   draw.rectangle((0, 120, 90, 110), fill=a[88], outline=(0, 0, 0))
   draw.rectangle((0, 130, 90, 120), fill=a[89], outline=(0, 0, 0))
   draw.rectangle((0, 140, 90, 130), fill=a[90], outline=(0, 0, 0))
   draw.rectangle((0, 150, 90, 140), fill=a[91], outline=(0, 0, 0))
   draw.rectangle((0, 160, 90, 150), fill=a[212], outline=(0, 0, 0))

   draw.rectangle((0, 10, 80, 0), fill=a[213], outline=(0, 0, 0))
   draw.rectangle((0, 20, 80, 10), fill=a[92], outline=(0, 0, 0))
   draw.rectangle((0, 30, 80, 20), fill=a[93], outline=(0, 0, 0))
   draw.rectangle((0, 40, 80, 30), fill=a[94], outline=(0, 0, 0))
   draw.rectangle((0, 50, 80, 40), fill=a[95], outline=(0, 0, 0))
   draw.rectangle((0, 60, 80, 50), fill=a[96], outline=(0, 0, 0))
   draw.rectangle((0, 70, 80, 60), fill=a[97], outline=(0, 0, 0))
   draw.rectangle((0, 80, 80, 70), fill=a[98], outline=(0, 0, 0))
   draw.rectangle((0, 90, 80, 80), fill=a[99], outline=(0, 0, 0))
   draw.rectangle((0, 100, 80, 90), fill=a[100], outline=(0, 0, 0))
   draw.rectangle((0, 110, 80, 100), fill=a[101], outline=(0, 0, 0))
   draw.rectangle((0, 120, 80, 110), fill=a[102], outline=(0, 0, 0))
   draw.rectangle((0, 130, 80, 120), fill=a[103], outline=(0, 0, 0))
   draw.rectangle((0, 140, 80, 130), fill=a[104], outline=(0, 0, 0))
   draw.rectangle((0, 150, 80, 140), fill=a[105], outline=(0, 0, 0))
   draw.rectangle((0, 160, 80, 150), fill=a[214], outline=(0, 0, 0))

   draw.rectangle((0, 10, 70, 0), fill=a[215], outline=(0, 0, 0))
   draw.rectangle((0, 20, 70, 10), fill=a[216], outline=(0, 0, 0))
   draw.rectangle((0, 30, 70, 20), fill=a[217], outline=(0, 0, 0))
   draw.rectangle((0, 40, 70, 30), fill=a[106], outline=(0, 0, 0))
   draw.rectangle((0, 50, 70, 40), fill=a[107], outline=(0, 0, 0))
   draw.rectangle((0, 60, 70, 50), fill=a[108], outline=(0, 0, 0))
   draw.rectangle((0, 70, 70, 60), fill=a[109], outline=(0, 0, 0))
   draw.rectangle((0, 80, 70, 70), fill=a[110], outline=(0, 0, 0))
   draw.rectangle((0, 90, 70, 80), fill=a[111], outline=(0, 0, 0))
   draw.rectangle((0, 100, 70, 90), fill=a[112], outline=(0, 0, 0))
   draw.rectangle((0, 110, 70, 100), fill=a[113], outline=(0, 0, 0))
   draw.rectangle((0, 120, 70, 110), fill=a[114], outline=(0, 0, 0))
   draw.rectangle((0, 130, 70, 120), fill=a[115], outline=(0, 0, 0))
   draw.rectangle((0, 140, 70, 130), fill=a[218], outline=(0, 0, 0))
   draw.rectangle((0, 150, 70, 140), fill=a[219], outline=(0, 0, 0))
   draw.rectangle((0, 160, 70, 150), fill=a[220], outline=(0, 0, 0))

   draw.rectangle((0, 10, 60, 0), fill=a[116], outline=(0, 0, 0))
   draw.rectangle((0, 20, 60, 10), fill=a[117], outline=(0, 0, 0))
   draw.rectangle((0, 30, 60, 20), fill=a[221], outline=(0, 0, 0))
   draw.rectangle((0, 40, 60, 30), fill=a[118], outline=(0, 0, 0))
   draw.rectangle((0, 50, 60, 40), fill=a[119], outline=(0, 0, 0))
   draw.rectangle((0, 60, 60, 50), fill=a[120], outline=(0, 0, 0))
   draw.rectangle((0, 70, 60, 60), fill=a[121], outline=(0, 0, 0))
   draw.rectangle((0, 80, 60, 70), fill=a[122], outline=(0, 0, 0))
   draw.rectangle((0, 90, 60, 80), fill=a[123], outline=(0, 0, 0))
   draw.rectangle((0, 100, 60, 90), fill=a[124], outline=(0, 0, 0))
   draw.rectangle((0, 110, 60, 100), fill=a[125], outline=(0, 0, 0))
   draw.rectangle((0, 120, 60, 110), fill=a[126], outline=(0, 0, 0))
   draw.rectangle((0, 130, 60, 120), fill=a[127], outline=(0, 0, 0))
   draw.rectangle((0, 140, 60, 130), fill=a[222], outline=(0, 0, 0))
   draw.rectangle((0, 150, 60, 140), fill=a[128], outline=(0, 0, 0))
   draw.rectangle((0, 160, 60, 150), fill=a[129], outline=(0, 0, 0))

   draw.rectangle((0, 10, 50, 0), fill=a[130], outline=(0, 0, 0))
   draw.rectangle((0, 20, 50, 10), fill=a[131], outline=(0, 0, 0))
   draw.rectangle((0, 30, 50, 20), fill=a[223], outline=(0, 0, 0))
   draw.rectangle((0, 40, 50, 30), fill=a[224], outline=(0, 0, 0))
   draw.rectangle((0, 50, 50, 40), fill=a[225], outline=(0, 0, 0))
   draw.rectangle((0, 60, 50, 50), fill=a[132], outline=(0, 0, 0))
   draw.rectangle((0, 70, 50, 60), fill=a[133], outline=(0, 0, 0))
   draw.rectangle((0, 80, 50, 70), fill=a[134], outline=(0, 0, 0))
   draw.rectangle((0, 90, 50, 80), fill=a[135], outline=(0, 0, 0))
   draw.rectangle((0, 100, 50, 90), fill=a[136], outline=(0, 0, 0))
   draw.rectangle((0, 110, 50, 100), fill=a[137], outline=(0, 0, 0))
   draw.rectangle((0, 120, 50, 110), fill=a[226], outline=(0, 0, 0))
   draw.rectangle((0, 130, 50, 120), fill=a[227], outline=(0, 0, 0))
   draw.rectangle((0, 140, 50, 130), fill=a[228], outline=(0, 0, 0))
   draw.rectangle((0, 150, 50, 140), fill=a[138], outline=(0, 0, 0))
   draw.rectangle((0, 160, 50, 150), fill=a[139], outline=(0, 0, 0))

   draw.rectangle((0, 10, 40, 0), fill=a[140], outline=(0, 0, 0))
   draw.rectangle((0, 20, 40, 10), fill=a[141], outline=(0, 0, 0))
   draw.rectangle((0, 30, 40, 20), fill=a[142], outline=(0, 0, 0))
   draw.rectangle((0, 40, 40, 30), fill=a[143], outline=(0, 0, 0))
   draw.rectangle((0, 50, 40, 40), fill=a[229], outline=(0, 0, 0))
   draw.rectangle((0, 60, 40, 50), fill=a[144], outline=(0, 0, 0))
   draw.rectangle((0, 70, 40, 60), fill=a[145], outline=(0, 0, 0))
   draw.rectangle((0, 80, 40, 70), fill=a[146], outline=(0, 0, 0))
   draw.rectangle((0, 90, 40, 80), fill=a[147], outline=(0, 0, 0))
   draw.rectangle((0, 100, 40, 90), fill=a[148], outline=(0, 0, 0))
   draw.rectangle((0, 110, 40, 100), fill=a[149], outline=(0, 0, 0))
   draw.rectangle((0, 120, 40, 110), fill=a[230], outline=(0, 0, 0))
   draw.rectangle((0, 130, 40, 120), fill=a[150], outline=(0, 0, 0))
   draw.rectangle((0, 140, 40, 130), fill=a[151], outline=(0, 0, 0))
   draw.rectangle((0, 150, 40, 140), fill=a[152], outline=(0, 0, 0))
   draw.rectangle((0, 160, 40, 150), fill=a[153], outline=(0, 0, 0))

   draw.rectangle((0, 10, 30, 0), fill=a[154], outline=(0, 0, 0))
   draw.rectangle((0, 20, 30, 10), fill=a[155], outline=(0, 0, 0))
   draw.rectangle((0, 30, 30, 20), fill=a[156], outline=(0, 0, 0))
   draw.rectangle((0, 40, 30, 30), fill=a[157], outline=(0, 0, 0))
   draw.rectangle((0, 50, 30, 40), fill=a[231], outline=(0, 0, 0))
   draw.rectangle((0, 60, 30, 50), fill=a[232], outline=(0, 0, 0))
   draw.rectangle((0, 70, 30, 60), fill=a[233], outline=(0, 0, 0))
   draw.rectangle((0, 80, 30, 70), fill=a[158], outline=(0, 0, 0))
   draw.rectangle((0, 90, 30, 80), fill=a[159], outline=(0, 0, 0))
   draw.rectangle((0, 100, 30, 90), fill=a[234], outline=(0, 0, 0))
   draw.rectangle((0, 110, 30, 100), fill=a[235], outline=(0, 0, 0))
   draw.rectangle((0, 120, 30, 110), fill=a[236], outline=(0, 0, 0))
   draw.rectangle((0, 130, 30, 120), fill=a[160], outline=(0, 0, 0))
   draw.rectangle((0, 140, 30, 130), fill=a[161], outline=(0, 0, 0))
   draw.rectangle((0, 150, 30, 140), fill=a[162], outline=(0, 0, 0))
   draw.rectangle((0, 160, 30, 150), fill=a[163], outline=(0, 0, 0))

   draw.rectangle((0, 10, 20, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 20, 10), fill=a[164], outline=(0, 0, 0))
   draw.rectangle((0, 30, 20, 20), fill=a[165], outline=(0, 0, 0))
   draw.rectangle((0, 40, 20, 30), fill=a[166], outline=(0, 0, 0))
   draw.rectangle((0, 50, 20, 40), fill=a[167], outline=(0, 0, 0))
   draw.rectangle((0, 60, 20, 50), fill=a[168], outline=(0, 0, 0))
   draw.rectangle((0, 70, 20, 60), fill=a[237], outline=(0, 0, 0))
   draw.rectangle((0, 80, 20, 70), fill=a[169], outline=(0, 0, 0))
   draw.rectangle((0, 90, 20, 80), fill=a[170], outline=(0, 0, 0))
   draw.rectangle((0, 100, 20, 90), fill=a[238], outline=(0, 0, 0))
   draw.rectangle((0, 110, 20, 100), fill=a[171], outline=(0, 0, 0))
   draw.rectangle((0, 120, 20, 110), fill=a[172], outline=(0, 0, 0))
   draw.rectangle((0, 130, 20, 120), fill=a[173], outline=(0, 0, 0))
   draw.rectangle((0, 140, 20, 130), fill=a[174], outline=(0, 0, 0))
   draw.rectangle((0, 150, 20, 140), fill=a[175], outline=(0, 0, 0))
   draw.rectangle((0, 160, 20, 150), fill=(0, 0, 0), outline=(0, 0, 0))

   draw.rectangle((0, 10, 10, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 20, 10, 10), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 30, 10, 20), fill=a[176], outline=(0, 0, 0))
   draw.rectangle((0, 40, 10, 30), fill=a[177], outline=(0, 0, 0))
   draw.rectangle((0, 50, 10, 40), fill=a[178], outline=(0, 0, 0))
   draw.rectangle((0, 60, 10, 50), fill=a[179], outline=(0, 0, 0))
   draw.rectangle((0, 70, 10, 60), fill=a[239], outline=(0, 0, 0))
   draw.rectangle((0, 80, 10, 70), fill=a[240], outline=(0, 0, 0))
   draw.rectangle((0, 90, 10, 80), fill=a[241], outline=(0, 0, 0))
   draw.rectangle((0, 100, 10, 90), fill=a[242], outline=(0, 0, 0))
   draw.rectangle((0, 110, 10, 100), fill=a[180], outline=(0, 0, 0))
   draw.rectangle((0, 120, 10, 110), fill=a[181], outline=(0, 0, 0))
   draw.rectangle((0, 130, 10, 120), fill=a[182], outline=(0, 0, 0))
   draw.rectangle((0, 140, 10, 130), fill=a[183], outline=(0, 0, 0))
   draw.rectangle((0, 150, 10, 140), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((0, 160, 10, 150), fill=(0, 0, 0), outline=(0, 0, 0))
   im.save('160x160.png', quality=100)
   im = Image.new('RGB', (200,200), (255, 255, 255))
   draw = ImageDraw.Draw(im)
   draw.rectangle((0, 200, 200, 0), fill=(0, 0, 0), outline=(0, 0, 0))
   draw.rectangle((10, 10, 190, 190), fill=(255, 255, 255), outline=(255, 255, 255))
   im.save("blank0.png",quality =100)
   im2 = Image.open('160x160.png')
   im1 = Image.open('blank0.png')
   back_im = im1.copy()
   back_im.paste(im2, (20, 20))
   back_im.save('yno0.png', quality=100)
   im = Image.new('RGB', (240,240), (255, 255, 255))
   draw = ImageDraw.Draw(im)
   im.save("blank10.png",quality =100)
   im2 = Image.open('yno0.png')
   im1 = Image.open('blank10.png')
   back_im = im1.copy()
   back_im.paste(im2, (20, 20))
   back_im.save('yn5601.png', quality=100)
  



# Minimum number of matches that have to be found
# to consider the recognition valid
MIN_MATCHES = 5
DEFAULT_COLOR = (255, 0, 0)

def ar():
   def main():
      """
This functions loads the target surface image,
"""
      filepath = askopenfilename(
         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
         )
      
      window.title(f"CRAR - {filepath}")
      image=cv2.imread(filepath)   #read in the image

      image=cv2.resize(image,(1300,800)) #resizing because opencv does not work well with bigger images
      orig=image.copy()
      gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  #RGB To Gray Scal
      '''
cv2.imshow("Title",gray) '''
      blurred=cv2.GaussianBlur(gray,(5,5),0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
      '''
cv2.imshow("Blur",blurred)'''
      edged=cv2.Canny(blurred,30,50)  #30 MinThreshold and 50 is the MaxThreshold
      '''
cv2.imshow("Canny",edged) '''
      contours,hierarchy=cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  #retrieve the contours as a list, with simple apprximation model
      contours=sorted(contours,key=cv2.contourArea,reverse=True)
      #the loop extracts the boundary contours of the page
      for c in contours:
         p=cv2.arcLength(c,True)
         approx=cv2.approxPolyDP(c,0.02*p,True)
         if len(approx)==4:
            target=approx
            break
      approx=mapper.mapp(target) #find endpoints of the sheet
      pts=np.float32([[0,0],[800,0],[800,800],[0,800]])  #map to 800*800 target window
      op=cv2.getPerspectiveTransform(approx,pts)  #get the top or bird eye view effect
      dst=cv2.warpPerspective(orig,op,(800,800))
      cv2.imwrite("IMAGE_NAME.png", dst)
      cv2.imshow("Scanned",dst)
      # creating an image object
      image1=cv2.imread("IMAGE_NAME.png")
      # loading the pixel data of the image'''
      im = Image.open("IMAGE_NAME.png")
      # Creating coordinates of the pixel (x,y)
      C=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
      C[0]= x, y = 700,340
      C[1]= x, y = 700,180
      C[2]= x, y = 700,220
      C[3]= x, y = 700,260
      C[4]= x, y = 700,300
      C[5]= x, y = 700,500
      C[6]= x, y = 700,540
      C[7]= x, y = 700,580
      C[8]= x, y = 700,620
      C[9]= x, y = 660,180
      C[10]= x, y = 660,220
      C[11]= x, y = 660,260
      C[12]= x, y = 660,300
      C[13]= x, y = 660,380
      C[14]= x, y = 660,420
      C[15]= x, y = 660,500
      h=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
      h[0]=im.getpixel(C[0])
      h[1]=im.getpixel(C[1])
      h[2]=im.getpixel(C[2])
      h[3]=im.getpixel(C[3])
      h[4]=im.getpixel(C[4])
      h[5]=im.getpixel(C[5])
      h[6]=im.getpixel(C[6])
      h[7]=im.getpixel(C[7])
      h[8]=im.getpixel(C[8])
      h[9]=im.getpixel(C[9])
      h[10]=im.getpixel(C[10])
      h[11]=im.getpixel(C[11])
      h[12]=im.getpixel(C[12])
      h[13]=im.getpixel(C[13])
      h[14]=im.getpixel(C[14])
      h[15]=im.getpixel(C[15])
      a=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
   '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
      for i in range(0,243):
         if(str(h[i])=="(255, 0, 0)"):
            a[i]="A"
         elif(str(h[i])=="(0, 255, 0)"):
            a[i]="B"
         elif(str(h[i])=="(0, 0, 255)"):
            a[i]="C"
         elif(str(h[i])=="(255, 255, 0)"):
            a[i]="D"
         elif(str(h[i])=="(0, 255, 255)"):
            a[i]="E"
         elif(str(h[i])=="(255, 0, 255)"):
            a[i]="F"
         elif(str(h[i])=="(192, 192, 192)"):
            a[i]="G"
         elif(str(h[i])=="(128, 128, 128)"):
            a[i]="H"
         elif(str(h[i])=="(128, 0, 0)"):
            a[i]="I"
         elif(str(h[i])=="(128, 128, 0)"):
            a[i]="J"
         elif(str(h[i])=="(0, 128, 0)"):
            a[i]="K"
         elif(str(h[i])=="(128, 0, 128)"):
            a[i]="L"
         elif(str(h[i])=="(0, 128, 128)"):
            a[i]="M"
         elif(str(h[i])=="(0, 0, 128)"):
            a[i]="N"
         elif(str(h[i])=="(255, 140, 0)"):
            a[i]="O" #'''darkorange'''
         elif(str(h[i])=="(255, 215, 0)"):
            a[i]="P" #'''gold'''
         elif(str(h[i])=="(85, 107, 47)"):
            a[i]="Q" #'''dark olive green'''
         elif(str(h[i])=="(173, 255, 47)"):
            a[i]="R" #'''green yellow'''
         elif(str(h[i])=="(50, 205, 50)"):
            a[i]="S" #''' lime green'''
         elif(str(h[i])=="(0, 250, 154)"):
            a[i]="T" #'''medium spring green'''
         elif(str(h[i])=="(47, 79, 79)"):
            a[i]="U" #'''dark slate gray'''
         elif(str(h[i])=="(0, 206, 209)"):
            a[i]="V" #'''dark turquoise'''
         elif(str(h[i])=="(100, 149, 237)"):
            a[i]="W" #'''corn flower blue'''
         elif(str(h[i])=="(0, 191, 255)"):
            a[i]="X" #'''dep sky blue'''
         elif(str(h[i])=="(127, 255, 212)"):
            a[i]="Y" #''' aqua marine'''
         elif(str(h[i])=="(0, 0, 205)"):
            a[i]="Z" #''' medium blue'''
         elif(str(h[i])=="(138, 43, 226)"):
            a[i]="a" #''' blue violet'''
         elif(str(h[i])=="(123, 104, 238)"):
            a[i]="b" # ''' medium slate blue'''
         elif(str(h[i])=="(148, 0, 211)"):
            a[i]="c"  #'''dark violet'''
         elif(str(h[i])=="(139, 0, 139)"):
            a[i]="d"  #''' dark mafneta'''
         elif(str(h[i])=="(75, 0, 130)"):
            a[i]="e"  #''' indigo'''
         elif(str(h[i])=="(128, 0, 128)"):
            a[i]="f" #''' purple'''
         elif(str(h[i])=="(238, 130, 238)"):
            a[i]="g"  #'''violet'''
         elif(str(h[i])=="(199, 21, 133)"):
            a[i]="h"  #''' medium violet red'''
         elif(str(h[i])=="(250, 235, 215)"):
            a[i]="i"  #''' antique white'''
         elif(str(h[i])=="(139, 69, 19)"):
            a[i]="j"   #''' saddle brown'''
         elif(str(h[i])=="(210, 105, 30)"):
            a[i]="k" #''' cholate '''
         elif(str(h[i])=="(244, 164, 96)"):
            a[i]="l"  #''' sandy brown '''
         elif(str(h[i])=="(188, 143, 143)"):
            a[i]="m"  #''' rosy brown'''
         elif(str(h[i])=="(176, 196, 222)"):
            a[i]="n"  #''' light steel vlue'''
         elif(str(h[i])=="(240, 255, 240)"):
            a[i]="o"  #'''honey dew'''
         elif(str(h[i])=="(189, 183, 107)"):
            a[i]="p"  #''' dark khaki'''
         elif(str(h[i])=="(34, 139, 34)"):
            a[i]="q"  #''' forest green'''
         elif(str(h[i])=="(60, 179, 113)"):
            a[i]="r"  #'' 'medium sea green'''
         elif(str(h[i])=="(255, 127, 80)"):
            a[i]="s"  #''' coral'''
         elif(str(h[i])=="(255, 99, 71)"):
            a[i]="t"  #''' tomato'''
         elif(str(h[i])=="(240, 128, 128)"):
            a[i]="u"  #''' light coral'''
         elif(str(h[i])=="(255, 160, 122)"):
            a[i]="v"  #''' light salmon'''
         elif(str(h[i])=="(70, 130, 180)"):
            a[i]="w"  #''' steel blue'''
         elif(str(h[i])=="(176, 224, 230)"):
            a[i]="x"  #''' powder blue'''
         elif(str(h[i])=="(30, 144, 255)"):
            a[i]="y"  #''' doger blue'''
         elif(str(h[i])=="(230, 230, 250)"):
            a[i]="z"  #''' lavender'''
         elif(str(h[i])=="(255, 250, 205)"):
            a[i]="0" #'''lemon chiffon'''
         elif(str(h[i])=="(233, 150, 122)"):
            a[i]="1"  #''' dark salmon '''
         elif(str(h[i])=="(255, 105, 180)"):
            a[i]="2" # ''' hot pink'''
         elif(str(h[i])=="(205, 133, 63)"):
            a[i]="3"  #''' rosy brown'''
         elif(str(h[i])=="(222, 184, 135)"):
            a[i]="4"  #''' burly wood'''
         elif(str(h[i])=="(255, 228, 181)"):
            a[i]="5"  #''' mocassin'''
         elif(str(h[i])=="(46, 139, 87)"):
            a[i]="6"  #''' sea green'''
         elif(str(h[i])=="(60, 179, 113)"):
            a[i]="7"  #''' medium sea green'''
         elif(str(h[i])=="(107, 142, 35)"):
            a[i]="8"  #''' dark olive drab'''
         elif(str(h[i])=="(205, 92, 92)"):
            a[i]="9"   #''' indian red'''
         elif(str(h[i])=="(147, 112, 219)"):
            a[i]="+" #''' medium purple'''
         elif(str(h[i])=="(245, 222, 179)"):
            a[i]="/"  #''' wheat'''
         elif(str(h[i])=="(240, 255, 240)"):
            a[i]="="  #''' honeydew'''
         elif(str(h[i])=="(255, 250, 250)"):
            a[i]="."
         else:
            a[i]=""
      print(h)
      print(a)
      def listToString(s):
         # initialize an empty string
         str1 = ""
         #traverse in the string
         for ele in s:
            str1 += ele
            # return string
         return str1 
      # Driver code
      f=listToString(a)
      print(listToString(f))
      sd=f.split(".",1)[0]
      hop=str(sd)
      print (sd)
      if(sd=="///Lox///"):
         goth="models\\fox.obj"
      else:
         print("Errorcode")

      homography = None
      # matrix of camera parameters (made up but works quite well for me)
      camera_parameters = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]])
      # create ORB keypoint detector
      orb = cv2.ORB_create()
      # create BFMatcher object based on hamming distance
      bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
      # load the reference surface that will be searched in the video stream
      dir_name = os.getcwd()
      model = cv2.imread(os.path.join(dir_name, filepath), 0)
      # Compute model keypoints and its descriptors
      kp_model, des_model = orb.detectAndCompute(model, None)
      # Load 3D model from OBJ file
      obj = OBJ(os.path.join(dir_name, goth), swapyz=True)
      # init video capture
      cap = cv2.VideoCapture(0)
      while True:
         # read the current frame
         ret, frame = cap.read()
         if not ret:
            print("Unable to capture video")
            return
         # find and draw the keypoints of the frame
         kp_frame, des_frame = orb.detectAndCompute(frame, None)
         # match frame descriptors with model descriptors
         matches = bf.match(des_model, des_frame)
         # sort them in the order of their distance
         # the lower the distance, the better the match
         matches = sorted(matches, key=lambda x: x.distance)
         # compute Homography if enough matches are found
         if len(matches) > MIN_MATCHES:
            # differenciate between source points and destination points
            src_pts = np.float32([kp_model[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
            # compute Homography
            homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if args.rectangle:
               # Draw a rectangle that marks the found model in the frame
               h, w = model.shape
               pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
               # project corners into frame
               dst = cv2.perspectiveTransform(pts, homography)
               # connect them with lines
               frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
               # if a valid homography matrix was found render cube on model plan
            if homography is not None:
               try:
                  # obtain 3D projection matrix from homography matrix and camera parameters
                  projection = projection_matrix(camera_parameters, homography)
                  # project cube or model
                  frame = render(frame, obj, projection, model, False)
                  #frame = render(frame, model, projection)
               except:
                  pass
               # draw first 10 matches.
            if args.matches:
               frame = cv2.drawMatches(model, kp_model, frame, kp_frame, matches[:5], 0, flags=2)
               # show result
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
               break
         else:
            print("Not enough matches found - %d/%d" % (len(matches), MIN_MATCHES))
      cap.release()
      cv2.destroyAllWindows()
      return 0
   def render(img, obj, projection, model, color=False):
      """
Render a loaded obj model into the current video frame
"""
      vertices = obj.vertices
      scale_matrix = np.eye(3) * 3
      h, w = model.shape
      for face in obj.faces:
         face_vertices = face[0]
         points = np.array([vertices[vertex - 1] for vertex in face_vertices])
         points = np.dot(points, scale_matrix)
         # render model in the middle of the reference surface. To do so,
         # model points must be displaced
         points = np.array([[p[0] + w / 2, p[1] + h / 2, p[2]] for p in points])
         dst = cv2.perspectiveTransform(points.reshape(-1, 1, 3), projection)
         imgpts = np.int32(dst)
         if color is False:
            cv2.fillConvexPoly(img, imgpts, DEFAULT_COLOR)
         else:
            color = hex_to_rgb(face[-1])
            color = color[::-1]  # reverse
            cv2.fillConvexPoly(img, imgpts, color)
      return img
   def projection_matrix(camera_parameters, homography):
      """
From the camera calibration matrix and the estimated homography
compute the 3D projection matrix
"""
      # Compute rotation along the x and y axis as well as the translation
      homography = homography * (-1)
      rot_and_transl = np.dot(np.linalg.inv(camera_parameters), homography)
      col_1 = rot_and_transl[:, 0]
      col_2 = rot_and_transl[:, 1]
      col_3 = rot_and_transl[:, 2]
      # normalise vectors
      l = math.sqrt(np.linalg.norm(col_1, 2) * np.linalg.norm(col_2, 2))
      rot_1 = col_1 / l
      rot_2 = col_2 / l
      translation = col_3 / l
      # compute the orthonormal basis
      c = rot_1 + rot_2
      p = np.cross(rot_1, rot_2)
      d = np.cross(c, p)
      rot_1 = np.dot(c / np.linalg.norm(c, 2) + d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
      rot_2 = np.dot(c / np.linalg.norm(c, 2) - d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
      rot_3 = np.cross(rot_1, rot_2)
      # finally, compute the 3D projection matrix from the model to the current frame
      projection = np.stack((rot_1, rot_2, rot_3, translation)).T
      return np.dot(camera_parameters, projection)
   def hex_to_rgb(hex_color):
      """
Helper function to convert hex strings to RGB
"""
      hex_color = hex_color.lstrip('#')
      h_len = len(hex_color)
      return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))
   # Command line argument parsing
   # NOT ALL OF THEM ARE SUPPORTED YET
   parser = argparse.ArgumentParser(description='Augmented reality application')
   parser.add_argument('-r','--rectangle', help = 'draw rectangle delimiting target surface on frame', action = 'store_true')
   parser.add_argument('-mk','--model_keypoints', help = 'draw model keypoints', action = 'store_true')
   parser.add_argument('-fk','--frame_keypoints', help = 'draw frame keypoints', action = 'store_true')
   parser.add_argument('-ma','--matches', help = 'draw matches between keypoints', action = 'store_true')
   # TODO jgallostraa -> add support for model specification
   #parser.add_argument('-mo','--model', help = 'Specify model to be projected', action = 'store_true')
   args = parser.parse_args()
   if __name__ == '__main__':
      main()


window = tk.Tk()
window.title("CRAR")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="File Con", command=open_file)
btn_open2 = tk.Button(fr_buttons, text="SCAN", command=open_file2)
btn_open3 = tk.Button(fr_buttons, text="OpenAR", command=ar)
btn_save = tk.Button(fr_buttons, text="Save As AR", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open2.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_open3.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

window.mainloop()
