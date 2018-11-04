#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6 
#define LED_COUNT 200

Adafruit_NeoPixel strip = Adafruit_NeoPixel(LED_COUNT, PIN, NEO_GRB + NEO_KHZ400);

/******************************************************/
void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}
/******************************************************/
void loop() {
  //Set an all Red string
  for(uint16_t i=0; i<strip.numPixels(); i++)
  { strip.setPixelColor(i,strip.Color(0,255,0)); }     
  strip.show();      
  delay(1500);
  
  //Set an all Green string
  for(uint16_t i=0; i<strip.numPixels(); i++)
  { strip.setPixelColor(i,strip.Color(255,0,0)); }     
  strip.show();      
  delay(1500);
  
  //Set an all Blue string
  for(uint16_t i=0; i<strip.numPixels(); i++)
  { strip.setPixelColor(i,strip.Color(0,0,255)); }     
  strip.show();      
  delay(1500);
  
  //Set an all White string
  for(uint16_t i=0; i<strip.numPixels(); i++)
  { strip.setPixelColor(i,strip.Color(255,255,255)); }     
  strip.show();      
  delay(1500);
  
}