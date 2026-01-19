import time

# Pokemon Sorting System (MERGE SORT)



# Pokemon Type Order (Given)

TYPE_ORDER = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
    "Fighting", "Poison", "Ground", "Flying", "Psychic",
    "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
]


# Pokemon Data

pokemon = [
    {"name": "Greninja", "evo": 3, "gen": 6, "hp": 72, "type": "Water"},
    {"name": "Bulbasaur", "evo": 1, "gen": 1, "hp": 45, "type": "Grass"},
    {"name": "Lucario", "evo": 2, "gen": 4, "hp": 70, "type": "Fighting"},
    {"name": "Pikachu", "evo": 2, "gen": 1, "hp": 35, "type": "Electric"},
    {"name": "Gardevoir", "evo": 3, "gen": 3, "hp": 68, "type": "Psychic"},
    {"name": "Charmander", "evo": 1, "gen": 1, "hp": 39, "type": "Fire"},
    {"name": "Froakie", "evo": 1, "gen": 6, "hp": 41, "type": "Water"},
    {"name": "Ivysaur", "evo": 2, "gen": 1, "hp": 60, "type": "Grass"},
    {"name": "Zoroark", "evo": 2, "gen": 5, "hp": 60, "type": "Dark"},
    {"name": "Charizard", "evo": 3, "gen": 1, "hp": 78, "type": "Fire"},
    {"name": "Riolu", "evo": 1, "gen": 4, "hp": 40, "type": "Fighting"},
    {"name": "Empoleon", "evo": 3, "gen": 4, "hp": 84, "type": "Water"},
    {"name": "Frogadier", "evo": 2, "gen": 6, "hp": 54, "type": "Water"},
    {"name": "Blaziken", "evo": 3, "gen": 3, "hp": 80, "type": "Fire"},
    {"name": "Eevee", "evo": 1, "gen": 1, "hp": 55, "type": "Normal"},
    {"name": "Sylveon", "evo": 2, "gen": 6, "hp": 95, "type": "Fairy"},
    {"name": "Tyranitar", "evo": 3, "gen": 2, "hp": 100, "type": "Rock"},
    {"name": "Abra", "evo": 1, "gen": 1, "hp": 25, "type": "Psychic"},
]


# MERGE SORT IMPLEMENTATION
#this is where splitting happens by dividing the array into halves recursively
def merge_sort(arr, key_func):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key_func)
    right = merge_sort(arr[mid:], key_func)

    return merge(left, right, key_func)

#once every array contains one element, merging happens here by comparing elements based on the key function
def merge(left, right, key_func):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# DISPLAY FUNCTION

def display(data):
    print("\nName        Evo  Gen  HP   Type")
    print("-" * 40)
    for p in data:
        print(f"{p['name']:<11} {p['evo']:<4} {p['gen']:<4} {p['hp']:<4} {p['type']}")
    print()


# FINAL MULTI-LEVEL SORT (MERGE SORT ONLY)

def final_merge_sort(data):
    data = merge_sort(data, lambda x: x["name"])                     # A-Z
    data = merge_sort(data, lambda x: TYPE_ORDER.index(x["type"]))  # Type
    data = merge_sort(data, lambda x: x["hp"])                       # HP
    data = merge_sort(data, lambda x: x["gen"])                      # Generation
    data = merge_sort(data, lambda x: x["evo"])                      # Evolution Stage
    return data



# MENU INTERFACE


def menu():
    current = pokemon[:]

    while True:
        print("""
====================================
Pokemon Sorting Menu (MERGE SORT)
====================================
1. Display Pokemon
2. Sort by Evolution Stage
3. Sort by Generation
4. Sort by HP
5. Sort by Pokemon Type
6. Sort Alphabetically (A-Z)
7. FINAL SORT (All Rules Applied)
0. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            display(current)

        elif choice == "2":
            current = merge_sort(current, lambda x: x["evo"])
            print("Sorted by Evolution Stage.")

        elif choice == "3":
            current = merge_sort(current, lambda x: x["gen"])
            print("Sorted by Generation.")

        elif choice == "4":
            current = merge_sort(current, lambda x: x["hp"])
            print("Sorted by HP.")

        elif choice == "5":
            current = merge_sort(current, lambda x: TYPE_ORDER.index(x["type"]))
            print("Sorted by Pokemon Type.")

        elif choice == "6":
            current = merge_sort(current, lambda x: x["name"])
            print("Sorted Alphabetically.")

        elif choice == "7":
            print("Sorting... Please wait.")

            start = time.perf_counter()  # Start timer

            current = final_merge_sort(pokemon)

            end = time.perf_counter()  # End timer

            print(f"\nFINAL SORT COMPLETED in {end - start:.6f} seconds")
            display(current)


        elif choice == "0":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Try again.")


# PROGRAM START

menu()
