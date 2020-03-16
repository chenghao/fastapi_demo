# coding: utf-8
__author__ = "gaunt"

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

pwd = pwd_context.hash("123456")
print(pwd)

pwd2 = pwd_context.verify("123456", "$2b$12$mOMiPNx.nlcQKE5ESpZV0O01f/jLWuxo7HxBDGKvdP7Qg/yyXlhoO")
print(pwd2)
