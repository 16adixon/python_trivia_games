questions = ["Do the rhcp have a star on hollywood"]
correct_answers = ["a", "b", "c", "d"]

answer = input(questions[0])
if answer.lower() == "yes":
    print("Correct!\n")
    score += 1
    answer = input(questions[0])
    if answer == correct_answers[3]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer was", correct_answers[3] + "\n")
else:
    print("They do have a star! It was unveiled in 2022!\n")



