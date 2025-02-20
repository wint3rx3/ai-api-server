from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    # "main:app"에서 main은 파일 이름(main.py)이고, app은 FastAPI 인스턴스입니다.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)