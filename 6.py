try:
    with open('input.txt', 'r') as f_in:
        first_line = f_in.readline().strip()
        N = int(first_line)
        lines = f_in.readlines()
    if len(lines) == N:
        res = "YES"
    else:
        res = "NO"
except ValueError:
    res = "ERROR"

with open('output.txt', 'w') as f_out:
    f_out.write(res)
