import sys
from PyQt5.QtWidgets import QDialog, QApplication, QDialogButtonBox
from demoLineEdit import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
        # Get the individual buttons from the QDialogButtonBox
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.Cancel)
        
        # Connect the clicked signals to the dispmessage method
        ok_button.clicked.connect(self.dispmessage)
        cancel_button.clicked.connect(self.dispmessage)

        # ok_button.clicked.disconnect()


        # Disconnect the default accepted signal of the Ok button
        
        self.show()

    def dispmessage(self):
        self.ui.label.setText("Hello " + self.ui.lineEdit.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())