import time

class Character:

    def __init__(self):

        self.get_class()

    def get_class(self):
        temp = True
        while temp == True:
            char_class = input("What class are you? Warrior / Priest / Archer ")

            if char_class == "warrior":
                text("You are a warrior!")
                temp = False

            elif char_class == "priest":
                text("You are a priest!")
                temp = False

            elif char_class == "archer":
                text("You are an archer!")
                temp = False

            else:
                text("please input a proper response")
                temp = True

        self.char_class = char_class

    def intro_stats(self):

        if self.char_class == "warrior":
            text("HP: 10")
            text("Magic: 0")
            text("Attack: 5")
            text("Defense: 5")
            text("Agility: 3")
            text("Resistance: 1")
            text("Accuracy: 3")

        elif self.char_class == "priest":
            text("HP: 10")
            text("Magic: 5")
            text("Attack: 1")
            text("Defense: 2")
            text("Agility: 4")
            text("Resistance: 4")
            text("Accuracy: 2")

        elif self.char_class == "archer":
            text("HP: 10")
            text("Magic: 1")
            text("Attack: 3")
            text("Defense: 3")
            text("Agility: 4")
            text("Resistance: 1")
            text("Accuracy: 1")

class Monster:

    def __init__(self,name):
        self.name = name
        self.fight_monster()

    def fight_monster(self):
        print("You are fighting a",self.name)

def text(line):
    #takes the text and spaces out the time
    time.sleep(0.5)
    print(line)

#Text based RPG
def intro():
    text("-----------------------------------------------------")
    text("-----------------------------------------------------")
    text("-----------------------HYDERAJ-----------------------")
    text("-----------------------------------------------------")
    text("-----------------------------------------------------")
    text("Your eyes dimly adjust to the bright light on a sunny beach...")
    text("You look to see palm trees and hear seagulls in the distance")
    text("As you grogilly wake up, you hear a voice in your mind")
    text("...")
    text("Welcome to Hyderaj. This place has many adventures!")

def branching_paths():
    text("...")
    text("As you walk to the edge of the beach, you see two paths")
    text("One path heads deep into a dark and lush jungle")
    text("The other path is a rocky trail on the side of a mountain")

    temp = False
    while temp == False:
        path = input("Which path do you take? jungle / mountain ")
        if path == "jungle":
            text("You walk into the dark canopy of trees.")
            temp = True
        elif path == "mountain":
            text("You step onto the cragged rocks of the mountain trail")
            temp = True
        else:
            text("please input a proper response")

    return path

def monster1():
    #in the dark jungle
    text("...")
    text("As you walk through the jungle, your eyes adjust to the darkness")
    text("The shrieks and calls of wild animals surround you as you venture deeper")
    text("Suddenly a creature falls from the trees")
    text("It's a Naga! A female being with the body of a snake")
    text("...")
    naga = Monster("Naga")
    text("You defeat the Naga")

def monster2():
    text("...")
    text("As you walk along the rocky path you wind up the mountain")
    text("The air gets thinner as you ascend")
    text("You begin to feel the presence of other creatures behind the rocks")
    text("Suddenly a goblin pops out from behind a rock!")
    text("...")
    goblin = Monster("Goblin")
    text("You defeat the goblin")

def ending():
    text("...")
    text("You see a tunnel before you.")
    text("Beside the tunnel is a signpost.")
    text("It seems to indicate that you are at the end of your journey")
    text("\"You have reached the end of Hyderaj. Congratulations!\"")

intro()
character = Character()
character.intro_stats()
path = branching_paths()
if path == "jungle":
    monster1()
else:
    monster2()
ending()
