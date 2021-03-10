# SQL Injection - инъекция кода, которая может разрушить базу данных. Техника WebHacking
import sqlite3

# Установка соединения с базой данных, если она существует, либо создаёт новую, если нет файла.
conn = sqlite3.connect('students_db.db')