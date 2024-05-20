import random

def mental_math():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*", "/"])
    problem = f"{num1} {operator} {num2}"
    answer = eval(problem) 
    userAnswer = float(input(f"what the solution to {problem}: "))
    if userAnswer == answer:
        print("good job you are not retarded")
    else:
        print(f"you goober the answer is {answer}")

if __name__ == "__main__":
    mental_math()
