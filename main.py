from fastapi import Depends, FastAPI
from schema import Mymodel
import Model
from database import engine,sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Model.base.metadata.create_all(engine)


def getDb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.put('/post')
def create(request:Mymodel,db:Session=Depends(getDb)):
    newBlog = Model.User(name=request.name, mobile=request.mobile)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog



@app.get("/")
def all(db:Session=Depends(getDb)):
    dataSet = db.query(Model.User).all()
    return dataSet

