def read_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                lines.append(line[:-1])
    except IOError:
        print 'Failed to open {}'.format(filename)
    return lines
