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


hp = [72, 45, 70, 35, 68, 39, 41, 60, 60, 78, 40, 84, 54, 80, 55, 95, 100, 25]

print(" ")
print("Unsorted:", hp)
print(" ")

start_time = time.perf_counter()   #  high-precision start
merge_sort(hp)
end_time = time.perf_counter()     #  high-precision end

elapsed = end_time - start_time

print("Sorted HP:", hp)
print(" ")



print(f"Time it took: {elapsed * 1000:.2f} milliseconds")
print(" ")

