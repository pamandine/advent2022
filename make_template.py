import sys,os
from pathlib import Path

if (len(sys.argv) < 2):
    print("Not enough argument.")
    sys.exit(1)

number = sys.argv[1]
if (len(number)<2):
    number = "0"+number

directory = "decembre"+number
print(f'Create directory {directory}')
os.mkdir(directory)

example = directory+"/decembre"+number+"Example.txt"
print(f'Create file {example}')
Path(example).touch()

input = directory+"/decembre"+number+".txt"
print(f'Create file {input}')
Path(input).touch()

txt = "debug=True\n"
txt += "if debug:\n\tf = open(\""+example+"\", \"r\")\n"
txt += "else:\n\t f = open(\""+input+"\", \"r\")\n" 
txt += "\n"
txt += "for line in f.readlines():\n\tprint(line)\n\nf.close()"

python = directory+"/decembre"+number+".py"
print(f'Create file {python}')
Path(python).touch()

f = open(python, "w")
f.write(txt)
f.close()
