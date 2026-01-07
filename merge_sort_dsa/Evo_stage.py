import time

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


Evolution_stage_values = [3, 1, 2, 2, 3, 1, 1, 2, 2, 3, 1, 3, 2, 3, 1, 2, 3, 1]

print(" ")
print("Unsorted:", Evolution_stage_values)
print(" ")

start_time = time.perf_counter()   #  high-precision start
merge_sort(Evolution_stage_values)
end_time = time.perf_counter()     #  high-precision end

elapsed = end_time - start_time

print("Sorted Evolution stage:", Evolution_stage_values)
print(" ")



print(f"Time it took: {elapsed * 1000:.2f} milliseconds")
print(" ")

