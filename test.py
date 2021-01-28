from sys import argv

print("In this program you are building stairs.")
print("Please tell me how big you want your stairs?")

height = int(input())

for i in range(height):
    print(" " * (height - i), end=' ')
    print("#" * (i + 1), end=' ')
    print("  ", end=' ')
    print("#" * (i + 1))




