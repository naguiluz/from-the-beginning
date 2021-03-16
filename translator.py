#Test Language
#vowels --> x
#ex: dog -> dxg, cat -> cxt

def translate(phrase): #setting up the function for a user phrase / phrase will later be defined while printing the translate function as (input("Enter a phrase:")"
    translation = "" #variable(user's input) is empty because it will be returned after going through the loop and changes are made
    for letter in phrase: #for each letter(index) in the phrase...
        if letter.lower() in "aeiou": #if a letter (made lowercase) is inside the user input of aeiou then...
            translation = translation + "x" #take the translation and add an x where aeiou was
        else: #otherwise translation keeps the letter
            translation = translation + letter #letter(index) must be included so that everything is printed, not just the newly changed letters
    return translation #return the users input with changes once loop is complete


print(translate(input("Enter a phrase:"))) #print the users input phrase after going through function