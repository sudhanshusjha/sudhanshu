from models import *
from database import database
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class PortfolioService:
    """Service layer for portfolio operations"""
    
    @staticmethod
    async def initialize_portfolio_data():
        """Initialize portfolio with Sudhanshu's updated data"""
        
        # Sudhanshu's updated portfolio data
        portfolio_data = PortfolioData(
            personal=PersonalInfo(
                name="Sudhanshu Shekhar Jha",
                title="Senior Technical Product & Program Leader | Gen AI Powered",
                tagline="Strategic Vision • Cross-Functional Orchestration • Outcome-Driven Leadership",
                location="Greater Noida West, India",
                email="sudhanshurg@gmail.com",
                phone="+91-7303436488, +91-9650261122",
                linkedin="https://www.linkedin.com/in/sudhanshu-s-jha/",
                profileImage="https://customer-assets.emergentagent.com/job_portfolio-pro-96/artifacts/9k9r7grb_WhatsApp%20Image%202025-09-10%20at%2019.48.04.jpeg",
                yearsExperience="19+",
                domain="IT & Tech Experience • Healthcare • SaaS • Enterprise"
            ),
            about=AboutInfo(
                summary="Accomplished Gen AI Powered Senior Technical Product & Program Leader with 19+ years in IT and 6+ years driving product management, agile delivery, and program governance across healthcare technology, SaaS, and enterprise ecosystems. Adept at blending strategic product vision with program execution discipline, ensuring delivery of high-value, compliant, and customer-centric solutions.",
                highlights=[
                    "Strategic product vision with program execution discipline",
                    "Gen AI powered solutions and advanced analytics expertise",
                    "End-to-end lifecycle management from strategy to sunset",
                    "C-level stakeholder communication and executive leadership",
                    "Healthcare technology and enterprise SaaS specialization",
                    "Quantifiable business impact with data-driven decision making",
                    "Cross-functional team leadership and matrix management",
                    "Director/Head of Product/Program positioned for leadership roles"
                ]
            ),
            skills=SkillsInfo(
                productManagement=[
                    "Product Vision & Roadmapping",
                    "Product Strategy & Execution", 
                    "Product Lifecycle Management",
                    "Product Requirements (PRDs, User Stories)",
                    "Feature Ownership & Prioritization",
                    "Customer Discovery & VOC",
                    "Data-Driven Feature Prioritization",
                    "Continuous Improvement & Post-Release Metrics"
                ],
                programDelivery=[
                    "Technical Program Management (TPM)",
                    "Program & Project Governance",
                    "Portfolio Oversight & Budget Management",
                    "Agile Program Delivery",
                    "Sprint Planning & Release Governance",
                    "Risk & Dependency Tracking",
                    "Benefits Realization & Value Stream",
                    "End-to-End Program Delivery"
                ],
                dataAndAI=[
                    "Gen AI & Advanced SQL",
                    "Power BI, SSRS, SSIS",
                    "KPI Dashboards & Reporting",
                    "Data-Driven Decision Making",
                    "EHR/EMR Integrations (HL7, FHIR)",
                    "Clinical Data Interchange",
                    "Data Archival & Purging Programs",
                    "Metrics Definition & Analytics"
                ],
                leadership=[
                    "C-Level Stakeholder Communication",
                    "Cross-Functional Collaboration",
                    "Matrix Leadership & Global Teams",
                    "Executive Storytelling & Communication",
                    "Coaching, Mentoring & Team Enablement",
                    "Change Enablement & Learning",
                    "Conflict Resolution & Escalation",
                    "Vendor & Partner Coordination"
                ],
                technical=[
                    "CRM & TMS Platforms",
                    "API Integrations & SaaS",
                    "JIRA & Azure DevOps",
                    "Confluence & GitHub",
                    "Agile Ceremonies & Tools",
                    "HIPAA Compliance",
                    "Enterprise Integrations",
                    "Flow Metrics & Sprint Health"
                ]
            ),
            experience=[
                ExperienceItem(
                    id=1,
                    title="Senior Technical Product Manager",
                    company="MIDAS IT Services Pvt. Ltd.",
                    location="New Delhi, India",
                    duration="Mar 2023 – Present",
                    type="Full-time",
                    highlights=[
                        "Defined product strategy for EHR analytics & provider engagement platforms",
                        "Led data archival & purging program reducing OPEX costs by 30%",
                        "Applied Gen AI-powered backlog analysis for faster prioritization",
                        "Mentored PMs/TPMs improving sprint predictability by 15-20%",
                        "Built executive dashboards enhancing roadmap visibility"
                    ]
                ),
                ExperienceItem(
                    id=2,
                    title="Technical Project Manager",
                    company="MIDAS IT Services Pvt. Ltd.",
                    location="New Delhi, India", 
                    duration="Mar 2020 – Feb 2023",
                    type="Full-time",
                    highlights=[
                        "Owned SaaS delivery programs with Agile governance frameworks",
                        "Reduced backlog items by 30% through agile ceremonies optimization",
                        "Coordinated stakeholder alignment reducing development time by 25%",
                        "Designed APIs & alerts reducing manual interventions by 25%",
                        "Drove VOC-backed enhancements improving retention by 20%"
                    ]
                ),
                ExperienceItem(
                    id=3,
                    title="Project Lead",
                    company="MIDAS IT Services Pvt. Ltd.",
                    location="New Delhi, India",
                    duration="Jun 2016 – Feb 2020", 
                    type="Full-time",
                    highlights=[
                        "Authored 100+ user stories improving sprint delivery by 15%",
                        "Integrated EMR & EPR features boosting data accuracy by 20%",
                        "Streamlined documentation cutting development time by 15%"
                    ]
                ),
                ExperienceItem(
                    id=4,
                    title="Tech Lead",
                    company="Incedo Inc. (formerly Indiabulls Tech Solutions)",
                    location="Gurgaon, India",
                    duration="Jul 2013 – Jun 2016",
                    type="Full-time",
                    highlights=[
                        "Directed SaaS CRM & workflow delivery achieving 20% data accuracy uplift",
                        "Coordinated multi-tenant systems with compliance adherence"
                    ]
                )
            ],
            projects=[
                ProjectItem(
                    id=1,
                    title="EHR Analytics & Provider Engagement Platform",
                    category="Product Strategy & Analytics",
                    description="Defined comprehensive product strategy and roadmap for Electronic Health Record analytics platform, driving significant improvements in provider engagement and client satisfaction.",
                    achievements=[
                        "30% increase in provider engagement",
                        "20% improvement in client satisfaction", 
                        "Enhanced analytics capabilities for healthcare providers",
                        "HIPAA, HL7, FHIR compliance alignment"
                    ],
                    technologies=["Healthcare Analytics", "EHR Integration", "HL7/FHIR", "Power BI", "SQL"],
                    impact="Transformed healthcare provider experience through data-driven insights and improved engagement strategies.",
                    metrics={
                        "engagement": "30%",
                        "satisfaction": "20%",
                        "timeline": "12 months"
                    }
                ),
                ProjectItem(
                    id=2,
                    title="Enterprise Data Archival & Cost Optimization",
                    category="Program Management & Operations",
                    description="Spearheaded comprehensive data archival and purging program to optimize storage costs and improve processing efficiency across healthcare SaaS platform.",
                    achievements=[
                        "30% reduction in storage costs",
                        "20% improvement in processing efficiency",
                        "Automated archival processes implementation",
                        "Compliance-aligned data retention policies"
                    ],
                    technologies=["Data Management", "Automated Processes", "SQL", "Storage Optimization", "Compliance"],
                    impact="Delivered significant cost savings while maintaining data integrity and compliance requirements.",
                    metrics={
                        "costReduction": "30%",
                        "efficiency": "20%",
                        "savings": "$2M+ annually"
                    }
                ),
                ProjectItem(
                    id=3,
                    title="Gen AI-Powered Product Delivery Framework",
                    category="Innovation & AI Implementation",
                    description="Pioneered implementation of Generative AI-powered frameworks to enhance requirement analysis, user feedback classification, and backlog management processes.",
                    achievements=[
                        "25% reduction in backlog grooming time",
                        "Accelerated feature prioritization process",
                        "Enhanced requirement analysis accuracy",
                        "Improved user feedback classification"
                    ],
                    technologies=["Generative AI", "Machine Learning", "Natural Language Processing", "Process Automation", "Analytics"],
                    impact="Revolutionary approach to product delivery optimization using cutting-edge AI technology.",
                    metrics={
                        "efficiency": "25%",
                        "accuracy": "40%",
                        "timeReduction": "10 hours/week"
                    }
                ),
                ProjectItem(
                    id=4,
                    title="Healthcare OPPE Features & User Engagement",
                    category="Healthcare Product Development",
                    description="Led development and implementation of high-quality OPPE (Ongoing Professional Practice Evaluation) features for healthcare providers, significantly enhancing user engagement.",
                    achievements=[
                        "30% higher user engagement than expected",
                        "Exceeded quality expectations for OPPE features",
                        "Enhanced healthcare provider workflows",
                        "Improved clinical decision support"
                    ],
                    technologies=["Healthcare Systems", "OPPE Standards", "Clinical Workflows", "User Experience", "Healthcare Analytics"],
                    impact="Transformed healthcare provider evaluation processes with intuitive, high-quality features.",
                    metrics={
                        "engagement": "30%",
                        "satisfaction": "95%",
                        "adoption": "85%"
                    }
                ),
                ProjectItem(
                    id=5,
                    title="Executive KPI Dashboards & Governance",
                    category="Data Analytics & Governance",
                    description="Established comprehensive JIRA + Power BI + SQL dashboard ecosystem to track KPIs, OKRs, and provide executive-level insights for strategic decision making.",
                    achievements=[
                        "40% reduction in executive decision latency",
                        "Enhanced roadmap visibility across organization",
                        "Automated KPI tracking and reporting",
                        "Improved program governance frameworks"
                    ],
                    technologies=["Power BI", "SQL Server", "JIRA", "Azure DevOps", "Executive Reporting", "KPI Analytics"],
                    impact="Empowered executive leadership with real-time insights for faster, data-driven decisions.",
                    metrics={
                        "decisionSpeed": "40%",
                        "visibility": "100%",
                        "automation": "80%"
                    }
                )
            ],
            certifications=[
                "ISB Product Management",
                "Project Management Professional (PMP)",
                "Professional Scrum Product Owner (PSPO)",
                "Professional Scrum Master (PSM)", 
                "Scaled Professional Scrum (SPS)",
                "Google AI Essentials"
            ],
            achievements=[
                Achievement(
                    title="Philips Recognition",
                    description="Awarded by Philips for error-free data transfer within timelines"
                ),
                Achievement(
                    title="Serco Pulse Award",
                    description="Best Employee (India) - Serco Global Services"
                ),
                Achievement(
                    title="Tech PMx Junction",
                    description="Author of professional newsletter sharing real-world lessons in product, project, and program management"
                )
            ]
        )
        
        # Save to database
        success = await database.upsert_portfolio_data(portfolio_data)
        if success:
            logger.info("Portfolio data initialized successfully")
        else:
            logger.error("Failed to initialize portfolio data")
        
        return success
    
    @staticmethod
    async def get_portfolio() -> Optional[PortfolioData]:
        """Get portfolio data from database"""
        return await database.get_portfolio_data()
    
    @staticmethod
    async def submit_contact_form(
        submission_data: ContactSubmissionCreate, 
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None
    ) -> ContactResponse:
        """Process contact form submission"""
        try:
            # Create contact submission object
            submission = ContactSubmission(
                **submission_data.dict(),
                ipAddress=ip_address,
                userAgent=user_agent
            )
            
            # Save to database
            success = await database.create_contact_submission(submission)
            
            if success:
                logger.info(f"Contact form submitted successfully: {submission.email}")
                return ContactResponse(
                    success=True,
                    message="Thank you for your message! I'll get back to you within 24 hours.",
                    submissionId=submission.id
                )
            else:
                logger.error("Failed to save contact submission")
                return ContactResponse(
                    success=False,
                    message="There was an error submitting your message. Please try again later."
                )
                
        except Exception as e:
            logger.error(f"Error processing contact form: {e}")
            return ContactResponse(
                success=False,
                message="There was an error submitting your message. Please try again later."
            )