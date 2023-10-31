from sample_code.student_code import list_function

def test_list_function():
    score = 0
    if list_function([1, 2, 3]) == 6:  # Sum of list elements
        score += 1
    print(f"List Function Score: {score}/1")

if __name__ == "__main__":
    test_list_function()
