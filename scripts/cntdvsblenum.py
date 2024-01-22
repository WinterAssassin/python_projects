def count_divisible_numbers(A, B, K):
    # Function to count the numbers divisible by K in the range [A, B]
    count = 0
    for num in range(A, B + 1):
        if num % K == 0:
            count += 1
    return count

def main():
    # Main function to handle input and output
    # input_file_path = input("Enter the path to the input file: ")

    with open("C:\\Users\\mjcab\\Downloads\\input.in", 'r') as file:
        # Read the number of test cases
        T = int(file.readline().strip())

        for case_number in range(1, T + 1):
            # Read input for each test case
            A = int(file.readline().strip())
            B = int(file.readline().strip())
            K = int(file.readline().strip())
            
            # Call the count_divisible_numbers function and print the result
            result = count_divisible_numbers(A, B, K)
            print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    main()

