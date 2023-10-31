from sample_code.student_code import list_function
import io
import sys

def test_list_function():
    score = 0
    test_list = list(range(10))  # List from 0 to 9
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call student's function
    length = list_function(test_list)
    
    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check if the function returns the correct length of 10
    if length == 10:
        score += 0.5

    # Check if the function printed all elements
    if captured_output.getvalue().strip() == "0 1 2 3 4 5 6 7 8 9":
        score += 0.5

    print(f"List Function Score: {score}/1")

if __name__ == "__main__":
    test_list_function()
