# todo : write out the other function - subtract,multiply and divide.
import art
def add(n1,n2):
    return n1 + n2
def substract(n1 , n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
# todo : add these 4 functions into a dictionary as the values. Keys = "+","-","*","/".
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
# todo :  use the dicyinoary operation to perform the calculations.multiply 4 * 8 using the dictionary.
#print(operations["*"](4,8))
def calculater():
    print( art.cculater)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick the operation:")
        num2 = float(input("What is the next number?: "))
        # print(num1 + num2)
        answer = operations[operation_symbol](num1, num2)
        print(f" {num1} {operation_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate == False
            print("/n" * 20)
            calculater()
calculater()