first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print(3)
elif first != second and second != third and third != first:
    print(0)
else:
    print(2)