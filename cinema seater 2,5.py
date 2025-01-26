# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

z = []
y = 0
for i in cinema_seats:
    z.append(cinema_seats[0][y])
    z.append(cinema_seats[1][y])
    z.append(cinema_seats[2][y])
    z.append(cinema_seats[3][y])
    z.append(cinema_seats[4][y])
    y = y + 1

print('CINEMA INFORMATION TABLE')
print('Total seats:', (len(z)))
print('Seats available:', z.count("A"))
print('Seats booked:', z.count("B"))
print('Seat in row 1, place 1:', (cinema_seats[0][0]))
print('Seat in row 5, place 5:', (cinema_seats[4][4]))
print('Seat in row 3, place 5:', (cinema_seats[2][4]))