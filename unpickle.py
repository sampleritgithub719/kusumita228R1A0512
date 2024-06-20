import pickle
fp = open("picklefile.txt","vb")
st = ["kusu","pranu","mano"]
unpickle = pickle.load(fp)
print(unpickle)