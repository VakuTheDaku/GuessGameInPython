import random

def main():
    num=random.randint(100,999)
    a=int(num%10)
    b=int(num/100)
    c=int((num/10)%10)
    print("I have a three digit number with me. Can you try guessing it?")
    while(a==b or a==c or c==b):
        num=random.randint(100,999)
        a=int(num%10)
        b=int(num/100)
        c=int((num/10)%10)
    print("CLOSE : if any number is correctly guessed but in the wrong position")
    print("MATCH : one of the number guessed is correct and in the same position")
    print("NOPE : When none of the numbers guessed is correct")
    number=str(num)
    print("Enter your guess ")
    n=input()
    div=0
    moves=0
    while(n!=number):
        moves+=1
        div=0
        print("Result :")
        for letter in n:
            for le in  number:
                if(letter==le and n.index(letter)==number.index(le)):
                    
                    div=1
                elif(letter==le):
                    
                    div=2
        if(div==0):
            print("NOPE")
        if(div==1):
            print("MATCH")
        if(div==2):
            print("CLOSE")
        print("Guess a new number (for exiting just give 'EXIT' as your guess)")
        n=input()
        if(n=="EXIT"):

            break;        
    if(div!=0):
        print("YOU WON!")
        print("Number of moves = {}".format(moves))                    
    print("The number was {}".format(num))
if __name__=="__main__":
    main()