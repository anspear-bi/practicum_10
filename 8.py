days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('input.txt', 'r') as f_in:
    data = [int(line.strip()) for line in f_in]

index = 0
averages = []
for days in days_in_month:
    month_data = data[index:index+days]
    avg = sum(month_data) / days
    averages.append(avg)
    index += days

with open('output.txt', 'w') as f_out:
    for avg in averages:
        f_out.write(str(avg) + '\n')
