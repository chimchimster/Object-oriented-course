lst_in = input().split()
integers = sum(list(map(int, filter(lambda x: x.strip('-').isdigit(), lst_in))))
print(integers)
