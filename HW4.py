part 1


vegetables=['carrot','lettuce','onion','radish']

def my_function(mylist):
    print(vegetables[0],',',vegetables[1],',',vegetables[2], 'and', vegetables[3]+'.')
    



part2 



gird = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]




my_new_image = ''
for x in range(len(grid[0])):
	for y in range(len(grid)):
		my_new_image += grid[y][x]
	print(my_new_image)
	my_new_image = ''

