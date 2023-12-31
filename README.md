# Learning Python Functions

## Description
This repository serves as a platform for learning and testing your understanding of Python functions. This is part of the Computiong for BI Course. Regardless of your programming background, this repository aims to help you grasp the basics of Python functions effectively.

## Topics Covered
- Function Declaration and Definition
- Function Calling
- Parameters and Arguments
- Return Statements


## Getting Started
1. Fork this repository to your GitHub account.
2. Clone the forked repository to your local machine.

## Directory Structure

```bash
SINES-NUST/Functions/
│
├── testfiles/                    # Folder containing test scripts
│   ├── test_hello_function.py
│   ├── test_sum_function.py
│   ├── test_for_loop.py
│   ├── test_list_function.py
│   └── test_combined.py
│
├── sample_code/                  # Folder containing sample code
│   └── student_code.py
│
└── README.md                     # This file
```

## Your Tasks

You are required to write code for the following topics:

- Basic functions
- Sum functions
- For loops
- List manipulations
- A combination of the above

Each topic has its own test file in the `testfiles/` directory. Make sure to write your code in a file named `student_code.py` at the root level of this repository.

## How to Test Your Code

Navigate to the root directory of this repository and run the test scripts one by one like so:

```bash
python testfiles/test_hello_function.py
python testfiles/test_sum_function.py
python testfiles/test_for_loop.py
python testfiles/test_list_function.py
python testfiles/test_combined.py
```

Each test will output your score for that specific task. Aim for a perfect score!

## Autograding

When you push your code to this repository, GitHub Classroom will automatically grade your submission based on the test files. Check your grade once the tests are done running.

## Function Requirements

### Say Hello Function (`say_hello`)

1. The function should be named `say_hello`.
2. It should take a single argument, which will be a string.
3. The function should print "Hello, [name]" where [name] is the input argument.

**Test Assessment:**
- Your implementation will be checked for printing the correct greeting. A correct answer will earn a score of `1`.

### Sum Function (`sum_function`)

1. The function should be named `sum_function`.
2. It should take two arguments, which could be integers or floats.
3. The function should return the sum of these two arguments.

**Test Assessment:**
- Your implementation will be checked to ensure that it sums the two arguments correctly. A correct answer will earn a score of `2`.

### List Function (`list_function`)

1. The function should be named `list_function`.
2. It should take a single argument, which will be a list of integers.
3. The function should print all elements of the list and return the length of the list.

**Test Assessment:**
- Your implementation will be checked to ensure that it prints the elements and returns the correct length of the list. A correct answer will earn a score of `2` (1 for print, 1 for length).

### Max Value Function (`loop_function`)

1. The function should be named `loop_function`.
2. It should accept a list of integers or floats as its argument.
3. Use a loop to find the maximum value in the given list.
4. The function should return the maximum value.

**Test Assessment:**
- Correctly finds the max value: +2
- Total marks: +2

### Combined Function (`combined_function`)

1. The function should be named `combined_function`.
2. It should accept a variable number of arguments that can be either integers or floats.
3. The function should raise a ValueError if any argument is a string.
4. Use a loop to find the average of the list of numbers.
5. The function should return a list of elements greater than the average.

**Test Assessment:**
- Loop used: +1
- List used: +1
- Function returning desired output: +1
- Total marks: +3