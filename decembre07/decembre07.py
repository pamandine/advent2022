import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
filePath = path+"/../inputs/in07.txt"

current_folder = None
mother_directory = None
filesystem = 70000000
update = 30000000
total = 0

class file():
    def __init__(self,name, size,parent_folder):
        self.size = size
        self.folder_in = parent_folder
        self.name = name
        print(f'Create file with name={name}, of size={size} in parent={parent_folder.name}')
        self.path = parent_folder.path+"."+name

class folder():
    def __init__(self, name, parent_folder):
        self.files = []
        self.folders = []
        self.folder_in = parent_folder
        self.name = name
        self.size = 0
        if (parent_folder is not None):
            print(f'Create folder with name={name}, in parent={parent_folder.name}')
            self.path = parent_folder.path+"."+name
        else:
            print(f'Create main folder with name={name}')
            self.path = name

    def addFile(self,file): # Add children files 
        self.files.append(file)
        print(f'Add file with name={file.name}, of size={file.size} in parent={self.name}')
        self.size = self.size + file.size
    def addFolder(self,folder): # Add children directories
        self.folders.append(folder)
        print(f'Add folder with name={folder.name} in parent={self.name}')

def getLine(f):
    line = f.readline()
    line = line.rstrip("\n")
    if (line.rstrip()):
        # not empty 
        pass
    else:
        line = None
    return line

f = open(filePath, "r")
line = getLine(f)
while line is not None:
    e = line.split()
    if (e[0] == "$"):
        # cd or ls
        if (e[1] == "ls"):
            # List everything in the current folder 
            line = getLine(f)
            if (line is not None): # end of file
                g = line.split()
                while (g[0] != "$"):
                    if (g[0] == "dir"):
                        name = g[1]
                        newFolder = folder(name, current_folder)
                        current_folder.addFolder(newFolder)
                    else: # file
                        name = g[1]
                        size = int(g[0])
                        newFile = file(name, size, current_folder)
                        current_folder.addFile(newFile)
                        total = total + size
                    line = getLine(f)
                    if (line is not None):
                        g = line.split()
                    else:
                        g = ["$"] # end the loop 
            
        elif (e[1] == "cd"):
            name = e[2]
            if (name != ".."):
                if (current_folder is None): # Mother directory 
                    newFolder = folder(name, current_folder) 
                    current_folder = newFolder
                    mother_directory = current_folder
                else: # Probably already created, find it and get into it
                    for directory in current_folder.folders:
                        if (directory.name == name):
                            current_folder = directory
                            break
            else:
                # Go back to parent 
                current_folder = current_folder.folder_in
            line = getLine(f)

def goDeep(dir, result):
    print(f'Looking into {dir.name} of size={dir.size}')
    print(f'With parent : {dir.folder_in.name} and Path = {dir.path}')
    
    size = dir.size
    for d in dir.folders:
        print(f'Go deep into {d.name}')
        size = size + goDeep(d, result)
    dir.size = size
    print(f'Folder {dir.name} is size={dir.size}')
    result[dir.path] = dir.size

    return size

result = {}
for d in mother_directory.folders:
    # Each folder have a size. Now add subfolders size to each upfolders size
    result[d.name] = goDeep(d, result)
f.close()
    
print("########## Function 1 ##########")
sum = 0
for k in result:
    if (result[k] <= 100000):
        sum = sum + result[k]

print (f'Sum for folders <= 100000 is {sum}')

print("########## Function 2 ##########")
print(f'Total size is {total}')
free = filesystem - total
print (f'Free space is {free}')
toBeRemoved = abs(free - update)
print (f'To be removed is {toBeRemoved}')

# Parse everthing
# Add free + size of folder
# Check if addition is > update
# If so, save it for later
# Then, take the minimum of all 
select = {}
for key in result.keys():
    if ((result[key] + free) >= update):
        select[key] = result[key]


new = {k: v for k, v in sorted(select.items(), key=lambda item: item[1])}
newList = list(new.keys())
print(f'Delete size : {new[newList[0]]} which is the smaller folder size among the selected ones')

