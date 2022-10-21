int melody[] = {
  150
};
int noteDurations[] = {
  3};

const int buzzpin=7; // 
const int soundpin=8;
const int threshold=500; // sets threshold value for sound sensor
void setup() {
Serial.begin(9600);
pinMode(buzzpin,OUTPUT);
pinMode(soundpin,INPUT);
}

void loop() {
int soundsens=analogRead(soundpin); // reads analog data from sound sensor
if (soundsens>=threshold) {
  delay(5000);
  if (soundsens>=threshold) {
    for (int thisNote = 0; thisNote < 1; thisNote=thisNote+1) {
       int noteDuration = 1000 / noteDurations[thisNote];
       tone(7, melody[thisNote], noteDuration);
       int pauseBetweenNotes = noteDuration * 1.30;
       delay(5000);
    noTone(7);

  }
}

}
}
