#include <MeAuriga.h>

// get encoder slots
MeEncoderOnBoard Encoder_1(SLOT1);
MeEncoderOnBoard Encoder_2(SLOT2);


//ISRs take in port reading. 
void isr_process_encoder1(void)
{
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    Encoder_1.pulsePosMinus();
  }
  else
  {
    Encoder_1.pulsePosPlus();;
  }
}

void isr_process_encoder2(void)
{
  if(digitalRead(Encoder_2.getPortB()) == 0)
  {
    Encoder_2.pulsePosMinus();
  }
  else
  {
    Encoder_2.pulsePosPlus();
  }
}

void setup()
{
  attachInterrupt(Encoder_1.getIntNum(), isr_process_encoder1, RISING);
  attachInterrupt(Encoder_2.getIntNum(), isr_process_encoder2, RISING);
  Serial.begin(115200);
  
  //Set PWM 8KHz
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);

//PIDs from example library 
  Encoder_1.setPulse(9);
  Encoder_2.setPulse(9);
  Encoder_1.setRatio(39.267);
  Encoder_2.setRatio(39.267);
  Encoder_1.setPosPid(0.18,0,0);
  Encoder_2.setPosPid(0.18,0,0);
  Encoder_1.setSpeedPid(0.18, 0, 0);
  Encoder_2.setSpeedPid(0.18, 0, 0);

  //TODO:


  //Set up HID read to replace serial inputs. 

  //Send info to python app for HUD?   


}

void loop()
{

    //---------------------------------- REPLACE WITH IF statement that takes input thresholds based on 16 bit value from wheel and 8 bit values from accel/brake ---------------------
    
  // if(Serial.available())
  // {
  //   char a = Serial.read();
  //   switch(a)
  //   {
  //     case '0':
  //     Encoder_1.runSpeed(0);
  //     Encoder_2.runSpeed(0);
  //     break;
  //     case '1':
  //     Encoder_1.runSpeed(100);
  //     Encoder_2.runSpeed(-100);
  //     break;
  //     case '2':
  //     Encoder_1.runSpeed(200);
  //     Encoder_2.runSpeed(-200);
  //     break;
  //     case '3':
  //     Encoder_1.runSpeed(255);
  //     Encoder_2.runSpeed(-255);
  //     break;
  //     case '4':
  //     Encoder_1.runSpeed(-100);
  //     Encoder_2.runSpeed(100);
  //     break;
  //     case '5':
  //     Encoder_1.runSpeed(-200);
  //     Encoder_2.runSpeed(200);
  //     break;
  //     case '6':
  //     Encoder_1.runSpeed(-255);
  //     Encoder_2.runSpeed(255);
  //     break;
  //     default:
  //     break;
  //   }
  // }


  Encoder_1.loop();
  Encoder_2.loop();
  Serial.print("Speed 1:");
  Serial.print(Encoder_1.getCurrentSpeed());
  Serial.print(" ,Speed 2:");
  Serial.println(Encoder_2.getCurrentSpeed());
}
