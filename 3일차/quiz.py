from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

find_matrix = db.movies.find_one({'title':'매트릭스'})
matrix_star = find_matrix['star']
#print (matrix_star)

same_star = list(db.movies.find({'star': matrix_star}))

"""for m in same_star:   
    print (m['title'])"""

db.movies.update_many({'star':matrix_star},{'$set':{'star': 0}})

"""for movie in same_star:   
    print (movie['star'])"""

bigger_than_9_38 = db.movies.find({'star':{'$gt':'9.38'}})
count_bt_9_38 =bigger_than_9_38.count()

print(count_bt_9_38)