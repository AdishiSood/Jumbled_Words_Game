#To use the random library, you need to import it. At the top of your program:
import random 
 
def choose():
     words=["program","computer","python","code","science","data","game"]
     pick=random.choice(words) #The choice() method returns a list with the randomly selected element from the specified sequence.
     return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word))) #The join() method takes all items in an iterable and joins them into one string.
#The sample() method returns a list with a randomly selection of a specified number of items from a sequence.    
    return jumbled

def thank(p1n,p2n,p1,p2):
    print("========= Score board ============= ")
    print(p1n,'Your score is : ',p1)
    print(p2n,'Your score is : ',p2)
    print('Thanks for playing')
    print('Have a nice day')
    print("===================================")


def main():
    p1name= input('Player 1, Please enter your name') #p1name= name of player1 
    p2name= input('Player 2, Please enter your name') #p2name= name of player2
    pp1 =0 #points of player 1
    pp2 =0 #points of player 2
    turn =0 #To keep track of whose turn it is let us have some variable or turn initially let it be zero i
    while(1):
        #computer's task
        picked_word =choose()
        #create question
        qn=jumble(picked_word)
        print (qn)
        #player1
        if turn%2==0:
            print(p1name,'its Your turn, What is on your mind?')
            ans=input()
            if ans==picked_word:
                pp1=pp1+1
                print('Your score is : ',pp1)
            else:
                print("Oh! better luck next time.")
                print('The correct answer is :',picked_word)
            c=int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
         #player2
        else:
            print(p2name,'its Your turn, What is on your mind?')
            ans=input()
            if ans==picked_word:
                pp2=pp2+1
                print('Your score is : ',pp2)
            else:
                print("Oh! better luck next time.")
                print('The correct answer is :',picked_word)
            c=int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
main()
