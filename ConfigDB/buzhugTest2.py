#from buzhug import Base
from buzhug.buzhug import Base
import shutil
import os
import datetime

dbPath = os.path.dirname(os.path.abspath(__file__)) + '/../database/people'
if os.path.exists(dbPath):
	shutil.rmtree(dbPath)
db = Base(dbPath)
# The following is an example in buzhug.py but it doesn't work. You can't create a DB with named params like this
#db.create(name=str,age=int,birthday=datetime.date)
db.create(('name',str),('age',int),('birthday', datetime.date))
db.open()

db.insert(name='homer',age=23,birthday=datetime.date(1994,10,7))
# select names for age > 20
# list comprehension
res = [ r.name for r in db if int(r.age) > 20 ]
print("Select using list comprehension")
print(res)

# select method (faster)
res = db.select(['name'],'age > v',v=20)
print("Select using Select method")
print(res)

# select for update, then update
recs = db.select_for_update(['name'],'age > v',v=20)
for record in recs:
    db.update(record,name=record.name.upper())

# direct access by __id__
#record = db[_id]

# delete a list of records
#db.delete(selected_records)

# delete one record identified by id
#del db[_id]

