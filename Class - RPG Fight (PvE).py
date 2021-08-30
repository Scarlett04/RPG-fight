import sys,time,random
class Adventurer:
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = level * 6
        self.hidden = False
    def __repr__(self):
        return f'{self.name} - HP: {self.HP}'
    def attack(self,target):
        if target.hidden == True:
            print(f'{self.name} can\'t see {target.name}')
        else:
            damage = self.strength + 4
            target.HP -= damage
            print(f'{self.name} attacks {target.name} for {damage} damage')

class Thief(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = level * 8
        self.hidden = True
    def attack(self,target):
        if self.hidden == False:
            super().attack(target)
        else:
            damage = (self.speed + self.level) * 5
            target.HP -= damage
            self.hidden = False
            target.hidden = False
            print(f'{self.name} sneak attacks {target.name} for {damage} damage')

class Mage(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.fireballs_left = power
    def attack(self,target):
        if self.fireballs_left == 0:
            super().attack(target)
        else:
            damage = self.level * 3
            target.HP -= damage
            target.hidden = False
            self.fireballs_left -= 1
            print(f'{self.name} casts fireball on {target.name} for {damage} damage')

class Ninja(Thief):
    def attack(self,target):
        super().attack(target)
        self.hidden = True
        self.HP += self.level
    
class Wizard(Mage):
    def __init__(self, name, level, strength, speed, power):
        super().__init__(name, level, strength, speed, power)
        self.HP = level * 4
        self.fireballs_left = power * 2

def battle(player_list, enemy_list):
    turn = 1
    while True:
        if turn%2 == 1:
            print('----------Player Turn----------')
            print('Your team:')
            for i in player_list:
                print(i)
            print('\n')
            for v in range(len(player_list)):
                for t in range(len(enemy_list)):
                    index = t + 1
                    print('Enemy ' + str(index) + ': ',end='')
                    print(enemy_list[t])
                print('Choose a target for ' + player_list[v].name +': ',end='')
                response = int(input())
                player_list[v].attack(enemy_list[response-1])
                if enemy_list[response-1].HP<=0:
                    print(enemy_list[response-1].name, ' was defeated!')
                    del enemy_list[response-1]
                if len(enemy_list)==0:
                    print('You win!')
                    print(player_list)
                    sys.exit()
                print('\n')
            turn += 1
            time.sleep(1.5)

        else:
            print('----------Enemy Turn----------')
            for i in range(len(enemy_list)):
                min_HP = player_list[0]
                for v in range(len(player_list)):
                    if player_list[v].HP < min_HP.HP:
                        min_HP = player_list[v]
                enemy_list[i].attack(min_HP)
                if min_HP.HP<=0:
                    print(min_HP.name,' was defeated!')
                    player_list.remove(min_HP)
                if len(player_list)==0:
                    print('You lose!')
                    print(enemy_list)
                    sys.exit()
            print('\n')
            turn += 1
            time.sleep(1.5)

members = []
size = int(input('Number of allies: '))
stat = 0
for i in range(1,size+1):
    print(f'Ally {i}')
    role =  str(input('What is your character\'s role? - '))
    name = str(input('Enter ally\'s name: '))
    level = int(input('Enter ally\'s level: '))
    strength = int(input('Enter ally\'s strength: '))
    speed = int(input('Enter ally\'s speed: '))
    power = int(input('Enter ally\'s power: '))
    STAT = max(level,strength,speed,power)
    stat += STAT
    if role == 'Adventure' or role == 'adventure' or role == 'A' or role == 'a':
        members.append(Adventurer(name,level,strength,speed,power))
    elif role == 'Thief' or role == 'thief' or role == 'T' or role == 't':
        members.append(Thief(name,level,speed,speed,power))
    elif role == 'Mage' or role == 'mage' or role == 'M' or role == 'm':
        members.append(Mage(name,level,strength,speed,power))
    elif role == 'Ninja' or role == 'ninja' or role == 'N' or role == 'n':
        members.append(Ninja(name,level,strength,speed,power))
    elif role == 'Wizard' or role == 'wizard' or role == 'W' or role == 'w':
        members.append(Wizard(name,level,strength,speed,power))
    else:
        print('Invalid input. Please try again.')
stat //= size
mode = str(input('Enter your game mode (E/M/H): '))
enemy = []

if mode == 'E' or mode == 'e':
    for e in range(len(members)):
        enemy.append(Adventurer('Orc',2,5,2,4))

elif mode == 'M' or mode == 'm':
    jaina = Mage("Jaina",10,8,2,6)
    arthur = Adventurer("Arthur",3,4,4,4)
    madeline = Ninja("Madeline",20,2,10,1)
    
    gandalf = Wizard("Gandalf",17,4,3,1)
    frisk = Adventurer("Frisk",4,7,5,9)
    westley = Thief("Westley",14,4,5,1)

    set1 = [jaina,arthur,madeline]
    set2 = [frisk,gandalf,westley]
    enemy = random.choice([set1,set2])

elif mode == 'H' or mode == 'h':
    mario = Mage("Mario",stat,stat,stat,stat)
    link = Thief("Link",stat,stat,stat,stat)
    fox = Adventurer("Fox",stat,stat,stat,stat)
    ness = Wizard("Ness",stat,stat,stat,stat)
    enemy = [ness,mario,fox,link]

battle(members,enemy)
    