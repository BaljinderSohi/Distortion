# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:10:02 2018

@author: baljot
"""




import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib.pyplot as plt


data = pd.read_csv("baljot.dat", header=None, delimiter=r"\s+")

x = data[0]
y = data[1]
xlist = []
ylist = []

# populate the lists with the contents of the columns read
#
    
for i in range(0,int(len(x))):
   xlist.append(float(x.iloc[i]))
   ylist.append(float(y.iloc[i]))   







f = open("out.dat", "w")

#CLIPPING DISTORTION
for i in range(0,int(len(y))):
    if(ylist[i]>0.5):
        ylist[i]=0.5
    elif(ylist[i]<-0.5):
        ylist[i]=-0.5
    
for i in range(0,int(len(y))):
    ylist[i]=ylist[i]*1.75    


    
    

plt.xlabel('time')
plt.ylabel('amplitude')   
plt.plot(xlist,y)
plt.axis([0.00,0.018,-1,1])
plt.show()
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(xlist,ylist)
plt.axis([0.00,0.018,-1,1])
plt.show()




# add header required for pcm file
# NOTE: we've slowed down the sample rate
#       because at 44100 it plays back fast.
#       I don't know why it does this!
f.write("; Sample Rate "+str(44100/8)+"\n")
f.write("; Channels 1"+"\n")
for i in range(0,int(len(xlist)-2)):
    f.write(str(xlist[i])+" "+str(((ylist[i])))+"\n")


f.close() 
