from tkinter import *
import math
import random

class HeartShow:
    def __init__(self):
        self.author=chr(65)+chr(105)+chr(107)+chr(107)+chr(111)
        #=====================参数设置=====================
        self.colorMode=1    #颜色模式：【1】 【2】
        self.jumpZoom=1     #跳动缩放：1-10
        self.speed = 0.05   #速度：0.05-0.1
        self.heartSize_max = 80 #心形大小：60-150
        self.size = 600     #窗体大小：600-1000
        self.acquisition_rate = 0.85    #采集率：0.1-1
        #==================================================
        self.heartSize_rate = 2
        self.heartSize_deviation = (self.heartSize_max - self.heartSize_max * self.heartSize_rate) *2.5
        self.rate = 1.15
        self.deviation = self.size / 2 - 2 * self.heartSize_max
        self.payback = 2 * self.heartSize_max + self.deviation
        self.core_Pos = (self.size / 2, self.size / 2 - self.heartSize_deviation*1.5)
        self.curJumpRate = 1
        self.defaultJumpInterval = 26
        self.jumpInterval = self.defaultJumpInterval
        self.zoomforwards = -1
        self.setRandomSlope()
        self.heart_Pos=self.getHeartPos()

    def setRandomSlope(self):
        #设置随机斜率
        self.randomSlope=[]
        for i in range(1,101):
            self.randomSlope.extend([101-i for x in range(int(1/(1/i**2)))])            
            
    def show(self):
        #生成窗体
        self.root=Tk()
        self.root.title('心跳')
        self.root.geometry(str(self.size)+'x'+str(self.size))
        self.root.resizable(0,0)
        self.Board=Canvas(self.root,width=self.size,height=self.size,bg='black')
        self.Board.pack(fill=BOTH,expand=0)
        self.root.after(1,self.heartJump)
        self.root.mainloop()
    
    def getHeartColor(self,distanceRate,mode):
        #获取心形渐变颜色
        if mode==1:
            distanceRate=distanceRate*2
            if distanceRate>1:
                distanceRate=1
            elif distanceRate<0:
                distanceRate=0
            _R=255-distanceRate*130
            _G=20+distanceRate*100
            _B=90+distanceRate*90
        else:
            distanceRate=distanceRate*2
            if distanceRate>1:
                distanceRate=1
            elif distanceRate<0:
                distanceRate=0
            _R=245+distanceRate*10
            _G=165-distanceRate*130
            _B=170-distanceRate*135
        
        _color='#'+str(hex(int(_R)))[2:].zfill(2)+str(hex(int(_G)))[2:].zfill(2)+str(hex(int(_B)))[2:].zfill(2)
        return _color

    def jumpCycle(self):
        #跳动周期
        if self.jumpInterval>0:
            self.jumpInterval-=1
            return 
        if self.zoomforwards>0:
            if self.curJumpRate>1:
                self.curJumpRate=1
                self.zoomforwards=-1
                self.jumpInterval=self.defaultJumpInterval
            else:
                self.curJumpRate += 0.3
        else:
            if self.curJumpRate<0:
                self.curJumpRate=0
                self.zoomforwards=1
            else:
                self.curJumpRate -= 0.3
                
    def jumpExpand(self):
        #跳动扩展
        return (1-self.curJumpRate)*0.04*self.jumpZoom+1  

    def jumpOffset(self):
        #跳动偏移
        return (1-self.curJumpRate)*self.heartSize_max/8*self.jumpZoom

    def heartJump(self):
        #心跳
        for i in range(len(self.heart_Pos)):
            self.Board.delete('heart_'+str(i))
            
            curPos_x=(self.heart_Pos[i][0]-self.core_Pos[0])*self.jumpExpand() -(self.heart_Pos[i][2]-self.core_Pos[0])*self.heart_Pos[i][4]/2 +self.core_Pos[0] 
            curPos_y=(self.heart_Pos[i][1]-self.core_Pos[1])*self.jumpExpand() +self.jumpOffset() -(self.heart_Pos[i][3]-self.core_Pos[1])*self.heart_Pos[i][4]/2 +self.core_Pos[1]
            curPos=(curPos_x, curPos_y)
            self.Board.create_rectangle(curPos[0],curPos[1],curPos[0]+1,curPos[1]+1,fill=self.getHeartColor(self.heart_Pos[i][4],self.colorMode),outline=self.getHeartColor(self.heart_Pos[i][4],self.colorMode),tags='heart_'+str(i))

            curPos_x=(self.heart_Pos[i][0]-self.core_Pos[0])-(self.heart_Pos[i][2]-self.core_Pos[0])*self.heart_Pos[i][4]/2 * -0.4 +self.core_Pos[0] 
            curPos_y=(self.heart_Pos[i][1]-self.core_Pos[1])-(self.heart_Pos[i][3]-self.core_Pos[1])*self.heart_Pos[i][4]/2 * -0.4 +self.core_Pos[1] 
            curPos=(curPos_x, curPos_y)

            if self.colorMode==1:
                out_color='#770115'
            else:
                out_color='#551313'
            self.Board.create_rectangle(curPos[0],curPos[1],curPos[0]+1,curPos[1]+1,fill=out_color,outline=out_color,tags='heart_'+str(i)) 
            
            _speed=self.speed * math.sqrt(abs(0-self.heart_Pos[i][4]))
            if _speed<0.01:
                _speed=0.004
            elif _speed>1:
                _speed=1

            self.heart_Pos[i][4]-=_speed
            if self.heart_Pos[i][4]<=0:
                self.heart_Pos[i][4]=random.choice(self.randomSlope)*0.01
        self.jumpCycle()
        self.Board.update()
        self.root.after(1,self.heartJump)
        
    def getHeartPos(self):
        #心形分布坐标
        posList=[]
        for x in range(-2 * self.heartSize_max,2 * self.heartSize_max):
            if random.random()<self.acquisition_rate:
                p1_x=self.payback+x
                p1_y=self.payback+self.getPosByX_1(x,self.heartSize_max)*self.heartSize_max*self.rate
                p1_x_min=self.payback+x*self.heartSize_rate
                p1_y_min=self.payback+self.getPosByX_1(x,self.heartSize_max)*self.heartSize_max*self.rate*self.heartSize_rate-self.heartSize_deviation
                
                p2_x=self.payback+x
                p2_y=self.payback+self.getPosByX_2(x,self.heartSize_max)*self.heartSize_max*self.rate
                
                p2_x_min=self.payback+x*self.heartSize_rate
                p2_y_min=self.payback+self.getPosByX_2(x,self.heartSize_max)*self.heartSize_max*self.rate*self.heartSize_rate-self.heartSize_deviation

                posList.append([p1_x,p1_y,p1_x_min,p1_y_min,random.choice(self.randomSlope)*0.01])  
                posList.append([p2_x,p2_y,p2_x_min,p2_y_min,random.choice(self.randomSlope)*0.01])
        random.shuffle(posList)
        return posList

    def getPosByX_1(self,x,heartSize):
        #心形生成函数part1
        x=x / heartSize
        y = - math.sqrt(1-(abs(x)-1)**2)
        return y
    def getPosByX_2(self,x,heartSize):
        #心形生成函数part2
        x=x / heartSize
        y= 2 * math.sqrt(1 - 0.5 * abs(x) )
        return y
        
if __name__=='__main__':
    heart=HeartShow()
    heart.show()
