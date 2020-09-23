This project contains basic implementation of PyQt5.
Windows are made using QT Designer tool

Follow below only for Linux distros:
1)Open terminal and create a folder for your project:
2)Create an environment:
	 python3 -n venv environment_name
3)Activate Environment:
	souce environment_name/bin/activate
4)Install PyQt5:
	sudo apt-get install python3-pyqt5
5)You can install Designer (Ubuntu Linux) with:
	sudo apt-get install qttools5-dev-tools
	sudo apt-get install qttools5-dev
6)Install slite3:
	sudo apt-get install sqlite3
7)Install sqlite3 browser:
	sudo apt-get install sqlitebrowser

Now you are ready for your project:

8)Open QT Designer:
	go to /usr/lib/qt5/bin and then type ./designer it will open QT Designer where you can build you windows.
	save this file in your folder.File will have .ui extension.
9)Generating .py using .ui:
	pyuic5 -x file_name.ui -o file_name.py
	It will generate file .py file which can be imported into your main .py file.

Tables:
CREATE TABLE "customer" (
	"CustomerId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Name"	TEXT,
	"Address"	TEXT,
	"MobileNo"	INTEGER
)

CREATE TABLE "product" (
	"productId"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"ProductName"	TEXT,
	"ProductPrice"	INTEGER,
	"ProductAvailQuantity"	INTEGER
)


