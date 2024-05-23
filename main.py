import random

def calculate(n1,n2,o):
    n_total_int = 0
    while True:
        n_total_str = input(f"{n1} {o} {n2} = ")
        try:
            n_total_int = int(n_total_str)
            return n_total_int
        except:
            print("Error: please write a number")

operation = ["+","-","*"]
m = len(operation)-1
NB_QUESTIONS = 10
points=0
for i in range(0, NB_QUESTIONS):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print(f"Question n#{i+1} out of {NB_QUESTIONS}")
    n = random.randint(0,m)
    n_total = calculate(n1,n2,operation[n])
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
    elif operation[n] == "**":
        if n_total == n1*n2:
            print("Right answer\n")
            points+=1
        else:
            print("Wrong answer")

print(f"Your points : {points} out of {NB_QUESTIONS}")
if points == NB_QUESTIONS:
    print("Excellent")
elif points > NB_QUESTIONS/2:
    print("Good")
elif points > 0 and points <= NB_QUESTIONS/2:
    print("You can do better")
elif points == 0:
    print("Improve your maths!")
