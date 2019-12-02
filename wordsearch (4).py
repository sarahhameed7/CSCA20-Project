# The random function is imported to allow us to implement code that generates
# random letters on the grid 
import random
# The time function is imported to allow us to use a timer that will countdown 
# the seconds, the user will have to find the words
import time
# Will allow us to run multiple functions at the same time
import threading

# The following function creates a timer, that will run until the game ends
def trigger():
    time.sleep(180)
    
    print("\n Time is up!")

    
# This function serves the purpose of replacing all empty spaces with randomly 
# generated letters, to make a grid
def randomFill(wordsearch):
    LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(0,12):
        for col in range(0,12):
            if wordsearch[row][col]=="-":
                randomLetter = random.choice(LETTERS)
                wordsearch[row][col]=randomLetter

# The following function serves the purpose of displaying the grid to the user
def displayWordsearch(wordsearch):
# the following numbers help serve as coordinates for letter positions
    print("      0 1 2 3 4 5 6 7 8 9 10 11")
    print("    __________________________")
  # This will create the boundaries around the grid
    for row in range(0,12):
        line="|  "
        for col in range(0,12):
            line = line + wordsearch[row][col] + " "
        line = line + " |"
        if len(str(row)) == 1:
            display_row = str(row)+"  "
        else: 
            display_row = str(row)+ " "
        print(display_row +line)
    print("   |___________________________|")  
   
#The following function will add a word to the wordsearch at a random position
def addWord(word,wordsearch):
    directions = [ "rightleft", "leftright", "updown", "downup" , "diagonalup", "diagonaldown"]
    # The code below will identify the orientation of the word, whether it will be 
    # added horizontally, vertically, reverse or diagonally    
    direction = random.choice(directions)
    print(direction)
    written = 0
  
    while (written!=1):
        if direction == "rightleft":
            step_x = -1
            step_y = 0
            # This is put to check that the word will fit in (within the 12 by 12 grid)
            x_pos1 = random.randint(len(word)-1,11)
            y_pos1 = random.randint(0,11)    
     
        elif direction == "leftright":
            step_x = 1
            step_y = 0
            x_pos1 = random.randint(0,12- len(word))
            y_pos1 = random.randint(0,11)    
     
        elif direction == "updown":
            step_x = 0
            step_y = 1  
            x_pos1 = random.randint(0,11)
            y_pos1 = random.randint(0,12- len(word))  
      
        elif direction == "downup":
            step_x = 0
            step_y = -1  
            x_pos1 = random.randint(0,11)
            y_pos1 = random.randint(len(word)-1,11)    
          
        elif direction == "diagonalup":
            step_x = 1
            step_y = -1  
            x_pos1 = random.randint(0,12- len(word))
            y_pos1 = random.randint(len(word)-1,11)      
          
        elif direction == "diagonaldown":
            step_x = -1
            step_y = 1  
            x_pos1 = random.randint(12-len(word),11)
            y_pos1 = random.randint(0,12- len(word))      
            #This is put in place to ensure that the word will pick a new position, and changes 
            # the position again based on the orientation. This is assuming the grid is empty. 
            #If the grid is not empty, it starts the loop again   
        for i in range(0,len(word)):
            new_pos_x = x_pos1 + (i*step_x)
            new_pos_y = y_pos1 + (i*step_y)
      
            print(word[i], new_pos_x , new_pos_y )
             
            if wordsearch[new_pos_y][new_pos_x] == '-':
                wordsearch[new_pos_y][new_pos_x]=word[i]
            
            else:
                break
       
            if i==len(word)-1:
                written = written+1
                #this ensures that each word will be written once , and if space is not available, it will try to write itself again 
                
# This function allows the user to input the coordinates of the beginning, and
# the end of the word          
def foundWord(word,wordsearch,found):
    x_coord1 = int(input(" x- coordinate for start of "+word + " "))
    y_coord1 = int(input(" y- coordinate for start of "+word + " "))
    x_coord2 = int(input(" x- coordinate for end of "+word + " "))
    y_coord2 = int(input(" y- coordinate for end of "+word + " "))
# Prints a statement in response to the users input, based on
# whether it is correct or not  
    if (wordsearch[int(y_coord1)][int(x_coord1)] == word[0]) and (wordsearch[int(y_coord2)][int(x_coord2)] == word[len(word)-1]):
        print("Good Job!")
        found = found+1
        return found
    else: 
        print("Not Quite, Try Again")
        return found
        
def category():
    print("Categories: (pick one integer) ")
    print("1.Computer Science")
    print("2.Animals")
    print("3.Cities")
    print("4.Miscellaneous")
    try:
        choice = int(input("Pick the number of the category you would like: "))
        if choice == 1:
            words= ["PYTHON","ALGORITHM","CODING","PROGRAM"]
            return words
        elif choice ==2:
            words= ["SNAKE","BEAVER","BEAR","COW"]
            return words        
        elif choice ==3:
            words= ["TORONTO", "SYDNEY","LA","LONDON"]
            return words
        elif choice ==4:
            words= ["FINANCE", "FISH","OUCH","RED"]
            return words    
    except ValueError:
        print("please try entering a numerical value instead")
        
play = True
while(play):
    
    print("Let's play Word Search!")
    words = category()
    
    # Create an empty 12 by 12 wordsearch (list of lists)
    wordsearch = []
    for row in range(0,12):
        wordsearch.append([])
        for col in range(0,12):
            wordsearch[row].append("-")
  
    # Adding the potential words to find in our wordsearch
  
    addWord(words[0],wordsearch)    
    addWord(words[1],wordsearch)    
    addWord(words[2],wordsearch)    
    addWord(words[3],wordsearch)    
  
    # All unused spaces in the wordsearch will be replaced with a random letter
    # (based on the function defined above)
    randomFill(wordsearch)
  
    # Display the fully competed wordseach on screen
    # (based on the function defined above)
    displayWordsearch(wordsearch)
  
    # Instructions that will be given to the user for the Word search 
    
    print("You have three minutes to find the following words : "+words[0]+" "+words[1]+" "+words[2]+" "+words[3]) 
    found = 0  
    thread = threading.Thread(target=trigger)
    thread.daemon = True
    thread.start()    
    while (found!=4):
        word = input("Which word did you find? ").upper()
        found = foundWord(word,wordsearch,found)
    # Implementation of the function defined above, that will give an output based
    # on the coordinates entered 
    if (found == 4):
        replay = input("You won! Would you like to play again? Reply with a Y or N")
        if (replay == "N"):
            print("Thank you for playing!")
            play = False
       
      

  
  
  
 

