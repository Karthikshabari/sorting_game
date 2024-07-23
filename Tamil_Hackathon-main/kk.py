import sys
import random
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QStackedWidget,QListWidgetItem,QListWidget,QLabel


class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi("Menu.ui",self)
        self.animals.clicked.connect(self.gotoAnimals)


    def gotoAnimals(self):
        A=Animals()
        widget.addWidget(A)
        widget.setCurrentIndex(widget.currentIndex()+1)




class Animals(QDialog):
    def __init__(self):
        super(Animals,self).__init__()
        loadUi("Animals.ui",self)
        Alist = ["ஒட்டகம்", "கரடி", "குதிரை", "சிங்கம்", "நரி", "நாய்", "பசு", "மான்", "யானை"]
        list = []
        self.Rlist=[]
        list = random.sample(Alist, 5)
        self.Rlist=list
        item1 = QListWidgetItem(list[0])
        self.A1.addItem(item1)
        item2 = QListWidgetItem(list[1])
        self.A2.addItem(item2)
        item3 = QListWidgetItem(list[2])
        self.A3.addItem(item3)
        item4 = QListWidgetItem(list[3])
        self.A4.addItem(item4)
        item5 = QListWidgetItem(list[4])
        self.A5.addItem(item5)
        for i in range(0, len(self.Rlist) - 1):
            for j in range(len(self.Rlist) - 1):
                if (self.Rlist[j] > self.Rlist[j + 1]):
                    temp = self.Rlist[j]
                    self.Rlist[j] = self.Rlist[j + 1]
                    self.Rlist[j + 1] = temp
        self.A=[self.A1,self.A2,self.A3,self.A4,self.A5]
        self.R=[self.R1,self.R2,self.R3,self.R4,self.R5]
        self.Output=[]
        self.dec=["சிறந்த பதில்!!!","தொடர்ந்து முயற்சி செய்யுங்கள்!!!"]
        self.j=0
        self.k=0
        f=0
        self.count=0
        print(self.Rlist)
        for i in range(0,5):
            self.A[i].itemPressed.connect(self.res)




    def res(self,im):
        if self.j<5:
            self.Attempts.clear()
            op=str(self.count)
            self.Decision.clear()
            self.R[self.j].addItem(im.text())
            if im.text()==self.Rlist[self.j]:
                 self.Decision.addItem(self.dec[0])
            else:
                self.Decision.addItem(self.dec[1])
                self.R1.clear()
                self.R2.clear()
                self.R3.clear()
                self.R4.clear()
                self.R5.clear()

            self.j += 1




                #main
app=QApplication(sys.argv)
menu=Menu()
widget = QStackedWidget()
widget.addWidget(menu)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
dict={"விலங்குகள்":"ஒட்டகம்,கரடி,குதிரை,சிங்கம்,நரி,நாய்,பசு,மான்,யானை",
      "கிரகங்கள்":"சனி,செவ்வாய்,நெப்டியூன்,புதன்,பூமி,யுரேனஸ்,வியாழன்,வெள்ளி",
      "காய்கறிகள்":"அவரைக்காய்,கத்தரிக்காய்,காரட்,கோவைக்காய்,தக்காளி,புடலங்காய்,பூசணிக்காய்,மாங்காய்,முருங்கைக்காய்",
      "வண்ணங்கள்":"ஆரஞ்சு,ஊதா,கருப்பு,சிவப்பு,தங்க,நீலம்,மஞ்சள்,பச்சை,வெள்ளி,வெள்ளை",
      "பழங்கள்":"அன்னாசிப்பழம்,ஆப்பிள்,எலுமிச்சை்ப்பழம்,தர்பூசணி,பசிப்பாழம்,பப்பாளி,பேரிக்காய்,மாதுளம் பழம்,வாழைப்பழம்,வுெண்ணைப்பழம்",
      "நாட்களில்":"சனிக்கிழமை,செவ்வாய் கிழமை,ஞாயிற்றுக்கிழமை,திங்கட்கிழமை,வியாழன்,வெள்ளி",
      "மாதங்கள்":"ஐப்பாசி,ஆடி,ஆணி,ஆவணி,கார்த்திகை,சித்திரை,பங்குனி,புரட்டாசி,மாசி,மார்கழி,வைகாசி"}
try:
    sys.exit(app.exec_())
except:
    print("EXITING")
