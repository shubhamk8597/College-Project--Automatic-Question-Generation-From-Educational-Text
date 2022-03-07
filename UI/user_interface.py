
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtGui
import sys
import pandas as pd
import ast
import random

true_false_df = pd.read_excel('true_false.xlsx')
true_false_df = true_false_df.reset_index(drop = True)
w = 0

class true_or_false_window(object):

    def exporting(self):
        true_false_df.to_excel(r'true_false_edited.xlsx', index = False)

    def previous_question(self):
        try:
            global w 
            global true_false_df
            w = w - 1           
            b = true_false_df[0][w]
            c = true_false_df[1][w]
            self.textBrowser.setText(b.capitalize())
            self.texteditor.setText(c)
            options = self.texteditor.toPlainText()
            print(options)
            options = self.texteditor.toPlainText()   
            length = len(true_false_df)
            print(w, length)    
            if w < 0:
                self.textBrowser.setText('No previous Questions')
                self.exporting()
        except:
            self.textBrowser.setText('No previous Questions')
            self.texteditor.setText('No previous Questions')
            self.exporting()

    def different_sentence(self):
        try:
            global w 
            global true_false_df
            i = 0
            for i in range(len(true_false_df)):
                if true_false_df[0][w] == true_false_df[0][w + 1]:
                    true_false_df.drop(true_false_df.index[w], inplace=True)
                    true_false_df = true_false_df.reset_index(drop = True)
                else:
                    true_false_df.drop(true_false_df.index[w], inplace=True)
                    true_false_df = true_false_df.reset_index(drop = True)
                    break
                i = i + 1         
            b = true_false_df[0][w]
            c = true_false_df[1][w]
            self.textBrowser.setText(b.capitalize())
            self.texteditor.setText(c)
            options = self.texteditor.toPlainText()
            print(options)
            options = self.texteditor.toPlainText() 
            length = len(true_false_df)
            print(a, length)    
            if w > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except:
            self.textBrowser.setText('End of List! No More Questions')
            self.exporting()

    def saving(self):
        try:
            global w 
            global true_false_df
            w = w + 1           
            b = true_false_df[0][w]
            c = true_false_df[1][w]
            self.textBrowser.setText(b.capitalize())
            self.texteditor.setText(c)
            options = self.texteditor.toPlainText()
            print(options)
            options = self.texteditor.toPlainText() 
            length = len(true_false_df)
            print(w, length)    
            if w > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except:
            self.textBrowser.setText('End of List! No More Questions')
            self.exporting()

    def deleteit1(self):
        try:
            global w 
            global true_false_df
            
            length = len(true_false_df)
            print(a, length)
            true_false_df.drop(true_false_df.index[w], inplace=True)
            true_false_df = true_false_df.reset_index(drop = True)
            b = true_false_df[0][w]
            c = true_false_df[1][w]
            self.textBrowser.setText(b.capitalize())

            self.texteditor.setText(c)
            options = self.texteditor.toPlainText()
            print(options)
            if w > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except:
            self.textBrowser.setText('End of List! No More Questions')
            self.exporting()

    def setupUi(self, MainWindow):
        global w 
        global true_false_df
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel1 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel1.setGeometry(QtCore.QRect(50, 25 , 500, 25))
        self.textlabel1.setObjectName("textlabel1")
        self.textlabel1.setText("TRUE SENTENCE")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 700, 100))
        self.textBrowser.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(true_false_df[0][w])

        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(50, 175, 500, 25))
        self.textlabel.setObjectName("textlabel")
        self.textlabel.setText("FALSE SENTENCE(Editable)")

        self.texteditor = QtWidgets.QTextEdit(self.centralwidget)
        self.texteditor.setGeometry(QtCore.QRect(50, 200, 700, 100))
        self.texteditor.setObjectName("texteditor")
        self.texteditor.setText(true_false_df[1][w])

        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(50, 325, 250, 35))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.deleteit1)

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(325, 325, 250, 35))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saving)

        self.next_sentence = QtWidgets.QPushButton(self.centralwidget)
        self.next_sentence.setGeometry(QtCore.QRect(325, 400, 250, 35))
        self.next_sentence.setObjectName("next_sentence")
        self.next_sentence.clicked.connect(self.different_sentence)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 400, 250, 35))
        self.back.setObjectName("save")
        self.back.clicked.connect(self.previous_question) 

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "True or False Teacher"))      
        self.delete_2.setText(_translate("MainWindow", "DELETE AND NEXT SENTENCE")) 
        self.save.setText(_translate("MainWindow", "SAVE AND NEXT"))  
        self.back.setText(_translate("MainWindow", "PREVIOUS SENTENCE"))
        self.next_sentence.setText(_translate("MainWindow", "DELETE AND NEXT QUESTION"))

mcq_question_options = pd.read_excel('mcq_.xlsx')
mcq_question_options = mcq_question_options.reset_index(drop = True)
a = 0


class mcq_window(object):
    
    def exporting(self):
        mcq_question_options.to_excel(r'mcq_edited.xlsx', index = False)
        mcq_question_options.to_excel(r'mtc_edited.xlsx', index = False)

    def previous_question(self):
        try:
            global a 
            global true_false_df    
            a = a - 1       
            b = mcq_question_options['Fill and Column'][a]
            c = mcq_question_options['Keywords'][a]
            x = mcq_question_options['Options'][a]
            self.textBrowser.setText("\n\n"+b.capitalize() +"\n\nAnswer -" +c.capitalize())
            if type(x) is list:
                pass
            else:
                x = ast.literal_eval(x)
            options1 = ""
            for i in x: 
                options1 = options1 + i + " " 
            self.texteditor.setText(options1)
            options = self.texteditor.toPlainText()
            print(options)
            options = self.texteditor.toPlainText()
            options = self.texteditor.toPlainText()   
            length = len(mcq_question_options)
            print(a, length)    
            if a < 0:
                self.textBrowser.setText('No previous Questions')
                self.exporting()
        except:
            self.textBrowser.setText('No previous Questions')
            self.texteditor.setText('No previous Questions')
            self.exporting()

    def saving(self):
        try:
            global a 
            global mcq_question_options
            a = a + 1   
            b = mcq_question_options['Fill and Column'][a]
            c = mcq_question_options['Keywords'][a]
            x = mcq_question_options['Options'][a]

            self.textBrowser.setText("\n\n"+b.capitalize() +"\n\nAnswer -" +c.capitalize())
            if type(x) is list:
                pass
            else:
                x = ast.literal_eval(x)
            options1 = ""
            for i in x: 
                options1 = options1 + i + " " 
            self.texteditor.setText(options1)
            options = self.texteditor.toPlainText()
            print(options)
            options = self.texteditor.toPlainText()
            print(options)
            options = options.split(" ")
            options = options[:-1]
            mcq_question_options['Options'][a] = options  
            length = len(mcq_question_options)
            print(a, length)
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except Exception as ex:
            print(mcq_question_options['Options'][a])
            self.textBrowser.setText('End of List! No More Questions' + str(ex))
            self.exporting()

    def deleteit1(self):
        try:
            global a 
            global mcq_question_options
            mcq_question_options.drop(mcq_question_options.index[a], inplace=True)
            mcq_question_options = mcq_question_options.reset_index(drop = True)
            b = mcq_question_options['Fill and Column'][a]
            c = mcq_question_options['Keywords'][a]
            x = mcq_question_options['Options'][a]
            self.textBrowser.setText("\n\n"+b.capitalize() +"\n\nAnswer -" +c.capitalize())
            x = ast.literal_eval(x)
            options1 = ""
            for i in x:
                options1 = options1 + i + ' '
            self.texteditor.setText(options1)
            options = self.texteditor.toPlainText()
            print(options)
            length = len(mcq_question_options)
            print(a, length)
            
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except:
            self.textBrowser.setText('End of List! No More Questions')
            self.exporting()

    def setupUi(self, MainWindow):

        global a 
        global mcq_question_options
        b = mcq_question_options['Fill and Column'][a]
        c = mcq_question_options['Keywords'][a]
        x = mcq_question_options['Options'][a]
        x = ast.literal_eval(x)
        options1 = ""
        for i in x:
            options1 = options1 + i + ' '
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel1 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel1.setGeometry(QtCore.QRect(50, 25 , 500, 25))
        self.textlabel1.setObjectName("textlabel1")
        self.textlabel1.setText("Questions")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 700, 150))
        self.textBrowser.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("\n\n"+b.capitalize() +"\n\nAnswer -" +c.capitalize())

        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(50, 225, 500, 25))
        self.textlabel.setObjectName("textlabel")
        self.textlabel.setText("EDIT or ADD options below.Seperate by space")

        self.texteditor = QtWidgets.QTextEdit(self.centralwidget)
        self.texteditor.setGeometry(QtCore.QRect(50, 250, 700, 30))
        self.texteditor.setObjectName("texteditor")
        self.texteditor.setText(options1)

        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(50, 375, 250, 35))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.deleteit1)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 325, 250, 35))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.previous_question) 

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(325, 325, 250, 35))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saving)   

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCQ Teacher"))     
        self.delete_2.setText(_translate("MainWindow", "DELETE QUESTION")) 
        self.back.setText(_translate("MainWindow", "PREVIOUS QUESTION"))
        self.save.setText(_translate("MainWindow", "SAVE and NEXT"))

class question_type(object):

    def open_mcq_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =mcq_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def true_or_false_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = true_or_false_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(325, 100, 500, 50))
        self.textlabel.setObjectName("textlabel")
        self.textlabel.setText("Choose Question Type")

        self.true_or_false = QtWidgets.QPushButton(self.centralwidget)
        self.true_or_false.setGeometry(QtCore.QRect(225, 200, 150, 100))
        self.true_or_false.setObjectName("true_or_false")
        self.true_or_false.clicked.connect(self.true_or_false_window)

        self.mcq = QtWidgets.QPushButton(self.centralwidget)
        self.mcq.setGeometry(QtCore.QRect(425, 200, 150, 100))
        self.mcq.setObjectName("mcq")
        self.mcq.clicked.connect(self.open_mcq_window)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Type"))     
        self.mcq.setText(_translate("MainWindow", "MCQ")) 
        self.true_or_false.setText(_translate("MainWindow", "TREUE FALSE"))

mcq_answer = pd.read_excel('mcq_edited.xlsx')
mcq_answer = mcq_answer.reset_index(drop = True)
m = 0

mtc_answer = pd.read_excel('mtc_edited.xlsx')
mtc_answer = mtc_answer.reset_index(drop = True)
y = 0

true_false_answers = pd.read_excel('true_false_edited.xlsx')
true_false_answers = true_false_answers.reset_index(drop = True)
z = 0

class student_question_type(object):

    def open_mcq_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =student_mcq_window()
        self.ui.setupUi(self.window)
        global mcq_answer
        for z in range(len(mcq_answer)):
            options = mcq_answer['Options'][z]
            if type(options) is list:
                pass
            else:
                options = ast.literal_eval(options)
            keyword = mcq_answer['Keywords'][z]
            options.append(keyword)
            random.shuffle(options)
            mcq_answer['Options'][z] = options
        print(mcq_answer)
        mcq_answer = pd.concat([mcq_answer[:1],mcq_answer[1:].sample(frac=1)]).reset_index(drop=True)
        print(mcq_answer)
        self.window.show()

    def open_mct_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = student_match_the_column_window()
        self.ui.setupUi(self.window)
        global mtc_answer
        
        print(mtc_answer)
        mtc_answer = pd.concat([mtc_answer[:4],mtc_answer[4:].sample(frac=1)]).reset_index(drop=True)
        print(mtc_answer)
        self.window.show()
        
    def true_or_false_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = student_true_or_false_window()
        self.ui.setupUi(self.window)
        global true_false_answers
        print(true_false_answers)
        true_df = pd.DataFrame()
        true_df['Questions'] = true_false_answers[0]
        true_df['Answers'] = 'True'
        true_df['True_Sentence'] = true_df['Questions']
        false_df = pd.DataFrame()
        false_df['Questions'] = true_false_answers[1]
        false_df['Answers'] = 'False'
        print(false_df)
        false_df['True_Sentence'] = true_df['Questions']
        true_false_answers = pd.concat([true_df,false_df]) 
        true_false_answers = true_false_answers.reset_index(drop=True)
        true_false_answers = true_false_answers.drop_duplicates(subset=['Questions','Answers'],keep='first')
        true_false_answers = true_false_answers.reset_index(drop=True)
        true_false_answers = pd.concat([true_false_answers[:1],true_false_answers[1:].sample(frac=1)]).reset_index(drop=True)
        print(true_false_answers)
        self.window.show()

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(325, 100, 500, 50))
        self.textlabel.setObjectName("textlabel")
        self.textlabel.setText("Choose Question Type")

        self.true_or_false = QtWidgets.QPushButton(self.centralwidget)
        self.true_or_false.setGeometry(QtCore.QRect(125, 200, 150, 100))
        self.true_or_false.setObjectName("true_or_false")
        self.true_or_false.clicked.connect(self.true_or_false_window)

        self.mcq = QtWidgets.QPushButton(self.centralwidget)
        self.mcq.setGeometry(QtCore.QRect(325, 200, 150, 100))
        self.mcq.setObjectName("mcq")
        self.mcq.clicked.connect(self.open_mcq_window)

        self.match_column = QtWidgets.QPushButton(self.centralwidget)
        self.match_column.setGeometry(QtCore.QRect(525, 200, 150, 100))
        self.match_column.setObjectName("match_column")
        self.match_column.clicked.connect(self.open_mct_window)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Question Types"))    
        self.mcq.setText(_translate("MainWindow", "MCQ"))
        self.true_or_false.setText(_translate("MainWindow", "TREUE FALSE"))
        self.match_column.setText(_translate("MainWindow", "MATCH COLUMNS"))

class student_true_or_false_window(object):

    def exporting(self):
        global true_false_answers
        true_false_answers.to_excel(r'true_false_edited.xlsx', index = False)
   
    def showing_answer(self):
        global z
        global true_false_answers
        c = true_false_answers['Answers'][z]
        d = true_false_answers['True_Sentence'][z]
        self.texteditor.setText(c.capitalize() +"\n\n" + d)

    def previous_question(self):
        try:
            global z
            global true_false_answers    
            z = z - 1       
            b = true_false_answers['Questions'][z]
            self.textBrowser.setText("\n\n" + b)
            self.texteditor.setText("")
            length = len(true_false_answers)
            print(m, length)    
            if m < 0:
                self.textBrowser.setText('No previous Questions')
                self.exporting()
        except:
            self.textBrowser.setText('No previous Questions')
            self.texteditor.setText('No previous Questions')
            self.exporting()

    def saving(self):
        try:
            global z 
            global true_false_answers
            z = z + 1   
            b = true_false_answers['Questions'][z]
            self.textBrowser.setText("\n\n" + b)
            self.texteditor.setText("")
            length = len(true_false_answers)
            print(z, length)
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except Exception as ex:
            print(true_false_answers['Options'][z])
            self.textBrowser.setText('End of List! No More Questions' + str(ex))
            self.exporting()

    def deleteit1(self):
        try:
            global z 
            global true_false_answers
            true_false_answers.drop(true_false_answers.index[z], inplace=True)
            true_false_answers = true_false_answers.reset_index(drop = True)
            b = true_false_answers['Questions'][z]
            self.textBrowser.setText("\n\n" + b)
            self.texteditor.setText("")
            length = len(true_false_answers)
            print(a, length)
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except:
            self.textBrowser.setText('End of List! No More Questions')
            self.exporting()

    def setupUi(self, MainWindow):

        global z
        global true_false_answers
        b = true_false_answers[0][z]
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel1 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel1.setGeometry(QtCore.QRect(50, 25 , 500, 25))
        self.textlabel1.setObjectName("textlabel1")
        self.textlabel1.setText("Is the Sentence True or False?")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 700, 150))
        self.textBrowser.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("\n\n" + b)

        self.show_answer = QtWidgets.QPushButton(self.centralwidget)
        self.show_answer.setGeometry(QtCore.QRect(50, 220, 250, 35))
        self.show_answer.setObjectName("show_answer")
        self.show_answer.clicked.connect(self.showing_answer)

        self.texteditor = QtWidgets.QTextEdit(self.centralwidget)
        self.texteditor.setGeometry(QtCore.QRect(50, 250, 700, 100))
        self.texteditor.setObjectName("texteditor")
        self.texteditor.setText("")

        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(50, 375, 250, 35))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.deleteit1)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 425, 250, 35))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.previous_question) 

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(325, 375, 250, 35))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saving)   

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "True or False Student"))     
        self.delete_2.setText(_translate("MainWindow", "CORRECT AND NEXT")) 
        self.back.setText(_translate("MainWindow", "PREVIOUS WRONG QUESTION"))
        self.save.setText(_translate("MainWindow", "WRONG and NEXT"))
        self.show_answer.setText(_translate("MainWindow", "SHOW ANSWER"))                    

class student_match_the_column_window(object):

    def exporting(self):
        global mtc_answer
        mtc_answer.to_excel(r'mtc_edited.xlsx', index = False)
   
    def showing_answer(self):
        global y
        global mtc_answer
        self.textBrowser4.setText(mtc_answer['Keywords'][y - 4])
        self.textBrowser5.setText(mtc_answer['Keywords'][y - 3])
        self.textBrowser6.setText(mtc_answer['Keywords'][y - 2])
        self.textBrowser7.setText(mtc_answer['Keywords'][y - 1])

    def previous_question(self):
        try:
            global y 
            global mtc_answer
            y = y - 8
            print(y)
            one = mtc_answer['Fill and Column'][y]
            one1 = mtc_answer['Keywords'][y]
            y = y + 1
            two = mtc_answer['Fill and Column'][y]
            two1 = mtc_answer['Keywords'][y]
            y = y + 1
            three = mtc_answer['Fill and Column'][y]
            three1 = mtc_answer['Keywords'][y]
            y = y + 1
            four= mtc_answer['Fill and Column'][y]
            four1 = mtc_answer['Keywords'][y]
            y = y + 1
            keyword_list = [one1,two1,three1,four1]
            random.shuffle(keyword_list)
            self.textBrowser.setText(one)
            self.textBrowser1.setText(two)
            self.textBrowser2.setText(three)
            self.textBrowser3.setText(four)
            self.textBrowser4.setText(keyword_list[0])
            self.textBrowser5.setText(keyword_list[1])
            self.textBrowser6.setText(keyword_list[2])
            self.textBrowser7.setText(keyword_list[3])
            length = len(true_false_answers)
            print(y, length)    
            if m < 0:
                self.textBrowser.setText('No previous Questions')
                self.exporting()
        except:
            self.textBrowser.setText('No previous Questions')
            self.exporting()

    def saving(self):
        try:
            global y 
            global mtc_answer
            one = mtc_answer['Fill and Column'][y]
            one1 = mtc_answer['Keywords'][y]
            y = y + 1
            two = mtc_answer['Fill and Column'][y]
            two1 = mtc_answer['Keywords'][y]
            y = y + 1
            three = mtc_answer['Fill and Column'][y]
            three1 = mtc_answer['Keywords'][y]
            y = y + 1

            four= mtc_answer['Fill and Column'][y]
            four1 = mtc_answer['Keywords'][y]
            y = y + 1

            keyword_list = [one1,two1,three1,four1]
            random.shuffle(keyword_list)
            self.textBrowser.setText(one)
            self.textBrowser1.setText(two)
            self.textBrowser2.setText(three)
            self.textBrowser3.setText(four)
            self.textBrowser4.setText(keyword_list[0])
            self.textBrowser5.setText(keyword_list[1])
            self.textBrowser6.setText(keyword_list[2])
            self.textBrowser7.setText(keyword_list[3])
            length = len(true_false_answers)
            print(y, length)
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except Exception as ex:
            self.textBrowser.setText('End of List! No More Questions' + str(ex))
            self.exporting()


    def setupUi(self, MainWindow):

        global y 
        global mtc_answer
        one = mtc_answer['Fill and Column'][y]
        one1 = mtc_answer['Keywords'][y]
        y = y + 1
        two = mtc_answer['Fill and Column'][y]
        two1 = mtc_answer['Keywords'][y]
        y = y + 1
        three = mtc_answer['Fill and Column'][y]
        three1 = mtc_answer['Keywords'][y]
        y = y + 1
        four= mtc_answer['Fill and Column'][y]
        four1 = mtc_answer['Keywords'][y]
        y = y + 1
        print(y)
        
        keyword_list = [one1,two1,three1,four1]
        random.shuffle(keyword_list)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel1 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel1.setGeometry(QtCore.QRect(50, 25 , 500, 25))
        self.textlabel1.setObjectName("textlabel1")
        self.textlabel1.setText("Match the Correct Keyword to Correct Sentence")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 75, 500, 75))
        self.textBrowser.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(one)

        self.textBrowser1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser1.setGeometry(QtCore.QRect(50, 150, 500, 75))
        self.textBrowser1.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser1.setObjectName("textBrowser1")
        self.textBrowser1.setText(two)

        self.textBrowser2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser2.setGeometry(QtCore.QRect(50, 225, 500, 75))
        self.textBrowser2.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser2.setObjectName("textBrowser")
        self.textBrowser2.setText(three)

        self.textBrowser3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser3.setGeometry(QtCore.QRect(50, 300, 500, 75))
        self.textBrowser3.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser3.setObjectName("textBrowser3")
        self.textBrowser3.setText(four)

        self.textBrowser4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser4.setGeometry(QtCore.QRect(550, 75, 200, 75))
        self.textBrowser4.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser4.setObjectName("textBrowser4")
        self.textBrowser4.setText(keyword_list[0])

        self.textBrowser5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser5.setGeometry(QtCore.QRect(550, 150, 200, 75))
        self.textBrowser5.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser5.setObjectName("textBrowser5")
        self.textBrowser5.setText(keyword_list[1])

        self.textBrowser6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser6.setGeometry(QtCore.QRect(550, 225, 200, 75))
        self.textBrowser6.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser6.setObjectName("textBrowser6")
        self.textBrowser6.setText(keyword_list[2])

        self.textBrowser7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser7.setGeometry(QtCore.QRect(550, 300, 200, 75))
        self.textBrowser7.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser7.setObjectName("textBrowser7")
        self.textBrowser7.setText(keyword_list[3])

        self.show_answer = QtWidgets.QPushButton(self.centralwidget)
        self.show_answer.setGeometry(QtCore.QRect(50, 375, 250, 35))
        self.show_answer.setObjectName("show_answer")
        self.show_answer.clicked.connect(self.showing_answer)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 425, 250, 35))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.previous_question) 

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(325, 425, 250, 35))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saving)   

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Match the Column Student"))     
        self.back.setText(_translate("MainWindow", "PREVIOUS QUESTION"))
        self.save.setText(_translate("MainWindow", "NEXT"))
        self.show_answer.setText(_translate("MainWindow", "SHOW ANSWER"))


class student_mcq_window(object):
    
    def exporting(self):
        mcq_answer.to_excel(r'mcq_edited.xlsx', index = False)

    def showing_answer(self):
        global m
        global mcq_answer
        c = mcq_answer['Keywords'][m]
        self.texteditor.setText(c.capitalize())

    def previous_question(self):
        try:
            global m
            global mcq_answer    
            m = m - 1       
            b = mcq_answer['Fill and Column'][m]
            c = mcq_answer['Keywords'][m]
            x = mcq_answer['Options'][m]
            self.texteditor.setText("")
            if type(x) is list:
                pass
            else:
                x = ast.literal_eval(x)
            options1 = ""
            h = 0
            for i in x:
                h = h + 1
                j = str(h) + ")" 
                options1 = options1 + j + i.capitalize() + " "
                j = "" 
            self.textBrowser.setText("\n\n"+b.capitalize() +"\n\n" + options1)  
            length = len(mcq_answer)
            print(m, length)    
            if m < 0:
                self.textBrowser.setText('No previous Questions')
                self.exporting()
        except:
            self.textBrowser.setText('No previous Questions')
            self.texteditor.setText('No previous Questions')
            self.exporting()

    def saving(self):
        try:
            global m 
            global mcq_answer
            m = m + 1   
            b = mcq_answer['Fill and Column'][m]
            c = mcq_answer['Keywords'][m]
            x = mcq_answer['Options'][m]
            self.texteditor.setText("")
            if type(x) is list:
                pass
            else:
                x = ast.literal_eval(x)
            options1 = ""
            h = 0
            for i in x:
                h = h + 1
                j = str(h) + ")" 
                options1 = options1 + j + i.capitalize() + " "
                j = "" 
            self.textBrowser.setText("\n\n"+b.capitalize() +"\n\n" + options1)
            length = len(mcq_answer)
            print(m, length)
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except Exception as ex:
            print(mcq_answer['Options'][m])
            self.textBrowser.setText('End of List! No More Questions' + str(ex))
            self.exporting()

    def deleteit1(self):
        try:
            global m 
            global mcq_answer
            mcq_answer.drop(mcq_answer.index[m], inplace=True)
            mcq_answer = mcq_answer.reset_index(drop = True)
            b = mcq_answer['Fill and Column'][m]
            c = mcq_answer['Keywords'][m]
            x = mcq_answer['Options'][m]
            self.texteditor.setText("")
            if type(x) is list:
                pass
            else:
                x = ast.literal_eval(x)
            options1 = ""
            h = 0
            for i in x:
                h = h + 1
                j = str(h) + ")" 
                options1 = options1 + j + i.capitalize() + " "
                j = "" 
            self.textBrowser.setText("\n\n"+b.capitalize() +"\n\n" + options1)
            length = len(mcq_answer)
            print(a, length)
            if a > length:
                self.textBrowser.setText('End of List! No More Questions')
                self.exporting()
        except:
            self.textBrowser.setText('End of List! No More Questions')
            self.exporting()

    def setupUi(self, MainWindow):

        global m 
        global mcq_answer
        b = mcq_answer['Fill and Column'][m]
        c = mcq_answer['Keywords'][m]
        x = mcq_answer['Options'][m]
        if type(x) is list:
            pass
        else:
            x = ast.literal_eval(x)
        x.append(c)
        options1 = ""
        h = 0
        for i in x:
            h = h + 1
            j = str(h) + ")" 
            options1 = options1 + j + i.capitalize() + " "
            j = ""
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel1 = QtWidgets.QLabel(self.centralwidget)
        self.textlabel1.setGeometry(QtCore.QRect(50, 25 , 500, 25))
        self.textlabel1.setObjectName("textlabel1")
        self.textlabel1.setText("Questions")


        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 700, 150))
        self.textBrowser.setStyleSheet("background:rgb(239,239,239);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("\n\n"+b.capitalize() +"\n\n" + options1)

        self.show_answer = QtWidgets.QPushButton(self.centralwidget)
        self.show_answer.setGeometry(QtCore.QRect(50, 220, 250, 35))
        self.show_answer.setObjectName("show_answer")
        self.show_answer.clicked.connect(self.showing_answer)

        self.texteditor = QtWidgets.QTextEdit(self.centralwidget)
        self.texteditor.setGeometry(QtCore.QRect(50, 250, 700, 30))
        self.texteditor.setObjectName("texteditor")
        self.texteditor.setText("")

        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(50, 325, 250, 35))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.deleteit1)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 375, 250, 35))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.previous_question) 

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(325, 325, 250, 35))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saving)   

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCQ Student"))     
        self.delete_2.setText(_translate("MainWindow", "CORRECT AND NEXT")) 
        self.back.setText(_translate("MainWindow", "PREVIOUS WRONG QUESTION"))
        self.save.setText(_translate("MainWindow", "WRONG and NEXT"))
        self.show_answer.setText(_translate("MainWindow", "SHOW ANSWER"))


class Ui_MainWindow(object):

    def open_question_type_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =question_type()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_student_question_type(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = student_question_type()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600,200,800,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(325, 100, 500, 50))
        self.textlabel.setObjectName("textlabel")
        self.textlabel.setText("CHOOSE YOUR ROLE")

        self.true_or_false = QtWidgets.QPushButton(self.centralwidget)
        self.true_or_false.setGeometry(QtCore.QRect(225, 200, 150, 100))
        self.true_or_false.setObjectName("true_or_false")
        self.true_or_false.clicked.connect(self.open_student_question_type)

        self.teacher = QtWidgets.QPushButton(self.centralwidget)
        self.teacher.setGeometry(QtCore.QRect(425, 200, 150, 100))
        self.teacher.setObjectName("mcq")
        self.teacher.clicked.connect(self.open_question_type_window)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # self.cont = False
            # i = 0
            
            # while(self.cont is not True):
            
            #     self.textBrowser.setText(a)
            #     print( "Waiting for user to push button 2")
            #     QtCore.QCoreApplication.processEvents()
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROLE"))     
        self.teacher.setText(_translate("MainWindow", "Teacher")) 
        self.true_or_false.setText(_translate("MainWindow", "Student"))


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

