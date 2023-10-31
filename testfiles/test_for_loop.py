import sys
import os

# Add the parent directory to sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from sample_code.student_code import combined_function

from sample_code.student_code import loop_function

def test_for_loop_function():
    score = 0
    test_list = [3, 8, 2, 1, 5, 7, 4, 6]  # Unordered list for test
    
    max_value = loop_function(test_list)
    
    if max_value == max(test_list):
        score += 2

    print(f"Max Value Function Score: {score}/2")

if __name__ == "__main__":
   test_for_loop_function()