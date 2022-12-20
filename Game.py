import random

# list of weapon
li = ["gun", "rocket", "knief"]


class CrossFire:

    # intializing user weapon
    def __init__(self, weapon):
        self.weapon = weapon

# this method compare user weapon with computer weapon and reclare winner whose weapon is biggest
    def ConditionsChk(self):

        if li[index] == "gun" and self.weapon == "rocket":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("you win :)")

        elif li[index] == "gun" and self.weapon == "knief":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("you lose")

        elif li[index] == "gun" and self.weapon == "gun":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("match tie")
        elif li[index] == "rocket" and self.weapon == "gun":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("you lose")

        elif li[index] == "rocket" and self.weapon == "knief":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("you lose")

        elif li[index] == "rocket" and self.weapon == "rocket":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("match tie")
        elif li[index] == "knief" and self.weapon == "knief":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("match tie")
        elif li[index] == "knief" and self.weapon == "gun":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print(" you won :)")

        elif li[index] == "knief" and self.weapon == "rocket":
            print("Computer:"+li[index] + " vs "+"Your :"+self.weapon)
            print("you won :)")

        else:
            print("please enter valid choice")


while True:
    index = random.randint(0, 2)  # genrating randoom number between 0 to 2
    print("Avaliable Weapon list")
    print("Rocket , Gun ,Knief")
    p = input("Enter your Weapon")
    p=p.lower()
    player1 = CrossFire(p)

    player1.ConditionsChk()
