import argparse

def tail():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--size",help="size of lines", type=int, default=10)
    parser.add_argument('filename', action="store")
    args = parser.parse_args()
    config = vars(args)
    file_name = config["filename"]
    size = config["size"]
    lines = []

    f = open(file_name, 'r')
    lines = f.readlines()
    
    if len(lines) < 10:
        start = 0
    else:
        start = len(lines) - size
    for i in range(size) :
        print(lines[start + i],end='')

if __name__ == "__main__":
    tail()
