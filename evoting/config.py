class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3307/evoting_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret123"