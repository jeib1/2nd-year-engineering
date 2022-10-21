const int OUT_PIN = 8;
const int SAMPLE_TIME = 100;
unsigned long millisCurrent;
unsigned long millisLast = 0;
unsigned long millisElapsed = 0;
unsigned long minimo = 500;
unsigned long buttonLongPressMillis; 
unsigned long buttonPressDuration;   
int sampleBufferValue = 0;


void setup() {
  Serial.begin(9600);
}
void loop() {

  millisCurrent = millis();
  millisElapsed = millisCurrent - millisLast;

  if (digitalRead(OUT_PIN) == LOW) {
    buttonLongPressMillis = millisCurrent;
    sampleBufferValue++;  
  }
  buttonPressDuration = millisCurrent - buttonLongPressMillis;
  if (digitalRead(OUT_PIN) == LOW && buttonPressDuration > minimo) {
   

  }
  if (millisElapsed > SAMPLE_TIME) {
    Serial.println(sampleBufferValue);
    sampleBufferValue = 0;
    millisLast = millisCurrent;
  }

}
