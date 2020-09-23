import sys,datetime
from PyQt5 import QtGui,QtCore,QtWidgets
import index,BillReciept,custRegister,addProduct
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel


class Ledger(QtWidgets.QMainWindow,index.Ui_MainWindow,custRegister.Ui_Dialog):
        
    def closeIt(self):
        print("close")
        self.close()

    def getProductDetails(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('ledger')
        db.open()
        query = QSqlQuery()
        qu1='select count(*) from product'
        query.exec_(qu1)
        while query.next():
            count = query.value(0)
        qu = 'select * from product'
        query.exec_(qu)
        index = 0
        self.tableWidget.setRowCount(count)
        while query.next():
            self.tableWidget.setItem(index,0,QTableWidgetItem(str(query.value(1))))
            self.tableWidget.setItem(index,1,QTableWidgetItem(str(query.value(3))))
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            index += 1
        db.close()
         

    def __init__(self,parent=None):
        super(Ledger,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(640, 480)
        self.getProductDetails()
        self.close()

class Customer(QtWidgets.QDialog,custRegister.Ui_Dialog):
    def __init__(self,parent=None):
        super(Customer,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.insertData)
        self.setFixedSize(640, 480)
    
    def insertData(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("ledger")
        if db.open():
            print("connnected")

        name =str(self.lineEdit.text())
        add =str(self.textEdit.toPlainText())
        mobile =str(self.lineEdit_3.text())
        query = QSqlQuery()
        qu ="insert into Customer (NAME,ADDRESS,MobileNo) VALUES ('" +name+ "','" +add+ "'," +mobile+") "
        query.exec_(qu)
        db.close()
        msg = QMessageBox()
        msg.setText("Data inserted successfully....!!!")
        msg.setWindowTitle("Message")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        self.close()


class AddProduct(QtWidgets.QDialog,addProduct.Ui_Dialog):
    def __init__(self,parent=None):
        super(AddProduct,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.insertData)
        self.setFixedSize(640, 480)

    def insertData(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("ledger")
        if db.open():
            print("connnected")

        name = str(self.lineEdit.text())
        qty  = str(self.spinBox.text())
        query = QSqlQuery()
        qu ="insert into product (productName,ProductAvailQuantity) VALUES ('" +name+ "','" +qty+"')"
        query.exec_(qu)
        db.close()
        msg = QMessageBox()
        msg.setText("Data inserted successfully....!!!")
        msg.setWindowTitle("Message")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        self.close()


class Bill(QtWidgets.QDialog,BillReciept.Ui_Dialog):
    def __init__(self,parent=None):
        super(Bill,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(640, 480)
        x = datetime.datetime.now()
        date1= x.strftime("%d-%b-%Y")
        self.lineEdit.setText(date1)
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("ledger")
        if db.open():
            qry = QSqlQuery(db)
            qry.prepare('select * from customer')
            qry.exec()
            cust = []
            while qry.next():
                cust.append(str(qry.value(0)) + '-' + str(qry.value(1)))
            self.comboBox.addItems(cust)
            print(cust)

        self.index = -1    
        self.total = 0
        self.pushButton_2.clicked.connect(self.TakeInputs)

    def TakeInputs(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("ledger")
        if db.open():
            qry = QSqlQuery(db)
            qry.prepare('select ProductName from product')
            qry.exec()
            prod = []
            while qry.next():
                prod.append(str(qry.value(0)))

        product, done1 = QtWidgets.QInputDialog.getItem(
                self, 'Input Dialog', 'Select Product:', prod)
        qty, done2 = QtWidgets.QInputDialog.getInt(
                self, 'Input Dialog', 'Enter Quantity')
        price, done3 = QtWidgets.QInputDialog.getDouble(
                self, 'Input Dialog', 'Enter Price Per Quantity')
        rowlist = [product,qty,price,qty*price]
        self.total += (qty*price)
        self.lineEdit_2.setText(str(self.total))
        self.addTableRow(self.tableWidget, rowlist)

    def addTableRow(self, tableWidget,rowlist):
        row = tableWidget.rowCount()
        tableWidget.setRowCount(row+1)
        col = 0
        print(rowlist)
        for item in rowlist:
            cell = QTableWidgetItem(str(item))
            tableWidget.setItem(row, col, cell)
            col += 1
    

def main():
    app = QApplication(sys.argv)
    ledger = Ledger()
    cust = Customer()
    prod = AddProduct()
    bill = Bill()
    ledger.pushButton.clicked.connect(cust.show)
    ledger.pushButton_3.clicked.connect(prod.show)
    ledger.pushButton_4.clicked.connect(ledger.getProductDetails)
    ledger.pushButton_2.clicked.connect(bill.show)

    ledger.show()
    app.exec_()
    sys.exit()


if __name__ == '__main__':
    main()


