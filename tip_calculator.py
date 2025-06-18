# Tip Calculator

monday = float(input("Enter Monday tips: "))
tuesday = float(input("Enter Tuesday tips: "))
wednesday = float(input("Enter Wednesday tips: "))

total = monday + tuesday + wednesday
average = total / 3

print("Total tips: $", total)
print("Average per day: $", round(average, 2))
