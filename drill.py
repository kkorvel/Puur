file = open("drill.ngc", 'r')
path = ""
for line in file:
    if line == "":
        continue
    elif "G81" in line:
        path = "" #puhastab enne koordinaate
        split_line = line.split(" ") # vasted line
        R_coordinate = split_line[1]
        F_coordinate = split_line[2]
        X_coordinate_init = split_line[3]
        Y_coordinate_init = split_line[4]
        #path.append[(x_coordinate_init, y_coordinate_init)]

    elif len(path) != 0: #something in there
        split_line = line.split(" ")
        X_coordinate = split_line[0]
        Y_coordinate = split_line[1]
