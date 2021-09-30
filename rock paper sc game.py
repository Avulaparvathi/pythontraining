p1=input("enter the choice")
p2=input("enter the choice")
while True:
 if p1==p2:
    print("tie")
 elif p1=="rock":
    if p2=="scissors":
        print("congratulatipns to p1")
    else:
        print("congratulation to p2")
 elif p1=="paper":
    if p2=="rock":
        print("congratulations to p1")
    else:
        print("congratulations to p2")
 elif p1=="scissors":
    if p2=="rock":
        print("congratulations to p2")
    else:
        print("congratulations to p1")
 playagain=input("play again? yes or no")
 if playagain!="yes":
     break


def rpsgame(p1,p2):
  while True:
    if p1 == p2:
       print("tie")
    elif p1 == "rock":
           if p2 == "scissors":
                print("congratulatipns to p1")
           else:
                print("congratulation to p2")
    elif p1 == "paper":
           if p2 == "rock":
                print("congratulations to p1")
           else:
                print("congratulations to p2")
    elif p1 == "scissors":
           if p2 == "rock":
                print("congratulations to p2")
           else:
                print("congratulations to p1")
    playagain = input("play again? yes or no")
    if playagain != "yes":
        break
  return 0
rpsgame("rock","paper")