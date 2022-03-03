import shelve
from config import shalveName
db = shelve.open(shalveName)
for i in range(10):
    db[str(i)] = i**2
for x in db.keys():
    print(db[x])
