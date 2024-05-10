import os

path = '.'

def walk(path:str):
    objs = os.listdir(path)
    for i in objs:
        obj = f'{path}/{i}'
        if os.path.isdir(obj):
            walk(obj)
        else:
            print(obj)


walk(path)