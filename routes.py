from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/upload-file')
async def post_upload_file(file_data: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_upload_file(db, file_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/testing')
async def post_testing(raw_data: schemas.PostTesting, db: Session = Depends(get_db)):
    try:
        return await service.post_testing(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

