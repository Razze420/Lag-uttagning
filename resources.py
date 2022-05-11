import random
from secrets import choice

class Player:
    def __init__(self, name, club, attack, defend):
        self.name = name
        self.club = club
        self.attack = attack
        self.defend = defend

    def __str__(self):
        return f"Name: {self.name}, Club: {self.club}, Attack: {self.attack}, Defend: {self.defend}"

    def get_club(self):
        return self.club

    def get_att(self):
        return self.attack
        
    def get_def(self):
        return self.defend
    
    def gett_all_attributes(self):
        return self.name, self.club, self.attack, self.defend

#    def alternative_players(self):
#        players = []
#        players.append(Players(""))


class Team:
    def __init__(self, name, players : list[Player]):
        self.name = name
        self.players = players
        self.combat_point = 0
        self.defense_point = 0
        for player in self.players:
            self.combat_point += player.attack
            self.defense_point += player.defend

    def __str__(self):
        return f"Name: {self.name}, Attack: {self.combat_point}, Defense: {self.defense_point}, P1: {self.players[0].name}, P2: {self.players[1].name}, P3: {self.players[2].name}"

    
def load_players():

    with open("Slutprojekt/players.txt", "r" , encoding="utf8") as f:
        players = []
        for line in f.readlines():
            attributes = line.split("/")
            this_player = Player(attributes[0],
                                  attributes[1],
                                  int(attributes[2]), 
                                  int(attributes[3]))
            players.append(this_player)
        return players


def create_player(available_players : list):
    print("HELLO!\nIt's time to chose your 3:a side team")
    print("this is the players you can chose from")

    picked_players = []

    for i in range(3): 
        print(f"Pick your #{i+1} player!")
        for j, player in enumerate(available_players):
            print(j, player.name)
        choice = input("Pick an index: ")
        picked_players.append(available_players.pop(int(choice)))
        

    print("===== YOUR TEAM =====")
    for player in picked_players:
        print(player)
    
    return picked_players

    # name = input("name: ")
    # while True:
    #     if name == "Bahoui" or "J.Larsson" or "Otieno":
    #         club = "AIK"
    #         True
    #     elif name == "Selmani" or "Besara" or "jehaze":
    #         club = "HIF"
    #         True
    #     elif name == "Edvardsen" or "Shuller" or "Ekdal":
    #         club = "DIF"
    #         True
    #     else:
    #         print("Din dumma jävel välj en av spelarna\nOBS!Glöm inte stor bokstav!")
    #         False
    
def load_opponents(available_players : list):
    opponents = []

    for _ in range(3):
        this_player = random.choice(available_players)
        opponents.append(this_player)

    return Team("Tuffa gänget", opponents)

def load_team(picked_players):
    team = create_player(picked_players)

    return Team("ditt lag", team)  

def fight():
    pass

def main():
    available_players = load_players()

    print("\n\n\n")
    for player in available_players:
        print(player)
    print("\n\n\n")
    
    team = load_team(available_players)
    print(team"\n")

    opponents = load_opponents(available_players)
    print(opponents)
    


if __name__ == "__main__":
    main()