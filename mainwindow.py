# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 755)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(320, 720))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.projectWidget = QtWidgets.QWidget()
        self.projectWidget.setObjectName("projectWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.projectWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.projectWidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 20))
        self.groupBox.setBaseSize(QtCore.QSize(0, 30))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openProject = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("folder-open")
        self.openProject.setIcon(icon)
        self.openProject.setFlat(True)
        self.openProject.setObjectName("openProject")
        self.horizontalLayout.addWidget(self.openProject)
        self.saveProject = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.saveProject.setIcon(icon)
        self.saveProject.setFlat(True)
        self.saveProject.setObjectName("saveProject")
        self.horizontalLayout.addWidget(self.saveProject)
        self.printReport = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("document-print")
        self.printReport.setIcon(icon)
        self.printReport.setFlat(True)
        self.printReport.setObjectName("printReport")
        self.horizontalLayout.addWidget(self.printReport)
        self.addTrace = QtWidgets.QPushButton(self.groupBox)
        self.addTrace.setAutoFillBackground(False)
        self.addTrace.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.addTrace.setIcon(icon)
        self.addTrace.setDefault(True)
        self.addTrace.setFlat(True)
        self.addTrace.setObjectName("addTrace")
        self.horizontalLayout.addWidget(self.addTrace)
        self.removeTrace = QtWidgets.QPushButton(self.groupBox)
        self.removeTrace.setText("")
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.removeTrace.setIcon(icon)
        self.removeTrace.setFlat(True)
        self.removeTrace.setObjectName("removeTrace")
        self.horizontalLayout.addWidget(self.removeTrace)
        self.recalculateEvents = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recalculateEvents.sizePolicy().hasHeightForWidth())
        self.recalculateEvents.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.recalculateEvents.setIcon(icon)
        self.recalculateEvents.setFlat(True)
        self.recalculateEvents.setObjectName("recalculateEvents")
        self.horizontalLayout.addWidget(self.recalculateEvents)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.treeView = QtWidgets.QTreeView(self.projectWidget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_3.addWidget(self.treeView)
        self.tabWidget.addTab(self.projectWidget, "")
        self.metaDataWidget = QtWidgets.QWidget()
        self.metaDataWidget.setObjectName("metaDataWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.metaDataWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.metaDataTable = QtWidgets.QTableWidget(self.metaDataWidget)
        self.metaDataTable.setObjectName("metaDataTable")
        self.metaDataTable.setColumnCount(0)
        self.metaDataTable.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.metaDataTable.setVerticalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.metaDataTable)
        self.tabWidget.addTab(self.metaDataWidget, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.dataWidget = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataWidget.sizePolicy().hasHeightForWidth())
        self.dataWidget.setSizePolicy(sizePolicy)
        self.dataWidget.setMinimumSize(QtCore.QSize(720, 720))
        self.dataWidget.setObjectName("dataWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dataWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphWidget = QtWidgets.QWidget(self.dataWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setMinimumSize(QtCore.QSize(710, 460))
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.graphWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphLayout = QtWidgets.QVBoxLayout()
        self.graphLayout.setObjectName("graphLayout")
        self.horizontalLayout_2.addLayout(self.graphLayout)
        self.verticalLayout_2.addWidget(self.graphWidget)
        self.widget = QtWidgets.QWidget(self.dataWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.eventTableView = QtWidgets.QTableView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventTableView.sizePolicy().hasHeightForWidth())
        self.eventTableView.setSizePolicy(sizePolicy)
        self.eventTableView.setMinimumSize(QtCore.QSize(300, 200))
        self.eventTableView.setSortingEnabled(True)
        self.eventTableView.setObjectName("eventTableView")
        self.horizontalLayout_4.addWidget(self.eventTableView)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_3.addWidget(self.dataWidget)
        MainWindow.setCentralWidget(self.mainWidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.projectWidget), _translate("MainWindow", "Project"))
        item = self.metaDataTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Project name"))
        item = self.metaDataTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location A"))
        item = self.metaDataTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Location B"))
        item = self.metaDataTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total distance (km)"))
        item = self.metaDataTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total distance"))
        item = self.metaDataTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Launch length (km)"))
        item = self.metaDataTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Recieve length (km)"))
        item = self.metaDataTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Average loss (dB/km)"))
        item = self.metaDataTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Total loss(dB)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.metaDataWidget), _translate("MainWindow", "Meta Data"))
