import shelve
sh = shelve.open("shelve")
print(list(sh.keys()))
print(list(sh.values()))
