#include <stdio.h>
#include <wiringPi.h>
 
char KEY = 29;
 
int main()
{
    if (wiringPiSetup() < 0)return 1 ;
    // Sets the pin as input.
    pinMode(KEY,INPUT);
    // Sets the Pull-up mode for the pin.
    pullUpDnControl(KEY, PUD_UP);
    printf("Key Test Program!!!\n");
    while(1)
    {  
        if (digitalRead(KEY) == 0) 
        {  
            printf ("KEY PRESS\n") ;
            // Returns the value read at the given pin. It will be HIGH or LOW (0 or 1).
            while(digitalRead(KEY) == 0)
                delay(100);
        }  
        delay(100);
    }  
}
