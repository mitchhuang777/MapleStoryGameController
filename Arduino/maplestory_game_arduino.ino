int pinDown = 5;       // 下方向腳位
int pinUp = 4;         // 上方向腳位
int pinRight = 7;      // 右方向腳位
int pinLeft = 6;       // 左方向腳位
int pinPedal1 = 10;    // 腳踏板1腳位
int pinPedal2 = 11;    // 腳踏板2腳位
int pinPedal3 = 12;    // 腳踏板3腳位

void setup() {
  Serial.begin(9600);
  pinMode(pinDown, INPUT);
  pinMode(pinUp, INPUT);
  pinMode(pinRight, INPUT);
  pinMode(pinLeft, INPUT);
  pinMode(pinPedal1, INPUT_PULLUP);
  pinMode(pinPedal2, INPUT_PULLUP);
  pinMode(pinPedal3, INPUT_PULLUP);
}

void loop() {
  int downState = digitalRead(pinDown);
  int upState = digitalRead(pinUp);
  int rightState = digitalRead(pinRight);
  int leftState = digitalRead(pinLeft);
  int pedalState1 = digitalRead(pinPedal1);
  int pedalState2 = digitalRead(pinPedal2);
  int pedalState3 = digitalRead(pinPedal3);

  Serial.print("Down: ");
  Serial.print(downState);
  Serial.print(" | Up: ");
  Serial.print(upState);
  Serial.print(" | Right: ");
  Serial.print(rightState);
  Serial.print(" | Left: ");
  Serial.print(leftState);
  Serial.print(" | Pedal1: ");
  Serial.print(pedalState1);
  Serial.print(" | Pedal2: ");
  Serial.print(pedalState2);
  Serial.print(" | Pedal3: ");
  Serial.print(pedalState3);

  Serial.println();

  delay(100);  // 延遲一段時間以便穩定讀取
}
