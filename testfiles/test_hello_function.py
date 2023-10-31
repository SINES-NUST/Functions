from sample_code.student_code import say_hello
import io
import sys

def test_hello_function():
    score = 0
    name = "Mehak"  # Variable for test

    captured_output = io.StringIO()
    sys.stdout = captured_output

    say_hello(name)

    sys.stdout = sys.__stdout__

    if captured_output.getvalue().strip() == f"Hello, {name}":
        score += 1

    print(f"Hello Function Score: {score}/1")

if __name__ == "__main__":
    test_hello_function()