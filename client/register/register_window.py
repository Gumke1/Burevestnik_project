# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 477)
        Dialog.setStyleSheet("background-color: rgb(45, 44, 44);\n"
"                color: white;\n"
"            ")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 812, 551))
        self.stackedWidget.setStyleSheet("background-color: rgb(45, 44, 44);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.education_page_3 = QtWidgets.QWidget()
        self.education_page_3.setObjectName("education_page_3")
        self.stackedWidget.addWidget(self.education_page_3)
        self.acc_page_3 = QtWidgets.QWidget()
        self.acc_page_3.setObjectName("acc_page_3")
        self.label_52 = QtWidgets.QLabel(parent=self.acc_page_3)
        self.label_52.setGeometry(QtCore.QRect(0, 0, 271, 271))
        self.label_52.setMinimumSize(QtCore.QSize(40, 40))
        self.label_52.setText("")
        self.label_52.setPixmap(QtGui.QPixmap("\n"
"                            :/res/kisspng-user-profile-2018-in-sight-user-conference-expo-5b554c0968c377.0307553315323166814291-fotor-bg-remover-20241102121640.png\n"
"                        "))
        self.label_52.setScaledContents(True)
        self.label_52.setObjectName("label_52")
        self.layoutWidget_7 = QtWidgets.QWidget(parent=self.acc_page_3)
        self.layoutWidget_7.setGeometry(QtCore.QRect(50, 320, 171, 35))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_53 = QtWidgets.QLabel(parent=self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_27.addWidget(self.label_53)
        self.lineEdit_expirience_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_7)
        self.lineEdit_expirience_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_expirience_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_expirience_reg.setStyleSheet("QLineEdit {\n"
"                                        border: 2px solid white;\n"
"                                        border-radius: 10px;\n"
"                                        color: white;\n"
"\n"
"                                        }\n"
"                                    ")
        self.lineEdit_expirience_reg.setObjectName("lineEdit_expirience_reg")
        self.horizontalLayout_27.addWidget(self.lineEdit_expirience_reg)
        self.layoutWidget_8 = QtWidgets.QWidget(parent=self.acc_page_3)
        self.layoutWidget_8.setGeometry(QtCore.QRect(290, 300, 451, 39))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_59 = QtWidgets.QLabel(parent=self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_28.addWidget(self.label_59)
        self.lineEdit_level_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_8)
        self.lineEdit_level_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_level_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_level_reg.setStyleSheet("QLineEdit {\n"
"                                        border: 2px solid white;\n"
"                                        border-radius: 10px;\n"
"                                        color: white;\n"
"\n"
"                                        }\n"
"                                    ")
        self.lineEdit_level_reg.setObjectName("lineEdit_level_reg")
        self.horizontalLayout_28.addWidget(self.lineEdit_level_reg)
        self.layoutWidget_9 = QtWidgets.QWidget(parent=self.acc_page_3)
        self.layoutWidget_9.setGeometry(QtCore.QRect(290, 10, 451, 289))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_61 = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_32.addWidget(self.label_61)
        self.lineEdit_login_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_login_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_login_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_login_reg.setStyleSheet("QLineEdit {\n"
"                                                border: 2px solid white;\n"
"                                                border-radius: 10px;\n"
"                                                color: white;\n"
"\n"
"                                                }\n"
"                                            ")
        self.lineEdit_login_reg.setObjectName("lineEdit_login_reg")
        self.horizontalLayout_32.addWidget(self.lineEdit_login_reg)
        self.verticalLayout_11.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_63 = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_33.addWidget(self.label_63)
        self.lineEdit_paswword_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_paswword_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_paswword_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_paswword_reg.setStyleSheet("QLineEdit {\n"
"                                                border: 2px solid white;\n"
"                                                border-radius: 10px;\n"
"                                                color: white;\n"
"\n"
"                                                }\n"
"                                            ")
        self.lineEdit_paswword_reg.setObjectName("lineEdit_paswword_reg")
        self.horizontalLayout_33.addWidget(self.lineEdit_paswword_reg)
        self.verticalLayout_11.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_65 = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_34.addWidget(self.label_65)
        self.lineEdit_midlname_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_midlname_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_midlname_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_midlname_reg.setStyleSheet("QLineEdit {\n"
"                                                border: 2px solid white;\n"
"                                                border-radius: 10px;\n"
"                                                color: white;\n"
"\n"
"                                                }\n"
"                                            ")
        self.lineEdit_midlname_reg.setObjectName("lineEdit_midlname_reg")
        self.horizontalLayout_34.addWidget(self.lineEdit_midlname_reg)
        self.verticalLayout_11.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_67 = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_35.addWidget(self.label_67)
        self.lineEdit_secondname_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_secondname_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_secondname_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_secondname_reg.setStyleSheet("QLineEdit {\n"
"                                                border: 2px solid white;\n"
"                                                border-radius: 10px;\n"
"                                                color: white;\n"
"\n"
"                                                }\n"
"                                            ")
        self.lineEdit_secondname_reg.setObjectName("lineEdit_secondname_reg")
        self.horizontalLayout_35.addWidget(self.lineEdit_secondname_reg)
        self.verticalLayout_11.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_69 = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_36.addWidget(self.label_69)
        self.lineEdit_name_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_name_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_name_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_name_reg.setStyleSheet("QLineEdit {\n"
"                                                border: 2px solid white;\n"
"                                                border-radius: 10px;\n"
"                                                color: white;\n"
"\n"
"                                                }\n"
"                                            ")
        self.lineEdit_name_reg.setObjectName("lineEdit_name_reg")
        self.horizontalLayout_36.addWidget(self.lineEdit_name_reg)
        self.verticalLayout_11.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_71 = QtWidgets.QLabel(parent=self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_37.addWidget(self.label_71)
        self.lineEdit_post_reg = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        self.lineEdit_post_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_post_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_post_reg.setStyleSheet("QLineEdit {\n"
"                                                border: 2px solid white;\n"
"                                                border-radius: 10px;\n"
"                                                color: white;\n"
"\n"
"                                                }\n"
"                                            ")
        self.lineEdit_post_reg.setObjectName("lineEdit_post_reg")
        self.horizontalLayout_37.addWidget(self.lineEdit_post_reg)
        self.verticalLayout_11.addLayout(self.horizontalLayout_37)
        self.pushButton_reg_reg = QtWidgets.QPushButton(parent=self.acc_page_3)
        self.pushButton_reg_reg.setGeometry(QtCore.QRect(10, 410, 721, 41))
        self.pushButton_reg_reg.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"                            color: white;\n"
"                            border-radius: 20px;\n"
"                        ")
        self.pushButton_reg_reg.setObjectName("pushButton_reg_reg")
        self.widget = QtWidgets.QWidget(parent=self.acc_page_3)
        self.widget.setGeometry(QtCore.QRect(290, 350, 451, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_55 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout.addWidget(self.label_55)
        self.lineEdit_age_reg = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_age_reg.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_age_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_age_reg.setStyleSheet("QLineEdit {\n"
"                                        border: 2px solid white;\n"
"                                        border-radius: 10px;\n"
"                                        color: white;\n"
"\n"
"                                        }\n"
"                                    ")
        self.lineEdit_age_reg.setObjectName("lineEdit_age_reg")
        self.horizontalLayout.addWidget(self.lineEdit_age_reg)
        self.stackedWidget.addWidget(self.acc_page_3)
        self.order_page_3 = QtWidgets.QWidget()
        self.order_page_3.setObjectName("order_page_3")
        self.lineEdit_id_input_3 = QtWidgets.QLineEdit(parent=self.order_page_3)
        self.lineEdit_id_input_3.setGeometry(QtCore.QRect(30, 50, 261, 30))
        self.lineEdit_id_input_3.setStyleSheet("QLineEdit {\n"
"                            border: 2px solid white;\n"
"                            border-radius: 10px;\n"
"                            color: white;\n"
"\n"
"                            }\n"
"                        ")
        self.lineEdit_id_input_3.setObjectName("lineEdit_id_input_3")
        self.lineEdit_coment_input_3 = QtWidgets.QLineEdit(parent=self.order_page_3)
        self.lineEdit_coment_input_3.setGeometry(QtCore.QRect(30, 120, 761, 201))
        self.lineEdit_coment_input_3.setStyleSheet("QLineEdit {\n"
"                            border: 2px solid white;\n"
"                            border-radius: 10px;\n"
"                            color: white;\n"
"\n"
"                            }\n"
"                        ")
        self.lineEdit_coment_input_3.setText("")
        self.lineEdit_coment_input_3.setObjectName("lineEdit_coment_input_3")
        self.label_73 = QtWidgets.QLabel(parent=self.order_page_3)
        self.label_73.setGeometry(QtCore.QRect(30, 90, 261, 16))
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(parent=self.order_page_3)
        self.label_74.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label_74.setObjectName("label_74")
        self.pushButton_send_order_3 = QtWidgets.QPushButton(parent=self.order_page_3)
        self.pushButton_send_order_3.setGeometry(QtCore.QRect(40, 330, 161, 41))
        self.pushButton_send_order_3.setStyleSheet("background-color: rgb(0, 153, 81);\n"
"                            color: white;\n"
"                            border-radius: 20px;\n"
"                        ")
        self.pushButton_send_order_3.setObjectName("pushButton_send_order_3")
        self.stackedWidget.addWidget(self.order_page_3)
        self.setting_page_3 = QtWidgets.QWidget()
        self.setting_page_3.setObjectName("setting_page_3")
        self.stackedWidget.addWidget(self.setting_page_3)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_53.setText(_translate("Dialog", "Стаж"))
        self.label_59.setText(_translate("Dialog", "Разряд"))
        self.label_61.setText(_translate("Dialog", "Никнейм"))
        self.label_63.setText(_translate("Dialog", "Пароль"))
        self.label_65.setText(_translate("Dialog", "Отчество"))
        self.label_67.setText(_translate("Dialog", "Фамилия"))
        self.label_69.setText(_translate("Dialog", "Имя"))
        self.label_71.setText(_translate("Dialog", "Должность"))
        self.pushButton_reg_reg.setText(_translate("Dialog", "Регистрация"))
        self.label_55.setText(_translate("Dialog", "Возраст"))
        self.label_73.setText(_translate("Dialog", "Введите личный коментарий(по желанию)"))
        self.label_74.setText(_translate("Dialog", "Введите номер станка"))
        self.pushButton_send_order_3.setText(_translate("Dialog", "Отправить заявку"))
