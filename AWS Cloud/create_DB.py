import sqlite3

# SQLite DB Name
DB_Name =  "agristick.db"

# SQLite DB Table Schema for sensor data raw value
TableSchema_SD="""
drop table if exists DATASEN ;
create table DATASEN (
  id integer primary key autoincrement,
  date_time text,
  soil_temp float,
  soil_moist int,
  atmp_temp float,
  atmp_hum float
);

"""


#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables for sensor data raw value
sqlite3.complete_statement(TableSchema_SD)
curs.executescript(TableSchema_SD)


#Close DB
curs.close()
conn.close()
