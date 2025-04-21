with open('input.txt', 'r') as f_in:
    lines = f_in.readlines()

with open('output.txt', 'w') as f_out:
    for line in lines:
        if len(line.rstrip('\n')) > 20:
            f_out.write(line)
