try:
    f = open("/Users/aniketsaini/Desktop/cwh-python/files_In_out/harry.txt" , "r")
    
    for line in f:
        print(line)
        
    f.close()
    
except FileNotFoundError:
    print("file not found")    