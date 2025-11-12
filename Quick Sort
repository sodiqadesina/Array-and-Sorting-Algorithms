import time
import os

# Load phone numbers from Bell.txt without displaying them
def load_phone_numbers(file_path):
    with open(file_path, 'r') as f:
        phone_numbers = [int(line.strip()[3:]) for line in f]  # Extract the 7-digit suffixes
    return phone_numbers

# Implemention of  quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Saving sorted phone numbers to a new file
def save_sorted_numbers(sorted_numbers, output_path):
    with open(output_path, 'w') as f:
        for number in sorted_numbers:
            f.write(f'647-{number:07d}\n')  # Reformat back to 647-XXXXXXX

# File paths
file_path = r'C:\Users\sina\Desktop\Masters of Appplied Computing\CP 600 Practical Algorithm Design\Bell.txt'
output_path = os.path.join(os.path.dirname(file_path), 'Quick_Sorted_Bell.txt')

# Load phone numbers
phone_numbers = load_phone_numbers(file_path)

# Track time for quick sort
start_time = time.time()
sorted_numbers = quick_sort(phone_numbers)
end_time = time.time()


save_sorted_numbers(sorted_numbers, output_path)

print(f"Quick Sort took {end_time - start_time:.6f} seconds and sorted numbers are saved in '{output_path}'.")
