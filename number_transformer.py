class NumberTransformer:
    def __init__(self, file_name):
        self.file_name = file_name

    def transform(self):
        with open(self.file_name, 'r') as input_file:
            number_list = list(map(int, input_file.read().split()))

        even_number_squares = [number**2 for number in number_list if number % 2 == 0]
        odd_number_cubes = [number**3 for number in number_list if number % 2 != 0]

        with open("squares.txt", 'w') as squares_file:
            squares_file.write(" ".join(map(str, even_number_squares)))

        with open("cubes.txt", 'w') as cubes_file:
            cubes_file.write(" ".join(map(str, odd_number_cubes)))