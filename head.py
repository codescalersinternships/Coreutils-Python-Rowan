import argparse

def head():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--size",help="size of lines", type=int, default=10)
    parser.add_argument('filename', action="store")
    args = parser.parse_args()
    config = vars(args)
    file_name = config["filename"]
    size = config["size"]

    f = open(file_name, 'r')
    for i in range(size) :
        print(f.readline(),end='')

if __name__ == "__main__":
    head()
