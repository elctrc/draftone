"""
draftone 1.0

A way to write, one line at a time

https://github.com/elctrc
"""

import argparse
import os


def handle_args():
    """Time to parse some arguments"""
    parser = argparse.ArgumentParser()
    #@TODO: Make optional. If no file is included, write to new file.
    parser.add_argument('story_file', help='location of story file to open')
    return parser.parse_args()


def main():
    """Main"""
    args = handle_args()

    # Open file to write an create new one if one does not exist
    with open(args.story_file, 'a+') as story_file:
        story = []

        # Let's start with a fresh screen
        os.system('cls' if os.name == 'nt' else 'clear')

        writing = True

        while writing:
            print('-- draftone v. 1.0 --')
            print('Type a sentence and hit enter/return\n(q)uit and save, (p)revious line, enter/return for newline\n')

            # Take input
            line = input('>> ')
            if line == 'q':
                complete = ''.join(story)
                print('--- New Text ---')
                print('\n(Character Count: {})\n'.format(len(complete)))
                print(complete)
                print('--- Complete Text ---')
                # @TODO: Print complete text of file

                # Write a line break at the end
                story_file.write('\n\n')
                writing = False
            elif line == 'p':
                try:
                    print(story[-1])
                except IndexError:
                    print('No previous entry for this session.')
            else:
                # Clear screen in between entries
                os.system('cls' if os.name == 'nt' else 'clear')

                # Create paragraph break or space
                if line == '':
                    line = '\n'
                else:
                    line = line + ' '

                # Write to file
                story.append(line)
                story_file.write(line)
                story_file.flush()

        quit()


if __name__ == '__main__':
    main()
