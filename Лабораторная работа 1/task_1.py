numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = 4
missing_index_1 = 5
n = numbers[:missing_index] + numbers[missing_index_1:]
numbers[missing_index] = sum(n)/len(numbers)
print("Измененный список:", numbers)
