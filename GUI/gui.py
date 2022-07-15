from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import Window_Check_Launchpad, Window_Check_Collection_Info, Window_Check_Listed_NFTs, Window_Setup_FP_Alerts, Window_Generate_NFT_Collection
import sys

# ------------ Main Window ------------ #
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.prepareWindows()
        self.MainUI()

    def MainUI(self):
        self.resize(300, 300)
        self.setWindowTitle("NFTinator 9000")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Select an Action")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setStyleSheet("font-size: 24px")
        layout.addWidget(self.label)

        btnCheckCollectionInfo = QPushButton("Check Collection Information")
        btnCheckCollectionInfo.clicked.connect(lambda: self.showWindow(self.windowCheckCollectionInfo))
        layout.addWidget(btnCheckCollectionInfo)

        btnCheckLaunchpad = QPushButton("Check ME Launchpad")
        btnCheckLaunchpad.clicked.connect(lambda: self.showWindow(self.windowCheckLaunchPad))
        layout.addWidget(btnCheckLaunchpad)

        btnCheckListed = QPushButton("Check Listed NFT's")
        btnCheckListed.clicked.connect(lambda: self.showWindow(self.windowCheckListedNFTs))
        layout.addWidget(btnCheckListed)

        btnFPAlerts = QPushButton("Setup FP Alerts")
        btnFPAlerts.clicked.connect(lambda: self.showWindow(self.windowSetupFPAlerts))
        layout.addWidget(btnFPAlerts)
        
        btnGenerateCollection = QPushButton("Generate NFT Collection")
        btnGenerateCollection.clicked.connect(lambda: self.showWindow(self.windowGenerateNFTCollection))
        layout.addWidget(btnGenerateCollection)
        
        btnExit = QPushButton("Exit")
        btnExit.clicked.connect(sys.exit)
        layout.addWidget(btnExit)


    def prepareWindows(self):
        self.windowCheckCollectionInfo = Window_Check_Collection_Info.WindowCheckCollectionInfo()
        self.windowCheckLaunchPad = Window_Check_Launchpad.WindowCheckLaunchpad()
        self.windowCheckListedNFTs = Window_Check_Listed_NFTs.WindowCheckListedNFTs()
        self.windowSetupFPAlerts = Window_Setup_FP_Alerts.WindowSetupFPAlerts()
        self.windowGenerateNFTCollection = Window_Generate_NFT_Collection.WindowGenerateNFTCollection()

    
    def showWindow(self, thisWindow):
        if thisWindow.isVisible():
            thisWindow.hide()
        else:
            thisWindow.show()


app = QApplication(sys.argv)
window = Window()
app.setStyleSheet("""
    QWidget {
        background-color: "#212529";
    }
    QLabel {
        color: "#FFFFFF";
    }
    QPushButton {
        font-size: 15px;
        background-color: "#F8F9FA";
    }
""")
window.show()
sys.exit(app.exec())
