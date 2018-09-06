import random
import re
import os.path

def wordScrambler(word):     #This function takes a word as an argument, creates underscroes, and scrambles the letters

    underscorePhrase = re.sub('[0-9a-zA-Z]', "_", word)  # the regex function replaces all chars in string with something else
    h = "  ".join(underscorePhrase)  # this will make an extra space between all chars in underscorePhrase string
    print("\n" + h)  # these are the underscores actually printing
    word1 = word.replace(" ", "")  # creates new variable, and word.replace method removed spaces...eg los angeles -> losangeles
    wordlist2 = (list(word1.lower()))  # puts the chars of the string, now without spaces, into a new list. Makes all the letters lowercase
    random.shuffle(wordlist2)  # scrambles the letters of the list
    print("\n")
    print("   ".join(wordlist2))  # turns the newly scrambled list into a string, with three spaces between chars
    print("\n")


def answerCheck(userGuess, correctAnswer):    #This function compares the user's guess to the correct answer
    userGuessL = userGuess.lower()   #This lowercases all the letters of the user's guess
    correctAnswerL = correctAnswer.lower()      #This lower cases all the letters othe correct answer
    correctAnswerC = correctAnswer.title()     #This capitalizes the first letter of each word

    if userGuessL == correctAnswerL:       #This compares the lowercased userGuess and correctAnswer
        print("\nCorrect! The answer is " + correctAnswerC)
        return True
    else:
        print("\nThat's incorrect.  The correct answer is " + correctAnswerC)


def random_line(fileName):     #This selects a single line from the specified text file
    lines = open(fileName).read().splitlines()
    return random.choice(lines)


def selectNumQuestions(txtFileName):   #This function uses the random_line function, and selects a specified number of random lines from a text file
    count = 0
    while len(tempSelection) < q and count < 100:  #I put a count in here in the case that there are less than 10 items in the txt file, it will run an infinite loop
        y = random_line(txtFileName)
        if y not in tempSelection:        #added this clause as to not get the same questions added
            tempSelection.append(y)
        count += 1


print("Welcome to Word Scramble, please select your category, or press enter for random category \n 1. Cities in Europe \n 2. NHL Hockey Teams \n 3. Ice Cream Flavors \n 4. US Presidents\n 5. Select Random Category")
selection = int(input("Please select \n"))

nameOfFile = input("Enter your name to save the report to a file? \n")  #This will give the file a name
filePath = "C:/Users/Jeff/pythonProj/createFileFolder"    #this is creating a variable for the file path for the file to be saved to
completeName = os.path.join(filePath, nameOfFile+".txt")  #This is joining together the path to the file and the file
file = open(completeName,"w")    #This is creating the file name

tempSelection = []    #Creating an empty list to have the questions added to
q = 5

if selection == 5:     #This will randomly select one of the other 4 categories
    selection = random.randint(1,4)

#Gives the user choices to what category they will do.  Then runs the selectNumQuestions function to read from that selection's text file
if selection == 1:
    selectNumQuestions('europe.txt')
    print ("The category is cities in Europe")

if selection == 2:
    selectNumQuestions('hockey.txt')
    print("The category is NHL Hockey Teams")

if selection == 3:
    selectNumQuestions('iceCream.txt')
    print("The category is Ice Cream Flavors")

if selection == 4:
    selectNumQuestions('presidents.txt')
    print("The category is US Presidents")



print(tempSelection)  #Prints the answers that have been randomly selected from the text files

score = 0   #initializing the score
print("There is a total of " + str(len(tempSelection)) + " questions. Each question is worth 1 point")
quesCount = 1   #Iniitialzing the question count
while tempSelection != []:    #As long as the list is not empty, loop through
    print("Current Score:  " + str(score))
    quesRem = str(len(tempSelection))    #Counts the number of items left in the string for the number of questions remaining
    print((quesRem) + " questions remaining")
    newWord = random.choice(tempSelection)  # newWord is the word that has been selected for the puzzle
    tempSelection.remove(newWord)   #Remove the current word from the list
    wordScrambler(newWord)    #Runs the wordScramber function on the newWord
    answer = input("What is your guess? \n")
    if answerCheck(answer, newWord) is True:   #Adds 1 to the score if the answer is correct
        score += 1

    file.write("Q" + str(quesCount) + "\nYour Answer: " + answer + "\nCorrect Answer: " + newWord + "\n\n")  #Writes to the report with the user's guess and correct answer for each question
    quesCount += 1

print ("GAME OVER \nYour total score is " + str(score) + "/" + str(q))  #Writes information at the bottom of the report, giving the name of the file and the score
print ("A report named \"" + nameOfFile + "\" has been saved in the file directory")
file.write("FILE NAME: " + nameOfFile + "\nTOTAL SCORE: " + str(score) + "/" + str(q))

file.close() #Closes the file






