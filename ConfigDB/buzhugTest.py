#from buzhug import Base
from buzhug.buzhug import Base
import shutil
import os
dbPath = os.path.dirname(os.path.abspath(__file__)) + '/../database/cities'
if os.path.exists(dbPath):
	shutil.rmtree(dbPath)
db = Base(dbPath)
db.create(('name',str),('zip',int))
