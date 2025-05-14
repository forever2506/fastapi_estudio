from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://talento:cartagena@nodossolutions.com:1435/PRUEBAjorge") #conexion a la db

conn = engine.connect()

meta_data = MetaData()
