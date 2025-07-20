from pathlib import Path
print(__file__) 
# it returns  name of the file

fpath = Path(__file__)

print(type(fpath)) 
# --> fives the type of the path based on os -- windows ?? linux ?? max ??
# <class 'pathlib.WindowsPath'> 

complete_path = fpath.resolve() 
# gives the complete path of the file

print(complete_path)

# writing in a single step
print(Path(__file__).resolve())

print(Path(__file__).resolve().parent)

print(Path(__file__).resolve().parent.parent)