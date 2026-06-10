class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y

player1=player(1,2)
player2=player(3,4)
player3=player(5,6)
player4=player(7,8)

players=[player1,player2,player3,player4]

for player in players:
    print(f"x:{player.x},y:{player.y}")