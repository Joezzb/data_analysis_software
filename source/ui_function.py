###########################################################################################
###                        CODE:       WRITTEN BY: ANJAL.P AUGUST 11 2020               ###
###                        PROJECT:    PELLIS Z1                                        ###
###                        PURPOSE:    WINDOWS/LINUX/MAC OS FLAT MODERN UI              ###
###                                    BASED ON QT DESIGNER, PySide2                    ###
###                        USE CASE:   TEMPLATE FOR SOFTWARES                           ###
###                        LICENCE:    MIT OPENSOURCE LICENCE                           ###
###                                                                                     ###
###                            CODE IS FREE TO USE AND MODIFY                           ###
###########################################################################################

###########################################################################################
#                                     DOCUMENTATION                                       #
#                                                                                         #
#                                                                                         #
#  Each line of the code described below is commented well, such as: the purpose of the   #
#  code, its function, returns e.t.c as in certain caes: the alternatives to that solul-  #
#  ution, other sources like included PDF document has also the working of the code.      #
#  CSS stylesheet of the buttons are given seperatly in the CSS.txt in the parent folder  #
###########################################################################################

###########################################################################################
#                                       CAUTION                                           #
#  SINCE MOST OF THE WORK IS DONE IN THE QT DESIGNER, YOU WAY NOT SEE THE STYLESHEET HERE #
#  FOR THAT PLEASE REFER THE CSS.txt FILE PROVIDED IN THIS SAME FILE.                     #
#  ALSO AMNY OF THE SETTINGS IS PREDEFINED IN THE QT DESIGNER ITSELF, SO HERE IN THIS FUN-#
#  CTION WHAY HAPPENS AFTER THIS I.E. WHEN THE USER CHANGES THE INPUT STATE, ONLY IS DELT #
#  HERE, SO IF YOU WANT TO MODIFY THE FILE, PLEASE OPEN THE CORRESPONDING .ui FILE IN QT  #
#  DESIGNER AND MADE THE MODIFICATION AND THENY COME BACK HERE TO ADD FUNCTIONALITY TO THE#
#  CHANGES.                                                                               #
########################################################################################### 


from main import * #IMPORTING THE MAIN.PY FILE

import numpy as np
import os
from sklearn.svm import OneClassSVM
import pickle

#########################################################################
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

matplotlib.use("Qt5Agg") 

class MyFigureCanvas(FigureCanvas):

    def __init__(self, parent=None, width=10, height=5, dpi=100):
        # 创建一个Figure
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白
 
        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)
 
        self.axes = fig.add_subplot(111)  # 添加子图
        self.axes.spines['top'].set_visible(False)  # 去掉绘图时上面的横线
        self.axes.spines['right'].set_visible(False)  # 去掉绘图时右面的横线
        #self.axes.set_xlim(xlim)
        #self.axes.set_ylim(ylim)

#########################################################################
GLOBAL_STATE = 0 #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
init = False # NECRESSERY FOR INITITTION OF THE WINDOW.

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.
class UIFunction(MainWindow):

    #----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE 
    #INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True
    ################################################################################################


    #------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)
    ################################################################################################


    #----> MAXIMISE/RESTORE FUNCTION
    #THIS FUNCTION MAXIMISES OUR MAINWINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DOEN OVER THE TOPFRMAE.
    #THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore") 
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png")) #CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide() #HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png")) #CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()
    ################################################################################################


    #----> RETURN STATUS MAX OR RESTROE
    #NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE


    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    #------> TOODLE MENU FUNCTION
    #THIS FUNCTION TOODLES THE MENU BAR TO DOUBLE THE LENGTH OPENING A NEW ARE OF ABOUT TAB IN FRONT.
    #ASLO IT SETS THE ABOUT>HOME AS THE FIRST PAGE.
    #IF THE PAGE IS IN THE ABOUT PAGE THEN PRESSING AGAIN WILL RESULT IN UNDOING THE PROCESS AND COMMING BACK TO THE 
    #HOME PAGE.
    def toodleMenu(self, maxWidth, clicked):

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
        if clicked:
            currentWidth = self.ui.frame_bottom_west.width() #Reads the current width of the frame
            minWidth = 80 #MINIMUN WITDTH OF THE BOTTOM_WEST FRAME
            if currentWidth==80:
                extend = maxWidth
                #----> MAKE THE STACKED WIDGET PAGE TO ABOUT HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                #-----> REVERT THE ABOUT HOME PAGE TO NORMAL HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            #THIS ANIMATION IS RESPONSIBLE FOR THE TOODLE TO MOVE IN A SOME FIXED STATE.
            self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    ################################################################################################


    #-----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        #-----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        #----> REMOVE NORMAL TITLE BAR 
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        #-----> RESIZE USING DRAG                                       THIS CODE TO DRAG AND RESIZE IS IN PROTOPYPE.
        #self.sizegrip = QSizeGrip(self.ui.frame_drag)
        #self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON FUNCTION 
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        #-----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: UIFunction.savehistory(self))
        self.ui.bn_close.clicked.connect(lambda: self.close())
    ################################################################################################################


    #----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.

        if buttonName=='bn_home':
            if self.ui.frame_bottom_west.width()==80  and index!=0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST 

            elif self.ui.frame_bottom_west.width()==160  and index!=1:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                #self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_bug':
            if self.ui.frame_bottom_west.width()==80 and index!=5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.lab_tab.setText("Bug")
                #self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=4:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.lab_tab.setText("About > Bug")
                #self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_android':
            if self.ui.frame_bottom_west.width()==80  and index!=7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
                self.ui.lab_tab.setText("Android")
                #self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160  and index!=3:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_android)
                self.ui.lab_tab.setText("About > Android")
                #self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
            #APFunction.visualisation_plot(self)
        elif buttonName=='bn_table':
            if self.ui.frame_bottom_west.width()==80 and index!=6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_table)
                self.ui.lab_tab.setText("Table")
                #self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=2:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
                self.ui.lab_tab.setText("About > Table")
                #self.ui.frame_cloud.setStyleSheet("background:rgb(255,255,255)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        #ADD ANOTHER ELIF STATEMENT HERE FOR EXECTUITING A NEW MENU BUTTON STACK PAGE.
    ########################################################################################################################


    #----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFOMR THE TASK IN THE STACKED WIDGET PAGE 
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def stackPage(self):

        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME
        #self.ui.lab_home_main_hed.setText("Profile")
        #self.ui.lab_home_stat_hed.setText("Stat")
        self.ui.overview_dataset.clicked.connect(lambda: APFunction.readfile(self, 0))
        self.ui.overview_model.clicked.connect(lambda: APFunction.readfile(self, 2))
        self.ui.dataname.currentIndexChanged.connect(lambda: APFunction.overview_plot(self))
        self.ui.rownumber.currentIndexChanged.connect(lambda: APFunction.overview_plot(self))
        self.ui.overview_predict.clicked.connect(lambda: APFunction.predictdata(self))
        ######### PAGE_BUG ############## 
        self.ui.analyst_traindata.clicked.connect(lambda: APFunction.readfile(self,1))
        self.ui.analyst_train.clicked.connect(lambda: APFunction.trainmodel(self))
        self.ui.analyst_save.clicked.connect(lambda: APFunction.savemodel(self))
        
        # THIS CALLS A SIMPLE FUNCTION LOOPS THROW THE NUMBER FORWARDED BY THE COMBOBOX 'comboBox_bug' AND DISPLAY IN PROGRESS BAR
        #ALONGWITH MOVING THE PROGRESS CHUNK FROM 0 TO 100%

        #########PAGE Table #############
        self.ui.table_delete.clicked.connect(lambda: APFunction.table_change(self))
        self.ui.table_search.clicked.connect(lambda: APFunction.table_search(self))
        #########PAGE ANDROID############
    
        ##########PAGE: ABOUT HOME #############
        #self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        #self.ui.text_about_home.setText('HI')
    
    #->Save history
    def savehistory(self):
        np.save("history.npy",self.history)
    ################################################################################################################################

    
#------> CLASS WHERE ALL THE ACTION OF TH SOFTWARE IS PERFORMED:
# THIS CLASS IS WHERE THE APPLICATION OF THE UI OR THE BRAINOF THE SOFTWARE GOES
# UNTILL NOW WE SEPCIFIED THE BUTTON CLICKS, SLIDERS, E.T.C WIDGET, WHOSE APPLICATION IS EXPLORED HERE. THOSE FUNCTION WHEN DONE IS 
# REDIRECTED TO THIS AREA FOR THE PROCESSING AND THEN THE RESULT ARE EXPOTED.
#REMEMBER THE SOFTWARE UI HAS A FUNCTION WHOSE CODE SHOULD BE HERE    
class APFunction():

    def readfile(self,mode):
        if mode==0:
            FileDialog = QFileDialog(self)
            FileDirectory = FileDialog.getExistingDirectory(self, "Dataset")
            allpath=os.listdir(FileDirectory)
            self.data={}
            self.ui.dataname.clear()
            for i in allpath:
                path=os.path.join(FileDirectory,i)
                self.data[i.split('.')[0]]=np.loadtxt(path,delimiter=',')
                self.ui.dataname.addItem(i.split('.')[0])
            
        elif mode==1:
            self.ui.textBrowser.append('----------')
            self.ui.textBrowser.append('Loading Train Data')
            FileDialog = QFileDialog(self)
            FileDirectory = FileDialog.getExistingDirectory(self, "Train Dataset")
            allpath=os.listdir(FileDirectory)
            self.traindata={}
            self.ui.analyst_trainname.clear()
            for i in allpath:
                self.ui.textBrowser.append('Load:'+i)
                path=os.path.join(FileDirectory,i)
                self.traindata[i.split('.')[0]]=np.loadtxt(path,delimiter=',')
                self.ui.analyst_trainname.addItem(i.split('.')[0])
            self.ui.textBrowser.append('Successful')
        elif mode==2:
            FileDialog = QFileDialog(self)
            filepath, _  = QFileDialog.getOpenFileName(self, "Model")
            with open(filepath,'rb') as f:
                self.model=pickle.load(f)
            self.ui.modelname.clear()
            for i in self.model.keys():
                self.ui.modelname.addItem(i)

    def overview_plot(self):
        name=self.ui.dataname.currentText()
        if name!='':
            rownumber=self.ui.rownumber.currentIndex()
            ydata=self.data[name]
            ydata=ydata[rownumber,:]
            self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphviews.width() / 101,height=self.ui.graphviews.height() / 101)
            xdata=np.array(range(len(ydata)))

            self.gv_visual_data_content.axes.plot(xdata, ydata)
            self.gv_visual_data_content.axes.set_title(name+':'+str(rownumber))
            # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
            self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
            self.graphic_scene.addWidget(self.gv_visual_data_content)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
            self.ui.graphviews.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
            self.ui.graphviews.show()

        if name in self.result:
            self.ui.line_home_3.setText(self.result[name][rownumber])

    def trainmodel(self):
        self.model={}
        self.ui.textBrowser.append('----------')
        self.ui.textBrowser.append('Training')
        name=self.ui.analyst_trainname.currentText()
        data=self.traindata[name]
        self.model[name]=OneClassSVM(nu=0.03,gamma='scale').fit(data)
        self.ui.textBrowser.append('Successful')
    
    def savemodel(self):
        self.ui.textBrowser.append('----------')
        self.ui.textBrowser.append('Saving')
        filepath=self.ui.analyst_savepath.text()
        filepath=os.path.abspath(filepath)
        with open(filepath,'wb') as f:
            pickle.dump(self.model,f)
        self.ui.textBrowser.append('Successful')

    def predictdata(self):
        name=self.ui.modelname.currentText()
        rownumber=self.ui.rownumber.currentIndex()
        dataname=self.ui.dataname.currentText()
        result=self.model[name].predict(self.data[name])
        self.result[dataname]=['Normal' if x ==1 else 'Abnormal' for x in result]
        self.ui.line_home_3.setText(self.result[dataname][rownumber])
        count=0
        for i in self.result[dataname]:
            if i =='Abnormal':
                self.ui.eventtable.insertRow(0)
                id=str(self.table_id)
                currentrow=np.array([id,'Warn',dataname,str(count)]).reshape(1,4)
                self.history=np.concatenate((self.history,currentrow),axis=0)
                self.ui.eventtable.setItem(0, 0, QTableWidgetItem(currentrow[0,0]))
                self.ui.eventtable.setItem(0, 1, QTableWidgetItem(currentrow[0,1]))
                self.ui.eventtable.setItem(0, 2, QTableWidgetItem(currentrow[0,2]))
                self.ui.eventtable.setItem(0, 3, QTableWidgetItem(currentrow[0,3]))    
                self.table_id+=1
            count+=1
    
    def table_change(self):
        #self.ui.eventtable.removeRow(self.ui.eventtable.currentRow())
        self.ui.eventtable.setItem(self.ui.eventtable.currentRow(), 1, QTableWidgetItem(self.ui.table_mode.currentText()))
        id=int(self.ui.eventtable.item(self.ui.eventtable.currentRow(),0).text())
        self.history[id,1]='Solved'
    
    def table_search(self):
        self.ui.eventtable.clearContents()
        self.ui.eventtable.setRowCount(0)
        if self.ui.table_line.text().isdigit():
            try:
                currentrow = self.history[int(self.ui.table_line.text()),:]
                self.ui.eventtable.insertRow(0)
                self.ui.eventtable.setItem(0, 0, QTableWidgetItem(currentrow[0]))
                self.ui.eventtable.setItem(0, 1, QTableWidgetItem(currentrow[1]))
                self.ui.eventtable.setItem(0, 2, QTableWidgetItem(currentrow[2]))
                self.ui.eventtable.setItem(0, 3, QTableWidgetItem(currentrow[3]))
            except:
                pass
        else:
            for i in range(len(self.history)-1):
                currentrow = self.history[len(self.history)-1-i,:]
                self.ui.eventtable.insertRow(0)
                self.ui.eventtable.setItem(0, 0, QTableWidgetItem(currentrow[0]))
                self.ui.eventtable.setItem(0, 1, QTableWidgetItem(currentrow[1]))
                self.ui.eventtable.setItem(0, 2, QTableWidgetItem(currentrow[2]))
                self.ui.eventtable.setItem(0, 3, QTableWidgetItem(currentrow[3]))    
                
    def visualisation_plot(self):
        env_start=0
        if len(self.env)>12:
            env_start=len(self.env)-12

        colors = ['lightskyblue','green','magenta','royalblue']
        #self.visual1.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.visual1.axes.clear()
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,1],label=self.env_class[0],color=colors[0])
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,2],label=self.env_class[1],color=colors[1])
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,3],label=self.env_class[2],color=colors[2])
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,4],label=self.env_class[3],color=colors[3])
        self.visual1.axes.set_title('Pollution trend')
        self.visual1.axes.legend(loc='best')
        self.visual1.axes.set_ylim(0,200)
        self.visual1.axes.set_xlim(env_start,env_start+14)
        self.visual1.draw()

        self.visual2.axes.clear()
        self.visual2.axes.pie(self.env[-1,1:],labels=self.env_class,autopct='%1.1f%%',shadow=False,startangle=150,colors=colors)
        self.visual2.axes.set_title('Pollution distribution')
        self.visual2.draw()

        self.visual3.axes.clear()
        self.visual3.axes.set_ylim(0,200)
        self.visual3.axes.set_xlim(env_start,env_start+14)
        self.visual3.axes.bar(x=self.env[env_start:,0],height=self.env[env_start:,1],color=colors[0])
        self.visual3.axes.set_title('O3 plot')
        self.visual3.draw()

        self.visual4.axes.clear()
        self.visual4.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.visual4.axes.set_ylim(0,200)
        self.visual4.axes.set_xlim(env_start,env_start+14)
        self.visual4.axes.plot(self.env[env_start:,0],self.env[env_start:,2],color=colors[1])
        self.visual4.axes.set_title('CO plot')
        self.visual4.axes.fill_between(self.env[env_start:,0],self.env[env_start:,2],0,facecolor=colors[1],alpha=0.5)
        self.visual4.draw()

        nextdata=np.random.randint(-3,3,(1,5))
        nextdata[0,1:]=nextdata[0,1:]+self.env[-1,1:]
        nextdata[0,0]=self.env[-1,0]+1
        self.env = np.vstack((self.env,nextdata))

    def init_plot(self):
        self.visual1 = MyFigureCanvas(width=self.ui.visualisation1.width() / 101,height=self.ui.visualisation1.height() / 101)
        env_start=0
        if len(self.env)>12:
            env_start=len(self.env)-12

        colors = ['lightskyblue','green','magenta','royalblue']
        self.visual1.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,1],label=self.env_class[0],color=colors[0])
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,2],label=self.env_class[1],color=colors[1])
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,3],label=self.env_class[2],color=colors[2])
        self.visual1.axes.plot(self.env[env_start:,0], self.env[env_start:,4],label=self.env_class[3],color=colors[3])
        self.visual1.axes.set_title('Pollution trend')
        self.visual1.axes.legend(loc='best')
        self.visual1.axes.set_ylim(0,200)
        self.visual1.axes.set_xlim(env_start,env_start+14)
        
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.visual1_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.visual1_scene.addWidget(self.visual1)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.visualisation1.setScene(self.visual1_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.visualisation1.show()


        self.visual2 = MyFigureCanvas(width=self.ui.visualisation2.width() / 101,height=self.ui.visualisation2.height() / 101)
        self.visual2.axes.pie(self.env[-1,1:],labels=self.env_class,autopct='%1.1f%%',shadow=False,startangle=150,colors=colors)
        self.visual2.axes.set_title('Pollution distribution')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.visual2_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.visual2_scene.addWidget(self.visual2)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.visualisation2.setScene(self.visual2_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.visualisation2.show()

        self.visual3 = MyFigureCanvas(width=self.ui.visualisation3.width() / 101,height=self.ui.visualisation3.height() / 101)
        self.visual3.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.visual3.axes.set_ylim(0,200)
        self.visual3.axes.set_xlim(env_start,env_start+14)
        self.visual3.axes.bar(x=self.env[env_start:,0],height=self.env[env_start:,1],color=colors[0])
        self.visual3.axes.set_title('O3 plot')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.visual3_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.visual3_scene.addWidget(self.visual3)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.visualisation3.setScene(self.visual3_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.visualisation3.show()

        self.visual4 = MyFigureCanvas(width=self.ui.visualisation3.width() / 101,height=self.ui.visualisation3.height() / 101)
        self.visual4.axes.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.visual4.axes.set_ylim(0,200)
        self.visual4.axes.set_xlim(env_start,env_start+14)
        self.visual4.axes.plot(self.env[env_start:,0],self.env[env_start:,2],color=colors[1])
        self.visual4.axes.set_title('CO plot')
        self.visual4.axes.fill_between(self.env[env_start:,0],self.env[env_start:,2],0,facecolor=colors[1],alpha=0.5)
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.visual4_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.visual4_scene.addWidget(self.visual4)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.visualisation4.setScene(self.visual4_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.visualisation4.show()

        nextdata=np.random.randint(-3,3,(1,5))
        nextdata[0,1:]=nextdata[0,1:]+self.env[-1,1:]
        nextdata[0,0]=self.env[-1,0]+1
        self.env = np.vstack((self.env,nextdata))