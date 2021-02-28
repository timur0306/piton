import random

tries = 7 
guess = 0 ;
number = random.randint(1, 100) 

while(tries > 0 ):
  guess = int (input('угадай чесло от 1 до 100: ' ))
  if (guess == number):
   input ('you won ' )
   break
  else:
   tries = tries - 1  
   if (tries == 0):
     print ("game over" + str (number ))
     input('')
     break
   if (guess > number):
     print ( " слишком много, давай по менчше ")
   else :  
    print( " слишком маленькое число , давай пjбольше" )
    
   
   