from pymongo import MongoClient
connection = MongoClient()
connection = MongoClient('localhost', 27017)
db = connection['test-database']
posts = db['test-collection']
import datetime
post = {"author": "Mike2",
       "text": "My first blog post!",
        "tags": ["mon2godb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

post_id = posts.insert(post)
print posts.find_one()
print posts.find_one({"author": "Mike2"})
print "#######"
for post in posts.find():
    print post

from pymongo import MongoClient
import gridfs

db = MongoClient().gridfs_example
fs = gridfs.GridFS(db)
filename = "bunny3.png"
datafile = open(filename,"rb")
thedata = datafile.read()
datafile.close()
#b = fs.put(thedata, filename="foo3", bar="baz")
for file in db.fs.files.find() :
    if file['filename'] == "foo2":
        fs.delete(file['_id'])
    print "toto"
    print file
    a =  fs.get(file['_id'])
    f = open('titi.png', 'wb')
    f.write(a.read())
    f.close()