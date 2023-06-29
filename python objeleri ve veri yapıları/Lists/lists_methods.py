numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
val = max(numbers)

val = max(letters)
val = min(letters)

numbers.append(49)
numbers.append(59)
numbers.insert(3, 78)
# numbers.insert(-1, 52)

# numbers.pop(-1)
numbers.remove(49)

numbers.sort()
letters.sort()

numbers.reverse()
letters.reverse()

# numbers.clear()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))
