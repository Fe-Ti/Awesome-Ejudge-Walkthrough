from sys import stdin

s = 0

# For easier debugging
def print_state(line, beg, end):
    print(f"begin:{beg}\nend:{end}")
    print(line)
    if beg == end:
        print(' '*beg, '*', sep='')
    else:
        print(' '*beg, '^',' '*(end - beg - 1), '^', sep='')

# Go through the whole stdin
for line in stdin:
    # Stripping useless spaces and such stuff
    line = line.strip()
    # Resetting pointers
    beg = 0
    end = 0
    # ~ print_state(line, beg, end)
    # Checking if the line is empty
    if line:
        while beg < len(line):
            # Astrologers proclaim week of "if" statement.
            # All dwellings increase population.
            if end < len(line):
                while line[end].isdigit():
                    end += 1
                    # ~ print_state(line, beg, end)
                    if end == len(line):
                        break

            if beg < len(line) and end <= len(line):
                # ~ print("- - - -")
                # ~ print_state(line, beg, end)
                # ~ print(line[beg:end])
                if line[beg:end]:
                    s += int(line[beg:end])
                # ~ print("- - - -")

            if end < len(line):
                while not line[end].isdigit():
                    end += 1
                    # ~ print_state(line, beg, end)
                    if end == len(line):
                        break
            beg = end
            if line[beg - 1] == '-' and end < len(line):
                beg -= 1

print(s)
