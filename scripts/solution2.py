# def count_word_occurrences(grid, word):
#     rows, cols = len(grid), len(grid[0])
#     word_length = len(word)
#     count = 0

#     for i in range(rows):
#         for j in range(cols):
#             # Check horizontally
#             if j + word_length <= cols and grid[i][j : j + word_length] == word:
#                 count += 1
#             # Check vertically
#             if i + word_length <= rows and all(grid[i + k][j] == word[k] for k in range(word_length)):
#                 count += 1
#             # Check diagonally (top-left to bottom-right)
#             if i + word_length <= rows and j + word_length <= cols and all(
#                 grid[i + k][j + k] == word[k] for k in range(word_length)
#             ):
#                 count += 1
#             # Check diagonally (top-right to bottom-left)
#             if i + word_length <= rows and j - word_length + 1 >= 0 and all(
#                 grid[i + k][j - k] == word[k] for k in range(word_length)
#             ):
#                 count += 1

#     return count

# def word_search_solver():
#     T = int(input("Enter the number of test cases: "))

#     for case_number in range(1, T + 1):
#         N, M = map(int, input().split())

#         # Read the grid
#         grid = [input().strip() for _ in range(N)]

#         # Read the word to search for
#         word = input().strip()

#         # Call the count_word_occurrences function and print the result
#         result = count_word_occurrences(grid, word)
#         print(f"Case {case_number}: {result}")

# if __name__ == "__main__":
#     word_search_solver()


def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    count = 0

    for i in range(rows):
        for j in range(cols):
            # Check horizontally
            if j + word_length <= cols and grid[i][j : j + word_length] == word:
                count += 1
            # Check vertically
            if i + word_length <= rows and all(grid[i + k][j] == word[k] for k in range(word_length)):
                count += 1
            # Check diagonally (top-left to bottom-right)
            if i + word_length <= rows and j + word_length <= cols and all(
                grid[i + k][j + k] == word[k] for k in range(word_length)
            ):
                count += 1
            # Check diagonally (top-right to bottom-left)
            if i + word_length <= rows and j - word_length + 1 >= 0 and all(
                grid[i + k][j - k] == word[k] for k in range(word_length)
            ):
                count += 1

    return count

def word_search_solver(file_path):
    with open(file_path, "r") as file:
        T = int(file.readline().strip())

        for case_number in range(1, T + 1):
            N = int(file.readline().strip())
            M = int(file.readline().strip())

            # Read the grid
            grid = [file.readline().strip() for _ in range(N)]

            # Read the word to search for
            word = file.readline().strip()

            # Call the count_word_occurrences function and print the result
            result = count_word_occurrences(grid, word)
            print(f"Case {case_number}: {result}")

if __name__ == "__main__":
    file_path = "C:\\Users\\mjcab\\Downloads\\input.in"
    word_search_solver(file_path)
