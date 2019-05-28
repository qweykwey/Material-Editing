# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 687)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.ResourceFrame = QtWidgets.QFrame(self.splitter)
        self.ResourceFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.ResourceFrame.setObjectName("ResourceFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ResourceFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LibraryBar = QtWidgets.QFrame(self.ResourceFrame)
        self.LibraryBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LibraryBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LibraryBar.setObjectName("LibraryBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LibraryBar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.libraryLabel = QtWidgets.QLabel(self.LibraryBar)
        self.libraryLabel.setObjectName("libraryLabel")
        self.horizontalLayout_2.addWidget(self.libraryLabel)
        self.libraryAdd = QtWidgets.QToolButton(self.LibraryBar)
        self.libraryAdd.setObjectName("libraryAdd")
        self.horizontalLayout_2.addWidget(self.libraryAdd)
        self.libraryRemove = QtWidgets.QToolButton(self.LibraryBar)
        self.libraryRemove.setObjectName("libraryRemove")
        self.horizontalLayout_2.addWidget(self.libraryRemove)
        self.verticalLayout.addWidget(self.LibraryBar)
        self.LibraryView = QtWidgets.QTreeView(self.ResourceFrame)
        self.LibraryView.setObjectName("LibraryView")
        self.verticalLayout.addWidget(self.LibraryView)
        self.CompendiumLabel = QtWidgets.QLabel(self.ResourceFrame)
        self.CompendiumLabel.setObjectName("CompendiumLabel")
        self.verticalLayout.addWidget(self.CompendiumLabel)
        self.CompendiumView = QtWidgets.QTreeView(self.ResourceFrame)
        self.CompendiumView.setObjectName("CompendiumView")
        self.verticalLayout.addWidget(self.CompendiumView)
        self.Mrl3EditorView = QtWidgets.QTabWidget(self.splitter)
        self.Mrl3EditorView.setEnabled(True)
        self.Mrl3EditorView.setMinimumSize(QtCore.QSize(760, 0))
        self.Mrl3EditorView.setAutoFillBackground(False)
        self.Mrl3EditorView.setElideMode(QtCore.Qt.ElideLeft)
        self.Mrl3EditorView.setTabsClosable(True)
        self.Mrl3EditorView.setMovable(True)
        self.Mrl3EditorView.setObjectName("Mrl3EditorView")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        self.menuMrl3 = QtWidgets.QMenu(self.menubar)
        self.menuMrl3.setObjectName("menuMrl3")
        self.menuLibrary = QtWidgets.QMenu(self.menubar)
        self.menuLibrary.setObjectName("menuLibrary")
        self.menuCompendium = QtWidgets.QMenu(self.menubar)
        self.menuCompendium.setObjectName("menuCompendium")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionAdd_Resource_Path = QtWidgets.QAction(MainWindow)
        self.actionAdd_Resource_Path.setObjectName("actionAdd_Resource_Path")
        self.actionReplace_Resource_Paths = QtWidgets.QAction(MainWindow)
        self.actionReplace_Resource_Paths.setObjectName("actionReplace_Resource_Paths")
        self.actionNew_Library = QtWidgets.QAction(MainWindow)
        self.actionNew_Library.setObjectName("actionNew_Library")
        self.actionOpen_Library = QtWidgets.QAction(MainWindow)
        self.actionOpen_Library.setObjectName("actionOpen_Library")
        self.actionSave_Library = QtWidgets.QAction(MainWindow)
        self.actionSave_Library.setObjectName("actionSave_Library")
        self.actionSave_Library_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Library_As.setObjectName("actionSave_Library_As")
        self.actionAdd_Material = QtWidgets.QAction(MainWindow)
        self.actionAdd_Material.setObjectName("actionAdd_Material")
        self.actionRebase_Compendium = QtWidgets.QAction(MainWindow)
        self.actionRebase_Compendium.setObjectName("actionRebase_Compendium")
        self.actionExpand_Compendium = QtWidgets.QAction(MainWindow)
        self.actionExpand_Compendium.setObjectName("actionExpand_Compendium")
        self.actionSave_Compendium = QtWidgets.QAction(MainWindow)
        self.actionSave_Compendium.setObjectName("actionSave_Compendium")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionCreate_Restore_Point = QtWidgets.QAction(MainWindow)
        self.actionCreate_Restore_Point.setObjectName("actionCreate_Restore_Point")
        self.actionLoad_Restore_Point = QtWidgets.QAction(MainWindow)
        self.actionLoad_Restore_Point.setObjectName("actionLoad_Restore_Point")
        self.menuMrl3.addAction(self.actionNew)
        self.menuMrl3.addAction(self.actionOpen)
        self.menuMrl3.addAction(self.actionSave)
        self.menuMrl3.addAction(self.actionSave_As)
        self.menuMrl3.addAction(self.actionSave_All)
        self.menuMrl3.addSeparator()
        self.menuMrl3.addAction(self.actionCreate_Restore_Point)
        self.menuMrl3.addAction(self.actionLoad_Restore_Point)
        self.menuLibrary.addAction(self.actionNew_Library)
        self.menuLibrary.addAction(self.actionOpen_Library)
        self.menuLibrary.addAction(self.actionSave_Library)
        self.menuLibrary.addAction(self.actionSave_Library_As)
        self.menuLibrary.addSeparator()
        self.menuCompendium.addAction(self.actionRebase_Compendium)
        self.menuCompendium.addAction(self.actionExpand_Compendium)
        self.menuCompendium.addAction(self.actionSave_Compendium)
        self.menubar.addAction(self.menuMrl3.menuAction())
        self.menubar.addAction(self.menuLibrary.menuAction())
        self.menubar.addAction(self.menuCompendium.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.libraryLabel.setText(_translate("MainWindow", "Library"))
        self.libraryAdd.setText(_translate("MainWindow", "Add"))
        self.libraryRemove.setText(_translate("MainWindow", "Remove"))
        self.CompendiumLabel.setText(_translate("MainWindow", "Compendium"))
        self.menuMrl3.setTitle(_translate("MainWindow", "Mrl3"))
        self.menuLibrary.setTitle(_translate("MainWindow", "Library"))
        self.menuCompendium.setTitle(_translate("MainWindow", "Compendium"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "Create an empty Mrl3"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create an empty Mrl3"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open an Mrl3"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open an Mrl3"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save current Mrl3"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save current Mrl3"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setToolTip(_translate("MainWindow", "Save current Mrl3 as"))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save current Mrl3 as"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionSave_All.setStatusTip(_translate("MainWindow", "Save all opened Mrl3"))
        self.actionSave_All.setWhatsThis(_translate("MainWindow", "Save all opened Mrl3"))
        self.actionSave_All.setShortcut(_translate("MainWindow", "Ctrl+Alt+Shift+S"))
        self.actionAdd_Resource_Path.setText(_translate("MainWindow", "Add Resource Path"))
        self.actionAdd_Resource_Path.setStatusTip(_translate("MainWindow", "Add a Resource Path to the Current Material"))
        self.actionAdd_Resource_Path.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionReplace_Resource_Paths.setText(_translate("MainWindow", "Replace Resource Paths"))
        self.actionReplace_Resource_Paths.setToolTip(_translate("MainWindow", "Performs a global replace on Resource Path Strings"))
        self.actionReplace_Resource_Paths.setStatusTip(_translate("MainWindow", "Performs a global replace on Resource Path Strings"))
        self.actionReplace_Resource_Paths.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionNew_Library.setText(_translate("MainWindow", "New Library"))
        self.actionNew_Library.setIconText(_translate("MainWindow", "Create a New Library"))
        self.actionNew_Library.setToolTip(_translate("MainWindow", "Create a New Library"))
        self.actionNew_Library.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionOpen_Library.setText(_translate("MainWindow", "Open Library"))
        self.actionOpen_Library.setIconText(_translate("MainWindow", "Open a Material Library"))
        self.actionOpen_Library.setToolTip(_translate("MainWindow", "Open a Material Library"))
        self.actionOpen_Library.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionSave_Library.setText(_translate("MainWindow", "Save Library"))
        self.actionSave_Library.setIconText(_translate("MainWindow", "Save the Material Library"))
        self.actionSave_Library.setToolTip(_translate("MainWindow", "Save the Material Library"))
        self.actionSave_Library.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionSave_Library_As.setText(_translate("MainWindow", "Save Library As"))
        self.actionSave_Library_As.setIconText(_translate("MainWindow", "Save the Material Library as"))
        self.actionSave_Library_As.setToolTip(_translate("MainWindow", "Save the Material Library as"))
        self.actionSave_Library_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionAdd_Material.setText(_translate("MainWindow", "Add Material"))
        self.actionAdd_Material.setIconText(_translate("MainWindow", "Add a material or a complete file to the Material Library"))
        self.actionAdd_Material.setToolTip(_translate("MainWindow", "Add a material or a complete file to the Material Library"))
        self.actionAdd_Material.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionRebase_Compendium.setText(_translate("MainWindow", "Rebase Compendium"))
        self.actionRebase_Compendium.setIconText(_translate("MainWindow", "Generates a new Compendium from Scratch"))
        self.actionRebase_Compendium.setToolTip(_translate("MainWindow", "Generates a new Compendium from Scratch"))
        self.actionRebase_Compendium.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionExpand_Compendium.setText(_translate("MainWindow", "Expand Compendium"))
        self.actionExpand_Compendium.setIconText(_translate("MainWindow", "Rebases the Compendium"))
        self.actionExpand_Compendium.setToolTip(_translate("MainWindow", "Rebases the Compendium"))
        self.actionExpand_Compendium.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionSave_Compendium.setText(_translate("MainWindow", "Save Compendium"))
        self.actionSave_Compendium.setIconText(_translate("MainWindow", "Saves changes to the Compendium"))
        self.actionSave_Compendium.setToolTip(_translate("MainWindow", "Saves changes to the Compendium"))
        self.actionSave_Compendium.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setIconText(_translate("MainWindow", "Copy the active selection"))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy the active selection"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setIconText(_translate("MainWindow", "Paste from the clipboard to the active selection"))
        self.actionPaste.setToolTip(_translate("MainWindow", "Paste from the clipboard to the active selection"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setIconText(_translate("MainWindow", "Delete Active Selection"))
        self.actionDelete.setToolTip(_translate("MainWindow", "Delete Active Selection"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
        self.actionCreate_Restore_Point.setText(_translate("MainWindow", "Create Restore Point"))
        self.actionLoad_Restore_Point.setText(_translate("MainWindow", "Load Restore Point"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
