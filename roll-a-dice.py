import random

response ="y"

en =input("Enter y to continue or n to exit")

while response =='y':
    no = random.randint(1,6)
    if response == 'n':
        break

    if no == 1:
      print("[-----]"+
            "[     ]"+
            "[  0  ]"+
            "[     ]"+
            "[-----]")
      en =''

    elif no ==2:
        print("[-----]"+
            "[     ]"+
            "[ 0 0 ]"+
            "[     ]"+
            "[-----]")
        en =''  

    elif no ==3:
         print("[-----]",
            "[     ]",
            "[0 0 0]",
            "[     ]",
            "[-----]") 
         en =''

    elif no ==4:           
        print("[-----]"+
              "[0   0]"+
              "[     ]"+
              "[0   0]"+
              "[-----]")
        en ='' 

    elif no ==5:
        print("[-----]"+
              "[0   0]"+
              "[  0  ]"+
              "[0   0]"+
              "[-----]")    
        en =''   

    elif no ==6:
         print("[------]"+
               "[ 0  0 ]"+
               "[ 0  0 ]"+
               "[ 0  0 ]"+
               "[------]")   
         en =''                 
           