
def porzadkuj_do_lewej(input_data):
    szerokosc_kolumny = [max(map(len, map(str, col))) for col in zip(*input_data)]  # maksymalna długość kolumn

    # tworzenie uporządkowania i wyrównania do lewej
    do_porzadkowania = [
        ['{:<{}}'.format(str(value), szerokosc_kolumny[i])
        for i, value in enumerate(row)]
        for row in input_data
                        ]

    # wyniki końcowe
    result = '\n'.join([' '.join(row) + (' ' if i % 2 else '') for i, row in enumerate(do_porzadkowania)])

    return result


input_data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output = porzadkuj_do_lewej(input_data)
print(output)

def format_data_right_aligned(data):

    szerokosc_kolumn = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
    
    
    formatted_data = []
    for wiersz in data:
        formatted_row = [str(value).rjust(width) for value, width in zip(wiersz, szerokosc_kolumn)]
        formatted_data.append(formatted_row)
    
    
    formatted_lines = [' '.join(wiersz) for wiersz in formatted_data]
    return '\n'.join(formatted_lines)

# Przykładowe użycie
input_data = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output = format_data_right_aligned(input_data)
print(output)

def test_format_data_right_aligned():
    input_data = [[[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
    expected_output = "[[1,   2   10  150\n 10    2 1000    2\n  1  120    1 1000"
    assert format_data_right_aligned(input_data) == expected_output

test_format_data_right_aligned()

