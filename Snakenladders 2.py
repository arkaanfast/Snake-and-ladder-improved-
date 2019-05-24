from random import randint

class Player:


    def __init__(self, name, pos, player_no):
        self.name = name
        self.pos = pos
        self.player_no = player_no


    def getPosition(self):
        return self.pos


    def updatePosition(self, no_dice):
        self.pos = self.pos + no_dice

def dice():
    x = randint(1, 6)
    return x

snl = {6: 17, 4: 3, 20: 15, 24: 26, 30: 44, 39: 33, 49: 62, 66: 53, 69: 58, 79: 67, 82: 86 ,84: 71,88: 36}

def main():
    running = True
    pl_list = []
    print("enter the number of players")
    n = input()
    for i in range(0, int(n)):
        name = input("enter the name")
        pl_list.append(Player(name, 0, i+1))
    while(running):
        for i in range(0, len(pl_list)):
            input("Player--> " + pl_list[i].name + " hit enter to roll the dice")
            no = dice()
            if pl_list[i].getPosition() >= 100:
                print(pl_list[i].name + "you are the winner")
                running = False
                break

            elif pl_list[i].getPosition() != 100:
                for x in snl:
                    if pl_list[i].getPosition() == x:
                        if x < snl[x]:
                            print("you reached a ladder advance")
                            pl_list[i].updatePosition(snl[x])
                            print(pl_list[i].name + " is in " + str(pl_list[i].getPosition()))
                            break
                        else:
                            print("you have encountered a snake")
                            pl_list[i].updatePosition(x)
                            print(pl_list[i].name + " is in " + str(pl_list[i].getPosition()))
                            break
                    else:
                        pl_list[i].updatePosition(no)
                        print(pl_list[i].name + " is in " + str(pl_list[i].getPosition()))
                        break
main()