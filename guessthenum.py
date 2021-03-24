'''
****************** Game : Guess the Price ***************

Game Scenario and Rules :
Suppose you went to the market and got yourself a beautiful wrist-watch.

The next evening when you go to your friend's place, She really liked your watch and asks you as
where you bought it from and at what price?

You tell her the shop name but ask her to guess the price that too over a Console Game.

1. Set an arbitrary number 'G' in the range of your choice as the price to be guessed. (Ex. G = 55)
2. Take inputs from user to guess the price with a limited number of guesses allowed. (Ex. ng = 10)
3. If the user guesses a number which is more than G, Print : "Hey, Its lesser than that !"
4. If the user guesses a number which is less than G, Print : "Aah, Its more than that !"
5. If the user is able to successfully guess the price, Print : "Wow! You guessed it right! Its G!"
6. Also Print "It took you n-guesses to get that. :)"
7. If the user, runs out of guesses, Print "Oops! Guess Over! It was G!"

'''

import random

# Setting a random price between 200 and 1000
price = random.randint(200, 1000)
success = False
print("\n\n *********** Guess the Price *************")

for ng in range(10):
    g = int(input("\n What's your Guess : "))
    if price < g:
        print("\n Hey, Its lesser than that !")
    elif price > g:
        print("\n Aah, Its more than that !")
    elif price == g:
        print(f"\n Wow! You guessed it right! Its {price}!"
              f"\n It took you {ng+1}-guesses to get that. :) ")
        success = True
        break

if not success:
    print(f"\nOops! Guess Over! It was {price}!")

print("\n\n *********** !! Thank You !! *************")
