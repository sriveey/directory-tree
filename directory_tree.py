import os
import argparse

# --output for output to .txt file
# --depth for how many levels of subdirectories to traverse

# ex - print to console: python directory_tree.py /path/to/your/project --depth 3
# ex - output to .txt: python directory_tree.py /path/to/your/project --depth 5 --output tree.txt


def generate_directory_tree(root_dir, max_depth):
    def tree(directory, prefix='', level=0):
        if level >= max_depth:
            return
        contents = os.listdir(directory)
        contents.sort()  # Sort to ensure consistent order
        pointers = ['├── '] * (len(contents) - 1) + ['└── ']
        for pointer, name in zip(pointers, contents):
            path = os.path.join(directory, name)
            if os.path.isdir(path):
                yield prefix + pointer + name + '/'
                extension = '│   ' if pointer == '├── ' else '    '
                yield from tree(path, prefix + extension, level + 1)
            else:
                yield prefix + pointer + name

    return '\n'.join(tree(root_dir))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directory tree")
    parser.add_argument('directory', type=str, help="Root directory")
    parser.add_argument('--depth', type=int, default=5, help="Maximum depth to traverse")
    parser.add_argument('--output', type=str, help="Output file", default=None)
    args = parser.parse_args()

    tree = generate_directory_tree(args.directory, args.depth)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(tree)
    else:
        print(tree)
