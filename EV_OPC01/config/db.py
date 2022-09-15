from sqlalchemy import create_engine, MetaData

# Connecto to tha database in mariadb
engine = create_engine('mysql+pymysql://root:123@localhost:3306/api', echo=True)

meta = MetaData()

conn = engine.connect()