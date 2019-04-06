import os

def convert():
    PATH = './content/posts/'
    for file in os.listdir(PATH):
        print(file)
        if file.endswith('.md'):
            with open(PATH + file, 'r') as (fin):
                data = fin.read().splitlines(True)
            header = data[0]
            print(header)
            if header.startswith('\\#+'):
                header = ('\n').join([i.split(' ')[0].lower() + ': ' + (' ').join(i.split(' ')[1:]) for i in header.split('\\#+')[1:]])
                print(header)
                with open(PATH + file, 'w') as (fout):
                    print(PATH + file)
                    print(header)
                    fout.writelines(header)
                    fout.writelines(data[1:])

convert()
