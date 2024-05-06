from peewee import SqliteDatabase,Model,CharField

data=[""]

db=SqliteDatabase("database.db")
class BaseModel(Model):
    class Meta:
        database=db
class User(BaseModel):
    UserName=CharField(null=True)
    UserSpec=CharField(null=True)
db.connect()
db.create_tables([User])
User.truncate_table()
db.close()
