from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional, Any
from datetime import datetime
import uuid

# Portfolio Data Models
class PersonalInfo(BaseModel):
    name: str
    title: str
    tagline: str
    location: str
    email: EmailStr
    phone: str
    linkedin: str
    profileImage: str
    yearsExperience: str
    domain: str

class AboutInfo(BaseModel):
    summary: str
    highlights: List[str]

class SkillsInfo(BaseModel):
    productManagement: List[str]
    programDelivery: List[str]
    dataAndAI: List[str]
    leadership: List[str]
    technical: List[str]

class ExperienceItem(BaseModel):
    id: int
    title: str
    company: str
    location: str
    duration: str
    type: str
    highlights: List[str]

class ProjectItem(BaseModel):
    id: int
    title: str
    category: str
    description: str
    achievements: List[str]
    technologies: List[str]
    impact: str
    metrics: Dict[str, Any]

class Achievement(BaseModel):
    title: str
    description: str

class PortfolioData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    personal: PersonalInfo
    about: AboutInfo
    skills: SkillsInfo
    experience: List[ExperienceItem]
    projects: List[ProjectItem]
    certifications: List[str]
    achievements: List[Achievement]
    lastUpdated: datetime = Field(default_factory=datetime.utcnow)

# Contact Form Models
class ContactSubmission(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    company: Optional[str] = Field(None, max_length=100)
    message: str = Field(..., min_length=10, max_length=2000)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: str = Field(default="portfolio_website")
    status: str = Field(default="new")
    ipAddress: Optional[str] = None
    userAgent: Optional[str] = None

class ContactSubmissionCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    company: Optional[str] = Field(None, max_length=100)
    message: str = Field(..., min_length=10, max_length=2000)

class ContactResponse(BaseModel):
    success: bool
    message: str
    submissionId: Optional[str] = None

# Analytics Models (Optional)
class PageView(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    page: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    ipAddress: Optional[str] = None
    userAgent: Optional[str] = None
    referrer: Optional[str] = None

class PageViewCreate(BaseModel):
    page: str
    referrer: Optional[str] = None