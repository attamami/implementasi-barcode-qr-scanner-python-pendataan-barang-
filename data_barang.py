# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

#Created By M. Badrut Tamam , Annas Subagyo , Rezha Setyo A. , M. Fadilla Ilham

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
class Ui_MainWindow(object):
    def koneksi(self):
        con = pymysql.connect(db='barang_daspro', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("Koneksi", "Berhasil Terhubung ke Database")
        else:
            self.messagebox("Koneksi", "Gagal Terhubung ke Database")
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def create(self):
        idb = self.plainTextEdit.toPlainText()
        jumlahb = self.plainTextEdit_2.toPlainText()
        hargab = self.plainTextEdit_3.toPlainText()
        merekb = self.plainTextEdit_4.toPlainText()
        jenisb = self.plainTextEdit_5.toPlainText()
        insert = (idb, jumlahb, hargab, merekb, jenisb)
        print(idb)
        print(jumlahb)
        print(hargab)
        print(merekb)
        print(jenisb)
        con = pymysql.connect(db='barang_daspro', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "INSERT INTO barang_daspro(id, jumlah_barang, harga, merek, jenis_barang)" + "VALUES"+str(insert)
        data = cur.execute(sql)
        self.listWidget.addItem(idb)
        self.listWidget_2.addItem(jumlahb)
        self.listWidget_3.addItem(hargab)
        self.listWidget_4.addItem(merekb)
        self.listWidget_5.addItem(jenisb)		
		
        if(data):
            self.messagebox("BERHASIL", "Data Tersimpan")
        else:
            self.messagebox("GAGAL", "Data Tidak Tersimpan")
    def check(self):
        id = self.plainTextEdit.toPlainText()
        db = pymysql.connect(db='barang_daspro', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM barang_daspro WHERE id='"+str(id)+"'")
        data = cursor.fetchall()
        if (data):
            for tp in data:
                self.plainTextEdit.setPlainText("" + tp[0])
                self.plainTextEdit_2.setPlainText("" + tp[1])
                self.plainTextEdit_3.setPlainText("" + tp[2])
                self.plainTextEdit_4.setPlainText("" + tp[3])
                self.plainTextEdit_5.setPlainText("" + tp[4])
                self.messagebox("INFO","Data Tersedia")
        else:
            self.messagebox("INFO", "Data Tidak Tersedia")
    def delete(self):
        id = self.plainTextEdit.toPlainText()
        con = pymysql.connect(db='barang_daspro', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "DELETE FROM barang_daspro where id=%s"
        data = cur.execute(sql, (id))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_3.setPlainText("")
        self.plainTextEdit_4.setPlainText("")
        self.plainTextEdit_5.setPlainText("")
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.listWidget_5.clear()
        if (data):
            self.messagebox("BERHASIL", "Data Terhapus")
        else:
            self.messagebox("GAGAL", "Data Tidak Terhapus")
    def scan(self):
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
		
            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key == ord ("q"):
                break
		
        self.plainTextEdit.setPlainText(str(obj.data))
        print("")
        print("Type : ", obj.type)
        print("Data : ", obj.data)
        print("")

    def setupUi(self, MainWindow):
        self.koneksi()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(234, 255, 210);")
        self.centralwidget.setObjectName("centralwidget")
		
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 105, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 310, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
		
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(210, 100, 301, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(210, 150, 301, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(210, 200, 301, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(210, 250, 301, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(210, 300, 301, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_5.setStyleSheet("background-color: rgb(255, 255, 255); ")
		
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 350, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: rgb(209, 255, 134); ")
        self.pushButton_2.clicked.connect(self.scan)
		
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 350, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: rgb(209, 255, 134); ")
        self.pushButton_3.clicked.connect(self.create)
		
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 350, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color: rgb(209, 255, 134); ")
        self.pushButton_4.clicked.connect(self.check)
		
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 350, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(209, 255, 134); ")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.delete)
		
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(512, 110, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(512, 160, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(512, 210, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(512, 260, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(512, 310, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
		
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(520, 100, 141, 31))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(520, 150, 141, 31))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(520, 200, 141, 31))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(520, 250, 141, 31))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_4.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(520, 300, 141, 31))
        self.listWidget_5.setObjectName("listWidget_5")
        self.listWidget_5.setStyleSheet("background-color: rgb(255, 255, 255); ")
		
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistem Pengelolaan Barang"))
        self.label.setText(_translate("MainWindow", "Sistem Pengelolaan Barang"))
        self.label_2.setText(_translate("MainWindow", "ID (tanpa petik)"))
        self.label_3.setText(_translate("MainWindow", "Jumlah"))
        self.label_4.setText(_translate("MainWindow", "Harga"))
        self.label_5.setText(_translate("MainWindow", "Merek"))
        self.label_6.setText(_translate("MainWindow", "Jenis Barang"))
        self.pushButton_2.setText(_translate("MainWindow", "Masukan Barcode"))
        self.pushButton_3.setText(_translate("MainWindow", "Tambah Barang"))
        self.pushButton_4.setText(_translate("MainWindow", "Cek Barang"))
        self.pushButton_5.setText(_translate("MainWindow", "Hapus Barang"))
        self.label_7.setText(_translate("MainWindow", ":"))
        self.label_8.setText(_translate("MainWindow", ":"))
        self.label_9.setText(_translate("MainWindow", ":"))
        self.label_10.setText(_translate("MainWindow", ":"))
        self.label_11.setText(_translate("MainWindow", ":"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
