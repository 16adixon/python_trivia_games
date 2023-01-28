print("Welcome to my computer quiz game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Okay let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

answer = input("What does DNS stand for? ")
if answer.lower() == "domain name system":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

answer = input("What does IDS stand for? ")
if answer.lower() == "intrusion detection software":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")    



print("You got " + str(score/5 * 100) + "%")



