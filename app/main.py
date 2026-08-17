from fastapi import FastAPI


from app.routers.media_routers import media_router

app = FastAPI()
app.include_router(media_router)

@app.get("/")
def status():
    return {
        "server":"on"
    }