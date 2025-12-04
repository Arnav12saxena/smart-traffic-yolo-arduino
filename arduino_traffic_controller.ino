int red = 13;
int yellow = 12;
int green = 11;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  Serial.begin(9600);
  allOff();
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    int redTime = 0, yellowTime = 0, greenTime = 0;

    // Parse timings: format "5000,2000,3000"
    sscanf(input.c_str(), "%d,%d,%d", &redTime, &yellowTime, &greenTime);

    // Update lights based on received durations
    allOff();
    digitalWrite(red, HIGH);
    delay(redTime);

    allOff();
    digitalWrite(yellow, HIGH);
    delay(yellowTime);

    allOff();
    digitalWrite(green, HIGH);
    delay(greenTime);

    allOff();
    delay(500);  // optional pause before next command
  }
}

void allOff() {
  digitalWrite(red, LOW);
  digitalWrite(yellow, LOW);
  digitalWrite(green, LOW);
}
