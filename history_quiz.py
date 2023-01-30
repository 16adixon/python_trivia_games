print("History Quiz")

score = 0

playing = "Press y to play"
if playing.lower() != "y":
    print("Good Luck!")
else:
    print("FUCK YOU!")
    quit()

print("Category 1: Civil War")
answer = input("""What was the South known as during the Civil War?
A) The Confederacy B) The Union C) The Great South D) The Bad Guys
""")
if answer.lower() == "a":
    print("Correct!")
    score += 1

else:
    print("Incorrect! The correct answer was A")



