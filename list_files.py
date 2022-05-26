import glob

file_list = []
for name in glob.glob('./*.py'):
    split1 = name.split('/')
    split2 = split1[1].split('.')
    file_list.append(split2[0])

f = open('bag_list.cfg', 'w')
for file in file_list:
    f.write(f'{file}\n')
f.close()

f = open('bag_list.cfg', 'r')
print(f.read())
