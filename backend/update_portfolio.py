#!/usr/bin/env python3
"""
Script to update portfolio data in MongoDB with new resume content
"""

import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Import our services
from database import database
from portfolio_service import PortfolioService

async def update_portfolio_data():
    """Update portfolio data with new resume content"""
    try:
        # Connect to database
        await database.connect()
        print("✅ Connected to database")
        
        # Clear existing portfolio data
        result = await database.db.portfolio_data.delete_many({})
        print(f"🗑️ Cleared {result.deleted_count} existing portfolio records")
        
        # Initialize new portfolio data
        success = await PortfolioService.initialize_portfolio_data()
        if success:
            print("✅ Portfolio data updated successfully with new resume content!")
        else:
            print("❌ Failed to update portfolio data")
            
    except Exception as e:
        print(f"❌ Error updating portfolio: {e}")
    finally:
        await database.disconnect()
        print("🔄 Database connection closed")

if __name__ == "__main__":
    asyncio.run(update_portfolio_data())