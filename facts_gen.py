# this files generates facts for epilog from the license properties in the 'licenses.yml'
import yaml
 
facts = []

with open("./licenses.yml") as file:
    lics = yaml.load(file)

    for l in lics:
        lic = lics[l]
        facts.append("cat(\"{}\",\"{}\")\n".format(l, lic["cat"]))

        if "addreq" in lic.keys():
            for r in lic["addreq"]:
                facts.append("addreq(\"{}\",\"{}\")\n".format(l, r))

        if "comp" in lic.keys():
            for c in lic["comp"]:
                facts.append("comp(\"{}\",\"{}\")\n".format(l, c))
        if "gc" in lic.keys():
            facts.append("gc(\"{}\")\n".format(l))

with open("facts.txt","w") as out:
    out.writelines(facts)
