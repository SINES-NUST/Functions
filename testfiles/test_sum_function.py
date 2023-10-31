from sample_code.student_code import sum_function

def test_sum_function():
    score = 0
    sample_input1 = 8
    sample_input2 = 18.9

    # Check if the function accepts integers and floats only
    try:
        result = sum_function(sample_input1, sample_input2)
        if isinstance(result, (int, float)):
            score += 1
    except:
        pass

    # Check if the function correctly adds 8 and 18.9 to get 26.9
    if sum_function(8, 18.9) == 26.9:
        score += 1
    
    print(f"Sum Function Score: {score}/1")

if __name__ == "__main__":
    test_sum_function()
