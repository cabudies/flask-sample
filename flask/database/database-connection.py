import sqlite3

connection = sqlite3.connect("database/restaurant.db")

TABLE_NAME = "restaurant"
MENU_ID = ""
MENU_NAME = ""
MENU_PRICE = ""
MENU_QUANTITY = ""

connection.execute("CREATE TABLE IF NOT EXISTS ")