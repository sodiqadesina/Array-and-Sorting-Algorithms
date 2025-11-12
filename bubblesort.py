import time
import os

# Load phone numbers from Bell.txt 

def load_phone_numbers(file_path):
    with open(file_path, 'r') as f:
        phone_numbers = [int(line.strip()[3:]) for line in f]  # Extract the 7-digit suffixes
    return phone_numbers

# Implement bubble sort on a sample
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Save sorted phone numbers to a new file
def save_sorted_numbers(sorted_numbers, output_path):
    with open(output_path, 'w') as f:
        for number in sorted_numbers:
            f.write(f'647-{number:07d}\n')  

# File paths
file_path = r'C:\Users\sina\Desktop\Masters of Appplied Computing\CP 600 Practical Algorithm Design\Bell.txt'
output_path = os.path.join(os.path.dirname(file_path), 'Bubble_Sorted_Sample.txt')

phone_numbers = load_phone_numbers(file_path)
sample_phone_numbers = phone_numbers[:40000]  # Take the first 40,000 numbers as a sample

# Track time for bubble sort
start_time = time.time()
sorted_numbers = bubble_sort(sample_phone_numbers)
end_time = time.time()

save_sorted_numbers(sorted_numbers, output_path)


print(f"Bubble Sort (Sample of 40,000) took {end_time - start_time:.6f} seconds and sorted numbers are saved in '{output_path}'.")
