import pickle
import base64
from tkinter import *
import math
import random

#=================================data====================================#
c_correspondingPos=r'''
gASVK1AAAAAAAABdlChdlChLXUvXhpRLUkvUhpRlXZQoS11L2IaUS1JL1IaUZV2UKEtdS9mGlEtRS9mGlGVdlChLXUvahpRLUUvahpRlXZQoS11L24aUS1FL2oaUZV2UKEtdS9yGlEtRS9qGlGVdlChLXUvdhpRLUUvahpRlXZQoS11L3oaUS1FL2oaUZV2UKEtdS9+GlEtQS9+GlGVdlChLXUvghpRLUEvghpRlXZQoS11L4YaUS1BL4YaUZV2UKEtdS+KGlEtQS+KGlGVdlChLXUvjhpRLUEvihpRlXZQoS11L5IaUS1BL4oaUZV2UKEtdS+WGlEtQS+KGlGVdlChLXUvmhpRLUEvihpRlXZQoS11L54aUS1BL4oaUZV2UKEtdS+iGlEtPS+iGlGVdlChLXUvphpRLT0vphpRlXZQoS15LyoaUS1VLyIaUZV2UKEteS8uGlEtVS8iGlGVdlChLXkvMhpRLVUvIhpRlXZQoS15LzYaUS1RLzIaUZV2UKEteS86GlEtUS8yGlGVdlChLXkvPhpRLVEvMhpRlXZQoS15L0IaUS1RLzIaUZV2UKEteS9GGlEtTS9CGlGVdlChLXkvShpRLU0vQhpRlXZQoS15L04aUS1NL0IaUZV2UKEteS9SGlEtTS9CGlGVdlChLXkvVhpRLUkvUhpRlXZQoS15L1oaUS1JL1IaUZV2UKEteS+qGlEtPS+qGlGVdlChLXkvrhpRLT0vrhpRlXZQoS15L7IaUS1BL8YaUZV2UKEteS+2GlEtQS/GGlGVdlChLXkvuhpRLUEvxhpRlXZQoS15L74aUS1BL8YaUZV2UKEteS/CGlEtQS/GGlGVdlChLXkvxhpRLUEvxhpRlXZQoS15L8oaUS1BL8oaUZV2UKEteS/OGlEtQS/OGlGVdlChLXkv0hpRLUEv0hpRlXZQoS19LxoaUS1dLwoaUZV2UKEtfS8eGlEtWS8WGlGVdlChLX0vIhpRLVkvFhpRlXZQoS19LyYaUS1ZLxYaUZV2UKEtfS/WGlEtQS/WGlGVdlChLX0v2hpRLUEv2hpRlXZQoS19L94aUS1BL94aUZV2UKEtfS/iGlEtRS/2GlGVdlChLX0v5hpRLUUv9hpRlXZQoS19L+oaUS1FL/YaUZV2UKEtfS/uGlEtRS/2GlGVdlChLYEvDhpRLWEu/hpRlXZQoS2BL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
'''

#心形坐标结对数据,格式为[[(pos_x_min1,pos_y_min1),(pos_x_max1,pos_y_max1),distance],[(pos_x_min2,pos_y_min2),(pos_x_max2,pos_y_max2),distance]...]，数据来源于提前获取的根据二值化描线图扫描提取的心形坐标数据
correspondingPos=pickle.loads(base64.b64decode(c_correspondingPos))

#=================================code====================================#

class heartJump:
    def __init__(self):
        #==========↓可调参数↓==========#
        self.fullmode=1                             #是否全屏 [0-1] 为1时全屏
        self.pixelMode=2                            #像素模式 [1-3] 模式为1时像素大小不可调
        self.pixelSize=1                            #像素大小 [1-3]
        self.color='#7E0827'                        #心颜色 [#000000-#FFFFFF]
        self.deviationDistance=50                   #随机散布的最大距离 [100-150]
        self.density=3                              #密度 [1-10]
        self.acquisition_rate = 0.75                #采样率 [0.1-1]
        self.colorIncrease=50                       #颜色增幅 [0-255]
        self.colorIncreaseRate=3                    #颜色增幅倍率 [1-10]
        self.jumpRange=0.8                          #跳动幅度 [0-1]
        self.jumpInterval=2                         #跳动间隔 [0-15] 默认为2
        self.flashColor='#CF91A1'                   #闪烁颜色 [#000000-#FFFFFF]
        self.flashRate=0.03                         #闪烁概率 [0-1]
        self.particleSwitch=1                       #粒子开关 [0-1] 为1时开启粒子
        self.particleDiffusionSize=80               #粒子扩散大小 [30-150]
        self.particleFlashRate=0.2                  #粒子闪烁率 [0-1]
        self.particleThickness=2                    #粒子厚度 [1-3]
        self.particleColor_state1='#D25979'         #粒子颜色状态1 [#000000-#FFFFFF]
        self.particleColor_state2='#AB3554'         #粒子颜色状态2 [#000000-#FFFFFF]

        #==========↑可调参数↑==========#
        self.rohtua_=chr(65)+chr(105)+chr(107)+chr(107)+chr(111)
        self.correspondingPos=correspondingPos  
        self.point=[]
        self.centerPos=(300,300)
        self.jumpDegree=0
        self.jumpFrame=0
        self.FrameList=[0.1,0.4,0.7,1.0,0.5,0.3,-0.1,-0.35,-0.1,0]
        for r in range(self.jumpInterval):
            self.FrameList.insert(0,0)
        self.setRandomPoint()
        self.setparticleColorRange()

    def show(self):
        self.root=Tk()
        self.root.title('心跳')
        self.root['bg']='#000000'
        self.root.resizable(0,0)
        if self.fullmode:
            self.root.geometry(str(self.root.winfo_screenwidth())+'x'+str(self.root.winfo_screenheight())+'+-10+0')
            self.root.attributes('-fullscreen',1)
            self.root.bind('<Motion>',self.changeFullScreen)
        else:
            self.root.geometry('600x600'+'+'+str(int(self.root.winfo_screenwidth()/2-300))+'+'+str(int(self.root.winfo_screenheight()/2-300)))
        self.Board=Canvas(self.root,width=600,height=600,bg='#000000',highlightthickness=0)
        self.Board.place(anchor='center',relx=0.5,rely=0.5)
        self.root.after(1,self.heartShow)
        self.root.mainloop()
        
    def heartShow(self):
        self.Board.delete('heart')
        #粒子效果部分         
        if self.particleSwitch:
            for data in self.correspondingPos:
                for i in range(self.particleThickness):          
                    if random.random()<=self.particleFlashRate:
                        
                        if random.random()>self.flashRate:
                            _color=self.particleColorChange(abs(self.FrameList[self.jumpFrame]))
                        else:
                            _color=self.flashColor
                            
                        _L1=-math.log(random.random())*0.15
                        if _L1>1:
                            _L1=1
                        _L2=-math.log(random.random())*0.15
                        if _L2>1:
                            _L2=1
                        _R1=random.random()*0.1
                        _R2=random.random()*0.1
                        _negaRate=1
                        if self.FrameList[self.jumpFrame]<0:
                            _negaRate=5
                        randomPos_x=data[0][0] +(data[0][0]-self.centerPos[0])*0.32 *(_L1*abs(self.FrameList[self.jumpFrame]))*_negaRate *abs(self.FrameList[self.jumpFrame]) +(data[0][0]-self.centerPos[0])*_R1
                        randomPos_y=data[0][1] +(data[0][1]-self.centerPos[1])*0.32 *(_L2*abs(self.FrameList[self.jumpFrame]))*_negaRate *abs(self.FrameList[self.jumpFrame]) +(data[0][1]-self.centerPos[1])*_R2
                        if self.pixelMode==1 or self.pixelMode==3:
                            self.Board.create_line(randomPos_x ,randomPos_y ,randomPos_x +1 ,randomPos_y +1 ,fill=_color,tags='heart')
                        elif self.pixelMode==2:
                            self.Board.create_oval(randomPos_x ,randomPos_y ,randomPos_x +2,randomPos_y +2,fill=_color,outline=_color,tags='heart')
                            
                    if random.random()<=self.particleFlashRate:                    
                        if random.random()>self.flashRate:
                            _color=self.particleColorChange(abs(self.FrameList[self.jumpFrame]))
                        else:
                            _color=self.flashColor
                        _R1=random.random()*0.04
                        _R2=random.random()*0.04
                        _negaRate=1
                        if self.FrameList[self.jumpFrame]<0:
                            _negaRate=5
                        randomPos_x=data[0][0] -(data[0][0]-self.centerPos[0]) *_negaRate *(abs(self.FrameList[self.jumpFrame]*2)+1.5)*_R1 +(data[0][0]-self.centerPos[0])*0.11
                        randomPos_y=data[0][1] -(data[0][1]-self.centerPos[1]) *_negaRate *(abs(self.FrameList[self.jumpFrame]*2)+1.5)*_R2 +(data[0][1]-self.centerPos[1])*0.11
                        if self.pixelMode==1 or self.pixelMode==3:
                            self.Board.create_line(randomPos_x ,randomPos_y ,randomPos_x +1 ,randomPos_y +1 ,fill=_color,tags='heart')
                        elif self.pixelMode==2:
                            self.Board.create_oval(randomPos_x ,randomPos_y ,randomPos_x +2,randomPos_y +2,fill=_color,outline=_color,tags='heart')
                
        #心形部分
        for point in self.point:
            if random.random()<self.acquisition_rate:
                distanceRate=point.curDistance(((point.curPos[0],point.curPos[1])))/point.centerDistance()
                if random.random()>self.flashRate:
                    _color=self.colorChange(distanceRate)
                else:
                    _color=self.flashColor
                curPos_x=point.pos[0]+self.jumpDegree*point.jumpDistance[0]*self.deviationRate(distanceRate)
                curPos_y=point.pos[1]+self.jumpDegree*point.jumpDistance[1]*self.deviationRate(distanceRate)
                point.curPos=(curPos_x,curPos_y)
                if self.pixelMode==1:
                    self.Board.create_line(curPos_x ,curPos_y ,curPos_x +1 ,curPos_y +1 ,fill=_color,tags='heart')
                elif self.pixelMode==2 or self.pixelMode==3:
                    self.Board.create_rectangle(curPos_x ,curPos_y ,curPos_x +point.size,curPos_y +point.size,fill=_color,outline=_color,tags='heart')   
        self.Board.update()
        self.jumpLoop()
        self.root.after(1,self.heartShow)
        
        
    def deviationRate(self,distanceRate):
        return math.pow((1-distanceRate),2)*self.jumpRange
       
    def setparticleColorRange(self):
        _s1_colorHEX=[self.particleColor_state1[1:3],self.particleColor_state1[3:5],self.particleColor_state1[5:7]]
        _s2_colorHEX=[self.particleColor_state2[1:3],self.particleColor_state2[3:5],self.particleColor_state2[5:7]]
        _s1_colorHEX=list(map(lambda l:int(l,16),_s1_colorHEX))
        _s2_colorHEX=list(map(lambda l:int(l,16),_s2_colorHEX))
        self._colorHexDifference=list(map(lambda c1,c2:c1-c2,_s2_colorHEX,_s1_colorHEX))
        self._colorHexDifference.extend(_s1_colorHEX)
       
    def particleColorChange(self,rate):
        _R=self._colorHexDifference[0]*rate+self._colorHexDifference[3]
        _G=self._colorHexDifference[1]*rate+self._colorHexDifference[4]
        _B=self._colorHexDifference[2]*rate+self._colorHexDifference[5]
        _color='#'+str(hex(int(_R)))[2:].zfill(2).upper()+str(hex(int(_G)))[2:].zfill(2).upper()+str(hex(int(_B)))[2:].zfill(2).upper()
        return _color
        
    def colorChange(self,distanceRate):
        distanceRate=math.pow((1-distanceRate),2)*self.colorIncreaseRate
        _R=int(self.color[1:3],16)+distanceRate*self.colorIncrease
        _G=int(self.color[3:5],16)+distanceRate*self.colorIncrease
        _B=int(self.color[5:7],16)+distanceRate*self.colorIncrease
        if _R>255:
            _R=255
        if _G>207:
            _G=207
        if _B>216: 
            _B=216
        _color='#'+str(hex(int(_R)))[2:].zfill(2).upper()+str(hex(int(_G)))[2:].zfill(2).upper()+str(hex(int(_B)))[2:].zfill(2).upper()
        return _color
        
    def jumpLoop(self):
        self.jumpFrame+=1
        if self.jumpFrame==len(self.FrameList):
            self.jumpFrame=0
        self.jumpDegree=self.FrameList[self.jumpFrame]
        
    def changeFullScreen(self,event):
        if event.y<50:
            self.root.attributes('-fullscreen',0)
        else:
            self.root.attributes('-fullscreen',1)
            
    def setRandomPoint(self):
        for i in range(self.density):
            for data in self.correspondingPos:
                _l=-math.log(random.random())
                if _l>6:
                    _l=6
                if _l<0:
                    _l=0
                _deviationDistance=self.deviationDistance * _l
                self.point.append(heartPoint(data[0],data[1],_deviationDistance,self.pixelSize,self.centerPos))

class heartPoint():
    def __init__(self,minPos,maxPos,deviation,size,centerPos=(300,300)):
        self.minPos=minPos
        self.maxPos=maxPos
        self.size=size
        self.deviation=deviation
        self.setMyPos()
        self.centerPos=centerPos
        self.curPos=self.pos
        self.jumpDistance=[(self.maxPos[0]-self.pos[0]),(self.maxPos[1]-self.pos[1])]
    
    def centerDistance(self):
        return abs(self.getDistance(self.maxPos,self.centerPos))
    
    def curDistance(self,curPos):
        return abs(self.getDistance(self.maxPos,curPos))
    
    def setMyPos(self):
        if self.minPos[0]>=self.maxPos[0]:
            _negat=1
        elif self.minPos[0]<self.maxPos[0]:
            _negat=-1
        if self.maxPos[0]-self.minPos[0]==0 and self.maxPos[1]-self.minPos[1]==0:
            self.pos=[self.minPos[0],self.minPos[1]]
        elif self.maxPos[0]-self.minPos[0]==0:
            self.pos=[self.minPos[0],self.minPos[1] + self.deviation * _negat]
        elif self.maxPos[1]-self.minPos[1]==0:
            self.pos=[self.minPos[0]+self.deviation * _negat,self.minPos[1]]
        else:
            self.slope=(self.maxPos[0]-self.minPos[0])/(self.maxPos[1]-self.minPos[1])
            _x=math.sqrt(self.deviation**2/(1+1/self.slope**2))
            _y=_x/self.slope
            self.pos=[self.minPos[0]-_x *-_negat,self.minPos[1]-_y *-_negat]
    
    def getDistance(self,pos1,pos2):
        return math.sqrt(math.pow((pos1[0]-pos2[0]),2)+math.pow((pos1[1]-pos2[1]),2))
    
    def getJumpMove(self,rate):
        return [self.jumpDistance[0]*rate,self.jumpDistance[1]*rate]
        
        
if __name__=='__main__':
    heart=heartJump()
    heart.show()
