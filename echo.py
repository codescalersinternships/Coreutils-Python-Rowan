import sys

def echo():
    print(*sys.argv[1:], sep=' ')
if __name__ == "__main__":
    echo()
