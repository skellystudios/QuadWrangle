#include <stdlib.h>   
char in[3];

void loop() {
  Serial.begin(115200);
  Serial.flush();
  
  A7105_Setup(); //A7105_Reset();
  int startTime, waitTime, hubsanWait,finishTime;
  //Serial.println("Preinit");
  initialize();

  rudder = aileron = elevator = 0x7F; 
  
  startTime = micros();
  while (1) {
    
    
    /*
    if (Serial.available()>4) {
      if (Serial.read()!=23) {
        throttle = rudder =aileron = elevator = 0;
      } else {
      throttle=Serial.read();
      rudder=Serial.read();
      aileron=Serial.read();
      elevator=Serial.read();
      }
    } */
    
      //if (state!=0 && state!=1 & state!=128) 
//Serial.print("State: ");

  
    if (Serial.available()>2){
      
      Serial.println("serial in");
      in[0] = Serial.read();
      in[1] = Serial.read();
      in[2] = Serial.read();
      throttle = atoi(in);
      Serial.println(throttle);
   
    }
  
  
  
    hubsanWait = hubsan_cb();
//    finishTime=micros();
//    waitTime = hubsanWait - (micros() - startTime);
//    Serial.print("hubsanWait: " ); Serial.println(hubsanWait);
//    Serial.print("waitTime: " ); Serial.println(waitTime);
    //Serial.println(hubsanWait);
    delayMicroseconds(hubsanWait);
    startTime = micros();
    
  }

}

