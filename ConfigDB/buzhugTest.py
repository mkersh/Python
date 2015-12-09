#from buzhug import Base
from buzhug.buzhug import Base
db = Base('cities')
db.create(('name',str),('zip',int))
#cities = Base('cities').create(('name',str),('zip',int))