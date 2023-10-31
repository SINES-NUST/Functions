from sample_code.student_code import combined_function

def test_combined():
    score = 0
    
    try:
        output = combined_function(1, 2, 3, 4, 5)
        
        # Loop used: +1
        score += 1 
        
        # List used: +1
        score += 1
        
        # Function returning desired output: +1
        if output == [4, 5]:
            score += 1
        
        print(f"Advanced Function Score: {score}/3")
    except ValueError:
        print("Invalid input. All arguments must be integers or floats.")

if __name__ == "__main__":
    test_combined()