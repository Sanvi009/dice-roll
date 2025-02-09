import random

def one():
    size = 7  
    symbol = "●" 
    border = "."  

    for i in range(size):
        for j in range(size):
            
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(border, end=" ")
            
            elif i == size // 2 and j == size // 2:
                print(symbol, end=" ")
            else:
                print(" ", end=" ")  
        print()  

    print("\n you got 1 \n")

def two():
    size = 7  
    symbol = "●"  
    border = "."  

    for i in range(size):
        for j in range(size):
            
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(border, end=" ")
            
            elif (i == 1 and j == 1) or (i == size - 2 and j == size - 2):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")  
        print()  
    print("\n you got 2 \n")

def three():
    size = 7  
    symbol = "●"  
    border = "."  

    for i in range(size):
        for j in range(size):
            # Border conditions (first & last row, first & last column)
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(border, end=" ")
            # Three dots: Top-right, center, and bottom-left
            elif (i == 1 and j == size - 2) or (i == size // 2 and j == size // 2) or (i == size - 2 and j == 1):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")  
        print()  
    print("\n you got 3 \n")
# Call the function to print dice face "3"


def four():
    size = 7  
    symbol = "●"  
    border = "."  

    for i in range(size):
        for j in range(size):
            # Border conditions (first & last row, first & last column)
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(border, end=" ")
            # Four dots: Top-left, Top-right, Bottom-left, Bottom-right
            elif (i == 1 and j == 1) or (i == 1 and j == size - 2) or (i == size - 2 and j == 1) or (i == size - 2 and j == size - 2):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")  
        print()  
    print("\n you got 4 \n")
# Call the function to print dice face "4"

def five():
    size = 7
    symbol = "●"
    border = "."
    for i in range(size):
        for j in range(size):
            # Border conditions (first & last row, first & last column)
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(border, end=" ")
            # Five dots: Top-left, Top-right, Center, Bottom-left, Bottom-right
            elif (i == 1 and j == 1) or (i == 1 and j == size - 2) or (i == size // 2 and j == size // 2) or (i == size - 2 and j == 1) or (i == size - 2 and j == size - 2):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")
        print()

    print("\n you got 5 \n")

def six():
    size = 7
    symbol = "●"
    border = "."

    for i in range(size):
        for j in range(size):
            # Border conditions (first & last row, first & last column)
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(border, end=" ")
            # Six dots: Two in each column (left & right)
            elif (i == 1 and j == 1) or (i == 1 and j == size - 2) or \
                 (i == size // 2 and j == 1) or (i == size // 2 and j == size - 2) or \
                 (i == size - 2 and j == 1) or (i == size - 2 and j == size - 2):
                print(symbol, end=" ")
            else:
                print(" ", end=" ")
        print()

    print("\n congratulations, you got 6 !! \n")

list = [one, two, three, four, five, six]
def roll_dice():
    while True:
        ask = input("Do you want to roll the dice? (yes/no): ")
        if ask == "yes":
            dice = random.choice(list)
            dice()
        elif ask == "no":
            print("\nThank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            

roll_dice()

