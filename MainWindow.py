import sys


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from UIMainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.login_button.clicked.connect(self.nextpage)
        self.username = 'admin'
        self.password = 'admin'
        self.ui.logout_button.clicked.connect(self.logout)

        self.exchangerates = {
            "ლარი" : {"დოლარი": 0.37, "ევრო":0.34},
            "დოლარი" : {"ლარი" : 2.69, "ევრო" : 0.91},
            "ევრო" : {"ლარი": 2.98, "დოლარი": 1.10}
        }

        self.ui.convert_button.clicked.connect(self.convert)
        self.ui.clear_button.clicked.connect(self.clearall)

    def show(self):
        self.main_win.show()

    def nextpage(self):
        if self.ui.name.text()==self.username and self.ui.password.text()==self.password:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.ui.name.setText("")
            self.ui.password.setText("")
            self.ui.text.setText("გთხოვთ შეიყვანოთ სახელი და პაროლი")
        else:
            self.ui.text.setText("არასწორია! გთხოვთ სწორად შეიყვანოთ")

    def logout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def convert(self):
        fromcur = self.ui.from_box.currentText()
        tocur = self.ui.to_box.currentText()

        amount = self.ui.inputamount.text()

        if amount=='':
            self.ui.empty_label.setText("გთხოვთ შეიყვანოთ თანხა")
        elif fromcur==tocur:
            self.ui.empty_label.setText(f"{amount} {fromcur} უდრის {amount} {tocur}")
        else:
            new = float(amount) * self.exchangerates[fromcur][tocur]
            self.ui.empty_label.setText(f"{amount} {fromcur} უდრის {new} {tocur}")

    def clearall(self):
        self.ui.empty_label.setText("")
        self.ui.inputamount.setText("")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
