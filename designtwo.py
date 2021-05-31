from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_13 = QtWidgets.QFrame(self.frame_2)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_4 = QtWidgets.QFrame(self.frame_13)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setMaximumSize(QtCore.QSize(150, 150))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.frame_9)
        spacerItem = QtWidgets.QSpacerItem(20, 10,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed
                                           )
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.vk_token_textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.vk_token_textEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.vk_token_textEdit.setMaximumSize(QtCore.QSize(200, 40))
        self.vk_token_textEdit.setObjectName("vk_token_textEdit")
        self.horizontalLayout_3.addWidget(self.vk_token_textEdit)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.vk_usr_id_textEdit = QtWidgets.QTextEdit(self.frame_6)
        self.vk_usr_id_textEdit.setMaximumSize(QtCore.QSize(100, 30))
        self.vk_usr_id_textEdit.setObjectName("vk_usr_id_textEdit")
        self.horizontalLayout_4.addWidget(self.vk_usr_id_textEdit)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.vk_album_listWidget = QtWidgets.QListWidget(self.frame_7)
        self.vk_album_listWidget.setMaximumSize(QtCore.QSize(100, 25))
        self.vk_album_listWidget.setObjectName("vk_album_listWidget")
        item = QtWidgets.QListWidgetItem()
        self.vk_album_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vk_album_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vk_album_listWidget.addItem(item)
        self.horizontalLayout_5.addWidget(self.vk_album_listWidget)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_6.addWidget(self.checkBox)
        self.spinBox = QtWidgets.QSpinBox(self.frame_8)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(5)
        self.spinBox.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.horizontalLayout_12.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_13)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(20, 5,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed
                                            )
        self.verticalLayout_7.addItem(spacerItem1)
        self.frame_17 = QtWidgets.QFrame(self.frame_10)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.frame_17)
        self.label_6.setMaximumSize(QtCore.QSize(180, 150))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_7.addWidget(self.frame_17)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.yd_token_textEdit = QtWidgets.QTextEdit(self.frame_11)
        self.yd_token_textEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.yd_token_textEdit.setMaximumSize(QtCore.QSize(200, 40))
        self.yd_token_textEdit.setObjectName("yd_token_textEdit")
        self.horizontalLayout_10.addWidget(self.yd_token_textEdit)
        self.verticalLayout_3.addWidget(self.frame_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed
                                            )
        self.verticalLayout_3.addItem(spacerItem2)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_12)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.yd_path_textEdit = QtWidgets.QTextEdit(self.frame_12)
        self.yd_path_textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.yd_path_textEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.yd_path_textEdit.setObjectName("yd_path_textEdit")
        self.horizontalLayout_11.addWidget(self.yd_path_textEdit)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.horizontalLayout_12.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_2)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_pushButton = QtWidgets.QPushButton(self.frame_15)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout.addWidget(self.start_pushButton)
        self.progressBar = QtWidgets.QProgressBar(self.frame_15)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout_4.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_16)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.verticalLayout_4.addWidget(self.frame_16)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "VKgrabber95 v02a2921"
                                             )
                                  )
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p>\
                     <img src=\"pic/vk_logo_min.png\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Token"))
        self.label_2.setText(_translate("MainWindow", "User id"))
        self.label_3.setText(_translate("MainWindow", "Album"))
        __sortingEnabled = self.vk_album_listWidget.isSortingEnabled()
        self.vk_album_listWidget.setSortingEnabled(False)
        item = self.vk_album_listWidget.item(0)
        item.setText(_translate("MainWindow", "profile"))
        item = self.vk_album_listWidget.item(1)
        item.setText(_translate("MainWindow", "wall"))
        item = self.vk_album_listWidget.item(2)
        item.setText(_translate("MainWindow", "saved"))
        self.vk_album_listWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(_translate("MainWindow", "Number of photo"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p>\
                     <img src=\"pic/yd_logo_min.png\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Token"))
        self.label_8.setText(_translate("MainWindow", "Path"))
        self.start_pushButton.setText(_translate("MainWindow", "Start"))
        self.label_9.setText(_translate("MainWindow", "ready"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
