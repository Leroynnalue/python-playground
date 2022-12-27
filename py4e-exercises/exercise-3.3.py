# Grading System

print("-------------")
print(" Score\tGrade")
print(">= 0.9\t  A")
print(">= 0.8\t  B")
print(">= 0.7\t  C")
print(">= 0.6\t  D")
print("<0 0.6\t  F")
print("-------------")
print("-------------\n")

try:
    score = float(input("Enter score: "))
    if score > 1:
        print("Bad Score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Bad Score")
except:
    print("Bad Score")