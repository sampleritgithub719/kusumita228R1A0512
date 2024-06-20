import marshal
fp = open("fact.txt","rb")
d = marshal.load(fp)
exec(d)