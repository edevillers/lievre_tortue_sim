import random
import pylab

class Game:
    '''la classe du jeu, qui comprend un board et des methodes pour progresser'''

    def __init__(self):
        self.board = {0: 'start'
                      , 1: 'vide'
                      , 2: 'laitue'
                      , 3: ['lapin','tortue']
                      , 4: 'vide'
                      , 5: 'carotte'
                      , 6: ['lapin']
                      , 7: 'vide'
                      , 8: 'vide'
                      , 9: ['lapin', 'tortue']
                      , 10: 'vide'
                      , 11: 'vide'
                      , 12: 'laitue'
                      , 13: 'carotte'
                      , 14: ['lapin']
                      , 15: 'vide'
                      , 16: ['tortue']
                      , 17: 'sieste'
                      , 18: ['lapin']
                      , 19: 'vide'
                      , 20: ['tortue']
                      , 21: 'laitue'
                      , 22: 'vide'
                      , 23: ['lapin']
                      , 24: 'laitue'
                      , 25: 'vide'
                      , 26: ['tortue']
                      , 27: 'vide'
                      , 28: 'vide'
                      , 29: 'laitue'
                      , 30: ['lapin', 'tortue']
                      , 31: 'sieste'
                      , 32: 'vide'
                      , 33: ['lapin', 'tortue']
                      , 34: 'laitue'
                      , 35: 'vide'
                      , 36: ['lapin']
                      , 37: 'vide'
                      , 38: 'vide'
                      , 39: 'laitue'
                      , 40: ['tortue']
                      , 41: ['lapin']
                      , 42: 'vide'
                      , 43: 'vide'
                      , 44: ['lapin']
                      , 45: ['lapin']
                      , 46: ['lapin', 'tortue']
                      , 47: 'sieste'
                      , 48: ['lapin', 'tortue']
                      , 49: ['lapin', 'tortue']
                      , 50: ['lapin', 'tortue']
                        }
        self.position = 0
        self.turn = 0

    def playTurnTortue(self, dice):
        '''on lance un de'''
        resultat = dice.throw()
        if resultat == 'tortue':
            print 'yeah une tortue !'
            self.position = self.getNextTurtle()
            self.turn += 1
            print 'un tour de plus !'
            return
        else:
            self.position += resultat
            if self.board[self.position] == 'laitue':
                print 'yeah ! une laitue. on rebrasse'
                self.playTurnTortue(dice)
            else:
                self.turn += 1
                print 'un tour de plus !'
                return

    def playTurnLapin(self, dice):
        '''on lance un de'''
        resultat = dice.throw()
        if resultat == 'lievre':
            print 'yeah un lapin !'
            self.position = self.getNextRabbit()
            self.turn += 1
            print 'un tour de plus !'
            return
        elif resultat == 'sleep':
            print 'non... on dort'
            self.turn+= 1
            print 'un tour de plus !'
        else:
            self.position += resultat
            if self.board[self.position] == 'carotte':
                print 'yeah ! une carotte. on rebrasse'
                self.playTurnLapin(dice)
            elif self.board[self.position] == 'sieste':
                print 'oh non... la sieste. on recule de deux'
                self.position -= 2
                print 'un tour de plus!'
            else:
                self.turn += 1
                print 'un tour de plus !'
                return


    def getNextTurtle(self):
        for e in range(self.position + 1, len(self.board)):
            if 'tortue' in self.board[e]:
                return e
        return self.position

    def getNextRabbit(self):
        for e in range(self.position + 1, len(self.board)):
            if 'lapin' in self.board[e]:
                return e
        return self.position

class TurtleDice:
    '''un petit de special pour une tortue'''

    def __init__(self):
        self.values = ['tortue', 'tortue', 2, 3, 3, 4]

    def throw(self):
        result = random.choice(self.values)
        print 'on a brasse: ', result
        return result

class RabbitDice:
    '''un petit de special pour un lievre'''

    def __init__(self):
        self.values = ['sleep', 'lievre', 3, 4, 5, 6]

    def throw(self):
        result = random.choice(self.values)
        print 'on a brasse: ', result
        return result

#le jeu

def jouerPartieTortue():
    newGame = Game()
    newDice = TurtleDice()

    while newGame.position < len(newGame.board):
        try:
            print 'le tour ', newGame.turn, ' commence'
            newGame.playTurnTortue(newDice)
            print 'la nouvelle position est ', newGame.position
        except(KeyError):
            print 'la partie est terminee en ', newGame.turn, ' tours.'
            return newGame.turn

def jouerPartieLapin():
    newGame = Game()
    newDice = RabbitDice()

    while newGame.position < len(newGame.board):
        try:
            print 'le tour ', newGame.turn, ' commence'
            newGame.playTurnLapin(newDice)
            print 'la nouvelle position est ', newGame.position
        except(KeyError):
            print 'la partie est terminee en ', newGame.turn, ' tours.'
            return newGame.turn

toursTortue = []
toursLapin = []
for i in range(0, 10000):
    toursTortue.append(jouerPartieTortue())

for i in range(0, 10000):
    toursLapin.append(jouerPartieLapin())

print 'le nb de tours moyens pour la tortue est: ', float(sum(toursTortue))/len(toursTortue)
print 'le nb de tours moyens pour le lapin est: ', float(sum(toursLapin))/len(toursLapin)

pylab.hist(toursTortue)
pylab.show()
pylab.hist(toursLapin)
pylab.show()
