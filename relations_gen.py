import yaml

rels = []

with open("./licenses.yml") as file:
    lics = yaml.load(file)

    for l in lics:
        lic = lics[l]
        rels.append("cat(\"{}\",\"{}\")\n".format(l, lic["cat"]))

        if "addreq" in lic.keys():
            for r in lic["addreq"]:
                rels.append("addreq(\"{}\",\"{}\")\n".format(l, r))

        if "comp" in lic.keys():
            for c in lic["comp"]:
                rels.append("comp(\"{}\",\"{}\")\n".format(l, c))
        if "gc" in lic.keys():
            rels.append("gc(\"{}\")\n".format(l))

with open("relations.txt","w") as out:
    out.writelines(rels)