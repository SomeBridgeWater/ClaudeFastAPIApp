import time
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RootResponse(BaseModel):
    message: str


class ItemResponse(BaseModel):
    item_id: int

# --- ここから追加 ---
def get_external_data():
    """外部APIからデータを取得する（想定）の重い処理"""
    print("Connecting to external API...")
    time.sleep(3)  # 3秒間、通信を待っているフリをする
    return {"status": "success", "data": "Real Data from Server"}

@app.get("/", response_model=RootResponse)
async def read_root() -> RootResponse:
    #data = get_external_data()
    return RootResponse(message="Hello World")


@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int) -> ItemResponse:
    return ItemResponse(item_id=item_id)

def main():
    uvicorn.run("my_package.main:app", host="0.0.0.0", port=8000, reload=True)

# ここから下は「uv run main.py(my-command)」、「python main.py」と打った時だけ動く
# uvicornを直接実行するときは、「uv run uvicorn my_package.main:app --reload」
if __name__ == "__main__":
    main()

    # memo
    # http://localhost:8000/docs