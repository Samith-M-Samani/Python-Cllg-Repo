import os 
cwd = os.getcwd() 
print("Current working directory:", cwd)

def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
current_path() 
os.chdir('../') 
current_path() 
