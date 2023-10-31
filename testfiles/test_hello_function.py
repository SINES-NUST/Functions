from sample_code.student_code import say_hello

def test_say_hello():
    score = 0
    test_input = "test_string"

    if isinstance(test_input, str) and say_hello(test_input) == f"Hello, {test_input}":
        score = 1

    print(f"Say Hello Score: {score}/1")

if __name__ == "__main__":
    test_say_hello()
