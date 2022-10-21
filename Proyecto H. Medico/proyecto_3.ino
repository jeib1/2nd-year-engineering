int reading = 0;
int mic = 8;
int buz = 7;
boolean beep = 1;
void setup() {
  pinMode(mic, INPUT);
  pinMode(mic, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  reading = analogRead(mic);
  Serial.begin(9600);
  if (reading > 20) {
    delay(500);
    for (int i = 0; i<1000; i++) {
      reading = analogRead(mic);
      delay(1); {
        beep = !beep;
        break;
      }
    }
  }
  if (beep==1) {
    tone(7,200,500);
  }
  else {
    noTone(7);
  }
}
