from fastapi import FastAPI

from routes.prompts import router as prompt_router
from routes.health import router as health_router

app = FastAPI(
    title="PromptLab",
    version="1.0.0"
)

app.include_router(prompt_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"PromptLab",

        "status":"running"

    }
