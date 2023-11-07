# Create a new dictionary, where
# "John", "Jane" and "Gerard" are keys and numbers are values.
phone_book = {"John": 123, "Jane": 234, "Gerard": 345}
print(phone_book)

# Add a new item to the dictionary.
phone_book["Jill"] = 345
print(phone_book)

# Remove a key-value pair from phone_book.
del phone_book["John"]

# Add Jared's number to the phone book
phone_book['Jared'] = 570

# Remove Gerard's number from the phone book
del phone_book['Gerard']

print(phone_book)
print(phone_book['Jane'])
