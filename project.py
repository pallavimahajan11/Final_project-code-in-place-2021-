import random
import time
from tkinter import Tk, Button, DISABLED, messagebox  #Add modules

"""This function will always display a symbol, but how it operates depends on whether
it’s the first or second turn in the matching attempt. If it’s the first turn, the
function just needs to remember which button was pressed. If it’s the second
turn, it needs to check if the symbols match. Symbols that don’t match are
hidden. Matching symbols are left showing and their buttons are disabled."""
def show_symbol(x, y):  #The x and y values tell the function which button has been pressed.
    global first, moves, match_found
    global previousX, previousY

    buttons[x, y]["text"] = button_symbols[x, y] #These lines show the symbol.
    buttons[x, y].update_idletasks()
    if first:
        previousX = x
        previousY = y
        first = False
        moves += 1

    if previousX != x or previousY != y:
       # If the symbols don’t match..
        if buttons[previousX, previousY]['text'] != buttons[x, y]["text"]:
            # Wait 0.5 seconds to give the player time to see the symbols,then hide them.
            time.sleep(0.5)
            buttons[previousX, previousY]['text'] = ""
            buttons[x, y]['text'] = ""
            root.update_idletasks()

        else:
            # Disable the pair of matching buttons so the player can’t press them again.
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
            match_found += 1 # Add 1 to the number of matches found
            if match_found == (len(buttons) / 2):
                #If all the pairs have been found run the code under line
                if messagebox.showinfo('Matching', 'Number of moves: ' + str(moves)) == "ok":
                    root.destroy()

        first = True
        print("Moves:", moves, "Match found", match_found)

#This lines create a Tkinter window and give tittle and keeps the window at original size
root = Tk()
root.title("Matchmaker")
root.resizable(width=False,height = False)

buttons = {} # This is a dictionary

moves = 0
match_found = 0
first = True   #This variable is used to check if the symbol is the first in the match
previousX = 0
previousY = 0
button_symbols = {} # The symbols for each button is stored in this dictionary

symbols = [u'\u2702', u'\u2702', u"\u2705", u'\u2705', u'\u2708', u'\u2708',
           u'\u2709', u'\u2709', u"\u270A", u'\u270A', u'\u270B', u'\u270B',
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
           u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']
# The shuffle() function from random module mixes up the shapes
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        # This line creates each button and sets its size and action when pressed
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), font=(" ",40),width=4, height=1,bg="#DF4018")
        # The buttons placed on the gui
        button.grid(column=x, row=y)
        #This line saves each button in the dictionary
        buttons[x, y] = button
        #The button symbols is set by this line
        button_symbols[x, y] = symbols.pop()

root.mainloop()



