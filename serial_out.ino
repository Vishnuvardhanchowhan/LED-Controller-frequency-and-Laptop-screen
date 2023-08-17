using namespace std;
int r,g,b,f;
const int g_ledPin = 13;
const int b_ledPin = 12;
const int r_ledPin = 11;

void led(int f, int *r, int *g, int *b){
    if (400 <= f < 484){
        *r = 255;
        *g = 0;
        *b = 0;}
    else if (484 <= f < 508){
        *r = 255;
        *g = 165;
        *b = 0;}
    else if (508 <= f < 526){
        *r = 255;
        *g = 255;
        *b = 0;}
    else if (526 <= f < 606){
        *r = 0;
        *g = 255;
        *b = 0;}
    else if (606 <= f < 668){
        *r = 0;
        *g = 0;
        *b = 255;}
    else if (668 <= f < 720){
        *r = 75;
        *g = 0;
        *b = 130;}
    else if (720 <= f < 800){
        *r = 238;
        *g = 130;
        *b = 238;}
    else{
        *r = 255;
        *g = 255;
        *b = 255;} 
}
void setup() {
  pinMode (r_ledPin, OUTPUT);
  pinMode (b_ledPin, OUTPUT);
  pinMode (g_ledPin, OUTPUT);
 Serial.begin(115200);
 Serial.setTimeout(1);
}
void loop() {
 while (Serial.available()){
 f = Serial.readString().toInt();
led(f,&r,&g,&b);
 analogWrite(r_ledPin, r);
 analogWrite(g_ledPin, g);
 analogWrite(b_ledPin, b);
 Serial.print(f);
 }
 
}
