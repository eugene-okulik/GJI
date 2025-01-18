PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

split_lines = PRICE_LIST.splitlines()
price_dict = {x.split()[0]: int(x.split()[1][:-1])
              for x in split_lines}


print(price_dict)
