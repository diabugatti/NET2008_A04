import random

choices = ['r', 's', 'p']
choice_meaning = {
    'r': 'Rock',
    's': 'Scissors',
    'p': 'Paper'
}

ai_choice = random.choice(choices)
ai_choice2 = random.choice(choices)
print('Two computers, AI1 and AI2, are going to choose from rock, scissors, and paper : ')

if ai_choice2 in choices:
        print(
        f"AI1's choice is {choice_meaning[ai_choice2]}.\nAnd AI2's choice is {choice_meaning[ai_choice]}.\n")
        if ai_choice2 == ai_choice:
            print("Tie")
        elif (ai_choice2 == 'r' and ai_choice == 's') or (ai_choice2 == 's' and ai_choice == 'p') or (ai_choice2 == 'p' and ai_choice == 'r'):
            print("AI2 won")
        else:
            print("AI1 lost\n")

