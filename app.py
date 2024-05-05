from fastapi import FastAPI

from controllers.ordersController import router 
app = FastAPI()

app.include_router(router)  # Mount the order router

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app --reload")