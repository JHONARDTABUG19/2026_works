import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------- MAIN PROGRAM --------
data = [3, 1, 4, 6, 5, 10, 9, 15, 11, 7]

start_time = time.time()        # ⏱ start timing
sorted_data = merge_sort(data)
end_time = time.time()          # ⏱ end timing

print("Sorted list:", sorted_data)
print("Time taken:", end_time - start_time, "seconds")
