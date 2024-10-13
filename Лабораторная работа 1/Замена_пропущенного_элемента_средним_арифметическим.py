numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
new_numbers = numbers[:4] + numbers[5:]

sum_of_numbers = sum(new_numbers)
count_of_numbers = len(new_numbers) + 1

average = round(sum_of_numbers / count_of_numbers, 2)

numbers[4] = average

print("Измененный список:", numbers)

