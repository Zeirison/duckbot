import random
def read_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                lines.append(line[:-1])
    except IOError:
        print 'Failed to open {}'.format(filename)
    return lines

stfu_phrases = read_lines('stfu_phrases.txt')

for i in range(10):
    print stfu_phrases[random.randrange(len(stfu_phrases))]
