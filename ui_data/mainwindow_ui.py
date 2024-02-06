# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import requests


def get_ll(arr):
    return ",".join(map(str, arr))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.zoom = 1
        self.position = [37.977751, 56.757718]
        self.map_type = 'map'
        self.step = 1 / self.zoom

        self.reload_map()

        self.btn_plus.clicked.connect(self.scale)
        self.btn_minus.clicked.connect(self.scale)
        self.map.clicked.connect(self.change_style)
        self.sat.clicked.connect(self.change_style)
        self.sat_skl.clicked.connect(self.change_style)

    def change_style(self):
        self.map_type = self.sender().text()
        self.reload_map()

    def scale(self, do=None):
        if not do:
            do = self.sender().text()

        if do == '+':
            self.zoom = min(self.zoom + 1, 21)
        if do == '-':
            self.zoom = max(self.zoom - 1, 0)

        self.reload_map()

    def keyPressEvent(self, event):
        key = event.key()
        self.step = 1 / (self.zoom * 2)
        if key == Qt.Key_W:
            self.position[1] += self.step
        if key == Qt.Key_S:
            self.position[1] -= self.step
        if key == Qt.Key_A:
            self.position[0] -= self.step
        if key == Qt.Key_D:
            self.position[0] += self.step

        self.reload_map()

    def reload_map(self):
        params = {
            "ll": get_ll(self.position),
            "l": self.map_type,
            'pt': f'{get_ll(self.position)},round',
            'z': self.zoom
        }

        response = requests.get('http://static-maps.yandex.ru/1.x/', params=params)

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(response.content)

        self.map_image.setPixmap(pixmap)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.find_palce = QtWidgets.QLineEdit(self.groupBox)
        self.find_palce.setObjectName("find_palce")
        self.verticalLayout.addWidget(self.find_palce)
        self.map_image = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map_image.sizePolicy().hasHeightForWidth())
        self.map_image.setSizePolicy(sizePolicy)
        self.map_image.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.map_image.setObjectName("map_image")
        self.verticalLayout.addWidget(self.map_image)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_plus = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setObjectName("btn_plus")
        self.horizontalLayout_3.addWidget(self.btn_plus)
        self.btn_minus = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setObjectName("btn_minus")
        self.horizontalLayout_3.addWidget(self.btn_minus)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.map = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setObjectName("map")
        self.horizontalLayout_2.addWidget(self.map)
        self.sat = QtWidgets.QPushButton(self.groupBox_2)
        self.sat.setObjectName("sat")
        self.horizontalLayout_2.addWidget(self.sat)
        self.sat_skl = QtWidgets.QPushButton(self.groupBox_2)
        self.sat_skl.setObjectName("sat_skl")
        self.horizontalLayout_2.addWidget(self.sat_skl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.map_image.setText(_translate("MainWindow", "🤡"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.map.setText(_translate("MainWindow", "map"))
        self.sat.setText(_translate("MainWindow", "sat"))
        self.sat_skl.setText(_translate("MainWindow", "sat,skl"))
