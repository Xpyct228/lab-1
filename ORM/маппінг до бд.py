from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()
engine = create_engine('mssql+pyodbc://PC0007/Pharmacy?driver=SQL+Server+Native+Client+11.0')

Base.prepare(engine, reflect=True)

User = Base.classes.User
Order = Base.classes.Order
Med = Base.classes.Med


session = Session(engine)

session.add(User(username="andrii",
                 firstName="ewewew",
                 lastName="ewewewewe",
                 email="yurkO@lpnu",
                 password="14881488",
                 phone="15621562",
                 userRole=3))
session.commit()
##with engine.connect() as connection:
##    result = connection.execute('''UPDATE [User]
##                                    SET userRole = 2
##                                    WHERE username=\'andriiii\'''')
####    for row in result:
####        print("username:", row['username'])
