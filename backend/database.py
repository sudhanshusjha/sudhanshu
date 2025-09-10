from motor.motor_asyncio import AsyncIOMotorClient
from models import PortfolioData, ContactSubmission, PageView
import os
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.client = None
        self.db = None
    
    async def connect(self):
        """Connect to MongoDB database"""
        try:
            mongo_url = os.environ['MONGO_URL']
            self.client = AsyncIOMotorClient(mongo_url)
            self.db = self.client[os.environ['DB_NAME']]
            logger.info("Successfully connected to MongoDB")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise
    
    async def disconnect(self):
        """Disconnect from MongoDB database"""
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")
    
    # Portfolio Data Operations
    async def get_portfolio_data(self) -> Optional[PortfolioData]:
        """Get the portfolio data"""
        try:
            portfolio_doc = await self.db.portfolio_data.find_one()
            if portfolio_doc:
                # Remove MongoDB's _id field and return the data
                portfolio_doc.pop('_id', None)
                return PortfolioData(**portfolio_doc)
            return None
        except Exception as e:
            logger.error(f"Error fetching portfolio data: {e}")
            return None
    
    async def upsert_portfolio_data(self, portfolio: PortfolioData) -> bool:
        """Insert or update portfolio data"""
        try:
            portfolio_dict = portfolio.dict()
            result = await self.db.portfolio_data.replace_one(
                {},  # Empty filter to replace the single document
                portfolio_dict,
                upsert=True
            )
            logger.info(f"Portfolio data upserted successfully: {result.upserted_id or 'updated'}")
            return True
        except Exception as e:
            logger.error(f"Error upserting portfolio data: {e}")
            return False
    
    # Contact Submission Operations
    async def create_contact_submission(self, submission: ContactSubmission) -> bool:
        """Create a new contact submission"""
        try:
            submission_dict = submission.dict()
            result = await self.db.contact_submissions.insert_one(submission_dict)
            logger.info(f"Contact submission created: {result.inserted_id}")
            return True
        except Exception as e:
            logger.error(f"Error creating contact submission: {e}")
            return False
    
    async def get_contact_submissions(self, limit: int = 50) -> List[ContactSubmission]:
        """Get recent contact submissions"""
        try:
            cursor = self.db.contact_submissions.find().sort("timestamp", -1).limit(limit)
            submissions = []
            async for doc in cursor:
                doc.pop('_id', None)  # Remove MongoDB's _id field
                submissions.append(ContactSubmission(**doc))
            return submissions
        except Exception as e:
            logger.error(f"Error fetching contact submissions: {e}")
            return []
    
    async def update_submission_status(self, submission_id: str, status: str) -> bool:
        """Update contact submission status"""
        try:
            result = await self.db.contact_submissions.update_one(
                {"id": submission_id},
                {"$set": {"status": status}}
            )
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error updating submission status: {e}")
            return False
    
    # Analytics Operations (Optional)
    async def log_page_view(self, page_view: PageView) -> bool:
        """Log a page view for analytics"""
        try:
            page_view_dict = page_view.dict()
            result = await self.db.page_views.insert_one(page_view_dict)
            logger.info(f"Page view logged: {result.inserted_id}")
            return True
        except Exception as e:
            logger.error(f"Error logging page view: {e}")
            return False
    
    async def get_analytics_summary(self, days: int = 30) -> dict:
        """Get analytics summary for the last N days"""
        try:
            from datetime import datetime, timedelta
            cutoff_date = datetime.utcnow() - timedelta(days=days)
            
            # Count total page views
            total_views = await self.db.page_views.count_documents({
                "timestamp": {"$gte": cutoff_date}
            })
            
            # Count contact submissions
            total_contacts = await self.db.contact_submissions.count_documents({
                "timestamp": {"$gte": cutoff_date}
            })
            
            # Top pages
            pipeline = [
                {"$match": {"timestamp": {"$gte": cutoff_date}}},
                {"$group": {"_id": "$page", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 10}
            ]
            
            top_pages_cursor = self.db.page_views.aggregate(pipeline)
            top_pages = []
            async for doc in top_pages_cursor:
                top_pages.append({"page": doc["_id"], "views": doc["count"]})
            
            return {
                "totalViews": total_views,
                "totalContacts": total_contacts,
                "topPages": top_pages,
                "period": f"Last {days} days"
            }
        except Exception as e:
            logger.error(f"Error getting analytics summary: {e}")
            return {}

# Global database instance
database = Database()