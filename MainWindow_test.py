# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 766)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tw_table = QtWidgets.QWidget()
        self.tw_table.setObjectName("tw_table")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tw_table)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.itemView = QtWidgets.QTableWidget(self.tw_table)
        self.itemView.setLineWidth(0)
        self.itemView.setShowGrid(True)
        self.itemView.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.itemView.setWordWrap(True)
        self.itemView.setRowCount(0)
        self.itemView.setColumnCount(14)
        self.itemView.setObjectName("itemView")
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.itemView.setHorizontalHeaderItem(13, item)
        self.gridLayout_3.addWidget(self.itemView, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tw_table, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdvanced = QtWidgets.QMenu(self.menubar)
        self.menuAdvanced.setObjectName("menuAdvanced")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuVerify = QtWidgets.QMenu(self.menubar)
        self.menuVerify.setObjectName("menuVerify")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuInformation = QtWidgets.QMenu(self.menubar)
        self.menuInformation.setObjectName("menuInformation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dw_treeview = QtWidgets.QDockWidget(MainWindow)
        self.dw_treeview.setObjectName("dw_treeview")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tw_home = QtWidgets.QWidget()
        self.tw_home.setObjectName("tw_home")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tw_home)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_6.setSpacing(4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.treeWidget = QtWidgets.QTreeWidget(self.tw_home)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/audio-and-sound-alerts-off@32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        self.gridLayout_6.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tw_home, "")
        self.tw_search = QtWidgets.QWidget()
        self.tw_search.setObjectName("tw_search")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tw_search)
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_7.setSpacing(4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.listView = QtWidgets.QListView(self.tw_search)
        self.listView.setObjectName("listView")
        self.gridLayout_7.addWidget(self.listView, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tw_search, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_10.setSpacing(4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.listView_2 = QtWidgets.QListView(self.tab)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_10.addWidget(self.listView_2, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab, "")
        self.tw_bookmark = QtWidgets.QWidget()
        self.tw_bookmark.setObjectName("tw_bookmark")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tw_bookmark)
        self.gridLayout_11.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_11.setSpacing(4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.listView_3 = QtWidgets.QListView(self.tw_bookmark)
        self.listView_3.setObjectName("listView_3")
        self.gridLayout_11.addWidget(self.listView_3, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tw_bookmark, "")
        self.gridLayout.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.dw_treeview.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dw_treeview)
        self.dw_notableview = QtWidgets.QDockWidget(MainWindow)
        self.dw_notableview.setObjectName("dw_notableview")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.dockWidgetContents_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_8.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.dw_notableview.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dw_notableview)
        self.dw_contentsview = QtWidgets.QDockWidget(MainWindow)
        self.dw_contentsview.setObjectName("dw_contentsview")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.dockWidgetContents_5)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tw_text = QtWidgets.QWidget()
        self.tw_text.setObjectName("tw_text")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tw_text)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tw_text)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tw_text, "")
        self.tw_hex = QtWidgets.QWidget()
        self.tw_hex.setObjectName("tw_hex")
        self.tabWidget_4.addTab(self.tw_hex, "")
        self.tw_summary = QtWidgets.QWidget()
        self.tw_summary.setObjectName("tw_summary")
        self.tabWidget_4.addTab(self.tw_summary, "")
        self.tw_notable = QtWidgets.QWidget()
        self.tw_notable.setObjectName("tw_notable")
        self.tabWidget_4.addTab(self.tw_notable, "")
        self.gridLayout_9.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.dw_contentsview.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dw_contentsview)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setCheckable(True)
        self.actionNew.setObjectName("actionNew")
        self.actionDevice = QtWidgets.QAction(MainWindow)
        self.actionDevice.setCheckable(True)
        self.actionDevice.setObjectName("actionDevice")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setCheckable(True)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setCheckable(True)
        self.actionSave.setObjectName("actionSave")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdvanced.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuVerify.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuInformation.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionDevice)
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.treeWidget.clicked['QModelIndex'].connect(MainWindow.ls_UI)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.itemView.setSortingEnabled(True)
        item = self.itemView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.itemView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Path"))
        item = self.itemView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        item = self.itemView.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MD5"))
        item = self.itemView.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SHA1"))
        item = self.itemView.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "MODIFY_TIME"))
        item = self.itemView.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ACCESS_TIME"))
        item = self.itemView.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CREATE_TIME"))
        item = self.itemView.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "MODIFY_ATTRIBUTE_TIME"))
        item = self.itemView.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "BACKUP_TIME"))
        item = self.itemView.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "INDEX_NUM"))
        item = self.itemView.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "FILE_NODE_NUM"))
        item = self.itemView.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "DATA_LOCATION"))
        item = self.itemView.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "FOLDER"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tw_table), _translate("MainWindow", "Table"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdvanced.setTitle(_translate("MainWindow", "Advanced"))
        self.menuReport.setTitle(_translate("MainWindow", "Report"))
        self.menuVerify.setTitle(_translate("MainWindow", "Verify"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuInformation.setTitle(_translate("MainWindow", "Information"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dw_treeview.setWindowTitle(_translate("MainWindow", "탐색"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "새 행"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "새 항목"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tw_home), _translate("MainWindow", "Explorer"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tw_search), _translate("MainWindow", "Key File"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "Time line"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tw_bookmark), _translate("MainWindow", "Bookmark"))
        self.dw_notableview.setWindowTitle(_translate("MainWindow", "System Warning"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tw_text), _translate("MainWindow", "Hex"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tw_hex), _translate("MainWindow", "PreView"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tw_summary), _translate("MainWindow", "Summary"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tw_notable), _translate("MainWindow", "Notable"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionDevice.setText(_translate("MainWindow", "Device"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

import UI_resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

