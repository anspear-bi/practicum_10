with open('input.txt', 'r') as f_in:
    lines = f_in.readlines()

with open('input.txt', 'w') as f_out:
    for line in lines:
        if line.strip() != '100':
            f_out.write(line)
