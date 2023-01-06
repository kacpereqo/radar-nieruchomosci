from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application():
    _app = FastAPI()

    # include_routes(_app)

    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
