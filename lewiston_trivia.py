from cgitb import text
from tkinter import *


questions = [

#[0]
"What year was Lewiston founded?\n",

#[1]
"Who bought out Potlatch?\n",

#[2]
"What is the elevation of the LC Valley?\n",

#[3]
"What is Idaho known as?\n",

#[4]
"What river runs through our valley?\n",

#[5]
"What is the population Clarkston?\n",

#[6]
"What was Idaho's first capital?\n",

#7 a is correct answer
"What was Lewiston's population in 1930?\n"

]

options = [
    ["It wasn't", "1844", "1901", "1861"],
    ["Vista Outdoor", "Schweitzer Engineering", "Wal Mart", "Clearwater Paper"],
    ["745'", "650'", "900'", "None of the above"],
    ["The Potato State", "The Evergreen State", "The Gem State", "Nowhere to go State"],
    ["The Colombia River", "The FET River", "The Snake River", "Crymea River"],
    ["30,056", "15,364", "7,194", "10,972"],
    ["Nampa", "Boise", "Caldwell", "None of the above"],
    ["1,783", "4,532", "9,361", "11,700"]
]

answers = [4, 4, 1, 3, 3, 3, 4, 3]

final_score = 0
num_questions = 8
question_no = 1

def next():
    global final_score,question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    elif val4.get() == 1:
        selected_option = 4
    else:
        selected_option = -1

    if(answers[question_no-1] == selected_option):
        final_score += 1

    question_no += 1

    if question_no > num_questions:
        root.pack_forget()
        score.place(relx=.45, rely=.45)
        score.config(text = "Score:\n" + str(final_score) + " out of 8 questions correct")

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        val4.set(0)
        question.config(text = questions[question_no-1])
        option1.config(text = options[question_no-1][0])
        option2.config(text = options[question_no-1][1])
        option3.config(text = options[question_no-1][2])
        option4.config(text = options[question_no-1][3])

def check(option):
    if(option == 1):
        val2.set(0)
        val3.set(0)
        val4.set(0)
    elif(option == 2):
        val1.set(0)
        val3.set(0)
        val4.set(0)
    elif(option == 3):
        val1.set(0)
        val2.set(0)
        val4.set(0)
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)

win = Tk()
win.title("Lewiston Trivia")

root = Frame()
root.pack()

#question[0]
question = Label(root, text=questions[0], width=60, font=(10))
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()

option1 = Checkbutton(root, variable=val1, text=options[0][0], command=lambda:check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=options[0][1], command=lambda:check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=options[0][2], command=lambda:check(3))
option3.pack()

option4 = Checkbutton(root, variable=val4, text=options[0][3], command=lambda:check(4))
option4.pack()

next_b = Button(root, text="next", command=next)
next_b.pack()

score = Label(win)
score.place_forget()

win.mainloop()
