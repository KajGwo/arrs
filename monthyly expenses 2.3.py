# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95],    # Week 4
]

# Calculates expenses
# Use loop statements

x = 0
z = []
b = []
a = []
c = -1
d = []
y = -1
for i in monthly_expenses:
     z.append(monthly_expenses[y][0])
     a.append(monthly_expenses[y][1])
     b.append(monthly_expenses[y][2])
     d.append(monthly_expenses[y][0])
     y = y + 1
     c = c + 1


print('MONTHLY EXPENSES')
print('----------------')
print('Food:',sum(z))
print('Transport:', sum(a))
print('Utilities:', sum(b))
print('Week 1:',sum(monthly_expenses[0]))
print('Week 2:',sum(monthly_expenses[1]))
print('Week 3:',sum(monthly_expenses[2]))
print('Week 4:',sum(monthly_expenses[3]))
print('---------------')
print('TOTAL:',sum(monthly_expenses[0]) + sum(monthly_expenses[1]) + sum(monthly_expenses[2]) + sum(monthly_expenses[3]))