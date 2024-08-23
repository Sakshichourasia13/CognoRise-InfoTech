import random as r
print('Rock Paper Scissors')
print('Rules : \n Rock v/s Scissors - ROCK WINS \n Paper v/s Scissors - SCISSORS WINS \n Rock v/s Paper - PAPER WINS \n')
print('\n Press 1 - Rock \n Press 2 - Paper \n Press 3 - Scissors \n Press Any other key to exit \n')
user_score=0
comp_score=0
round_no=1
while True:
    print('Round ',round_no)
    #choice input
    user_inp=int(input('Enter Your Choice : '))
    choices=["Rock","Paper","Scissors"]
    if user_inp<4 and user_inp>0:
        user_choice=choices[user_inp-1]
        comp_choice=r.choice(choices)
        print('\nUser Choice : ',user_choice,)
        print('Computer Choice : ',comp_choice,'\n')
        print(user_choice ,'v/s', comp_choice,'\n')
        #result
        if user_choice==comp_choice:
            result="It's a Tie"
            print(result)
        elif user_choice=='Rock' and comp_choice=='Paper':
            result='Computer Won!!'
            print(result)
        elif user_choice=='Rock' and comp_choice=='Scissors':
            result='User Won!!'
            print(result)
        elif user_choice=='Scissors' and comp_choice=='Rock':
            result='User Won!!'
            print(result)
        elif user_choice=='Scissors' and comp_choice=='Paper':
            result='Computer Won!!'
            print(result)
        elif user_choice=='Paper' and comp_choice=='Scissors':
            result='Computer Won!!'
            print(result)
        elif user_choice=='Paper' and comp_choice=='Rock':
            result='User Won!!'
            print(result)
    else:
        break
    #scores
    if result=="User Won!!":
        user_score=user_score+1
    elif result=="Computer Won!!":
        comp_score=comp_score+1
    else:
        print('Thanks For Playing!!')
    print('\nScores')
    print('User : ',user_score)
    print('Computer : ',comp_score,'\n\n')
    round_no=round_no+1
