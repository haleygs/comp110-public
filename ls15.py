"""Sorting, ranges, and for...in loops."""



"""Examples of built-in sorting facilities in Python."""

scores: list[int] = [95, 96, 80, 99, 78, 60]
sorted_scores: list[int] = sorted(scores)

print("Built-in sort function")
print(f"sorted_scores: {sorted_scores}")
print(f"scores: {scores}")



"""The insertion sort algorithm."""

def isort(xs: list[int]) -> None:
    i: int = 1
    j: int 
    while i < len(xs):
        j = i
        while j > 0 and xs[j] < xs[j-1]:
            swap(xs, j, j - 1)
            j -= 1
        
        i += 1

def swap(xs: list[int], i: int, j: int) -> None:
    temp: int = xs[i]
    xs[i] = xs[j]
    xs[j] = temp



"""Range example."""

start: int = 0
stop: int = 100
step: int = 10

a_range: range = range(start, stop, step)
print(a_range.start)
print(a_range.stop)
print(a_range.step)

a_range = range(10, 100) # Default step value is 1



"""for...in loop examples."""

# Iterate through each item in a list
letters: list[str] = ["a", "b", "c", "d", "e", "f", "g"]

# Print each letter in the letters list
print("Each letter...")
for letter in letters:
    print(letter)

# Print every other letter in letters list
print("Every other letter...")
for i in range(0, len(letters), 2):
    print(letters[i])

# Iterate through each index in a sequence
for i in range(len(letters)):
    print(f"i: {i} - letters[i]: {letters[i]}")