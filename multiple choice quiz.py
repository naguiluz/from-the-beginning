from Question import Question

question_prompts = [ # create an array of prompts to be referenced in our objects
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [ # create an array consisting of our objects / values set as prompt = question prompt index / answer = input
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions): # creating a function to run the predefined variable "questions"
    score = 0 # score created to be tracked and given at the end
    for question in questions: # for each question(value/index) in questions array
        answer = input(question.prompt)   # answer is equal to the input to our question.prompt (set in our class and defined in "questions" array above^)
        if answer == question.answer: # if the answer^ is equal to the question.answer (also set in our class and defined in "questions" array above^) then...
            score += 1 # add 1 to our score
    print("You got " +str(score) + "/" + str(len(questions)) + " correct.") # print the score and the "length(amount)" of questions in the question array

run_test(questions)