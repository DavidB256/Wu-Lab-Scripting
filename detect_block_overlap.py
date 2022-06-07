intervals = []
with open("block_appearance_intervals.txt", "r") as f:
    line = f.readline()
    overlap_counter = 0
    while line:
        words = line.split()
        start = int(words[0])
        end = int(words[1])
        seq_id = words[2]

        for interval in intervals:
            if (interval[0] <= start <= interval[1]) or (interval[0] <= end <= interval[1]):
                overlap_counter += 1
                print(line)
                print(interval)
                print()

        intervals.append([start, end])
        line = f.readline()

print("Total number of overlaps: %d" % overlap_counter)
