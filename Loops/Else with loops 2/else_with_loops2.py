def contains_even_number(lst):
    even = False
    for num in lst:
        if num % 2 == 0:
            even = True
            break
    if even:
        print(f"List {lst} contains an even number.")
    else:
        print(f"List {lst} does not contain an even number.")



contains_even_number([1, 9, 8])
contains_even_number([1, 3, 5])