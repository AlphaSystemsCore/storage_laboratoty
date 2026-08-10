from fastapi import FastAPI


from app.routers.upload_router import uploads_router

app = FastAPI()
app.include_router(uploads_router)