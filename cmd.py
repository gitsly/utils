# Usage: import by: 'from utils import cmd'
# then: cmd.execute('ls')
# will do a list files in current directory and then 
# return the result in a list of strings (one entry in the list is one row)
import subprocess

# Nice utility function to get another process output per line into a list
def execute(cmd):
    pOut = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(pOut.stdout.readline, b''):
        line = line.rstrip().decode("utf-8") # what format is the output from the commandline?
        lines.append(line)
    return lines


