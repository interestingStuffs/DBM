from fastapi import FastAPI
from app.api.api_v1.endpoints import event, user
from starlette.middleware.cors import CORSMiddleware



app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust to the URL of your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event.router, prefix="/api/v1/events", tags=["events"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
