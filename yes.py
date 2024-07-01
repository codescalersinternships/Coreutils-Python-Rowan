import sys

def yes():
    if len(sys.argv) == 1:
        while True:
            print("y")
    else:
        while True:
            print(*sys.argv[1:], sep=' ')
    
if __name__ == "__main__":
    yes()
