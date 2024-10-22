"""
This module contains the FastAPI application and its endpoints.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict:
    """Root endpoint that returns a greeting message.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"message": "Hello World"}
