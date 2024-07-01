import argparse

def cat():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--size",help="size of lines", type=int, default=-1)
    parser.add_argument('filename', action="store")
    args = parser.parse_args()
    config = vars(args)
    file_name = config["filename"]
    size = config["size"]
    lines = []

    f = open(file_name, 'r')
    lines = f.readlines()
    
    if size == -1:
        size = len(lines)
    
    for i in range(size) :
        print(lines[i],end='')

if __name__ == "__main__":
    cat()
