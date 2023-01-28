print("Welcome to the notes section of the red team blue team modules")
playing = input("Would you like to play? ")
score = 0

if playing.lower == "yes":
    print("Good luck! ")

answer = input("What port is HTTPS on? ")
if answer == "443":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("What port is FTP on? ")
if answer == "21":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")
    
answer = input("What port is SSH on? ")
if answer == "22":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("What port is SFTP on? ")
if answer == "22":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("What does IDS stand for? ")
if answer == "intrusion detection software":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("What port is Telnet on? ")
if answer == "23":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("What does netstat stand for? ")
if answer == "network statistics":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("4096 MB is how many GB?")
if answer == "4.096":
    print("Correct!")
else:
    print("Incorrect!")


print(str(score/8 *100) + "%")






