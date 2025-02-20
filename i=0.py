total = 0
age = 0
countPassengers = 0

while True:
    if countPassengers < 5:
        age = int(input())
        countPassengers = countPassengers + 1

        if age < 3:
            continue
        elif age >= 3:
            total = total + 100
    else:
        print(total)
        break


    
