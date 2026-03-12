import random

# 2. Sort: Recursive Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return sorted(left + right) # Simplified recursion for the lab

# 4. Execute: Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def run_judging():
    # 1. Generate Data
    scores = [random.randint(50, 100) for _ in range(10)]
    print(f"Original Scores: {scores}")

    # Sort
    sorted_scores = merge_sort(scores)
    print(f"Sorted Scores: {sorted_scores}")

    # 3. Search
    try:
        target = int(input("Enter a score to find the rank: "))
        rank = binary_search(sorted_scores, target)
        
        if rank != -1:
            print(f"Candidate with score {target} found at rank {rank}.")
        else:
            print("Score not found in the list.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    run_judging()
