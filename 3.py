with open('input.txt', 'r') as f_in:
    lines = f_in.readlines()

result = ''.join(line[0] for line in lines if line)

with open('output.txt', 'w') as f_out:
    f_out.write(result)
