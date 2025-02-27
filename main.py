import uvicorn
from fastapi import FastAPI
from routes import todo_router, index_router
from database.config import Base, engine # Yangi

Base.metadata.create_all(bind=engine) # Databse faylini yaratish. 


app = FastAPI()
app.include_router(todo_router)
app.include_router(index_router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)