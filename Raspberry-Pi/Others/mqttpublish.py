#publish.single("agristick1", "\"1,2019-03-21 20:56:09.300794\",31.25,695,30.5,67.5", hostname="13.232.96.33",auth = {'username':"ubuntu", 'password':"ceglaeee"})
import paho.mqtt.publish as publish
import sqlite3

DB_Name = "/home/pi/FYP/agristick.db"

publish.single("agristick1", "\"2019-03-24 21:56:09.300794\",32.25,595,33.5,57.5", hostname="13.232.96.33",auth = {'username':"ubuntu", 'password':"ceglaeee"})


