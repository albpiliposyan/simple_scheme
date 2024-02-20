## DESCRIPTION
A simple interpreter written in python to run scheme scripts.
The script gets the input file as an argument of 'interpret' function.

#### Parsing:
(parsing.py)
It parses the file with '(' and ')' delimiters: goes character by character
through the file, places each token as an element of a list. If there is another
open parenthesis, it creates a list with its element in the parent list. By the way,
it checks if there is a redundant or a missing parenthesis keeping that number in
'parens = 0' variable. It also ignores all comments on the input_file.

#### Interpreting:
(scheme_methods.py)
There are dictionaries for scheme methods, defined identifiers and defined functions
in 'scheme_methods.py' file. There featured scheme methods are mentioned in the
'dicitonary' dict. There are also simple implementations above it.
All user defined functions will be stored in another dictionary called 'functions'.
This dict will have the function name as a key, and will have a list of passed
arguments and defined function body as a its value.

#### Evaluating:
(interpreter.py)
We start interpreting the scheme script recursively. The program finds the child
list and then returns its value to its parent list, and continues to interpret that
current list. If the first element of the current list exists in the dictionary of
scheme methods or defined functions, it straigthly replaces its return value instead
of the current list. When seeing a declared variable matching with a key in
of 'identifiers' dictionary, the program replaces it with its value.
At the end, the program returns the root expression with already interpreted values.

#### Testing:
(functional_testing/)
All written functions are tested in functional_testing/tester.py file. You can run
the test files calling 'python3 testers.py'


## FILES
README.md: Script description
parsing.py: Parses the scheme file with parentheses
scheme_methods.py: A library with necessary scheme method
interpreter.py: Interpretes the scheme script
test.scm: A basic scheme file to check if out interpreter runs properly
tester.py: Functional testing

## REQUIREMENTS
Python3: sudo apt-get install python3


## USAGE
Pass the runnable scheme script's path an 'input_file' in interpret function in
interpreter.py
Type 'python3 interpreter.py' in terminal to run the interpreter


## NOTES
There is a test scheme script in current directory to check if the program
runs properly.

