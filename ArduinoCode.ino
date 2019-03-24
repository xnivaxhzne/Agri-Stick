#include <SPI.h> // for SPI LoRa
#include <LoRa.h> // For LoRa
#include <OneWire.h> // for DS18b20
#include <DallasTemperature.h> for DS18b20
#include<stdlib.h> // included for floatToString function
#include <DHT.h>; // For DHT22

#define DHTPIN 4     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); // Initialize DHT sensor for normal 16mhz Arduino

#define ONE_WIRE_BUS 5 // DS18b20 pin
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

String data_string = " ";
String data_string_p = " ";
String temp_string = " ";
String hum_string = " ";
String airtemp_string = " ";
String soilmois_string = " ";

float soil_temp_float; //Stores soil temperature value
float atm_hum;  //Stores humidity value
float atm_temp; //Stores atmospheric temperature value
int soil_mois; //Stores soil moisture value

// Function for converting float to string
String floatToString(float x, byte precision = 4) {
  char tmp[7];
  dtostrf(x, 0, precision, tmp);
  return String(tmp);
}

void setup()
{
  Serial.begin(9600);
  Serial.println(" Welcome to AgriStick Sensor Node ");
  Serial.println(" It includes \n Soil temperature,\n Soil moisture,\n Atmospheric temperature,\n Atmospheric humidity \n");

  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  dht.begin();
  sensors.begin();
  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");

    while (1);
  }
  LoRa.enableCrc();
}

void loop() {
  sensors.requestTemperatures();
  soil_temp_float = sensors.getTempCByIndex(0);
  temp_string = floatToString(soil_temp_float);

  atm_hum = dht.readHumidity();
  hum_string = floatToString(atm_hum);
  atm_temp = dht.readTemperature();
  airtemp_string = floatToString(atm_temp);

  soil_mois = analogRead(A1);
  soilmois_string = String(soil_mois);

  data_string = ( temp_string + soilmois_string + airtemp_string + hum_string );
  data_string_p = ( "Soil Temp: " + temp_string + " Soil Moist: " + soilmois_string + " Atmp Temp: " + airtemp_string + " Atmp Hum: " + hum_string );
  Serial.println(data_string_p);

  LoRa.beginPacket();
  uint8_t data[(data_string.length() + 2)];
  data_string.toCharArray(data, (data_string.length() + 2));
  LoRa.write(data, sizeof(data));
  Serial.println("Packet sent");
  LoRa.endPacket();

  delay(2000);
}
