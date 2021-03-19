import random

# Program to implement Snake-Water-Gun Game with Computer

print("\n\n *********** Snake-Water-Gun Game ****************")
print("\n Let Computer choose its choice (s/w/g)...")
c = random.choice(['s', 'w', 'g'])
y = input("\n Choose your option (s/w/g) : ")

print(f"\n Computer : {c} \n You : {y}")


def swgwinner(comp, you):
    if comp == you:
        return None
    else:
        if comp == 's':
            if you == 'g':
                return True
            elif you == 'w':
                return False
        elif comp == 'w':
            if you == 's':
                return True
            elif you == 'g':
                return False
        elif comp == 'g':
            if you == 'w':
                return True
            elif you == 's':
                return False


winner = swgwinner(c, y)

if winner is None:
    print("\n Oops! Its a Tie!")
elif winner:
    print("\n Congrats! You Won..!")
else:
    print("\n Aah, You Lose!")


print("\n **********************************************")