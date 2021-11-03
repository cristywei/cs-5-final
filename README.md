# HMC CS 5 Final Project - Mastermind

My final project for HMC's CS 5 class was the game <a href="https://en.wikipedia.org/wiki/Mastermind_(board_game)">Mastermind</a>, which is meant to be played in terminal of VS Code.

In the game, the human player can play either as a "codebreaker" or "codemaker" against the AI, who will take the other unselected role. Each game runs a maximum of 15 turns. The codebreaker and codemaker will alternate turns.

The codemaker creates a 4-letter secret code, consisting of the letters R, G, B, and Y, no letters repeating. It is the codebreaker's job to guess the secret code within 15 turns. After their guess, the codemaker will tell the codebreaker how many of the letters the codebreaker guessed in the correct positions.

If the AI is the codemaker, then the AI will create a randomly-generated code, analyzing the human player's guesses, and tell them how many of their letters are in the correct position. The AI will also let you know how many turns/guesses you have remaining.

If the AI is the codebreaker, then the AI's actions will depend on the human player's feedback. The AI makes a randomized initial guess, with all 4 letters randomly placed. If the player tells the AI that 0 of the letters in its guess are correct, then the AI will randomly generate a new code. If the player tells the AI that there are 1 or 2 correct letter positions, then it will randomly choose 1 or 2 letters respectively to keep, randomizing the remaining letter positions. In all 3 of these cases, the AI will reference a dictionary of previous guesses so that it does not re-guess previous codes. It will continue generating new codes until it has generated one that has not been guessed before playing its turn. 
