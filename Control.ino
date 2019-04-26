#define outputA 6
#define outputB 7
#define pwm 5
#define dir 3
#define cons 0
#define wait 2
#define runm A2
#define stopm A3
int i;

#include <Stepper.h>

const int stepsPerRevolution = 2000;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 11, 12);
int pwm_value = 60;
int counter = 0; 
 int aState;
 int aLastState; 
 int a=0,b=300;
 int pre_val =0;
int c1,c2;
int b1;
int clockwise()
{analogWrite(pwm,pwm_value);
  digitalWrite(dir,HIGH);
  
}
int anticlockwise()
{analogWrite(pwm,pwm_value);
  digitalWrite(dir,LOW);
}

int stop()
{
  analogWrite(pwm,0);
}


void setup() {
   pinMode(cons,OUTPUT);
   pinMode(wait,OUTPUT);
   pinMode(runm,OUTPUT);
   pinMode(stopm,OUTPUT);
   myStepper.setSpeed(180);
  pinMode (outputA,INPUT);
   pinMode (outputB,INPUT);
   // Reads the initial state of the outputA
   aLastState = digitalRead(outputA);  
  Serial.begin(9600);
  pinMode(pwm,OUTPUT);
pinMode(dir,OUTPUT);
pinMode(13,OUTPUT);
pinMode(A0,INPUT);
int l= analogRead(A0);
  
}
void loop() {
  int k = Serial.read();
  digitalWrite(stopm,HIGH);
  if(k=='1')
  {
    
for (int j=1;j<=200;j++){
   digitalWrite(runm,HIGH);
//  step one revolution in the other direction:
  //Serial.println("counterclockwise");
  myStepper.step(stepsPerRevolution);
  //delay(10);
 /* aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       a ++;
     } else {
       b --;
     }
     Serial.print("Position: ");
     Serial.println(a);
     Serial.println(b);
     
   } 
   aLastState = aState; 
 if(a<160)
  {
     clockwise();
     
  }

 else if(a>=160 && a<240)
  {
    anticlockwise();
  }
  else if(a=240) 
  {
    a=0;
  }*/
}
for(int i=1;i<=100;i++)
  {  digitalWrite(runm,HIGH);
    myStepper.step(-stepsPerRevolution);
  //delay(10);
 /*   aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       a ++;
     } else {
       b --;
     }
     Serial.print("Position: ");
     Serial.println(a);
     Serial.println(b);
     
   } 
   aLastState = aState; 
 if(a<160)
  {
     clockwise();
     
  }

 else if(a>=160 && a<240)
  {
    anticlockwise();
  }
  else 
  {
    a=0;
    myStepper.setSpeed(180);
  }
  */
  }

  }
 if(k=='2')
 {
  digitalWrite(3,LOW);
  digitalWrite(5,LOW);
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  
 }

 if(k=='3')
 {
  int ch=0;
  if(ch<=1)
  { digitalWrite(runm,HIGH);
    for(int i=1;i<=50;i++)
  {digitalWrite(runm,HIGH);
    myStepper.step(-stepsPerRevolution);
  delay(10);}

  delay(1000);
/*for (int j=1;j<=200;j++){
//  step one revolution in the other direction:
  Serial.println("counterclockwise");
  myStepper.step(stepsPerRevolution);
  delay(10);}*/
  }
  for(i=1;i<10;i++)
  {
   
  aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       a ++;
     } else {
       b --;
     }
    // Serial.print("Position: ");
   //  Serial.println(a);
   //  Serial.println(b);
     
   } 
   aLastState = aState; 
   if(a<160)
  {
     clockwise();
     digitalWrite(runm,HIGH);
  }

 else if(a>=160 && a<240)
  {
    anticlockwise();
    digitalWrite(runm,HIGH);
  }
 else if(a=240)
 {
  a=0;
 }
  }
 }
 
if(k=='8')
{ 
  c2= analogRead(A0);
  int c3 = map(c2,0,1024,0,128);
c1= 64-c3; 
         
if(c1>0)
{
  digitalWrite(dir,HIGH);
  analogWrite(pwm,pwm_value); 
  delayMicroseconds(c1);  
  analogWrite(pwm,pwm_value); 
  delayMicroseconds(c2);
  digitalWrite(wait,HIGH);
}
if(c1<0)
{
   digitalWrite(dir,LOW);
  analogWrite(pwm,pwm_value); 
  delayMicroseconds(c1);  
  analogWrite(pwm,pwm_value); 
  delayMicroseconds(c2);
  digitalWrite(wait,HIGH);
}
if(c1=0)
{
  digitalWrite(dir,LOW);
  digitalWrite(pwm,LOW);
  digitalWrite(wait,HIGH);
}

 
}

if(k=='5')
{
  for(int i=1;i<=100;i++)
  {digitalWrite(runm,HIGH);
    myStepper.step(stepsPerRevolution);
  delay(10);}
  for(int i=1;i<=100;i++)
  {digitalWrite(runm,HIGH);
    myStepper.step(-stepsPerRevolution);
  delay(10);}
  
}

if(k=='9')
{
  for(i=1;i<1000;i++)
  {
  digitalWrite(stopm,HIGH);
  digitalWrite(wait,LOW);
  digitalWrite(runm,LOW);
  delay(100);
  digitalWrite(stopm,LOW);
  digitalWrite(wait,HIGH);
  digitalWrite(runm,LOW);
  delay(100);
  digitalWrite(stopm,LOW);
  digitalWrite(wait,LOW);
  digitalWrite(runm,HIGH);
  delay(100);
  }
}
}
/*int backward()
{
  // step one revolution  in one direction:
  //Serial.println("clockwise");
  for(int i=1;i<=200;i++)
  {
    myStepper.step(stepsPerRevolution);
  delay(10);}
}
int forward()
{
  for (int j=1;j<=200;j++){
//  step one revolution in the other direction:
  //Serial.println("counterclockwise");
  myStepper.step(-stepsPerRevolution);
  delay(10);}
  }*/

