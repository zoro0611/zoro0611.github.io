def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operation = {
    "+":add,
    "-":minus,
    "*":multiply,
    "/":divide
}

def Calculator():
    userNum1 = float(input("Please input your first number: "))
    keepOperate = True
    while keepOperate:
        userNum2 = float(input("Please input your next number: "))
        for op in operation:
            print(op)
        userOperation = input("Please input your operation: ")
        answer1 = operation[userOperation](userNum1,userNum2)
        print(f"{userNum1} {userOperation} {userNum2} = {answer1}")
        ifCtn = input("Type 'y' if you want to continue. Otherwise, type 'n' to restart new calculator.")
        if ifCtn != "y":
            keepOperate = False
            Calculator()
            
        else:
            userNum1 = answer1
Calculator()

