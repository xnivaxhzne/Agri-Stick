import paho.mqtt.subscribe as subscribe
import sqlite3

# SQLite DB Name
DB_Name =  "/home/ubuntu/flaskapp/agristick.db"
#sqliteConnection    = sqlite3.connect(DB_Name)
#sqliteConnection.execute('pragma journal_mode=wal;')
#cursorObject   = sqliteConnection.cursor()

#===============================================================

def on_message(client, userdata, message):
    #print("%s %s" % (message.topic, message.payload))
    mqttmessage = str(message.payload)
    topic = str(message.topic)
    mqttmessage = mqttmessage[2:-1]
    print(mqttmessage)
    dt = mqttmessage[0:26]
    st = float(mqttmessage[27:34])
    sm = int(mqttmessage[35:38])
    at = float(mqttmessage[39:46])
    ah = float(mqttmessage[47:54])

    print(mqttmessage)
    print(dt)
    print(st)
    print(sm)
    print(at)
    print(ah)

    sqliteConnection    = sqlite3.connect(DB_Name)
    cursorObject        = sqliteConnection.cursor()
    sqliteConnection.execute('pragma journal_mode=wal;')
    cursorObject.execute("INSERT INTO DATASEN (date_time,soil_temp,soil_moist,atmp_temp,atmp_hum) VALUES(?,?,?,?,?)",[dt,st,sm,at,ah])
    cursorObject.execute("COMMIT")
    cursorObject.close()
    print ("Inserted Data into DATASEN Database.")

topics = ["agristick1","agristick2"]
subscribe.callback(on_message, topics, hostname="13.232.96.33",auth = {'username':"ubuntu", 'password':"ceglaeee"}) #10.134.67.132
