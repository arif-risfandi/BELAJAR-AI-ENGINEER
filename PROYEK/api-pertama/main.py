from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def halaman_awal():
    return {
        "pesan" : "API berjalan"
    }