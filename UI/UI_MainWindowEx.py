# -*- coding: utf-8 -*-

import qdarkstyle
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainwindow import Ui_MainWindow
'''
    create our MainWindow from a sketch created by Qt Designer.
'''
class UI_MainWindowEx(Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UI_MainWindowEx, self).__init__( )
        self.main_window_ = MainWindow
        self.__setupGUI( )
        self.__setupStockListDockWidget()
        
    def __setupGUI(self):
        super(UI_MainWindowEx, self).setupUi(self.main_window_)
        
    def __setupStockListDockWidget(self):
        #self.mdi_area_.setContentsMargins(2, 2, 2, 2)
        self.stocks_list_dock_widget_ = QtWidgets.QDockWidget(self.main_window_)
        self.stocks_list_dock_widget_.setContentsMargins(0, 0, 0, 0)
        '''
        AllDockWidgetFeatures = 7，DockWidgetClosable = 1，DockWidgetFloatable = 4，DockWidgetMovable = 2
        DockWidgetVerticalTitleBar = 8
        NoDockWidgetFeatures = 0
        '''
        self.stocks_list_dock_widget_.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)    
        self.stocks_list_dock_widget_.setObjectName("stocks_list_dock_1")        
        self.stocks_list_table_widget_ = QtWidgets.QTabWidget(self.main_window_)
                
        self.favorite_stock_table_ = QtWidgets.QTableView()
        self.shenzhen_stock_table_ = QtWidgets.QTableView()
        self.shanghai_stock_table_ = QtWidgets.QTableView()
        self.favorite_stock_table_.setContentsMargins(0, 0, 0, 0)
        self.shenzhen_stock_table_.setContentsMargins(0, 0, 0, 0)
        self.shanghai_stock_table_.setContentsMargins(0, 0, 0, 0)
        
        self.stocks_list_table_widget_.addTab(self.favorite_stock_table_, '')
        self.stocks_list_table_widget_.addTab(self.shenzhen_stock_table_, 'shenzhen stock')
        self.stocks_list_table_widget_.addTab(self.shanghai_stock_table_, 'shanghai stock')
        
        
        self.stocks_list_dock_widget_.setWidget(self.stocks_list_table_widget_)
        self.main_window_.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.stocks_list_dock_widget_)
        
        self.__retranslateUi(self.main_window_)
        
    def __retranslateUi(self, MainWindow):
        #super(UI_MainWindowEx, self).retranslateUi(self.main_window_)
        _translate = QtCore.QCoreApplication.translate
        self.stocks_list_table_widget_.setTabText(self.stocks_list_table_widget_.indexOf(self.favorite_stock_table_), _translate("MainWindow", "自选股"))
        self.stocks_list_table_widget_.setTabText(self.stocks_list_table_widget_.indexOf(self.shenzhen_stock_table_), _translate("MainWindow", "深圳A股"))
        self.stocks_list_table_widget_.setTabText(self.stocks_list_table_widget_.indexOf(self.shanghai_stock_table_), _translate("MainWindow", "上海A股"))
        
        self.stocks_list_dock_widget_.setWindowTitle(_translate("MainWindow", "股票列表"))
        return
        
if __name__ == "__main__":
    import sys
    import os
    from QuotesMain import QuotesMainWindow
    
    app = QApplication(sys.argv)
    win = QuotesMainWindow( )
    win.show()
    sys.exit(app.exec_())