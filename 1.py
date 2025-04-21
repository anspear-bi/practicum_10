with open('input.txt', 'r') as f_in:
    data = f_in.read()

with open('output.txt', 'w') as f_out:
    f_out.write(data.upper())
    
