print("Welcome to my computer quiz game!")

questions = [

"What does CPU stand for?\n", #[0]
"What does DNS stand for?\n", #[1]
"What does GPU stand for?\n", #[2]
"What does PSU stand for?\n", #[3]
"What does IDS stand for?\n" #[4]

]

questions.append("What does API stand for?\n") #[5]
questions.append("What does JSON stand for?\n") #[6]
questions.append("A computer reads digital signals. The internet uses analog signals. What device demodulates analog signals into digital signals?") #[7]

correct_answers = {"a", "b", "c", "d"}

score = 0

answer = input(questions[0])
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was Central Processing Unit")

answer = input(questions[1])
if answer.lower() = "domain name system":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was Domain Name System")

answer = input(questions[2])
if answer.lower == "graphical user interface":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was graphical user interface")

answer = input(questions[3])
if answer.lower() == "power supply unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was Power Supply Unit")

answer = input(questions[4])
if answer.lower() == "intrusion detection software":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was Intrusion Detection Software")

answer = input(questions[5])
if answer.lower() == "application programming interface":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was Application Programming Interface")

answer = input(questions[6])
if answer.lower() == "javascript object notation":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer was JavaScript Object Notation")

answer = input(questions[7])
if answer.lower() == "modem":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! A modem demodulates signals from the internet for your computer to understand")




