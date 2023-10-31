from sample_code.student_code import say_hello

def test_hello_function():
    score = 0
    if say_hello("Mehak") == "Hello, Mehak":
        score += 1
    print(f"Hello Function Score: {score}/1")

if __name__ == "__main__":
    test_hello_function()
