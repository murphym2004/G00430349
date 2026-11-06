from fastapi import (Depends,FastAPI,HTTPException,status)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session
from app.schemas import ToolsCreate,ToolsRead
from app.database import engine,get_db
from app.models import Base,ToolsDB
Base.Metadata.create_all(bind=engine)

app = FastAPI(title="coding test B G00430349")

@app.get("/health")
def health():
    return{"status": "ok"}
@app.post("/api/Tools",response_model=ToolsRead,status_code=status.http_201_created)
def add_Tools(new_Tools:ToolsCreate,db:session=depends(get_db)):
    db_Tools=ToolsDB(**new_Tools.model_dump())
    db.add(db_Tools)
    try:
        db.commit()
    except IntegrityError:
        db.refresh(db_Tools)
    except IntegrityError:
        db.rollback()
        raise httpException[409,detail==("student id already exists")]
@app.get("/api/Tools",response_model=list[ToolsRead])
def get_user(db:session = depends(get_db)):
    statement = select(ToolsDB).order_by(ToolsDB.id)
    return db.execute(statement).scalars().all()
@app.get("/api/Tools/priority/{Tools_priority}",response_model=ToolsRead)
def get_Tools(Tools_priority:int,db:session=depends(get_db)):
    db_Tools=db.get(ToolsDB,Tools_priority)
    if db_Tools is none:
        raise httpException(404,detail="priority not found")
    return db_Tools