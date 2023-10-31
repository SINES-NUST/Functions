from sample_code.student_code import sum_function

def test_sum_function():
    score = 0
    if sum_function(3, 4) == 7:
        score += 1
    print(f"Sum Function Score: {score}/1")

if __name__ == "__main__":
    test_sum_function()
