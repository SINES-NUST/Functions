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