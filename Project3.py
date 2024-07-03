#Kelsey Nobles (Klnobles)
#COP2002 0M1
#7/2/2024
#Project 3
# This program is meant to call the defintion of a term when a number is entered.

terms_definitions = {
    "Algorithm": "is a set of instructions that are followed to solve a problem.",
    "Variable": "container that holds a single number, word, or other information that you can use throughout a program.",
    "Variable Type (data type)": "Basic variable types include: string (words and phrases), char (short for 'character;' a single letter or symbol you can type), int (short for 'integer;' for whole numbers), double or float (for decimal numbers), and bool (short for 'boolean;' for true or false values.",
    "Array": "containers that hold variables of the same data type.",
    "If statement": "runs a block of code based on whether or not a condition is true.",
    "Loop": "check a condition and then run a code block. The loop will continue to check and run until a specified condition is reached.",
    "Function": "block of code that can be referenced by name to run the code it contains.",
    "Class": "template definition of the methods and variables in a particular kind of object.",
    "Object": "data type that has unique attributes and behavior.",
    "Method": "programmed procedure that is defined as part of a class and is available to any object instantiated from that class.",
    "Programming Language": "system of notation for writing computer programs. Python is an example.",
    "Control Structure": "basic blocks for decision making processes in computing."
}


def print_menu():
    print("Terms Menu:")
    print("1. Algorithm")
    print("2. Variable")
    print("3. Variable Type (data type)")
    print("4. Array")
    print("5. If statement")
    print("6. Loop")
    print("7. Function")
    print("8. Class")
    print("9. Object")
    print("10. Method")
    print("11. Programming Language")
    print("12. Control Structure")
    print("m. Exit")


while True:
    print_menu()
    choice = input("\nChoose a number to get the definition (m to exit): ").strip().lower()

    if choice == 'm':
        print("Program Complete. Goodbye!")
        break
    
    elif choice in terms_definitions:
        term = list(terms_definitions.keys())[int(choice) - 1]
        definition = terms_definitions[term]
        print(f"\n{term}: {definition}\n")
    
    else:
        print("\n<Error> Error! Not a valid choice.\n")
