#Charles Kelsey 1/29/22
#Reverse Polish Notation calculator (2nd attempt)
#Things I learned making this:
#-basic Python syntax
#-basic console I/O
#-lots of otherwise complicated things can be specified in one line!
#-python's concept of scope (or lack thereof)

#i can already see why python has a reputation for being concise and easy to use. 
#it took some time to read through documentation (and stackoverflow) for proper syntax, 
#but it feels good to have the procedural stuff abstracted away so i can focus on actually building the program. 

#read inputs from left to right.
#on reaching a value, push it to the stack. 
#on reaching an operator, pop 2 values, reverse their order, and do a calculation step using the operator; push the result.
#after all input elements are consumed, there is only one element in the stack (the result)
def calculate(inputs):
    stack = []
    for x in inputs:
        if isinstance(x, float):
            stack.append(x)
        elif isinstance(x, str):
            val1 = stack.pop()
            val2 = stack.pop()            
            match x:
                case "+":
                    stack.append(val2 + val1)
                case "-":
                    stack.append(val2 - val1)
                case "*":
                    stack.append(val2 * val1)
                case "/":
                    stack.append(val2 / val1)
                case "**":
                    stack.append(val2 ** val1)
    return stack[0]

def parse(input):
    #split string into a list of elements
    stack = input.split(" ")
    #convert all numbers from strings to floats
    #for some reason, elements in a list can't be cast using a normal for-in loop
    for i in range(len(stack)):
            try:
                stack[i] = float(stack[i])
            except ValueError:
                pass
    return stack

#validates that the stack contains parsable input
def validate(stack):
    floats = strings = 0
    for x in stack:
        if isinstance(x, float):
            floats += 1
        else:
            strings += 1
            #fails if the string is not a valid operator
            if not x in ['+', '-', '*', '/', '**']:
                print("Error: invalid operator.")
                return False
            #fails if any operator has more than (numbers - operators - 1) operators before it
            if strings > floats - 1:
                print("Error: too many operators.")
                return False
    #fails if there isn't exactly 1 more operand than operator
    if floats != strings + 1:
        print("Error: not enough operators.")
        return False
    #fails (with more than 1 input) if the last input is not an operator
    if len(stack) != 1:
        if not isinstance(stack[-1], str): #(selecting the last element like this is so concise)
            print("Error: last input not operator.")
            return False
    return True

#inputs = []
#elements = []
#muscle memory, this isn't actually necessary

print("Enter Reverse Polish Notation calculation:")
while True:
    #get input
    inputs = input()
    if inputs in ["exit", "Exit"]:
        break
    #parse the input
    elements = parse(inputs)
    #check that it's valid (clear it if not)
    if not validate(elements):
        continue
    else:
        #calculate
        result = calculate(elements)
        print(result)
print("Exiting...")