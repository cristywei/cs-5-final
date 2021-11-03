# main() initiates the menu and allows you to choose to play the game
# it is included right at the end of the file so when you run it it runs on its own
# which can be deleted for testing purposes
import random               # DO NOT DELETE
import time

def menu():
    """ this prints the user menu
    """
    print("\nWelcome to Mastermind!")
    print()
    print("(0) Play game as codebreaker vs. AI")
    print("(1) Play game as codemaker vs. AI")
    print("(2) Rules")
    print("(3) See wins scoreboard")
    print("(4) Quit")

def rules():
    """ this prints the rules
        make edits as it develops!
    """
    print()
    print("There are two roles the player can play as:")
    print()
    print("Codebreaker: In this role, the player will be tasked within decipering a secret code, which is set by the AI.")
    print()
    print("Codemaker: In those role, the player's job is to create a secret code, which the AI will attempt to guess.")
    print()
    print("The code: The code will be a 4-letter sequence consisting of the letters R, B, G, and Y. Each letter will appear once in the sequence.")
    print()
    print("The codebreaker will guess the code.")
    print("Then, the codemaker will tell the codebreaker the number of letters that were in the correct position in their guess.")
    print("The codebreaker will have 12 turns to correctly guess the secret code.")
    print("The codebreaker wins if they guess the secret code correctly within 12 turns.")
    print("Otherwise, the codemaker will win.")

class Board:
    """ Mastermind board
    """
    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = 5
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        W = self.width
        H = self.height
    
    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board
        s += '\n'

        for col in range(0, self.width):
            s += ' ' + str(col)

        return s       # the board is complete, return it
    
    def addMove(self, col, color):
        """ adds a single "colored" ball into the board
            col: column to be added to
            color: color of the ball
        """
        H = self.height
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = color
                return
            
        self.data[H-1][col] = color

    def aiCode(self):
        """ AI that creates the code for the player to break
            using 4-letters in place of colored balls
        """
        L = ['B', 'G', 'R', 'Y']
        C = []
        for x in range(len(L)):
            color = random.choice(L)
            C += [color]
            del L[L.index(color)]
        return C
    
    def makeCode(self):
        """ allows the player to make the code
            to use against the ai
        """
        L = ['R', 'G', 'B', 'Y']
        C = []
        for x in range(len(L)):
            print("\nYour remaining letters are:", L)
            color = input("Choose a letter for slot " + str(x) + ": ")
            while not color in L:
                print("\nThat is not a valid input!")
                print("Please try again.")
                print("These are valid inputs: ", L)
                color = input("Choose a letter for slot " + str(x) + ": ")
            C += [color]
            del L[L.index(color)]
        print("You have made your code!")
        print("Your code is: ", C)
        return C

    def aiGuess(self):
        """ allows the ai to make an initial guess when playing
            the role of codebreaker
            +++ adds the moves to the board
        """
        L = ['R', 'G', 'B', 'Y']
        C = []

        for x in range(len(L)):
            color = random.choice(L)
            C += [color]
            del L[L.index(color)]
            

        th = C[0]
        self.addMove(0, th)

        st = C[1]
        self.addMove(1, st)

        nd = C[2]
        self.addMove(2, nd)

        rd = C[3]
        self.addMove(3, rd)

        return C

    def aiGuess0(self, G, prev):
        """ makes an AI guess where the AI got 0 correct in a previous turn
            so it changes all of its previous letters
        """
        L = ['R', 'G', 'B', 'Y']
        for x in range(len(L)):
            new = random.choice(L)
            while new == G[x]:
                new = random.choice(L)
            G[x] = new
            del L[L.index(new)]
        
        if str(G) in prev:
            self.aiGuess0(G, prev)
        else: 
            th = G[0]
            self.addMove(0, th)

            st = G[1]
            self.addMove(1, st)

            nd = G[2]
            self.addMove(2, nd)

            rd = G[3]
            self.addMove(3, rd)
        
        return G

    def aiGuess1(self, G, prev):
        """ makes an AI guess where the AI got 1 correct in a previous turn
            so it only changes 3 of its previous letters
        """
        L = ['R', 'G', 'B', 'Y']
        IND = [0, 1, 2, 3]
        keepInd = random.choice(IND)        # choose a random index in the list to keep
        keep = G[keepInd]

        for x in range(len(G)):
            if x == keepInd:
                G[x] = G[x]
                del L[L.index(keep)]
            else:
                new = random.choice(L)
                while new == keep or new == G[x]:
                    new = random.choice(L)
                G[x] = new
                del L[L.index(new)]
        
        if str(G) in prev:
            self.aiGuess1(G, prev)
        else:
            th = G[0]
            self.addMove(0, th)

            st = G[1]
            self.addMove(1, st)

            nd = G[2]
            self.addMove(2, nd)

            rd = G[3]
            self.addMove(3, rd)
        
        return G

    def aiGuess2(self, G, prev):
        """ makes an AI guess where the AI got 2 correct in a previous turn
            so it only changes 2 of the letters in its previous guess
        """
        L = ['R', 'G', 'B', 'Y']
        IND = [0, 1, 2, 3]
        keepInd = random.choice(IND)        # choose a random index in the list to keep
        keep = G[keepInd]
        del IND[IND.index(keepInd)]
        keepInd2 = random.choice(IND)        # choose a random 2nd index in the list to keep
        keep2 = G[keepInd2]

        for x in range(len(G)):
            if x == keepInd:
                G[x] = G[x]
                del L[L.index(keep)]
            elif x == keepInd2:
                G[x] = G[x]
                del L[L.index(keep2)]
            else:
                new = random.choice(L)
                while new == keep or new == keep2:
                    new = random.choice(L)
                G[x] = new
                del L[L.index(new)]
        
        if str(G) in prev.values():
            self.aiGuess2(G, prev)
        else: 
            th = G[0]
            self.addMove(0, th)

            st = G[1]
            self.addMove(1, st)

            nd = G[2]
            self.addMove(2, nd)

            rd = G[3]
            self.addMove(3, rd)

        return G

    def codeBreaker(self, wins):
        """ hosts a game of Mastermind
            against an ai who is the "codemaker"
            while player is the codebreaker
        """
        G = ['', '', '', '']
        correct = 0
        turns = 0
        L = ['R', 'G', 'B', 'Y']

        print("Welcome to Mastermind!")
        C = self.aiCode()
        print(Board.__repr__(self))
        print("The AI has finished making the secret code.")

        while True:
            print("\nThese are your remaining letters: ", L)
            th = input("Letter to place in slot 0: ")
            while not th in L:
                print("You have chosen an invalid input! Please choose a valid input.")
                print("List of valid inputs:", L)
                th = input("Letter to place in slot 0: ")
            self.addMove(0, th)
            G[0] = th
            del L[L.index(th)]

            print("\nThese are your remaining letters: ", L)
            st = input("Letter to place in slot 1: ")
            while not st in L:
                print("\nYou have chosen an invalid input! Please choose a valid input.")
                print("List of valid inputs:", L)
                st = input("Letter to place in slot 1: ")
            self.addMove(1, st)
            G[1] = st
            del L[L.index(st)]

            print("\nThese are your remaining letters: ", L)
            nd = input("Letter to place in slot 2: ")
            while not nd in L:
                print("You have chosen an invalid input! Please choose a valid input.")
                print("List of valid inputs:", L)
                nd = input("Letter to place in slot 2: ")
            self.addMove(2, nd)
            G[2] = nd
            del L[L.index(nd)]

            print("\nThese are your remaining letters: ", L)
            rd = input("Letter to place in slot 3: ")
            while not rd in L:
                print("You have chosen an invalid input! Please choose a valid input.")
                print("List of valid inputs:", L)
                rd = input("Letter to place in slot 3: ")
            self.addMove(3, rd)
            G[3] = rd
            del L[L.index(rd)]

            turns += 1
            print(G)
            for x in range(len(G)):
                if G[x] == C[x]:
                    correct += 1
            self.addMove(4, str(correct))
            print(Board.__repr__(self))

            if correct == 4:
                print("You win! The code was:", C)
                wins[1] += 1
                break
            elif turns >= 15:
                print("You have run out of turns!")
                print("The code was:", C)
                print("The AI wins!")
                wins[0] += 1
                break
            else:
                if correct == 1:
                    print("You have", correct, "letter in the correct position!")
                else:
                    print("You have", correct, "letters in the correct position!")
                if turns > 11:
                    print("\nYou have", 15-turns, "turns left.")
                    print("Try to make better guesses.")
                else:
                    print("\nYou have", 15-turns, "turns left.")
                correct = 0 # resets the correct amount
                L = ['R', 'G', 'B', 'Y']     # resets the list of valid guesses

    def codeMaker(self, wins):
        """ hosts a game of Mastermind
            where the player is the Codemaker
            and the ai is the Codebreaker
        """
        turns = 0
        autocorrect = 0
        prev = {}

        print()
        print("You have chosen to be the Codemaker!")
        print("Please make your secret code.")
        C = self.makeCode()                         # prompts user to make code
        G = self.aiGuess()              #adds the AI's initial guess to the board

        while True:
            time.sleep(1.5)         # to give the illusion of thought
            turns += 1
            print(Board.__repr__(self))

            print("The AI guessed", G)
            prev[turns] = str(G)

            print("For reference, your secret code was", C)
            for x in range(len(G)):             # fail-safe for user error
                if G[x] == C[x]:
                    autocorrect += 1
            correct = int(input("How many did the AI get correct?: "))
            while not correct == autocorrect:
                print("\nAre you sure about that?")
                print("Please check your answer.")
                correct = int(input("How many did the AI get correct?: "))

            self.addMove(4, str(correct))
            print(Board.__repr__(self))

            print()

            if correct == 4:
                print("The AI wins!")
                wins[0] += 1
                break
            elif turns >= 15:
                print("The AI has run out of turns!")
                print("You win!")
                wins[1] += 1
                break
            elif correct < 4:
                autocorrect = 0     # resets the auto-checking correct variables
                print("The AI will continue guessing!\n")

                if correct == 0:
                    G = self.aiGuess0(G, prev)
                elif correct == 1:
                    G = self.aiGuess1(G, prev)
                elif correct == 2:
                    G = self.aiGuess2(G, prev)
                correct = 0         # resets correct variables after conditionals

def main():
    """ Main user-interaction loop
        Dictates what actions should be taken based on user input
    """
    wins = {0: 0, 1: 0}

    while True:
        menu()
        choice = input("Choose an option: ")

        try:        # try to make sense of input
            choice = int(choice)
        except:
            print("I didn't understand your input! Continuing...")
            continue
        
        if choice == 4:     # quits the menu
            break
        
        elif choice == 0:       # ai game as codeBreaker
            b = Board(5, 15)
            b.codeBreaker(wins)

        elif choice == 1:       # ai game as codeMaker
            b = Board(5, 15)
            b.codeMaker(wins)

        elif choice == 2:       # prints rules
            rules()
            continue
        
        elif choice == 3:
            print("\nSCORES")
            print("\nAI wins:", wins[0])
            print("\nHuman wins:", wins[1])

        else:
            print()
            print(choice, "is not an option!")
            print("Please try again.")
    
    print("See you soon!")

main()