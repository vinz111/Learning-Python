print("Welcome to my computer quiz!")

playing = input("Do you want to play?(Yes/No) ")

if playing.lower() != "yes":
    print("Okay Goodbye")
    quit()
else:
    print("Okay! Let's play :)")
score = 0

answer = input("What is avocado in Indonesian? ")
if answer.lower() == "alpukat":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is grape in Indonesian? ")
if answer.lower() == "anggur":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is star fruit in Indonesian? ")
if answer.lower() == "belimbing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is orange in Indonesian? ")
if answer.lower() == "jeruk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is lychee in Indonesian? ")
if answer.lower() == "leci":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is lemon in Indonesian? ")
if answer.lower() == "lemon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is mango in Indonesian? ")
if answer.lower() == "mangga":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is jackfruit in Indonesian? ")
if answer.lower() == "nangka":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is pineapple in Indonesian? ")
if answer.lower() == "nanas":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is banana in Indonesian? ")
if answer.lower() == "pisang":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 10) * 100 ) + "%")