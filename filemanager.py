import os

def create_file(name: str):
    open(name, 'w')

def write_file(name: str, thing_to_write: str):
    try:
        open(name, 'r').read()
        cool = True
    except:
        cool = False
    if cool == True:
        open(name, 'w').write(thing_to_write)
    else:
        print(f'ERROR: {name} not found!')
        exit()

def read_file(name: str):
    try:
        return open(name, 'r').read()
    except:
        print(f'ERROR: {name} not found!')
        exit()

def delete_file(name: str):
    os.remove(name)

def create_folder(name: str):
    os.mkdir(name)


#does something

def delete_folder(name: str):
    try:
        os.rmdir(name)
    except:
        print(f'Error: {name} not empty')
        exit()

def rename_file(name: str, new_name: str):
    os.rename(name, new_name)

def clear_folder(name: str):
    data = os.listdir(name)
    for file in data:
        os.remove(f'{name}/{file}')

def delete_folderAndContents(name:str):
    data = os.listdir(name)
    for file in data:
        os.remove(f'{name}/{file}')
    os.rmdir(name)

def see_contents(name: str):
    return os.listdir(name)

def append_file(name: str, thing: str):
    data = open(name, 'a')
    data.write(thing)
