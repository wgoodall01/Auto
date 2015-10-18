# -----AUTO AUTOMATION SCRIPT v2.0-----          #

import sys
import xml.etree.ElementTree as ElementTree
import webbrowser as webbrowser
import os
import platform


if os.name == "nt": os.system("cls")  # run cls on windows platforms
if os.name == "posix": os.system("clear")  # run clear on unix platforms


queries = []

if sys.stdin.isatty():
    if len(sys.argv) != 1:  # If there are cmd line args run off those
        queries.append(sys.argv[1:])
    else:  # If not, run interactively
        queries.append(raw_input("Query:").split())
else:
    for i, line in enumerate(sys.stdin):
        queries.append(line.split())

if len(queries) == 0:  # if there are no queries
    exit("Exiting: No queries.")

e = ElementTree.parse('data.xml').getroot()

shortcutelement = None

for i in e.getchildren():
    if i.tag == "shortcuts":
        shortcutelement = i
        break;

if shortcutelement == None:
    exit("Error: Could not locate shortcut tag")

def runaction(element, query, roottag):
    if (element.get("name") == query[0]) or element.tag == roottag or query[0] == "*":  # if a desirable node
        if (not element.getchildren()) or (len(query) == 1 and element.tag != roottag):  # if an endpoint node
            # run all params
            if element.get("url"):
                print("Opening page:" + element.get("url"))
                webbrowser.open(element.get("url"), new=2, autoraise=True)
        else:  # If a group node
            for j in element.getchildren():
                if element.tag == "shortcuts":
                    runaction(j, query, roottag)
                else:  # By this point it is established that len(query) is at least 2
                    runaction(j, query[1:], roottag)



for query in queries:
    runaction(shortcutelement, query, "shortcuts")

exit()