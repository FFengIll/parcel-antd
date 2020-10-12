import uvicorn
if __name__ == "__main__":

    uvicorn.run("backend.server:app",
                host="127.0.0.1", port=5050,
                reload=True,
                workers=1,
                log_level="info")
