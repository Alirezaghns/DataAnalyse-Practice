class Player:
    VALID_POSITIONS = ['gheychi', 'kaghaz', 'sang']

    def __init__(self, name):
        self.name = name
        self.position = self._get_valid_position()

    def _get_valid_position(self):
        while True:
            try:
                pos = input(f"{self.name}, enter your position {self.VALID_POSITIONS}: ").lower()
                if pos in self.VALID_POSITIONS:
                       return pos
                raise ValueError('invalid input try again') 
            except ValueError as e:
                print(f'enter the valid position :{e}')



class Game:
    def __init__(self, p1: Player, p2: Player):
        self.p1 = p1
        self.p2 = p2
    def winner(self):
        if self.p1.position == self.p2.position:
            print(" Draw!")
            return
        if (self.p1.position, self.p2.position) in [
                   ('gheychi', 'kaghaz'),
                    ('kaghaz', 'sang'),
                    ('sang', 'gheychi')]:
            winner = self.p1
        else:
            winner = self.p2
        print(f" {winner.name} won!")
        
        # 2th soloution
        # rules = {
        #     ('gheychi', 'kaghaz'): self.p1,
        #     ('kaghaz', 'sang'): self.p1,
        #     ('sang', 'gheychi'): self.p1,
        # }
        # winner = rules.get((self.p1.position, self.p2.position), self.p2)
        # print(f" {winner.name} won!")

player1 = Player("Player 1")
player2 = Player("Player 2")

game = Game(player1, player2)
game.winner()

