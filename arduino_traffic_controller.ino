int RA = 13;
int YA = 12;
int GA = 11;

int RB = 10;
int YB = 9;
int GB = 8;

void allOff() {
  digitalWrite(RA, LOW);
  digitalWrite(YA, LOW);
  digitalWrite(GA, LOW);

  digitalWrite(RB, LOW);
  digitalWrite(YB, LOW);
  digitalWrite(GB, LOW);
}

void roadAGreen() {
  allOff();

  digitalWrite(GA, HIGH);
  digitalWrite(RB, HIGH);
}

void roadBGreen() {
  allOff();

  digitalWrite(RA, HIGH);
  digitalWrite(GB, HIGH);
}

void setup() {
  pinMode(RA, OUTPUT);
  pinMode(YA, OUTPUT);
  pinMode(GA, OUTPUT);

  pinMode(RB, OUTPUT);
  pinMode(YB, OUTPUT);
  pinMode(GB, OUTPUT);

  Serial.begin(9600);

  roadBGreen(); // default state
}

void loop() {

  if (Serial.available()) {

    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "A") {
      roadAGreen();
    }

    else if (cmd == "B") {
      roadBGreen();
    }
  }
}
