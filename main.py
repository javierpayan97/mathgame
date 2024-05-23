import random

operation = ["+","-","*"]
m = len(operation)-1
NB_QUESTIONS = 4
points=0
for i in range(0, NB_QUESTIONS):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print(f"Question n#{i+1} out of {NB_QUESTIONS}")
    n = random.randint(0,m)
    n_total = int(input(f"{n1} {operation[n]} {n2} = "))
    if operation[n] == "+":
        if n_total == n1+n2:
            print("Right answer\n")
            points+=1
        else:
            print("Wrong Answer")
    elif operation[n] == "-":
        if n_total == n1-n2:
            print("Right answer\n")
            points+=1
        else:
            print("Wrong Answer")
    elif operation[n] == "*":
        if n_total == n1*n2:
            print("Right answer\n")
            points+=1
        else:
            print("Wrong Answer")

print(f"Your points : {points} out of {NB_QUESTIONS}")
if points == NB_QUESTIONS:
    print("Excellent")
elif points > NB_QUESTIONS/2:
    print("Good")
elif points > 0 and points < NB_QUESTIONS/2:
    print("You can do better")
elif points == 0:
    print("Improve your maths!")
