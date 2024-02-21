import os


def create_file(name: str):
    open(name, 'w')


def write_file(name: str, thing_to_write: str):
    open(name, 'w').write(thing_to_write)


def read_file(name: str):
    return open(name, 'r').read()


def delete_file(name: str):
    os.remove(name)


def create_folder(name: str):
    os.mkdir(name)


def delete_folder(name: str):
    try:
        os.rmdir(name)
    except:
        print(f'Error: {name} not empty')


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
