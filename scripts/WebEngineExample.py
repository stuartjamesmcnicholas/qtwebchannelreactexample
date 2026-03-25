import sys
try:
   from PySide6.QtWidgets import QApplication, QMainWindow
   from PySide6.QtWebEngineWidgets import QWebEngineView
   from PySide6.QtCore import QUrl, Slot, Signal, QObject
   from PySide6.QtWebChannel import QWebChannel
except:
   from PySide2.QtWidgets import QApplication, QMainWindow
   from PySide2.QtWebEngineWidgets import QWebEngineView
   from PySide2.QtCore import QUrl, Slot, Signal, QObject
   from PySide2.QtWebChannel import QWebChannel

class WebToolBarButtonBridge(QObject):
    buttonClicked = Signal(str)
    buttonList = Signal(list)
    @Slot(str)
    def clicked(self,buttonName):
        self.buttonClicked.emit(buttonName)

class WebEngineView(QWebEngineView):
    buttonClicked = Signal(str)
    buttonList = Signal(list)
    
    def __init__(self,parent=None):
        QWebEngineView.__init__(self,parent)
        
        self.channel = QWebChannel()
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

@Slot(str)
def handleClick(s):
       print("clicked!")
       print(s,"was clicked")

webview.buttonClicked.connect(handleClick)

sys.exit(app.exec_())
