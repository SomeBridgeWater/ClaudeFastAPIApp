import asyncio
import time
import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter(prefix="/v1")


class CommitInfo(BaseModel):
    commit1: str
    commit2: str


class RootResponse(BaseModel):
    message: str
    commit: CommitInfo
    data: list[str]


class ItemResponse(BaseModel):
    item_id: int

# ミドルウェアで一括設定する
#@app.middleware("http")
#async def add_process_time_header(request: Request, call_next):
#    await asyncio.sleep(3) # 全てのリクエストに3秒追加
#    response = await call_next(request)
#    return response

@router.get("/", response_model=RootResponse)
async def read_root() -> RootResponse:
    # 3秒間待機(非同期)
    await asyncio.sleep(3)

    return RootResponse(
        message="Hello World",
        commit=CommitInfo(commit1="commit1test", commit2="commit2test"),
        data=["data1", "data2", "data3"],
    )


@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int) -> ItemResponse:
    return ItemResponse(item_id=item_id)

app.include_router(router)

def main():
    uvicorn.run("my_package.main:app", host="0.0.0.0", port=8000, reload=True)

# ここから下は「uv run main.py(my-command)」、「python main.py」と打った時だけ動く
# uvicornを直接実行するときは、「uv run uvicorn my_package.main:app --reload」
if __name__ == "__main__":
    main()

    # memo
    # http://localhost:8000/docs