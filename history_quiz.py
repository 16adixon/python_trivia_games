print("THIS IS YOUR HISTORY QUIZ YOU BETTER FUCKING STUDY")
print("Each topic has 5 questions. Can you get them all?")

score = 0

playing = "Press y to play"
if playing.lower() != "y":
    print("Good Luck!")
else:
    print("FUCK YOU!")
    quit()

#1st Civil War Question
print("Category 1: Civil War")
answer = input("""What was the South known as during the Civil War?
A) The Confederacy B) The Union C) The Great South D) The Bad Guys
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1
    #2nd Civil War Question
    answer = input("Who was the President during the Civil War? Please type your answer\n")
    if answer.lower() == "abraham lincoln":
        print("Correct!")
        score += 1
        #3rd Civil War Question
        answer = input("""What year did the Civil War start?
        A) 1858 B) 1861 C) 1865 D) 1897
        """)
        if answer.lower() == "b":
            print("Correct!")
            score += 1
    else:
        print("Incorrect.")
        print("You got", score + "/5 questions correct!")

else:
    print("Incorrect! The correct answer was A")



