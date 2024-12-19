import sys

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            line = line.strip()
            number = int(line)
            numbers.append(number)
    return numbers

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    total_moves = 0
    for num in nums:
        total_moves += abs(num - median)
    return total_moves

file_path = sys.argv[1]
numbers = read_numbers(file_path)
print(min_moves(numbers))
