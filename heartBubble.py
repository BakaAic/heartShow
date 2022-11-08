from tkinter import *
import math
import random

class HeartShow:
    def __init__(self):
        self.author=chr(65)+chr(105)+chr(107)+chr(107)+chr(111)
        self.size = 600     #画布大小
        self.Heart_Count = 100   #小心心数量
        self.Heart_max = 15 #小心心的最大尺寸
        self.Heart_min = 6 #小心心的最小尺寸
        self.speed_max = 4   #小心心的最大移动速度
        self.speed_min = 1   #小心心的最小移动速度
        #=======================
        self.heart={}
    
    def show(self):
        #生成窗体
        self.root=Tk()
        self.root.title('心')
        self.root.geometry(str(self.size)+'x'+str(self.size))
        self.root.resizable(0,0)
        self.Board=Canvas(self.root,width=self.size,height=self.size,bg='black')
        self.Board.pack(fill=BOTH,expand=0)
        self.Board.bind('<B1-Motion>',self.buildBubble)
        self.initBubble()
        self.root.after(1,self.heartBubble)
        self.root.mainloop()
    
    def drawLittleHeart(self,_pos,_size,_color,_num):
        #绘制小心心
        self.Board.create_arc(_pos[0] , _pos[1] , _pos[0] + _size , _pos[1] + _size ,start=0,extent=180,fill=_color,outline=_color,tags='heart_'+str(_num))
        self.Board.create_arc(_pos[0] - _size , _pos[1], _pos[0] + _size - _size , _pos[1] + _size ,start=0,extent=180,fill=_color,outline=_color,tags='heart_'+str(_num))
        self.Board.create_arc(_pos[0] - _size, _pos[1] - 0.5 * _size, _pos[0] + _size , _pos[1] + 1.44 * _size ,start=-180,extent=180,fill=_color,outline=_color,tags='heart_'+str(_num))
        self.Board.create_polygon(_pos[0],_pos[1]+1.80*_size , _pos[0] - 0.86*_size,_pos[1] + 0.9*_size, _pos[0] + 0.86*_size,_pos[1] + 0.9*_size,fill=_color,outline=_color,tags='heart_'+str(_num))
        
    def getHeartSize(self,max=15,min=6):
        return random.randint(min,max)

    def getHeartSpeed(self,max=5,min=1):
        return random.randint(min,max)
    
    def getInitPosx(self):
        return random.randint(0,self.size)
    
    def getInitPosy(self):
        return random.randint(0,self.size)
    
    def getShockRange(self):
        return random.randint(0,int(self.size/15))
    
    def getRandomName(self):
        while True:
            _name=str(random.randint(0,self.Heart_Count*100)).zfill(len(str(self.Heart_Count))+2)
            if _name not in self.heart:
                return _name
    
    def initBubble(self):
        while True:
            if len(self.heart)<self.Heart_Count:
                _name=self.getRandomName()
                self.heart[_name]=Heart(self.getHeartSize(self.Heart_max,self.Heart_min),self.getHeartSpeed(self.speed_max,self.speed_min),self.getInitPosx(),self.getInitPosy(),self.getShockRange(),_name)
            else:
                break  

    def buildBubble(self,event):
        if len(self.heart)<3*self.Heart_Count:
            _name=self.getRandomName()
            self.heart[_name]=Heart(self.getHeartSize(self.Heart_max,self.Heart_min),self.getHeartSpeed(self.speed_max,self.speed_min),event.x,event.y,self.getShockRange(),_name)

    def heartBubble(self):
        #跳动起来
        while True:
            if len(self.heart)<self.Heart_Count:
                _name=self.getRandomName()
                self.heart[_name]=Heart(self.getHeartSize(self.Heart_max,self.Heart_min),self.getHeartSpeed(self.speed_max,self.speed_min),self.getInitPosx(),self.size,self.getShockRange(),_name)
            else:
                break
        deleteList=[]
        for _name in self.heart:
            self.heart[_name].rise()
            self.Board.delete('heart_'+_name)
            self.drawLittleHeart(self.heart[_name].getPos(),self.heart[_name].size,self.heart[_name].getHeartColor(self.heart[_name].posy/self.size),_name)
            if not self.heart[_name].life:
                deleteList.append(_name)
        self.Board.update()
        for _name in deleteList:
            self.heart.pop(_name)
        self.root.after(2,self.heartBubble)
        
        
class Heart:
    def __init__(self,size,speed,init_posx,init_posy,shockRange,name):
        self.life=True
        self.size=size
        self.speed=speed
        self.posx_mid=init_posx
        self.posx=self.posx_mid
        self.posx_shock=random.random()
        self.shock_side=random.choice([-1,1])
        self.shockRange=shockRange
        self.shockspeedMax=0.1
        self.shockspeedMin=0.01
        self.posy_size_payoff=self.size*2
        self.posy=init_posy+self.posy_size_payoff
        self.tagsName=name
        self.rgb=self.getRandomInitColor()
    def getPos(self):
        return [self.posx,self.posy]
    def getRandomInitColor(self):
        return [random.randint(0,115),random.randint(0,98),random.randint(0,98)]
    def getHeartColor(self,distanceRate):
        if distanceRate>1:
            distanceRate=1
        elif distanceRate<0:
            distanceRate=0
        distanceRate=math.sqrt(distanceRate)
        _R=255-distanceRate*self.rgb[0]
        _G=0+distanceRate*self.rgb[1]
        _B=0+distanceRate*self.rgb[2]
        _color='#'+str(hex(int(_R)))[2:].zfill(2)+str(hex(int(_G)))[2:].zfill(2)+str(hex(int(_B)))[2:].zfill(2)
        return _color
    def shock(self):
        #震动
        if self.shock_side==1:
            if self.posx_shock>=1:
                self.posx_shock=1
                self.shock_side=-self.shock_side
            else:
                shockspeed=math.sqrt(abs(0-self.posx_shock))*math.sqrt(abs(1-self.posx_shock))*0.2
                if shockspeed<self.shockspeedMin:
                    shockspeed=self.shockspeedMin
                elif shockspeed>self.shockspeedMax:
                    shockspeed=self.shockspeedMax
                self.posx_shock+=shockspeed
        else:
            if self.posx_shock<=0:
                self.posx_shock=0
                self.shock_side=-self.shock_side
            else:
                shockspeed=math.sqrt(abs(0-self.posx_shock))*math.sqrt(abs(1-self.posx_shock))*0.2
                if shockspeed<self.shockspeedMin:
                    shockspeed=self.shockspeedMin
                elif shockspeed>self.shockspeedMax:
                    shockspeed=self.shockspeedMax
                self.posx_shock-=shockspeed
    def rise(self):
        if self.posy+self.posy_size_payoff>0:
            self.posy-=self.speed
            self.shock()
            self.posx=self.posx_mid+self.posx_shock*self.shockRange
        else:
            self.life=False
        
if __name__=='__main__':
    heart=HeartShow()
    heart.show()
