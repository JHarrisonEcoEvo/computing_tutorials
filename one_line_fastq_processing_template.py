#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Load fastq and process one line at a time.
# This template was written with GH copilot, so thanks to whoever's code was used by the model!

import gzip
import sys

# Open the file, use gzip if it is gzipped, else open normally.
# Recall that the 0th index is the present script, so we want the 1st index to open the file.
if sys.argv[1].endswith('.gz'):
    # Mode 'rt' means read text
    file = gzip.open(sys.argv[1], 'rt')
else:
    # Mode 'r' means read
    file = open(sys.argv[1], 'r')

# Read the file line by line
# Initialize a counter to keep track of the number of lines
line_count = 0

# Initialize a counter to keep track of the number of reads
read_count = 0

# Build a dictionary to store the read counts for each sequence
read_counts = {}

# Build a dictionary to store the sequence.
seq_dict = {}

# Loop through each line in the file.

for line in file:
    # Increment the line counter
    line_count += 1

    # Remove the newline character from the end of the line
    line = line.strip()

    # If the line is a header line, increment the read counter and store the read ID
    if line_count % 4 == 1:
        read_count += 1
        read_id = line
        read_counts[read_id] = 0

    # If the line is a sequence line, increment the read count for that read ID
    elif line_count % 4 == 2:
        read_counts[read_id] += 1
        seq_dict[read_id] = line

    # If the line is a quality line, do nothing
    else:
        pass

# Close the file
file.close()

# Determine unique sequences.
unique_seq = set(seq_dict.values())

# Print the number of unique sequences.
print(f"Number of unique sequences: {len(unique_seq)}")

# How many times does each unique sequence occur?

# # Print the median read count
# sorted_read_counts = sorted(read_counts.values())
# print(f"Median read count: {sorted_read_counts[len(sorted_read_counts) // 2]}")
#
# # Print the mode read count
# mode_read_count = max(read_counts.values())
# print(f"Mode read count: {mode_read_count}")
#
# # Print the read ID with the mode read count
# for read_id, read_count in read_counts.items():
#     if read_count == mode_read_count:
#         print(f"Mode read ID: {read_id}")
#         break


# End this program.
