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
