# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(656, 551)
        JanelaPrincipal.setFocusPolicy(QtCore.Qt.TabFocus)
        JanelaPrincipal.setStyleSheet("/*QPushButton {\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgba(93, 93, 93, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: rgb(39, 39, 39);\n"
"    border-style: solid;\n"
"    min-width: 10em;\n"
"    font: bold;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgba(113, 113, 113, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgba(73, 73, 73, 255);\n"
"    border-color: orange;\n"
"\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgb(207, 207, 207);\n"
"    alternate-background-color: cyan;\n"
"    background-color: rgba(93, 93, 93, 255);\n"
"    font: bold;\n"
"    border-width: 1px;\n"
"    border-color: rgb(136, 136, 136);\n"
"}*/")
        self.centralWidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralWidget.setStyleSheet("/*QPushButton {\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgba(93, 93, 93, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: rgb(39, 39, 39);\n"
"    border-style: solid;\n"
"    min-width: 10em;\n"
"    font: bold;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgba(113, 113, 113, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgba(73, 73, 73, 255);\n"
"    border-color: orange;\n"
"\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgb(207, 207, 207);\n"
"    alternate-background-color: cyan;\n"
"    background-color: rgba(93, 93, 93, 255);\n"
"    font: bold;\n"
"    border-width: 1px;\n"
"    border-color: rgb(136, 136, 136);\n"
"}*/")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listaImpressoras = QtWidgets.QTableView(self.centralWidget)
        self.listaImpressoras.setObjectName("listaImpressoras")
        self.verticalLayout.addWidget(self.listaImpressoras)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botaoImprimir = QtWidgets.QPushButton(self.centralWidget)
        self.botaoImprimir.setObjectName("botaoImprimir")
        self.horizontalLayout.addWidget(self.botaoImprimir)
        self.botaoConfigurar = QtWidgets.QPushButton(self.centralWidget)
        self.botaoConfigurar.setObjectName("botaoConfigurar")
        self.horizontalLayout.addWidget(self.botaoConfigurar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        JanelaPrincipal.setCentralWidget(self.centralWidget)
        self.barraMenus = QtWidgets.QMenuBar(JanelaPrincipal)
        self.barraMenus.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.barraMenus.setObjectName("barraMenus")
        self.menuArquivos = QtWidgets.QMenu(self.barraMenus)
        self.menuArquivos.setObjectName("menuArquivos")
        self.menuBanco_de_Dados = QtWidgets.QMenu(self.barraMenus)
        self.menuBanco_de_Dados.setObjectName("menuBanco_de_Dados")
        JanelaPrincipal.setMenuBar(self.barraMenus)
        self.barraStatus = QtWidgets.QStatusBar(JanelaPrincipal)
        self.barraStatus.setObjectName("barraStatus")
        JanelaPrincipal.setStatusBar(self.barraStatus)
        self.barraFerramentas = QtWidgets.QToolBar(JanelaPrincipal)
        self.barraFerramentas.setEnabled(False)
        self.barraFerramentas.setMinimumSize(QtCore.QSize(1, 1))
        self.barraFerramentas.setAutoFillBackground(False)
        self.barraFerramentas.setMovable(False)
        self.barraFerramentas.setFloatable(False)
        self.barraFerramentas.setObjectName("barraFerramentas")
        JanelaPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.barraFerramentas)
        self.dockListaDeTabelas = QtWidgets.QDockWidget(JanelaPrincipal)
        self.dockListaDeTabelas.setObjectName("dockListaDeTabelas")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listaDeTabelas = QtWidgets.QListView(self.dockWidgetContents_3)
        self.listaDeTabelas.setObjectName("listaDeTabelas")
        self.verticalLayout_2.addWidget(self.listaDeTabelas)
        self.dockListaDeTabelas.setWidget(self.dockWidgetContents_3)
        JanelaPrincipal.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockListaDeTabelas)
        self.action_selecionar_banco = QtWidgets.QAction(JanelaPrincipal)
        self.action_selecionar_banco.setObjectName("action_selecionar_banco")
        self.action_configurar_tabela = QtWidgets.QAction(JanelaPrincipal)
        self.action_configurar_tabela.setObjectName("action_configurar_tabela")
        self.action_abrir_outro_projeto = QtWidgets.QAction(JanelaPrincipal)
        self.action_abrir_outro_projeto.setObjectName("action_abrir_outro_projeto")
        self.action_sair = QtWidgets.QAction(JanelaPrincipal)
        self.action_sair.setObjectName("action_sair")
        self.action_apontar_tabela = QtWidgets.QAction(JanelaPrincipal)
        self.action_apontar_tabela.setObjectName("action_apontar_tabela")
        self.action_nova_tabela = QtWidgets.QAction(JanelaPrincipal)
        self.action_nova_tabela.setObjectName("action_nova_tabela")
        self.action_novo_banco = QtWidgets.QAction(JanelaPrincipal)
        icon = QtGui.QIcon.fromTheme("Normal")
        self.action_novo_banco.setIcon(icon)
        self.action_novo_banco.setObjectName("action_novo_banco")
        self.action_remover_tabela = QtWidgets.QAction(JanelaPrincipal)
        self.action_remover_tabela.setObjectName("action_remover_tabela")
        self.action_imprimir = QtWidgets.QAction(JanelaPrincipal)
        self.action_imprimir.setObjectName("action_imprimir")
        self.action_salvar = QtWidgets.QAction(JanelaPrincipal)
        self.action_salvar.setObjectName("action_salvar")
        self.menuArquivos.addAction(self.action_novo_banco)
        self.menuArquivos.addAction(self.action_selecionar_banco)
        self.menuArquivos.addSeparator()
        self.menuArquivos.addAction(self.action_abrir_outro_projeto)
        self.menuArquivos.addAction(self.action_salvar)
        self.menuArquivos.addAction(self.action_sair)
        self.menuBanco_de_Dados.addAction(self.action_apontar_tabela)
        self.menuBanco_de_Dados.addAction(self.action_configurar_tabela)
        self.menuBanco_de_Dados.addSeparator()
        self.menuBanco_de_Dados.addAction(self.action_nova_tabela)
        self.menuBanco_de_Dados.addAction(self.action_remover_tabela)
        self.menuBanco_de_Dados.addSeparator()
        self.menuBanco_de_Dados.addAction(self.action_imprimir)
        self.barraMenus.addAction(self.menuArquivos.menuAction())
        self.barraMenus.addAction(self.menuBanco_de_Dados.menuAction())
        self.barraFerramentas.addAction(self.action_novo_banco)

        self.retranslateUi(JanelaPrincipal)
        self.action_sair.triggered.connect(JanelaPrincipal.close)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "Gerenciador de Scanners"))
        self.botaoImprimir.setText(_translate("JanelaPrincipal", "Imprimir"))
        self.botaoConfigurar.setText(_translate("JanelaPrincipal", "Configurar Base de Dados"))
        self.menuArquivos.setTitle(_translate("JanelaPrincipal", "&Arquivos"))
        self.menuBanco_de_Dados.setTitle(_translate("JanelaPrincipal", "Banco de &Dados"))
        self.dockListaDeTabelas.setWindowTitle(_translate("JanelaPrincipal", "Lista de Tabelas"))
        self.action_selecionar_banco.setText(_translate("JanelaPrincipal", "Selecion&ar banco"))
        self.action_selecionar_banco.setToolTip(_translate("JanelaPrincipal", "Selecione outro banco para usar, substituindo o atual por ele"))
        self.action_selecionar_banco.setShortcut(_translate("JanelaPrincipal", "Ctrl+B"))
        self.action_configurar_tabela.setText(_translate("JanelaPrincipal", "&Configurar tabela"))
        self.action_configurar_tabela.setShortcut(_translate("JanelaPrincipal", "Ctrl+T"))
        self.action_abrir_outro_projeto.setText(_translate("JanelaPrincipal", "Abrir &outro projeto..."))
        self.action_abrir_outro_projeto.setShortcut(_translate("JanelaPrincipal", "Ctrl+A"))
        self.action_sair.setText(_translate("JanelaPrincipal", "Sai&r"))
        self.action_sair.setShortcut(_translate("JanelaPrincipal", "Ctrl+Q"))
        self.action_apontar_tabela.setText(_translate("JanelaPrincipal", "&Selecionar Tabela"))
        self.action_nova_tabela.setText(_translate("JanelaPrincipal", "&Nova tabela"))
        self.action_novo_banco.setText(_translate("JanelaPrincipal", "&Novo banco"))
        self.action_remover_tabela.setText(_translate("JanelaPrincipal", "&Remover tabela"))
        self.action_imprimir.setText(_translate("JanelaPrincipal", "&Imprimir"))
        self.action_imprimir.setShortcut(_translate("JanelaPrincipal", "Ctrl+P"))
        self.action_salvar.setText(_translate("JanelaPrincipal", "&Salvar alterações no banco"))
        self.action_salvar.setShortcut(_translate("JanelaPrincipal", "Ctrl+S"))

