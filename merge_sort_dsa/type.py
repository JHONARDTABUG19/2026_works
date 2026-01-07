import time


type_order = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting",
    "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost",
    "Dragon", "Dark", "Steel", "Fairy"
]


type_rank = {t: i for i, t in enumerate(type_order)}        #Creates a dictionary where keys are the Pokémon types (t)
                                                            #Values are their index (i)

unsorted_types = [
    "Water", "Grass", "Fighting", "Electric", "Psychic", "Fire", "Water",
    "Grass", "Dark", "Fire", "Fighting", "Water", "Water", "Fire",
    "Normal", "Fairy", "Rock", "Psychic"
]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right): 
            if type_rank[left[i]] < type_rank[right[j]]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

print(" ")
print("Unsorted types:", unsorted_types)

start_time = time.perf_counter() 

merge_sort(unsorted_types)

end_time = time.perf_counter()

elapsed = end_time - start_time

print(" ")
print("Sorted types:", unsorted_types)
print(" ")

print(f"Time it took: {elapsed * 1000:.2f} milliseconds")
print(" ")

