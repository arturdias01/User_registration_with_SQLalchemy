from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cadastro_usuarios.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
