import argparse

def wc():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lflag", action='store_true')
    parser.add_argument("-w", "--wflag", action='store_true')
    parser.add_argument("-c", "--cflag", action='store_true')
    parser.add_argument('filename')
    args = parser.parse_args()
    config = vars(args)
    file_name = config["filename"]
    lines = 0
    words = 0
    chars = 0
    try:
        with open(file_name) as f:
            for line in f:
                lines += 1
                words += len(line.split())
                chars += len(line)
    except Exception as err:
        print("Error found:",err)
    if config['lflag']:
        print(lines,"", end='')
    if config['wflag']:
        print(words,"", end='')
    if config['cflag']:
        print(chars,"", end='')
    print()
if __name__ == "__main__":
    wc()
