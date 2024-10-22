"""
This module contains the FastAPI application and its endpoints.
"""
from fastapi import FastAPI
from mycareer.routers.v1_goals import router as v1_goals_router

tags_metadata = [
     {
        "name": "server tools",
        "description": "The endpoints to test the server.",
    },
    {
        "name": "goals",
        "description": "The endpoints to manages goals.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(v1_goals_router)

@app.get("/echo", tags=["server tools"])
async def echo() -> dict:
    """
    ## Description

    Echo endpoint that returns a greeting message.

    ## Returns

        dict: A dictionary containing a greeting message.
    """
    return {"message": "echo"}
