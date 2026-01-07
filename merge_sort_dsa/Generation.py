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


Generation = [6, 1, 4, 1, 3, 1, 6, 1, 5, 1, 4, 4, 6, 3, 1, 6, 2, 1]


print(" ")
print("Unsorted:", Generation)
print(" ")

start_time = time.perf_counter()   #  high-precision start
merge_sort(Generation)
end_time = time.perf_counter()     #  high-precision end

elapsed = end_time - start_time

print("Sorted Generation:", Generation)
print(" ")



print(f"Time it took: {elapsed * 1000:.2f} milliseconds")
print(" ")

