import random
from PIL import Image
def roll_dice():
    number=random.randint(1,6)
    display(number)

def display(n):
    if n==1:
        im=Image.open("1.png")
        im.show()
    elif n==2:
        im = Image.open("2.png")
        im.show()
    elif n==3:
        im = Image.open("3.png")
        im.show()
    elif n==4:
        im = Image.open("4.png")
        im.show()
    elif n==5:
        im = Image.open("5.png")
        im.show()
    else:
        im = Image.open("6.png")
        im.show()
if __name__=="__main__":
    key='y'
    while key=='y':
        key=input("Enter y to roll the dice or n to exit")
        if key=='y':
            roll_dice()
        else:
            exit()
