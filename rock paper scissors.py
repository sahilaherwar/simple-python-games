import random
def game(comp,a):
    if comp == a:
        None
    elif comp == 'r':
        if a == 'p':
            return True
        elif a == 'c':
            return False
    elif comp == 'p':
        if a == 'c':
            return True
        elif a == 'r':
            return False        
    elif comp == 'c':
        if a == 'r':
            return True
        elif a == 'p':
            return False
    else:
        print("invalid input")
Player = input("Enter USername for the session: ")
print(f"Welcome to the game {Player}!!")
print("Computer is choosing...")
r = random.randint(1,3)
if r == 1:
    comp = 'r'
elif r == 2:
    comp = 'p'
elif r == 3:
    comp = 'c'

print("Computer has chosen its option. Its your turn!")
a = input(f"Enter Rock(r),Paper(p) or Scissor(c): ")
g = game(comp,a)

print(f"The Computer has choosen {comp} and you have choosed {a}")

if g == None:
    print("So it is a tie")
elif g:
    print("So You win")
else:
    print("So You loose")
