def porzadkuj_do_lewej(input_data):
    szerokosc_kolumny = [max(map(len, map(str, col))) for col in zip(*input_data)]  # maksymalna długość kolumn

    do_porzadkowania = [
        ['{:<{}}'.format(str(value), szerokosc_kolumny[i])
        for i, value in enumerate(row)]
        for row in input_data
                        ]

    result = '\n'.join([' '.join(row) + (' ' if i % 2 else '') for i, row in enumerate(do_porzadkowania)])

    return result


input_data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output = porzadkuj_do_lewej(input_data)
print(output)
