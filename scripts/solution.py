def count_divisible_numbers(A, B, K):
    # Function to count the numbers divisible by K in the range [A, B]
    count = 0
    for num in range(A, B + 1):
        if num % K == 0:
            count += 1
    return count

def main():
    # Main function to handle input and output
    T = int(input("Enter the number of test cases: "))  # Number of test cases
    
    for case_number in range(1, T + 1):
        # Loop through each test case
        A = int(input())  # Lower bound of the range
        B = int(input())  # Upper bound of the range
        K = int(input())  # Divisor
        
        # Call the count_divisible_numbers function and print the result
        result = count_divisible_numbers(A, B, K)
        print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    main()
