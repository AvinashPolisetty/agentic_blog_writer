from __future__ import annotations

import json
import logging
import uuid
from pathlib import Path
from typing import Any, Generator

from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
import uvicorn
# ---------------------------------------------------------
# Import the existing compiled LangGraph workflow.
#
# backend.py remains completely unchanged.
# backend.app is the compiled LangGraph workflow.
# ---------------------------------------------------------