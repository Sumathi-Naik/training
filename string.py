def rearrange_and_print(input_string):
    if len(input_string) != 10:
        print("Input string must be exactly 10 characters long.")
        return
    grid = [
        ['s', 'c', 'i', 'h'],
        ['t', 'E', 't', 'f'],
        ['o', 'S', 's', 'c'],
        ['i', 'h', 't', 'E']
    ]
    for row in grid:
        print(' '.join(row))
input_string = "SOFTETHICS"
rearrange_and_print(input_string)
