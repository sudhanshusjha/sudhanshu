from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Import our models and services
from models import *
from database import database
from portfolio_service import PortfolioService

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Application lifecycle management
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up portfolio backend...")
    try:
        await database.connect()
        
        # Initialize portfolio data if not exists
        existing_portfolio = await database.get_portfolio_data()
        if not existing_portfolio:
            logger.info("No existing portfolio data found, initializing...")
            await PortfolioService.initialize_portfolio_data()
        else:
            logger.info("Portfolio data already exists in database")
            
        logger.info("Portfolio backend startup complete")
        yield
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise
    finally:
        # Shutdown
        logger.info("Shutting down portfolio backend...")
        await database.disconnect()

# Create the main app with lifespan management
app = FastAPI(
    title="Sudhanshu's Portfolio API",
    description="Backend API for professional portfolio website",
    version="1.0.0",
    lifespan=lifespan
)

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Portfolio endpoints
@api_router.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Portfolio API is running", "status": "healthy"}

@api_router.get("/portfolio", response_model=PortfolioData)
async def get_portfolio():
    """Get complete portfolio data"""
    try:
        portfolio = await PortfolioService.get_portfolio()
        if not portfolio:
            raise HTTPException(status_code=404, detail="Portfolio data not found")
        return portfolio
    except Exception as e:
        logger.error(f"Error fetching portfolio: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.post("/contact", response_model=ContactResponse)
async def submit_contact_form(submission: ContactSubmissionCreate, request: Request):
    """Handle contact form submissions"""
    try:
        # Get client IP and user agent
        client_ip = request.client.host if request.client else None
        user_agent = request.headers.get("user-agent")
        
        # Process the submission
        response = await PortfolioService.submit_contact_form(
            submission,
            ip_address=client_ip,
            user_agent=user_agent
        )
        
        if not response.success:
            raise HTTPException(status_code=400, detail=response.message)
            
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing contact form: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.get("/contact/submissions")
async def get_contact_submissions(limit: int = 50):
    """Get recent contact submissions (for admin use)"""
    try:
        submissions = await database.get_contact_submissions(limit)
        return {"submissions": submissions, "count": len(submissions)}
    except Exception as e:
        logger.error(f"Error fetching contact submissions: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Analytics endpoints (optional)
@api_router.post("/analytics/page-view")
async def log_page_view(page_view_data: PageViewCreate, request: Request):
    """Log a page view for analytics"""
    try:
        client_ip = request.client.host if request.client else None
        user_agent = request.headers.get("user-agent")
        
        page_view = PageView(
            **page_view_data.dict(),
            ipAddress=client_ip,
            userAgent=user_agent
        )
        
        success = await database.log_page_view(page_view)
        if success:
            return {"success": True, "message": "Page view logged"}
        else:
            raise HTTPException(status_code=500, detail="Failed to log page view")
            
    except Exception as e:
        logger.error(f"Error logging page view: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@api_router.get("/analytics/summary")
async def get_analytics_summary(days: int = 30):
    """Get analytics summary"""
    try:
        summary = await database.get_analytics_summary(days)
        return summary
    except Exception as e:
        logger.error(f"Error fetching analytics summary: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Include the router in the main app
app.include_router(api_router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)