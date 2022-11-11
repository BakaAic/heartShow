from PIL import Image
import os
import pickle
import base64
import math

path=os.getcwd()

img_min=Image.open(path+'/state1.png')
img_max=Image.open(path+'/state2.png')

heartpos_min=[]
heartpos_max=[]

for x in range(600):
    for y in range(600):
        _pixel=img_min.getpixel((x,y))
        if _pixel[0]==255 and _pixel[1]==255 and _pixel[2]==255:
            heartpos_min.append((x,y))
        _pixel=img_max.getpixel((x,y))
        if _pixel[0]==255 and _pixel[1]==255 and _pixel[2]==255:
            heartpos_max.append((x,y))
            
print(len(heartpos_min))
print(len(heartpos_max))

def getDistance(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)

def getCorrespondingPosByDistance(pos_min,pos_max):
    correspondingPos=[]
    for _posMin in pos_min:
        minDistance=[-1,(-1,-1)]
        for _posMax in pos_max:
            distance=getDistance(_posMin,_posMax)
            if minDistance[0]>distance or minDistance[0]==-1:
                minDistance=[distance,_posMax]
        correspondingPos.append([(_posMin[0],_posMin[1]),(minDistance[1][0],minDistance[1][1])])
    return correspondingPos

correspondingPos=getCorrespondingPosByDistance(heartpos_min,heartpos_max)

pk=pickle.dumps(correspondingPos)
with open(path+'/Recurrence/correspondingPos.txt','w') as f:
    dat=str(base64.b64encode(pk))[2:-1]
    f.write("'''\n")
    while True:
        _dat=dat[:3000]+'\\\n'
        dat=dat[3000:]
        if len(dat)==0:
            f.write(_dat[:-2]+'\n')
            break
        else:
            f.write(_dat)
    f.write("'''")

# position visualization test
_list=correspondingPos
from tkinter import *        
root=Tk()
root.geometry('600x600')
root.resizable(0,0)
root.title('test')
cv=Canvas(root,width=600,height=600,bg='black')
cv.pack(fill=BOTH,expand=0)
for min,max in _list:
    cv.create_line(min[0],min[1],min[0]+1,min[1]+1,fill='red')
    cv.create_line(max[0],max[1],max[0]+1,max[1]+1,fill='blue')
root.mainloop()
    
    
