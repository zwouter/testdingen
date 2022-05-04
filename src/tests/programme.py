
inp = open("input").readlines()
out = open("output", "w")

people = {"bl": "+bart.leenheer", "ws": "+Wouter Suidgeest", "wj": "+Wesley Joosten", "bd": "+Bram van Dartel",
          "mj": "+Michael Janssen", "rm": "+Rosan Maas"}
# "od": "+Oliver Davies", "mm": "+Maarten Meijer", "jb": "+Jochem Bleeker", "qh": "+Quirijn Hoenink",
# "wv": "+Wout Velthuis", "nr": "+Niels Rotmensen", "mf": "+Mariska Frelier"}

for line in inp:
    line = line.replace("  ", "").replace("\t", "")
    if line[:3] == "\\ap":
        parts = line.split("{")
        if parts[1][1:3] in people:
            out.write("vand {} {}\n".format(people[parts[1][1:3]], parts[2][:-2]))


