import random
sharks= ["lsurus oxyrincus","Sphyrnidae","Galeocerdo cuvier", "Carcharhinus leucas","Carcharodon carcharias"] # Mako, hammerhead, tiger, bull, great white
shark_layman= ["Mako","Hammerhead","Tiger","Bull","Great White"]
random_shark= random.randint(0,4)
word= sharks[random_shark]
def shark():
    innocent_dude= [
    " 0  ", 
    "\|/ ",
    "/ \ "]
    def innocent_dude_function():
        print(innocent_dude[0])
        print(innocent_dude[1])
        print(innocent_dude[2])

    wrong=0 # keeps count of wrong words
    incorrect_guesses= [] # displays incorrect character guesses and displays te for player
    levels= ["","   ________/\          ","  /O\  }}}   \_______/|","<<_______    ________ |","         \  /        \|","          \/","",]
# draws character hangman style as part of list w/indexable variables
    letters= list(word) # creates list of characters in word
    spaces= ["__"] * len(word) # creates list with line per character of word
    win= False # used to check i player has won
    print ("Guess the correct letters to spell out a shark species' name.\nIf you guess incorrectly, the poor innocent \nswimmer dude will be eaten and it'll all be your fault.")
    innocent_dude_function()
    while wrong < len(levels)-1: # game will continue as long as guesses are less than word length
        print ("\n") # prints space for aesthetics
        print ("Incorrect Guesses: ",incorrect_guesses)
        answer= input("Type in a letter.\n> ")
        if answer in letters:
            letter_index = letters.index(answer)
            spaces[letter_index] = answer
            letters[letter_index] = '$'
            if answer in letters: # second if statement ensures all instances o correct guess are filled in
                letter_index=letters.index(answer)
                spaces[letter_index]=answer
        else:
            wrong += 1 # increments amount wrong
            incorrect_guesses.append(answer)
        print ((' '.join(spaces)))
        print ('\n'.join(levels[0:wrong + 1]))
        innocent_dude_function()
        if '__' not in spaces:
               print ("You win! The dude lives to fight another day!")
               print (' '.join(spaces))
               win = True
               break
    if not win:
        print ('\n'.join(levels[0: wrong]))
        print ("Game over! The word was '{}' you dummy".format(word))
        shark_name=sharks.index(word)
        shark_easy=shark_layman[shark_name]
        print ("Everybody knows that %s is the scientific name for %s.\nOur innocent swimmer dude was eaten because of your icompetence!\nIt's all on you. I hope you're happy." % (word,shark_easy))

shark()
        
