file_ptr = open(filename) -- Opens a file for reading.

file_ptr.read() -- reads all the lines from a file.

file_ptr.close() -- Close an open file.

file_ptr = open(filename, 'w') -- Opens a file for writing to.  Truncates the file first.
file_ptr = open(filename, 'r') -- Opens a file for reading.  Same as open(filename)
file_ptr = open(filename, 'a') -- Opens a file for appending.  Same as 'w' but no truncation.
file_ptr = open(filename, 'r+') -- Opens a file for reading and writing.  Pointer is set to the start of the file.
file_ptr = open(filename, 'w+') -- Opens a file for writing and reading.  File is truncated first.

file_ptr.truncate() -- Truncates a file.

from os.path import exists
exists(to_file) -- Returns true if to_file name exists.
