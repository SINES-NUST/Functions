from sample_code.student_code import list_function
import io
import sys

def test_list_function():
    score = 0
    test_list = list(range(10))  # Variable for test

    captured_output = io.StringIO()
    sys.stdout = captured_output

    length = list_function(test_list)

    sys.stdout = sys.__stdout__

    if length == 10:
        score += 1

    if captured_output.getvalue().strip() == ' '.join(map(str, test_list)):
        score += 1

    print(f"List Function Score: {score}/2")

if __name__ == "__main__":
    test_list_function()
