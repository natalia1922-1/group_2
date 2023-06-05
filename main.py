def porzadkuj_do_lewej(input):
    szerokosc_kolumny = [max(len(str(row[i])) for row in input) for i in range(len(input[0]))]
    output = []

    for row in input:
        kolumna = [str(value).ljust(width) for value, width in zip(row, szerokosc_kolumny)]
        output.append(kolumna)

    wiersz = [' '.join(row) for row in output]
    return '\n'.join(wiersz)


input_data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output = porzadkuj_do_lewej(input_data)
print(output)
