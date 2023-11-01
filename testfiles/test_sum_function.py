import sys
import os

# Add the parent directory to sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


from sample_code.student_code import sum_function

def test_sum_function():
    score = 0
    a, b = 8, 18.9  # Variables for test
    
    if sum_function(a, b) == a + b:
        score += 2

    print(f"Sum Function Score: {score}/2")

if __name__ == "__main__":
    test_sum_function()
