# Adam Clemons
# 11/9/16 - GuessWho.py - Python implementation of Excersise found in the TEALS Computer Science curriculum
import pygame

class GuessWho():
    def __init__(self, listOfNames):
        self.nameList = listOfNames

    def WelcomeAll(self):
        for name in self.nameList:
            print("Welcome, "+name+"!")

    def welcomeAllAtOnce(self):
        output=""
        for name in self.nameList:
            output += "Welcome, "+name+"!"

    def sayEveryOtherName(self):
        for index, name in enumerate(self.nameList):
            if index % 2 == 0:
                print(name)

    def sayEveryoneBackwards(self):
        for name in reversed(self.nameList):
            print(name)

    def sayAllWithMoreThanFourLetters(self):
        for name in self.nameList:
            if len(name) >= 4:
                print(name)

    def sayAllEndingInY(self):
        for name in self.nameList:
            if name[len(name)-1:len(name)] == 'y' or name[len(name)-1:len(name)] == 'Y':
                print(name)

    def sayAllBeginningInC(self):
        for name in self.nameList:
            if name[:1] == 'c' or name[:1] == 'C':
                print(name)

    def sayAllButFirstAndLastTwo(self):
        for index,name in enumerate(self.nameList):
            if index > 1 and index < (len(self.nameList) -2):
                print(name)

    def sayAllWithLetterE(self):
        for name in self.nameList:
            if 'e' in name or 'E' in name:
                print(name)



class GuessWhoUI():
    def __init__(self, guessWhoObject):
        self.guessWho = guessWhoObject
        self.run()
        pass

    def run(self):

        pygame.init()
        screen = pygame.display.set_mode([80, 60])
        pygame.display.set_caption('GuessWho')
        pygame.mouse.set_visible(0)
        font = pygame.font.Font(None, 36)

        clock = pygame.time.Clock()
        keepRunning = True

        while keepRunning:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_program = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        # Do Key '0'
                        self.guessWho.sayEveryoneBackwards()
                    elif event.key == pygame.K_1:
                        # Do Key '1'
                        self.guessWho.sayAllWithMoreThanFourLetters()
                    elif event.key == pygame.K_2:
                        # do key 2
                        self.guessWho.sayAllBeginningInC()
                    elif event.key == pygame.K_3:
                        self.guessWho.sayAllEndingInY()
                    elif event.key == pygame.K_4:
                        self.guessWho.sayAllButFirstAndLastTwo()
                    elif event.key == pygame.K_5:
                        self.guessWho.sayAllWithLetterE()



        pygame.quit()


if __name__ == '__main__':
    nameList = ["Adam","Bob","Robert","Charlie","Tommy","John","Albert","Rose","David","Tom","Shareese","Annette","George","Donald"]
    guessWho = GuessWho(nameList)
    guesWhoUI = GuessWhoUI(guessWho)
