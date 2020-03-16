# coding: utf-8
__author__ = "gaunt"

from fastapi import FastAPI
from fastapi.logger import logger
from config import fastapi_docs_url, fastapi_redoc_url

demo = FastAPI(openapi_prefix="/demo", docs_url=fastapi_docs_url, redoc_url=fastapi_redoc_url, title="FastAPI Demo示例")


@demo.get("/index")
def index(p: str, i: int, j: int = None):
    logger.info("aaaaaaaaaaaaaaaaaaaaaa")
    return {"p": p, "i": i, "j": j}


@demo.get("/index2/{p}")
def index2(p: str):
    logger.info("bbbbbbbbbbbbbbbbbbbbbb")
    return {"p": p}
