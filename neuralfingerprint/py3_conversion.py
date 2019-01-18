f = open("util.py", "r")
f_out = open("util3.py", "w")

for line in f:
    if "print " in line:
        if "neuralfingerprint" in line:
            f_out.write(line)
            continue
        idx_print = line.find("print ")
        line = line.replace(line[idx_print:idx_print+len("print ")], "print(")
        line = line[:-1] + ")\n"

        f_out.write(line)
    else:
        f_out.write(line)

f.close()
f_out.close()