# Read a sequence of numbers
sequence_input = input("Enter a sequence of numbers separated by spaces: ")
sequence = [float(num) for num in sequence_input.split()]

# Read the dimensions of the 2D array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Read the 2D array
array = []

for i in range(rows):
    row = []
    for j in range(cols):
        num = float(input(f"Enter element [{i}][{j}]: "))
        row.append(num)
    array.append(row)

# Display the sequence and array
print("\n--- Results ---")

print("Sequence of numbers:")
print(sequence)

print("\n2D Array:")
for row in array:
    print(row)