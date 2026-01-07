import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:  # alphabetical comparison
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


names = [
    "Greninja",
    "Bulbasaur",
    "Lucario",
    "Pikachu",
    "Gardevoir",
    "Charmander",
    "Froakie",
    "Ivysaur",
    "Zoroark",
    "Charizard",
    "Riolu",
    "Empoleon",
    "Frogadier",
    "Blaziken",
    "Eevee",
    "Sylveon",
    "Tyranitar",
    "Abra"
]

print(" ")
print("Unsorted names:", names)
print(" ")
print(" ")

start_time = time.perf_counter()   #  high-precision start
merge_sort(names)
end_time = time.perf_counter() 

elapsed = end_time - start_time

print("Alphabetically sorted names:", names)
print(" ")

print(f"Time it took: {elapsed * 1000:.2f} milliseconds")
print(" ")

