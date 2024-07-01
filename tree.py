import os, argparse


def tree():
    # print(os.listdir())
    parser = argparse.ArgumentParser()
    parser.add_argument("-L", "--depth",help="size of lines", type=int, default=1)
    parser.add_argument('path', action="store")
    args = parser.parse_args()
    config = vars(args)
    path = config["path"]
    depth = config["depth"]
    print(path)

    initial_depth = 0
    for root,dirs, files in os.walk(path):
        initial_depth += 1
        print('{}{}\n'.format(' '*initial_depth, os.path.basename(root)))
        for file in files:
            print('{}{}\n'.format(' ' *2*(initial_depth + 1), file))
        if initial_depth == depth:
            break

if __name__ == "__main__":
    tree()
