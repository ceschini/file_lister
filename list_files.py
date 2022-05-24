from fs import open_fs

home_fs = open_fs('.')
file_list = home_fs.listdir('/')

f = open('bag_list.cfg', 'a')
for file in file_list:
    f.write(f'{file}\n')
f.close()

f = open('bag_list.cfg', 'r')
print(f.read())
