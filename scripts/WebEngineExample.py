import sys
try:
   from PySide6.QtWidgets import QApplication, QMainWindow
   from PySide6.QtWebEngineWidgets import QWebEngineView
   from PySide6.QtCore import QUrl
   from PySide6 import QtCore, QtWebChannel
except:
   from PySide2.QtWidgets import QApplication, QMainWindow
   from PySide2.QtWebEngineWidgets import QWebEngineView
   from PySide2.QtCore import QUrl
   from PySide2 import QtCore, QtWebChannel

class WebToolBarButtonBridge(QtCore.QObject):
    buttonClicked = QtCore.Signal(str)
    buttonList = QtCore.Signal(list)
    @QtCore.Slot(str)
    def clicked(self,buttonName):
        self.buttonClicked.emit(buttonName)
    @QtCore.Slot('QJsonArray')
    def namesRequest(self,buttonNames):
        ls = []
        for i in range(buttonNames.count()):
            ls.append(buttonNames.at(i).toString())
        self.buttonList.emit(ls)

class WebEngineView(QWebEngineView):
    buttonClicked = QtCore.Signal(str)
    buttonList = QtCore.Signal(list)
    
    def __init__(self,parent=None):
        QWebEngineView.__init__(self,parent)
        
        self.channel = QtWebChannel.QWebChannel()
        self.handler = WebToolBarButtonBridge()
        self.channel.registerObject('handler', self.handler)
        self.page().setWebChannel(self.channel)
        self.handler.buttonClicked.connect(self.buttonClicked.emit)
        self.handler.buttonList.connect(self.buttonList.emit)

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Minimal QWebEngineView")
window.resize(1024, 750)

# Create the web view
webview = WebEngineView()
if len(sys.argv) > 1:
    webview.load(QUrl(sys.argv[1]))
else:
    webview.load(QUrl("https://www.moorhen.org"))

window.setCentralWidget(webview)
window.show()

@QtCore.Slot(str)
def handleClick(s):
       print("clicked!")
       print(s,"was clicked")

webview.buttonClicked.connect(handleClick)

sys.exit(app.exec_())
