import os

SRC_DIR = 'PATH TO THE ZONDICONS DIRECTORY'
OUTPUT = {}
def main():
    for file in os.listdir(SRC_DIR):
        if file.endswith('.svg'):
            name = file.replace('.svg', '')
            contents = file_get_contents(os.path.join(SRC_DIR, file))
            contents = contents.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">', '')
            contents = contents.replace('</svg>', '')
            OUTPUT[name] = { 'contents' : contents }

    print OUTPUT


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

if __name__ == "__main__":
    main()
