# TODO Найдите количество книг, которое можно разместить на дискете
size_floppy_in_Mb = 1.44
size_floppy = 1.44 * 1024 * 1024

numbers_of_page = 100
numbers_of_string = 50
numbers_of_symbol = 25
weight_of_symbol = 4

size_of_book = weight_of_symbol * numbers_of_symbol * numbers_of_string * numbers_of_page

count_of_book = round(size_floppy / size_of_book)
print("Количество книг, помещающихся на дискету:", count_of_book)
