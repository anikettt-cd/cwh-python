word = ["python", "rocks", "ai"]

lengths = [ n for w  in word if (n := len(w)) >= 4 ]

print(lengths)