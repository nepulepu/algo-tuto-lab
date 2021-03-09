check={
    "rock":"scissors",
    "scissors":"paper",
    "paper":"rock"
}
while(True):
    p1=input("Oh P1. rock,paper,or scissor?: ")
    p2=input("Oh P2. rock,paper,or scissor?: ")

    if p1==p2:
        print("ITS DRAW!")
    elif check.get(p1)==p2:
        print("P1 WINS!")
    else:
        print("P2 WINS!")
    
    a=input("Quit? : ")

    if a=="yes":
        break
        


