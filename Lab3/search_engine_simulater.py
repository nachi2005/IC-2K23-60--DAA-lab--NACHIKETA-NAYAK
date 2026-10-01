# Program 8: Search Engine Simulator
# DAA Lab 3

from binary_search import binary_search


# 30+ words with document IDs
word_data = {
    "algorithm": 101,
    "array": 102,
    "binary": 103,
    "bubble": 104,
    "code": 105,
    "computer": 106,
    "data": 107,
    "database": 108,
    "graph": 109,
    "hash": 110,
    "heap": 111,
    "insertion": 112,
    "integer": 113,
    "iteration": 114,
    "linear": 115,
    "merge": 116,
    "network": 117,
    "node": 118,
    "program": 119,
    "python": 120,
    "quick": 121,
    "radix": 122,
    "recursion": 123,
    "search": 124,
    "selection": 125,
    "sort": 126,
    "stack": 127,
    "string": 128,
    "tree": 129,
    "variable": 130,
    "vector": 131,
    "queue": 132,
    "linked": 133,
    "matrix": 134,
    "function": 135
}

words = list(word_data.keys())


# ---------------- BINARY SEARCH ----------------
def binary_search_word(word_list, target):
    comparisons = 0
    low = 0
    high = len(word_list) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if word_list[mid] == target:
            return mid, comparisons
        elif word_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# ---------------- CUSTOM HASH FUNCTION ----------------
def custom_hash(word, table_size):
    hash_value = 0

    for char in word:
        hash_value = (hash_value * 31 + ord(char)) % table_size

    return hash_value


# ---------------- CHAINING ----------------
def create_chaining_table(word_list, table_size):
    table = [[] for _ in range(table_size)]

    for word in word_list:
        index = custom_hash(word, table_size)
        table[index].append(word)

    return table


def search_chaining(table, target):
    index = custom_hash(target, len(table))
    comparisons = 0

    for word in table[index]:
        comparisons += 1

        if word == target:
            return True, comparisons

    return False, comparisons


# ---------------- LINEAR PROBING ----------------
def create_linear_probing_table(word_list, table_size):
    table = [None] * table_size
    probes = 0

    for word in word_list:
        index = custom_hash(word, table_size)

        while table[index] is not None:
            probes += 1
            index = (index + 1) % table_size

        table[index] = word

    return table, probes


def search_linear_probing(table, target):
    index = custom_hash(target, len(table))
    probes = 0

    while table[index] is not None:
        probes += 1

        if table[index] == target:
            return True, probes

        index = (index + 1) % len(table)

    return False, probes


# ---------------- MAIN PROGRAM ----------------

words.sort()

print("===== SEARCH ENGINE SIMULATOR =====")

print("\nAvailable words:")
print(", ".join(words))

target = input("\nEnter word to search: ").lower()


# Binary Search
index, binary_comparisons = binary_search_word(words, target)

print("\n--- Binary Search ---")

if index != -1:
    print("Word found at index:", index)
else:
    print("Word not found")

print("Comparisons:", binary_comparisons)


# Hash Table - Chaining
table_size = 11

chaining_table = create_chaining_table(words, table_size)

found_chain, chain_comparisons = search_chaining(
    chaining_table, target
)

print("\n--- Hashing with Chaining ---")

if found_chain:
    print("Word found")
else:
    print("Word not found")

print("Comparisons:", chain_comparisons)


# Hash Table - Linear Probing
linear_table, insertion_probes = create_linear_probing_table(
    words, 37
)

found_linear, linear_probes = search_linear_probing(
    linear_table, target
)

print("\n--- Hashing with Linear Probing ---")

if found_linear:
    print("Word found")
else:
    print("Word not found")

print("Search probes:", linear_probes)

print("\n===== SEARCH COMPLETE =====")