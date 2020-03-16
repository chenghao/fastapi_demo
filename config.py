# coding: utf-8
__author__ = "gaunt"


# 接口文档请求地址
fastapi_docs_url = "/docs"
fastapi_redoc_url = None

# uvicorn 启动参数
uvicorn_host = "127.0.0.1"
uvicorn_port = 8000
uvicorn_log_level = "info"
uvicorn_reload = True
uvicorn_workers = 1
uvicorn_http = "auto"  # Options: 'auto', 'h11', 'httptools'. Default: 'auto'
uvicorn_loop = "auto"  # Options: 'auto', 'asyncio', 'uvloop', 'iocp'. Default: 'auto'


# 日志配置
logging_config_log_formatters = {
    "log": {
        "()": "logging.Formatter",
        "fmt": '%(asctime)s %(pathname)s %(funcName)s %(lineno)s %(levelname)s %(message)s',
    },
}
logging_config_log_handlers = {
    "log": {
        "formatter": "log",
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": "/home/logs/fastapi.log",
        "when": "D",
    },
}
