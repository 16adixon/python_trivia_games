score = 0

#for use with non-multiple choice 
answer = input("______")
if answer == "____":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was __\n")

#for use with multiple choice answers
answer = input("""__________________
A)  B)  C)  D)
""")
if answer.lower() == "__":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was __\n")

