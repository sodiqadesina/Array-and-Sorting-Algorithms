import time
import os


# Loading phone numbers from Bell.txt 
def load_phone_numbers(file_path):
    with open(file_path, 'r') as f:
        phone_numbers = [int(line.strip()[3:]) for line in f]  # Extract the 7-digit suffixes
    return phone_numbers

# Implementing bucket sort
def bucket_sort(arr):
    max_val = max(arr)
    size = len(arr)
    buckets = [[] for _ in range(size)]
    
    for i in range(size):
        index = arr[i] * size // (max_val + 1)
        buckets[index].append(arr[i])
    
    for i in range(size):
        buckets[i].sort()  # Sorting each bucket
    
    result = []
    for i in range(size):
        result.extend(buckets[i])
    
    return result

# Save sorted phone numbers to a new file
def save_sorted_numbers(sorted_numbers, output_path):
    with open(output_path, 'w') as f:
        for number in sorted_numbers:
            f.write(f'647-{number:07d}\n')  # Reformat back to 647-XXXXXXX

# File paths
file_path = r'C:\Users\sina\Desktop\Masters of Appplied Computing\CP 600 Practical Algorithm Design\Bell.txt'
output_path = os.path.join(os.path.dirname(file_path), 'BucketSorted_Bell.txt')

# Load phone numbers
phone_numbers = load_phone_numbers(file_path)

# Trackin time for bucket sort
start_time = time.time()
sorted_numbers = bucket_sort(phone_numbers)
end_time = time.time()

# Saving sorted phone numbers to the output file
save_sorted_numbers(sorted_numbers, output_path)

# output time taken
print(f"Bucket Sort took {end_time - start_time:.6f} seconds and sorted numbers are saved in '{output_path}'.")

