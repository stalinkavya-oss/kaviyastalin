from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.session import Base, engine
from app.api import expenses, budgets, ai, recommendations


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Smart Budget and Recommendation Assistant"
)


# Enable CORS so the React frontend can communicate
# with the FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routes
app.include_router(expenses.router)
app.include_router(budgets.router)
app.include_router(ai.router)
app.include_router(recommendations.router)


# Health check API
@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "ai_configured": bool(settings.openai_api_key)
    }