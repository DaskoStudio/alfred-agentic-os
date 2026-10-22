from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/tools")
def list_tools() -> None:
    # logique privée — non incluse
    raise HTTPException(status_code=501, detail="not implemented")


@router.post("/tools/{name}/call")
def call_tool(name: str) -> None:
    # logique privée — non incluse
    raise HTTPException(status_code=501, detail="not implemented")


@router.post("/agents/run")
def run_agent() -> None:
    # logique privée — non incluse
    raise HTTPException(status_code=501, detail="not implemented")
