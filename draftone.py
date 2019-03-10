"""
draftone

A way to write, one line at a time
"""

import argparse


def handle_args():
    """Time to parse some arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('story_file', help='location of story file to open')
    return parser.parse_args()


def load_file(file):
    """Open file for writing and create a new file if it does not exist"""
    return open(file, 'a+')


def main():
    """Main"""
    args = handle_args()
    story_file = load_file(args.story_file)
    story = []

    writing = True
    while writing:

        print('(q)uit and save, (p)revious line, (n)ew paragraph')
        line = input()
        if line == 'q':
            complete = ''.join(story)
            print("--- New Text ---")
            print("\n(Character Count: {})\n".format(len(complete)))
            print(complete)
            print("--- Complete Text ---")
            # @TODO: Print complete text of file

            # Write a line break at the end
            story_file.write('\n\n')
            # Close file
            story_file.close()
            writing = False
        elif line == 'p':
            print(story[-1])
        else:
            if line == 'n':
                line = '\n'
            story.append(line + ' ')
            story_file.write(line + ' ')

    quit()


if __name__ == '__main__':
    main()
