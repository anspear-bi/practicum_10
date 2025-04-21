try:
    with open('input.txt', 'r') as f_in:
        a = int(f_in.readline())
        b = int(f_in.readline())
        c = int(f_in.readline())
    result = a / b + c
except ValueError:
    result = "ValueError"
except ZeroDivisionError:
    result = "ZeroDivisionError"

with open('output.txt', 'w') as f_out:
    f_out.write(str(result))
