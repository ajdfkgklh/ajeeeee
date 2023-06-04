/*=================================================================*/    
    # include <Servo.h>
    # define IRE 7 // IR at end point
    # define SA  6 // Servo a
    # define SB  5 // Servo b 
    # define SC  9 // Servo b 
    # define IN1 4 // Motor pin LOW to stop
    # define MS  3 // Motor speed control PWM pin
    # define IRC 2 // IR at camera point
    # define kochi 45
    # define Kottayam 100
 /*=================================================================*/
    Servo servoA;
    Servo servoB;
    Servo servoC;
/*=================================================================*/
    int val=0; 
    int i=0;//Motor a pos hand
    int j=180;//Motor b pos aRM
    int start =1;
    int box = 0;
/*=================================================================*/
    void Serial_test();
    void open_hand();
    void close_hand();
    void arm_to_convair();
    void arm_to_collection_tower();
    void move_convair();
    void stop_convair();
    void pick_box();
/*=================================================================*/
    void setup() 
    {
      Serial.begin(9600);
      Serial.println("Automated parcel sorting");
      pinMode(IN1,OUTPUT);
      pinMode(IRC,INPUT);
      pinMode(IRE,INPUT);
      pinMode(MS,OUTPUT);
      analogWrite(MS, 0);
      digitalWrite(IN1,LOW);
      servoA.attach(SA);
      servoB.attach(SB);
      servoC.attach(SC);
      servoA.write(j);
      servoB.write(i);
      servoC.write(kochi);
    }
/*=================================================================*/   
    void loop() 
    {
      Serial_test();
      if(start ==1)
      {
        if(digitalRead(IRE)==0 && box ==0)
        {
          box =1;
          delay(800);
          stop_convair();
          pick_box();
          while(digitalRead(IRC) == 1)
            {
               move_convair();
               delay(50);
            }
            stop_convair();
        }
      }
    }
/*=================================================================*/
    void Serial_test()
    {
      char x;
      if(Serial.available())
      {
          x=Serial.read();
          if(x=='a')
          {  
            start =1;         
            pick_box();
            while(digitalRead(IRC) == 1)
            {
               move_convair();
               delay(50);
            }
            stop_convair();
          }
          if(x=='b')
          { 
            stop_convair();
          }
          if(x=='c')
          { 
            pick_box();
          }
          if(x=='d')
          {
            move_convair();
          }
          if(x=='m')
          {
            servoC.write(Kottayam);
            delay(150);
            box=0;
          }
          if(x=='n')
          {
            servoC.write(kochi);
            delay(150);
            box=0;
          }
          if(x=='s')
          { 
            start =0;
            box=0;
            stop_convair();
          }
          
      }
    }
/*=================================================================*/
    void open_hand()
    {      
      if(i<20)
      {
        Serial.println("Hand Already opened");
      }
      else
      {
         Serial.println("hand opening");
         for(i=150;i>=0;i--)
         {
           servoB.write(i);
           delay(8);
         }
      }
    }
/*=================================================================*/
    void close_hand()
    {
      if(i>140)
      {
        Serial.println("Hand Already Closed");
      }
      else
      {
         Serial.println("hand closing");
         for(i=0;i<=150;i++)
         {
           servoB.write(i);
           delay(8);
         }
      }
    }
/*=================================================================*/
    void arm_to_convair()
    {
      if(j>140)
      {
        Serial.println("Hand Already At convair");
      }
      else
      {
         Serial.println("Moving to convair");
         for(j=90;j<=180;j++)
         {
           servoA.write(j);
           delay(8);
         }
      }
    }
/*=================================================================*/
    void arm_to_collection_tower()
    {
      if(j<100)
      {
        Serial.println("Hand Already At Collection tower");
      }
      else
      {
         Serial.println("Moving to Collection tower");
         for(j=180;j>=90;j--)
         {
           servoA.write(j);
           delay(8);
         }
      }
    }
/*=================================================================*/
    void pick_box()
    {
      box=1;
            open_hand();
            delay(1000);
            arm_to_collection_tower();
            delay(1000);
            close_hand();
            delay(1000);
            arm_to_convair();
            delay(1000);
            open_hand();
    }
/*=================================================================*/
    void move_convair()
    {
            Serial.println("Moving Convair");
            analogWrite(MS, 255);
            digitalWrite(IN1,HIGH);
    }
/*=================================================================*/
    void stop_convair()
    {
            Serial.println("Stop Convair");
            analogWrite(MS, 255);
            digitalWrite(IN1,LOW);
    }
/*=================================================================*/
