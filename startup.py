# coding: utf-8
__author__ = "gaunt"

from fastapi import FastAPI
# 子节点
from demo import demo
from jwtdemo import jwtdemo


app = FastAPI()
# 加载子节点
app.mount("/demo", demo)
app.mount("/jwtdemo", jwtdemo)


# 服务器运行
# dev： uvicorn startup:app --reload  # 热重启

if __name__ == "__main__":
    import uvicorn
    import config
    from uvicorn.config import LOGGING_CONFIG

    #LOGGING_CONFIG["formatters"].update(config.logging_config_log_formatters)
    #LOGGING_CONFIG["handlers"].update(config.logging_config_log_handlers)
    #LOGGING_CONFIG["loggers"][""]["handlers"] = ['log']

    print("启动==========》")
    uvicorn.run("startup:app", host=config.uvicorn_host, port=config.uvicorn_port, log_level=config.uvicorn_log_level,
                reload=config.uvicorn_reload, workers=config.uvicorn_workers, loop=config.uvicorn_loop,
                http=config.uvicorn_http, access_log=True, log_config=LOGGING_CONFIG)
