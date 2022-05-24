import glob

file_list = []
for name in glob.glob('./*.py'):
    splitted_name = name.split('/')
    file_list.append(splitted_name[1])

f = open('bag_list.cfg', 'w')
for file in file_list:
    f.write(f'{file}\n')
f.close()

f = open('bag_list.cfg', 'r')
print(f.read())
