number = int(input("Enter the number of which you want the table to be generated\n:"))
print(number)

for i in range(1,13):
    answer = number * i
    print(f"{number} x {i} : {answer}")