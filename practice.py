questions = ["What does CPU stand for?"]
correct_answers = ["c"]

score = 0

x = input(questions[0]) 
print("""A) Central Park United B) Can't Perform Uptown
C) Central Processing Unit D) None of the Above
""")

if x.lower() == correct_answers[0]:
    print("Correct!")
    score += 1
else:
    print("Incorrect")

