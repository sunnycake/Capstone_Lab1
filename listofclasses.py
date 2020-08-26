class_qty = int(input("How many classes are you taking this semester? "))

total = []
for classes in range(class_qty):
    className = input("Enter the name of the class: ")
    total.append(className)
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
print("The classes you are taking are: ", *total, sep="\n")
