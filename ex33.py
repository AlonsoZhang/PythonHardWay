i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("numbers now:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers:")

for num in numbers:
    print(num)


# study drills

# ex33: While Loops


def create_numbers(maxnum, step):
    number = []
    for j in range(0, maxnum, step):
        print("At the top i is %d" % j)
        number.append(j)

        print("Numbers now: ", number)
        print("At the bottom i is %d" % j)
    return number


numbers = create_numbers(10, 2)

print("The number: ")

for num in numbers:
    print(num)
