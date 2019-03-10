"""
draftone

A way to write, one line at a time
"""

import argparse
import os


def handle_args():
    """Time to parse some arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('story_file', help='location of story file to open')
    return parser.parse_args()


def main():
    """Main"""
    args = handle_args()
    story_file = open(args.story_file, 'a+')
    story = []

    # Let's start with a fresh screen
    os.system('cls' if os.name == 'nt' else 'clear')

    writing = True

    while writing:
        print('-- draftone v. 1.0 --')
        print('Type a sentence and hit enter\n(q)uit and save, (p)revious line, (n)ew paragraph')

        # Take input
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
            # Clear screen in between entries
            os.system('cls' if os.name == 'nt' else 'clear')

            if line == 'n':
                line = '\n'
            else:
                line = line + ' '
            story.append(line)
            story_file.write(line)

    quit()


if __name__ == '__main__':
    main()
