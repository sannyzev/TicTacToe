import random
import numpy as np

class Game:

    gameArray = np.array([[0,0,0],[0,0,0],[0,0,0]])
    #currTurn = 0
    winOne = np.array([1,1,1])
    winTwo = np.array([2,2,2])

    inputs = {
        0: [0,0],
        1: [0,1],
        2: [0,2],
        3: [1,0],
        4: [1,1],
        5: [1,2],
        6: [2,0],
        7: [2,1],
        8: [2,2]
    }
    
    
    def resetGameArray(self):
        self.gameArray = np.array([[0,0,0],[0,0,0],[0,0,0]])
        #self.currTurn = 0
    
    def handlePlayerTurn(self):
        playerChoice = False
        while playerChoice == False:
            choice = int(input("please input tile choice from 0 - 8 counting from the left top to bottom right."))
            valueList = self.inputs[choice]
            choiceMade = self.gameArray[valueList[0],valueList[1]]
            if choiceMade == 0:
                self.gameArray[valueList[0],valueList[1]] = 1
                playerChoice == True
                return
            else:
                continue
    
    def handleBotTurn(self):
        botChoice = False
        while botChoice == False:
            x = random.randint(0,2)
            y = random.randint(0,2)
            choiceMade = self.gameArray[x,y]
            if choiceMade == 0:
                self.gameArray[x,y] = 2
                botChoice = True
                return
            else:
                continue

    # Old attempt at handling turns was difficult to implement in gym environment.
    """ 
    def handleTurns(self, action = None):
        if self.currTurn == 0:
            if action == None:
                playerChoice = False
                while playerChoice == False:
                    choice = int(input("please input tile choice from 0 - 8 counting from the left top to bottom right."))
                    valueList = self.inputs[choice]
                    choiceMade = self.gameArray[valueList[0],valueList[1]]
                    if choiceMade == 0:
                        self.gameArray[valueList[0],valueList[1]] = 1
                        playerChoice == True
                        self.currTurn = 1
                        return
                    else:
                        continue
            else:
                

        else:
            botChoice = False
            while botChoice == False:
                x = random.randint(0,2)
                y = random.randint(0,2)
                choiceMade = self.gameArray[x,y]
                if choiceMade == 0:
                    self.gameArray[x,y] = 2
                    botChoice = True
                    self.currTurn = 0
                    return
                else:
                    continue 
    """

    def printGame(self):
        print(self.gameArray[0][0], self.gameArray[0][1], self.gameArray[0][2])
        print(self.gameArray[1][0],self.gameArray[1][1],self.gameArray[1][2])
        print(self.gameArray[2][0],self.gameArray[2][1],self.gameArray[2][2])

    def checkWin(self):
        if np.array_equal(self.gameArray[0:3,0], self.winOne) \
        or np.array_equal(self.gameArray[0:3,1], self.winOne) \
        or np.array_equal(self.gameArray[0:3,2], self.winOne) \
        or np.array_equal(self.gameArray[0,0:3], self.winOne) \
        or np.array_equal(self.gameArray[1,0:3], self.winOne) \
        or np.array_equal(self.gameArray[2,0:3], self.winOne) \
        or np.array_equal([self.gameArray[0,0], self.gameArray[1,1], self.gameArray[2,2]], self.winOne) \
        or np.array_equal([self.gameArray[2,0], self.gameArray[1,1], self.gameArray[0,2]], self.winOne):
            print("win")
            return True

        if np.array_equal(self.gameArray[0:3,0], self.winTwo) \
        or np.array_equal(self.gameArray[0:3,1], self.winTwo) \
        or np.array_equal(self.gameArray[0:3,2], self.winTwo) \
        or np.array_equal(self.gameArray[0,0:3], self.winTwo) \
        or np.array_equal(self.gameArray[1,0:3], self.winTwo) \
        or np.array_equal(self.gameArray[2,0:3], self.winTwo) \
        or np.array_equal([self.gameArray[0,0], self.gameArray[1,1], self.gameArray[2,2]], self.winTwo) \
        or np.array_equal([self.gameArray[2,0], self.gameArray[1,1], self.gameArray[0,2]], self.winTwo):
            print("loss")
            return True
        
        if np.all(np.greater(self.gameArray, np.array([[0,0,0],[0,0,0],[0,0,0]]))):
            print("draw")
            return True
        
        return False
    
    def checkWinGYM(self):
        if np.array_equal(self.gameArray[0:3,0], self.winOne) \
        or np.array_equal(self.gameArray[0:3,1], self.winOne) \
        or np.array_equal(self.gameArray[0:3,2], self.winOne) \
        or np.array_equal(self.gameArray[0,0:3], self.winOne) \
        or np.array_equal(self.gameArray[1,0:3], self.winOne) \
        or np.array_equal(self.gameArray[2,0:3], self.winOne) \
        or np.array_equal([self.gameArray[0,0], self.gameArray[1,1], self.gameArray[2,2]], self.winOne) \
        or np.array_equal([self.gameArray[2,0], self.gameArray[1,1], self.gameArray[0,2]], self.winOne):
            print("win")
            return True, "win"

        if np.array_equal(self.gameArray[0:3,0], self.winTwo) \
        or np.array_equal(self.gameArray[0:3,1], self.winTwo) \
        or np.array_equal(self.gameArray[0:3,2], self.winTwo) \
        or np.array_equal(self.gameArray[0,0:3], self.winTwo) \
        or np.array_equal(self.gameArray[1,0:3], self.winTwo) \
        or np.array_equal(self.gameArray[2,0:3], self.winTwo) \
        or np.array_equal([self.gameArray[0,0], self.gameArray[1,1], self.gameArray[2,2]], self.winTwo) \
        or np.array_equal([self.gameArray[2,0], self.gameArray[1,1], self.gameArray[0,2]], self.winTwo):
            print("loss")
            return True, "loss"
        
        if np.all(np.greater(self.gameArray, np.array([[0,0,0],[0,0,0],[0,0,0]]))):
            print("draw")
            return True, "draw"
        
        return False, "ingame"

    def runGame(self):
        gameWin = False
        while gameWin == False:
            self.handleTurns()
            self.printGame()
            gameWin = self.checkWin()