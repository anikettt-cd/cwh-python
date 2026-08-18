try:
    file = open("/Users/aniketsaini/Desktop/cwh-python/files_In_out/harry.txt" , "r")
    
    for line in file:
        print(line.strip())
    file.close()
    
except FileNotFoundError:
    print("file not found")    
    
        