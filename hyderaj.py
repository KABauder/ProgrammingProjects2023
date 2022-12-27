import time

class Character:

    def __init__(self):
        self.get_class()
        self.hp = 0
        self.magic = 0
        self.attack = 0
        self.defense = 0
        self.agility = 0
        self.resistance = 0
        self.accuracy = 0

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
            self.hp = 10
            self.magic = 0
            self.attack = 5
            self.defense = 5
            self.agility = 3
            self.resistance = 1
            self.accuracy = 3
            text("HP: 10")
            text("Magic: 0")
            text("Attack: 5")
            text("Defense: 5")
            text("Agility: 3")
            text("Resistance: 1")
            text("Accuracy: 3")

        elif self.char_class == "priest":
            self.hp = 10
            self.magic = 5
            self.attack = 1
            self.defense = 2
            self.agility = 4
            self.resistance = 4
            self.accuracy = 2
            text("HP: 10")
            text("Magic: 5")
            text("Attack: 1")
            text("Defense: 2")
            text("Agility: 4")
            text("Resistance: 4")
            text("Accuracy: 2")

        elif self.char_class == "archer":
            self.hp = 10
            self.magic = 1
            self.attack = 3
            self.defense = 3
            self.agility = 4
            self.resistance = 1
            self.accuracy = 1
            text("HP: 10")
            text("Magic: 1")
            text("Attack: 3")
            text("Defense: 3")
            text("Agility: 4")
            text("Resistance: 1")
            text("Accuracy: 1")

    def update_stats(self,hp,magic,attack,defense,agility,resistance,accuracy):
        self.hp = hp
        self.magic = magic
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.resistance = resistance
        self.accuracy = accuracy

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
def newgame():
    text("-----------------------------------------------------")
    text("-----------------------------------------------------")
    text("-----------------------HYDERAJ-----------------------")
    text("-----------------------------------------------------")
    text("-----------------------------------------------------")
    newgame = input("New game or continue? new / continue ")
    temp = False
    while temp == False:
        if newgame == "new":
            text("Creating a new game...")
            name = input("What do you want to call your save file? ")
            file1 = open(name,"a")
            file1.write("1")
            file1.close()
            temp = True

        elif newgame == "continue":
            savefile = input("input the name of your save file ")
            file1 = open(savefile,"r+")
            #get dictionary
            save_dict = {}
            for line in file1:
                dict_temp = ""
                key_temp = ""
                dict_temp = line.split(":")[0]
                key_temp = line.split(":")[1]
                key_temp = key_temp[:-1]
                save_dict[dict_temp] = key_temp

            #go to location
            temp = True
        else:
            text("please input a proper response")

    print("save_dict",save_dict)
    return save_dict

def intro():
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

def game_path():
    save_dict = newgame()
    location = int(save_dict["location"])
    while location <= 3:
        if location == 1:
            intro()
            character = Character()
            character.intro_stats()
            location +=1
        elif location == 2:
            path = branching_paths()
            if path == "jungle":
                monster1()
            else:
                monster2()
            location +=1
        elif location == 3:
            ending()
            location +=1

game_path()
