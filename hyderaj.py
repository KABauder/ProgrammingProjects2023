import time

class Character:

    def __init__(self):
        self.current_hp = 0
        self.current_magic = 0
        self.hp = 0
        self.magic = 0
        self.attack = 0
        self.defense = 0
        self.agility = 0
        self.resistance = 0
        self.accuracy = 0
        self.char_class = "warrior"
        self.level = 1
        self.exp = 0
        self.location = 1

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

    def update_stats(self,hp,magic,attack,defense,agility,resistance,accuracy,char_class,level,exp):
        self.hp = hp
        self.magic = magic
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.resistance = resistance
        self.accuracy = accuracy
        self.char_class = char_class
        self.level = level
        self.exp = exp

    def add_exp(self,exp):
        exp = int(exp)
        self.exp += exp

        if exp >= 50 and self.level < 2:
            text("You are level 2!")
            self.level = 2
            self.level_up()

        if exp >= 150 and self.level < 3:
            text("You are level 3!")
            self.level = 3
            self.level_up()

        if exp >= 300 and self.level < 4:
            text("You are level 4!")
            self.level = 4
            self.level_up()

        if exp >= 500 and self.level < 5:
            text("You are level 5!")
            self.level = 5
            self.level_up()

        if exp >= 750 and self.level < 6:
            text("You are level 6!")
            self.level = 6
            self.level_up()

        if exp >= 1050 and self.level < 7:
            text("You are level 7!")
            self.level = 7
            self.level_up()

        if exp >= 1450 and self.level < 8:
            text("You are level 8!")
            self.level = 8
            self.level_up()

        if exp >= 1950 and self.level < 9:
            text("You are level 9!")
            self.level = 9
            self.level_up()

        if exp >= 2500 and self.level < 10:
            text("You are level 10!")
            self.level = 10
            self.level_up()

    def level_up(self):

        if self.char_class=="warrior":
            self.hp += 2
            self.magic += 1
            self.attack += 2
            self.defense += 2
            self.agility += 2
            self.resistance += 1
            self.accuracy += 2

        if self.char_class=="archer":
            self.hp += 2
            self.magic += 1
            self.attack += 2
            self.defense += 2
            self.agility += 2
            self.resistance += 1
            self.accuracy += 2

        if self.char_class=="priest":
            self.hp += 2
            self.magic += 2
            self.attack += 1
            self.defense += 1
            self.agility += 2
            self.resistance += 2
            self.accuracy += 2

    def save_data(self):

        lines = ""
        lines += "location:" + str(self.location) + "\n"
        lines += "class:" + str(self.char_class) + "\n"
        lines += "hp:" + str(self.hp) + "\n"
        lines += "magic:" + str(self.magic) + "\n"
        lines += "attack:" + str(self.attack) + "\n"
        lines += "defense:" + str(self.defense) + "\n"
        lines += "agility:" + str(self.agility) + "\n"
        lines += "resistance:" + str(self.resistance) + "\n"
        lines += "accuracy:" + str(self.accuracy) + "\n"
        lines += "level:" + str(self.level) + "\n"
        lines += "exp:" + str(self.exp) + "\n"

        return lines

    def change_location(self,new):
        self.location = new

    def get_location(self):
        return self.location

    def get_agility(self):
        return self.agility

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_current_hp(self):
        return self.current_hp

    def get_hp(self):
        return self.hp

    def update_hp(self,hp):
        self.current_hp = hp


class Monster:

    def __init__(self,name,exp,hp,magic,attack,defense,agility,resistance,accuracy):
        self.name = name
        self.exp = exp
        self.hp = hp
        self.magic = magic
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.resistance = resistance
        self.accuracy = accuracy
        self.fight_monster()

    def fight_monster(self):
        print("You are fighting a",self.name)

    def defeat_monster(self):
        print("You got %d experience points" % self.exp)

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_name(self):
        return self.name

    def get_current_hp(self):
        return self.current_hp

    def update_hp(self,hp):
        self.current_hp = hp

class Battle:

    def __init__(self,character,enemy):
        self.turn = 0
        if character.get_agility >= enemy.get_agility:
            self.current_turn = 0
            self.player_turn()
        else:
            self.current_turn = 1
            self.enemy_turn()

    def enemy_turn(self):
        #enemy does some kind of move, let's just start with a basic Attack
        text("%d attacks!" % enemy.get_name())
        hp = character.get_current_hp() - (enemy.get_attack() - character.get_defense())
        if hp <= 0:
            hp = 0
        character.update_hp(hp)
        text("%d / %d HP" % character.get_current_hp(), character.get_hp())
        if character.get_current_hp() == 0:
            self.player_defeated()
        else:
            self.player_turn()

    def player_turn(self):
        text("Character attacks!")
        hp = enemy.get_current_hp() - (character.get_attack() - enemy.get_defense())
        if hp <= 0:
            hp = 0
        enemy.update_hp(hp)
        if enemy.get_current_hp() == 0:
            self.enemy_defeated()
        else:
            self.enemy_turn()

    def player_defeated(self):
        text("Your character died in battle! ")

    def enemy_defeated(self):
        text("You killed the %d" % enemy.get_name())


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
    save_file = False
    while temp == False:
        if newgame == "new":
            text("Creating a new game...")
            name = input("What do you want to call your save file? ")
            file1 = open(name,"w")
            file1.close()
            temp = True
            save_dict={"location":1,"class":"","hp":0,"magic":0,"attack":0,"defense":0,"agility":0,"resistance":0,"accuracy":0,"level":1,"exp":0}

        elif newgame == "continue":
            savefile = input("input the name of your save file ")
            file1 = open(savefile,"r+")
            save_dict = {}
            #get dictionary
            for line in file1:
                dict_temp = ""
                key_temp = ""
                dict_temp = line.split(":")[0]
                key_temp = line.split(":")[1]
                key_temp = key_temp[:-1]
                save_dict[dict_temp] = key_temp

            #go to location
            temp = True
            file1.close()
            save_file = True
        else:
            text("please input a proper response")

    return save_dict, save_file

def save_game(character,location):
    temp = False
    name = input("What is the name of your savefile? ")
    file = open(name,"w")
    save_data = character.save_data()
    file.writelines(save_data)
    file.close()

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

def monster1(character):
    #in the dark jungle
    text("...")
    text("As you walk through the jungle, your eyes adjust to the darkness")
    text("The shrieks and calls of wild animals surround you as you venture deeper")
    text("Suddenly a creature falls from the trees")
    text("It's a Naga! A female being with the body of a snake")
    text("...")
    naga = Monster("Naga",100,4,3,3,3,2,3,2)
    battle = Battle(naga,character)
    naga.defeat_monster()
    text("You defeat the Naga")
    exp = 100
    return exp

def monster2():
    text("...")
    text("As you walk along the rocky path you wind up the mountain")
    text("The air gets thinner as you ascend")
    text("You begin to feel the presence of other creatures behind the rocks")
    text("Suddenly a goblin pops out from behind a rock!")
    text("...")
    goblin = Monster("Goblin",50,5,0,3,3,2,0,2)
    goblin.defeat_monster()
    text("You defeat the goblin")
    exp = 50
    return exp

def ending():
    text("...")
    text("You see a tunnel before you.")
    text("Beside the tunnel is a signpost.")
    text("It seems to indicate that you are at the end of your journey")
    text("\"You have reached the end of Hyderaj. Congratulations!\"")

def final_end():
    text("-----------------------------------------------------")
    text("-----------------------THE END-----------------------")
    text("-----------------------------------------------------")
    text("-----------------created by Kyle Bauder--------------")
    text("-----------------------------------------------------")

def game_path():
    save_dict, save_file = newgame()
    location = int(save_dict["location"])
    character = Character()
    #get whether continuing a save file or not

    save_file = False
    while location <= 3:
        if location == 1:
            character.get_class()
            intro()
            character.intro_stats()
            character.change_location(2)
            location = character.get_location()
            save_game(character,location)
        elif location == 2:
            if save_file == True:
                character.update_stats(int(save_dict["hp"]),int(save_dict["magic"]),int(save_dict["attack"]), \
                int(save_dict["defense"]),int(save_dict["agility"]),int(save_dict["resistance"]), \
                int(save_dict["accuracy"]),str(save_dict["class"]),int(save_dict["level"]),int(save_dict["exp"]))
            path = branching_paths()
            if path == "jungle":
                exp = monster1(character)
                character.add_exp(exp)
            else:
                exp = monster2()
                character.add_exp(exp)
            character.change_location(3)
            location = character.get_location()
            save_game(character,location)
        elif location == 3:
            if save_file == True:
                character.update_stats(int(save_dict["hp"]),int(save_dict["magic"]),int(save_dict["attack"]), \
                int(save_dict["defense"]),int(save_dict["agility"]),int(save_dict["resistance"]), \
                int(save_dict["accuracy"]),str(save_dict["class"]),int(save_dict["level"]),int(save_dict["exp"]))
            ending()
            character.change_location(4)
            location = character.get_location()
            save_game(character,location)


    final_end()

game_path()
