from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def post_upload_file(db: Session, file_data: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await file_data.read()

    name = file_data.filename
    file_path = file_path + "/" + name

    import mimetypes

    file_data.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        file_data.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(file_data.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    file_return_url = file_url
    res = {
        "file_returns": file_return_url,
    }
    return res


async def post_testing(db: Session, raw_data: schemas.PostTesting):
    number_pages: int = raw_data.number_pages
    street_name: str = raw_data.street_name
    offset_value: int = raw_data.offset_value

    query = db.query(models.Addresses)
    query = query.filter(and_(models.Addresses.street == street_name))

    query = query.order_by(models.Addresses.street.asc())

    query = query.limit(number_pages)

    streets = query.all()
    streets = [new_data.to_dict() for new_data in streets] if streets else streets
    res = {
        "street_list": streets,
    }
    return res
