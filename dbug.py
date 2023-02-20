import argparse
import sys

# This creates a new ArgumentParser object and adds a positional argument called "text" that represents the highlighted text from the terminal. 
# The parse_args() method then reads the command-line arguments and returns a namespace object that contains the argument values.
parser = argparse.ArgumentParser()
parser.add_argument("text", help="the highlighted text from the terminal")
args = parser.parse_args()

# This reads input from the terminal and assigns it to the text variable.
text = sys.stdin.read()

# This simply prints the highlighted text to the console.
print("Highlighted text: " + text)

