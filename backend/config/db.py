from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:@localhost:3306/proyecto_dbp')
meta = MetaData(bind=engine)
meta.reflect()
conn = engine.connect()