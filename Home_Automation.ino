#include<dht.h>
dht DHT;
#define DHT11_PIN 10
#define RELAY1 4
#define RELAY2 5
#define RELAY3 6
#define RELAY4 7
String BLT_input;
String BLT_mode;
void setup() {
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);
  pinMode(RELAY3, OUTPUT);
  pinMode(RELAY4, OUTPUT);
  pinMode(DHT11_PIN,INPUT);
  digitalWrite(RELAY1,HIGH);
  digitalWrite(RELAY2,HIGH);
  digitalWrite(RELAY3,HIGH);
  digitalWrite(RELAY4,HIGH);
    
   Serial.begin(9600);       // start serial communication at 9600bps
}
void loop() {
  if( Serial.available() )       // if data is available to read
  {
    BLT_mode = Serial.readString();         // read it and store it in BLT_input
  }
 
  //1st block
  if(BLT_mode=="auto")
  {  
  int chk = DHT.read11(DHT11_PIN);
  Serial.println("auto mode");
  Serial.println(" Humidity " );

  Serial.println(DHT.humidity, 1);

  Serial.println(" Temparature ");

  Serial.println(DHT.temperature, 1);
  if(DHT.temperature >=31)
  {
    Serial.println("fan on");
    digitalWrite(RELAY2,LOW);
  }
  else
  {
  Serial.println(" fan off");
  digitalWrite(RELAY2,HIGH);
  }
  delay(1000);
   
  
  }
  //-----------------user mode-------------------------
 
 else if(BLT_mode=="user")       // if data is available to read
    {
      BLT_input = Serial.readString();
     if( BLT_input == "d11")              
    {
      digitalWrite(RELAY1,LOW);  // turn ON the relay
    } 
    else if(BLT_input =="d10")
    { 
      digitalWrite(RELAY1, HIGH);   // otherwise turn it OFF
    }
    else if( BLT_input == "d21")               
    {
      digitalWrite(RELAY2, LOW);  // turn ON the relay
    } 
    else if(BLT_input =="d20")
    { 
      digitalWrite(RELAY2, HIGH);   // otherwise turn it OFF
    }
    else if( BLT_input == "d31")                 
   {
      digitalWrite(RELAY3, LOW);  
   }
   else if(BLT_input =="d30")
    { 
    digitalWrite(RELAY3, HIGH);   // otherwise turn it OFF
    }
    else if( BLT_input == "d41")               // if  "device4 on"was received
    {
    digitalWrite(RELAY4, LOW);  // turn ON the relay
    } 
    else if(BLT_input =="d40")
   { 
     digitalWrite(RELAY4, HIGH);   // otherwise turn it OFF
   } 
  
  }
   

}
