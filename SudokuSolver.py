'''
Author: Tanner Barcus
Date: 1/7/23
Purpose: Recursive DFS Sudoku Solver
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1000)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 86, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 86, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 86, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 86, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sudoku_table = QtWidgets.QTableWidget(self.centralwidget)
        self.sudoku_table.setGeometry(QtCore.QRect(710, 120, 787, 750))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 86, 60))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.sudoku_table.setPalette(palette)
        self.sudoku_table.setFrameShape(QtWidgets.QFrame.HLine)
        self.sudoku_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sudoku_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sudoku_table.setObjectName("sudoku_table")
        self.sudoku_table.setColumnCount(9)
        self.sudoku_table.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.sudoku_table.setHorizontalHeaderItem(8, item)
        self.sudoku_table.horizontalHeader().setVisible(False)
        self.sudoku_table.horizontalHeader().setDefaultSectionSize(10)
        self.sudoku_table.horizontalHeader().setMinimumSectionSize(10)
        self.sudoku_table.verticalHeader().setVisible(False)
        self.sudoku_table.verticalHeader().setDefaultSectionSize(83)
        self.sudoku_table.verticalHeader().setMinimumSectionSize(83)

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setEnabled(True)
        self.title_label.setGeometry(QtCore.QRect(150, 70, 400, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.title_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.title_label.setFont(font)
        self.title_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_label.setLineWidth(6)
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.instruct_label = QtWidgets.QLabel(self.centralwidget)
        self.instruct_label.setGeometry(QtCore.QRect(100, 450, 500, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 227, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 227, 181, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 227, 181))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 227, 181, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.instruct_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instruct_label.setFont(font)
        self.instruct_label.setAlignment(QtCore.Qt.AlignCenter)
        self.instruct_label.setObjectName("instruct_label")

        self.info_button = QtWidgets.QPushButton(self.centralwidget)
        self.info_button.setGeometry(QtCore.QRect(300, 900, 100, 50))
        self.info_button.setStyleSheet("background-color: #422011; color: #f1e4b6")
        self.info_button.setObjectName("info_button")
        self.info_button.clicked.connect(self.info)

        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(300, 900, 100, 50))
        self.back_button.setStyleSheet("background-color: #422011; color: #f1e4b6")
        self.back_button.setObjectName("info_button")
        self.back_button.clicked.connect(self.back)
        self.back_button.hide()

        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.solve_button.setGeometry(QtCore.QRect(1055, 900, 100, 50))
        self.solve_button.setStyleSheet("background-color: #422011; color: #f1e4b6")
        self.solve_button.clicked.connect(self.click)
        self.solve_button.setObjectName("solve_button")

        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(1397, 900, 100, 50))
        self.reset_button.setStyleSheet("background-color: #422011; color: #f1e4b6")
        self.reset_button.clicked.connect(self.reset)
        self.reset_button.setObjectName("solve_button")
        self.reset_button.hide()

        self.hline1 = QtWidgets.QFrame(self.centralwidget)
        self.hline1.setGeometry(QtCore.QRect(707, 112, 793, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.hline1.setPalette(palette)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hline1.setLineWidth(5)
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setObjectName("hline1")

        self.hline2 = QtWidgets.QFrame(self.centralwidget)
        self.hline2.setGeometry(QtCore.QRect(707, 360, 793, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.hline2.setPalette(palette)
        self.hline2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hline2.setLineWidth(5)
        self.hline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline2.setObjectName("hline2")

        self.hline3 = QtWidgets.QFrame(self.centralwidget)
        self.hline3.setGeometry(QtCore.QRect(707, 610, 793, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.hline3.setPalette(palette)
        self.hline3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hline3.setLineWidth(5)
        self.hline3.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline3.setObjectName("hline3")

        self.hline4 = QtWidgets.QFrame(self.centralwidget)
        self.hline4.setGeometry(QtCore.QRect(707, 860, 793, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.hline4.setPalette(palette)
        self.hline4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hline4.setLineWidth(5)
        self.hline4.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline4.setObjectName("hline4")

        self.vline1 = QtWidgets.QFrame(self.centralwidget)
        self.vline1.setGeometry(QtCore.QRect(699, 120, 20, 749))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.vline1.setPalette(palette)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vline1.setLineWidth(5)
        self.vline1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline1.setObjectName("vline1")

        self.vline_2 = QtWidgets.QFrame(self.centralwidget)
        self.vline_2.setGeometry(QtCore.QRect(960, 120, 20, 749))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.vline_2.setPalette(palette)
        self.vline_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vline_2.setLineWidth(5)
        self.vline_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_2.setObjectName("vline_2")

        self.vline_3 = QtWidgets.QFrame(self.centralwidget)
        self.vline_3.setGeometry(QtCore.QRect(1220, 120, 20, 749))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.vline_3.setPalette(palette)
        self.vline_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vline_3.setLineWidth(5)
        self.vline_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_3.setObjectName("vline_3")

        self.vline_4 = QtWidgets.QFrame(self.centralwidget)
        self.vline_4.setGeometry(QtCore.QRect(1487, 120, 20, 749))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 32, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.vline_4.setPalette(palette)
        self.vline_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vline_4.setLineWidth(5)
        self.vline_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_4.setObjectName("vline_4")

        self.inv_label = QtWidgets.QLabel(self.centralwidget)
        self.inv_label.setGeometry(QtCore.QRect(725, 10, 900, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.inv_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inv_label.setFont(font)
        self.inv_label.setObjectName("inv_label")
        self.inv_label.hide()

        self.results = QtWidgets.QLabel(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(725, 10, 900, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.results.setFont(font)
        self.results.setObjectName("inv_label")
        self.results.hide()

        self.no_sol = QtWidgets.QLabel(self.centralwidget)
        self.no_sol.setGeometry(QtCore.QRect(100, 450, 500, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.no_sol.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.no_sol.setFont(font)
        self.no_sol.setAlignment(QtCore.Qt.AlignCenter)
        self.no_sol.setObjectName("no_sol")
        self.no_sol.hide()

        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(100, 200, 500, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 228, 182))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.info_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_label.setFont(font)
        self.info_label.setAlignment(QtCore.Qt.AlignLeft)
        self.info_label.setObjectName("info_label")
        self.info_label.hide()

        self.board = []
        self.results = []

        self.counter = 0

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku Solver"))
        item = self.sudoku_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.sudoku_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "r0"))
        item = self.sudoku_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "r1"))
        item = self.sudoku_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "r2"))
        item = self.sudoku_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "r3"))
        item = self.sudoku_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "r4"))
        item = self.sudoku_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "r5"))
        item = self.sudoku_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "r6"))
        item = self.sudoku_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "r8"))
        item = self.sudoku_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.sudoku_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "c0"))
        item = self.sudoku_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "c1"))
        item = self.sudoku_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "c2"))
        item = self.sudoku_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "c3"))
        item = self.sudoku_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "c4"))
        item = self.sudoku_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "c5"))
        item = self.sudoku_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "c6"))
        item = self.sudoku_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "c8"))

        self.title_label.setText(_translate("MainWindow", "Sudoku\n""Solver"))
        self.instruct_label.setText(_translate("MainWindow", "Fill in any desired cells with\n""a value (1-9) and then\n""click Solve!"))
        self.info_button.setText(_translate("MainWindow", "Info"))
        self.solve_button.setText(_translate("MainWindow", "Solve!"))
        self.inv_label.setText(_translate("MainWindow", "Invalid Input (please clear value and try again)"))
        self.no_sol.setText(_translate("MainWindow", "The given input has no\n""solution, please press Reset\n""and try again."))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.info_label.setText(_translate("MainWindow", "The Sudoku Solver uses recursive\n""depth-first-search (DFS) to find\n""the first possible valid solution.\n""Upon arriving in a cell, the\n""checker searches among the row,\n""column, and 3x3 square it lies\n""in. Then places its value (1-9)\n""in the cell. It will exhaust\n""all possible solutions until one\n""is found, unless it is presented\n""an unsolvable input."))
        self.back_button.setText(_translate("MainWindow", "Back"))

    def possible_move(self, x, y, val, board):
        for index in range(0, 9):
            if board[y][index] == val:
                return False
        for index in range(0, 9):
            if board[index][x] == val:
                return False
        x_in_square = (x//3)*3
        y_in_square = (y//3)*3
        for index in range(0, 3):
            for i in range(0, 3):
                if board[y_in_square + index][x_in_square + i] == val:
                    return False
        return True

    def is_solved(self, board):
        for x in range(9):
            for y in range(9):
                if board[y][x] == 0:
                    return False
        return True

    def solver(self, board):
        self.counter = self.counter + 1
        if self.counter > 50000:
            raise RecursionError
        if self.is_solved(board):
            return True
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    for val in range(1, 10):
                        if self.possible_move(x, y, val, board):
                            board[y][x] = val
                            if self.solver(board):
                                return True
                        board[y][x] = 0
                    return False

    def click(self):
        self.back()
        self.inv_label.hide()
        board_og = []
        num_rows = self.sudoku_table.rowCount()
        num_cols = self.sudoku_table.columnCount()
        for row in range(num_rows):
            cols = []
            for col in range(num_cols):
                item = self.sudoku_table.item(row, col)
                cols.append(item.text() if item else '')
            board_og.append(cols)
        valid_inp = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '']
        conv_ints = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for rowz in board_og:
            row_new = []
            for i in rowz:
                if i not in valid_inp:
                    self.inv_label.show()
                    return
                if i in conv_ints:
                    num = int(i)
                    row_new.append(num)
                if i == '':
                    i = 0
                    row_new.append(i)
            self.board.append(row_new)
        try:
            if self.solver(self.board):
                r = -1
                i = 0
                for row in self.board:
                    r = r + 1
                    c = -1
                    j = 0
                    for val in row:
                        c = c + 1
                        item = QtWidgets.QTableWidgetItem(self.board[i][j])
                        item.setText(str(self.board[i][j]))
                        self.sudoku_table.setItem(r, c, item)
                        j = j + 1
                    i = i + 1
                self.sudoku_table.hide()
                self.sudoku_table.repaint()
                self.sudoku_table.update()
                self.sudoku_table.show()
                self.reset_button.show()
                return
        except:
            self.instruct_label.hide()
            self.no_sol.show()
            self.reset_button.show()
            return

    def reset(self):
        self.counter = 0
        self.sudoku_table.clearContents()
        self.board = []
        self.reset_button.hide()
        self.no_sol.hide()
        self.instruct_label.show()

    def info(self):
        self.instruct_label.hide()
        self.title_label.hide()
        self.info_button.hide()
        self.info_label.show()
        self.back_button.show()

    def back(self):
        self.info_label.hide()
        self.back_button.hide()
        self.info_button.show()
        self.title_label.show()
        self.instruct_label.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
