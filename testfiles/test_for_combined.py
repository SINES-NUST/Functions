from sample_code.student_code import combined_function

def test_combined():
    score = 0
    if combined_function([1, 2], 3) == [1, 2, 3]:
        score += 1
    print(f"Combined Topics Score: {score}/1")

if __name__ == "__main__":
    test_combined()
