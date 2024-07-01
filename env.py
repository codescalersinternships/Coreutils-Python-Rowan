import os

def env():
    for data in os.environ:
        print(data, end='')
        print('=', end='')
        print(os.environ[data])
if __name__ == "__main__":
    env()
