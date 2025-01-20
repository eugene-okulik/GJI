PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

split_lines = PRICE_LIST.splitlines()

split_parts = [x.split() for x in split_lines]

price_dict = {x[0]: int(x[1][:-1]) for x in split_parts}


print(price_dict)
