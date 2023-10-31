from sample_code.student_code import for_loop_function

def test_for_loop():
    score = 0
    if for_loop_function(5) == 15:  # Sum of numbers from 1 to 5
        score += 1
    print(f"For Loop Score: {score}/1")

if __name__ == "__main__":
    test_for_loop()
