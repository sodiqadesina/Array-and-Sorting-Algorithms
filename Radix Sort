import time
import os

def load_phone_numbers(file_path):
    with open(file_path, 'r') as f:
        phone_numbers = [int(line.strip()[3:]) for line in f]  # Extract the 7-digit suffixes
    return phone_numbers

# Implementing counting sort as a helper for radix sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Because we are working with digits 0-9
    
    # Storing count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so that count[i] contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copy the output array to arr[]
    for i in range(n):
        arr[i] = output[i]

# Implement radix sort
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Save sorted phone numbers to a new file
def save_sorted_numbers(sorted_numbers, output_path):
    with open(output_path, 'w') as f:
        for number in sorted_numbers:
            f.write(f'647-{number:07d}\n') 

# File paths
file_path = r'C:\Users\sina\Desktop\Masters of Appplied Computing\CP 600 Practical Algorithm Design\Bell.txt'
output_path = os.path.join(os.path.dirname(file_path), 'Radix_Sorted_Bell.txt')

# Load phone numbers
phone_numbers = load_phone_numbers(file_path)

# Tracking time for radix sort
start_time = time.time()
radix_sort(phone_numbers)
end_time = time.time()

# Savin sorted phone numbers to the output file
save_sorted_numbers(phone_numbers, output_path)

print(f"Radix Sort took {end_time - start_time:.6f} seconds and sorted numbers are saved in '{output_path}'.")
