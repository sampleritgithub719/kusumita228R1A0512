import marshal
fp = open("marshal.txt","rb")
d = marshal.load(fp)
exec(d)