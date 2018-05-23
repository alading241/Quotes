# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1482, 931)
        self._central_widget = QtWidgets.QWidget(MainWindow)
        self._central_widget.setObjectName("_central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self._central_widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self._central_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalSlider = QtWidgets.QSlider(self._central_widget)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self._central_widget)
        self._menu_bar = QtWidgets.QMenuBar(MainWindow)
        self._menu_bar.setGeometry(QtCore.QRect(0, 0, 1482, 23))
        self._menu_bar.setDefaultUp(False)
        self._menu_bar.setObjectName("_menu_bar")
        self._file_menu = QtWidgets.QMenu(self._menu_bar)
        self._file_menu.setObjectName("_file_menu")
        self._edit_menu = QtWidgets.QMenu(self._menu_bar)
        self._edit_menu.setObjectName("_edit_menu")
        self._view_menu = QtWidgets.QMenu(self._menu_bar)
        self._view_menu.setObjectName("_view_menu")
        MainWindow.setMenuBar(self._menu_bar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self._stocks_list_dock = QtWidgets.QDockWidget(MainWindow)
        self._stocks_list_dock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self._stocks_list_dock.setObjectName("_stocks_list_dock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.stocks_list = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.stocks_list.setGeometry(QtCore.QRect(0, 0, 256, 192))
        self.stocks_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.stocks_list.setRowCount(1)
        self.stocks_list.setColumnCount(2)
        self.stocks_list.setObjectName("stocks_list")
        self._stocks_list_dock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self._stocks_list_dock)
        self._tool_bar = QtWidgets.QToolBar(MainWindow)
        self._tool_bar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea)
        self._tool_bar.setOrientation(QtCore.Qt.Horizontal)
        self._tool_bar.setObjectName("_tool_bar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self._tool_bar)
        self._stocks_info_dock = QtWidgets.QDockWidget(MainWindow)
        self._stocks_info_dock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self._stocks_info_dock.setObjectName("_stocks_info_dock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.stock_info = QtWidgets.QTableWidget(self.dockWidgetContents_2)
        self.stock_info.setGeometry(QtCore.QRect(0, 0, 50, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_info.sizePolicy().hasHeightForWidth())
        self.stock_info.setSizePolicy(sizePolicy)
        self.stock_info.setObjectName("stock_info")
        self.stock_info.setColumnCount(0)
        self.stock_info.setRowCount(0)
        self._stocks_info_dock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self._stocks_info_dock)
        self._draw_panel = QtWidgets.QToolBar(MainWindow)
        self._draw_panel.setOrientation(QtCore.Qt.Horizontal)
        self._draw_panel.setObjectName("_draw_panel")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self._draw_panel)
        MainWindow.insertToolBarBreak(self._draw_panel)
        self.actionSelect_Data_Source = QtWidgets.QAction(MainWindow)
        self.actionSelect_Data_Source.setCheckable(True)
        self.actionSelect_Data_Source.setObjectName("actionSelect_Data_Source")
        self.action_kline_1m = QtWidgets.QAction(MainWindow)
        self.action_kline_1m.setCheckable(True)
        self.action_kline_1m.setObjectName("action_kline_1m")
        self.action_kline_5m = QtWidgets.QAction(MainWindow)
        self.action_kline_5m.setCheckable(True)
        self.action_kline_5m.setObjectName("action_kline_5m")
        self.action_kline_30m = QtWidgets.QAction(MainWindow)
        self.action_kline_30m.setCheckable(True)
        self.action_kline_30m.setObjectName("action_kline_30m")
        self.action_kline_days = QtWidgets.QAction(MainWindow)
        self.action_kline_days.setCheckable(True)
        self.action_kline_days.setObjectName("action_kline_days")
        self.action_kline_week = QtWidgets.QAction(MainWindow)
        self.action_kline_week.setCheckable(True)
        self.action_kline_week.setObjectName("action_kline_week")
        self.action_kline_month = QtWidgets.QAction(MainWindow)
        self.action_kline_month.setCheckable(True)
        self.action_kline_month.setObjectName("action_kline_month")
        self.action_kline_season = QtWidgets.QAction(MainWindow)
        self.action_kline_season.setCheckable(True)
        self.action_kline_season.setObjectName("action_kline_season")
        self.action_kline_year = QtWidgets.QAction(MainWindow)
        self.action_kline_year.setCheckable(True)
        self.action_kline_year.setObjectName("action_kline_year")
        self._file_menu.addAction(self.actionSelect_Data_Source)
        self._view_menu.addAction(self.action_kline_1m)
        self._view_menu.addAction(self.action_kline_5m)
        self._view_menu.addAction(self.action_kline_30m)
        self._view_menu.addAction(self.action_kline_days)
        self._view_menu.addAction(self.action_kline_week)
        self._view_menu.addAction(self.action_kline_month)
        self._view_menu.addAction(self.action_kline_season)
        self._view_menu.addAction(self.action_kline_year)
        self._menu_bar.addAction(self._file_menu.menuAction())
        self._menu_bar.addAction(self._edit_menu.menuAction())
        self._menu_bar.addAction(self._view_menu.menuAction())
        self._tool_bar.addSeparator()
        self._draw_panel.addSeparator()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.action_kline_1m.triggered['bool'].connect(MainWindow.onKLineChanged)
        self.action_kline_30m.triggered['bool'].connect(MainWindow.onKLineChanged)
        self.horizontalSlider.rangeChanged['int','int'].connect(MainWindow.onKLinePeriodChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._file_menu.setTitle(_translate("MainWindow", "文件"))
        self._edit_menu.setTitle(_translate("MainWindow", "编辑"))
        self._view_menu.setTitle(_translate("MainWindow", "查看"))
        self._tool_bar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self._draw_panel.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSelect_Data_Source.setText(_translate("MainWindow", "Select Data Source"))
        self.action_kline_1m.setText(_translate("MainWindow", "1分钟"))
        self.action_kline_5m.setText(_translate("MainWindow", "5分钟"))
        self.action_kline_30m.setText(_translate("MainWindow", "30分钟"))
        self.action_kline_days.setText(_translate("MainWindow", "日线"))
        self.action_kline_week.setText(_translate("MainWindow", "周线"))
        self.action_kline_month.setText(_translate("MainWindow", "月线"))
        self.action_kline_season.setText(_translate("MainWindow", "季线"))
        self.action_kline_year.setText(_translate("MainWindow", "年线"))

