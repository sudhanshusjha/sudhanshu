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
                    title="Senior Technical Product Manager / Senior Technical Project Manager",
                    company="MIDAS IT Services Pvt. Ltd.",
                    location="New Delhi, India",
                    duration="Mar 2023 – Present",
                    type="Full-time",
                    highlights=[
                        "Defined product strategy and executed roadmaps for EHR analytics and provider engagement solutions",
                        "Built and owned end-to-end product lifecycles from ideation to launch with data-driven insights",
                        "Leveraged SQL, Power BI, and Google Analytics to optimize product adoption, retention, and ROI",
                        "Led cross-functional agile teams to deliver AI/GenAI-driven solutions and complex product initiatives",
                        "Partnered with engineering, data science, design, and clinical stakeholders ensuring regulatory compliance (HIPAA)",
                        "Built and monitored product KPIs resulting in 25% improvement in feature adoption"
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
                        "Owned multiple product areas within healthcare SaaS platforms, driving agile product delivery",
                        "Defined clear product requirements and user stories, balancing user needs and business objectives",
                        "Improved product-market fit resulting in measurable increase in customer satisfaction and retention",
                        "Facilitated backlog grooming, sprint reviews, and agile ceremonies for team alignment",
                        "Launched integrated APIs and real-time alerts, reducing manual tasks by 25%",
                        "Built governance dashboards (JIRA + Power BI) increasing leadership visibility and decision speed"
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
                        "Managed full product lifecycle, delivering API-integrated solutions in healthcare and supply chain domains",
                        "Improved cross-functional team productivity by 40% and launched high-impact SaaS features",
                        "Led data-driven product enhancements using SQL and analytics for real-time user feedback prioritization"
                    ]
                ),
                ExperienceItem(
                    id=4,
                    title="Tech Lead",
                    company="Incedo Inc. (formerly Indiabulls Technology Solutions)",
                    location="Gurgaon, India",
                    duration="Jul 2013 – Jun 2016",
                    type="Full-time",
                    highlights=[
                        "Implemented TMS and CRM systems improving cross-functional productivity by 40%",
                        "Executed supply chain automation for ADIDAS, boosting operational output by 20%"
                    ]
                ),
                ExperienceItem(
                    id=5,
                    title="Senior Application Developer",
                    company="Serco Global Services Pvt. Ltd. (Infovision Solutions Pvt. Ltd.)",
                    location="Gurgaon, India",
                    duration="Sep 2007 – Jun 2013",
                    type="Full-time",
                    highlights=[
                        "Developed SFTP-based EDI apps, enhancing real-time data exchange accuracy by over 95%",
                        "Designed multi-tier database architecture, increasing data retrieval efficiency by 40%"
                    ]
                )
            ],
            projects=[
                ProjectItem(
                    id=1,
                    title="EHR Analytics & Provider Engagement Platform Evolution",
                    category="Product Strategy & Analytics",
                    description="Led strategic product evolution for Electronic Health Record analytics platform, focusing on provider engagement solutions with comprehensive data visualization and dashboard capabilities.",
                    achievements=[
                        "30% increase in provider engagement through strategic product initiatives",
                        "20% improvement in client satisfaction by aligning features with business needs", 
                        "Enhanced data visualization and dashboarding solutions",
                        "HIPAA, HL7, FHIR compliance alignment and regulatory framework adherence"
                    ],
                    technologies=["Healthcare Analytics", "EHR Integration", "HL7/FHIR", "Power BI", "SQL", "Data Visualization"],
                    impact="Transformed healthcare provider experience through strategic product vision and improved engagement strategies.",
                    metrics={
                        "engagement": "30%",
                        "satisfaction": "20%",
                        "timeline": "18 months"
                    }
                ),
                ProjectItem(
                    id=2,
                    title="Gen AI-Powered Product Delivery & Analytics Framework",
                    category="Innovation & AI Implementation",
                    description="Pioneered implementation of Generative AI-powered solutions across product delivery lifecycle, establishing advanced analytics modules and data-driven decision-making frameworks.",
                    achievements=[
                        "40% reduction in time-to-insight through analytics modules launch",
                        "Advanced SQL-powered dashboards for executive decision making",
                        "Gen AI integration for product lifecycle management",
                        "Sustainable reporting frameworks using JIRA, Power BI, and SQL"
                    ],
                    technologies=["Generative AI", "Advanced SQL", "Power BI", "JIRA", "Google Analytics", "Data Science"],
                    impact="Revolutionary approach to product delivery optimization using cutting-edge AI technology and data science.",
                    metrics={
                        "timeToInsight": "40%",
                        "decisionSpeed": "40%",
                        "framework": "Comprehensive"
                    }
                ),
                ProjectItem(
                    id=3,
                    title="Enterprise Data Management & Operational Efficiency",
                    category="Program Management & Operations",
                    description="Spearheaded comprehensive data management initiatives including automated archival, purging programs, and operational efficiency improvements across healthcare SaaS platforms.",
                    achievements=[
                        "30% reduction in storage costs through automated archival and purging",
                        "20% improvement in data processing efficiency",
                        "30% improvement in on-time delivery through program roadmaps",
                        "Enhanced delivery predictability by 25% with structured governance"
                    ],
                    technologies=["Data Management", "Automated Processes", "SQL", "Storage Optimization", "Program Governance"],
                    impact="Delivered significant operational efficiency and cost savings while maintaining data integrity and compliance.",
                    metrics={
                        "costReduction": "30%",
                        "efficiency": "20%",
                        "deliveryImprovement": "30%"
                    }
                ),
                ProjectItem(
                    id=4,
                    title="Healthcare SaaS Platform & Customer Adoption Growth",
                    category="Healthcare Product Development",
                    description="Led comprehensive product initiatives for B2B healthcare SaaS platforms, focusing on user engagement mechanics, clinical workflow optimization, and customer adoption strategies.",
                    achievements=[
                        "35% improvement in customer adoption through business-centric features",
                        "30% improvement in user engagement through data-driven engagement mechanics",
                        "25% improvement in feature adoption through user-centric design",
                        "Enhanced clinical workflow automation reducing manual tasks"
                    ],
                    technologies=["Healthcare SaaS", "B2B Platforms", "Clinical Workflows", "User Experience", "Engagement Analytics"],
                    impact="Transformed healthcare SaaS platform adoption and user engagement through strategic product initiatives.",
                    metrics={
                        "adoption": "35%",
                        "engagement": "30%",
                        "featureAdoption": "25%"
                    }
                ),
                ProjectItem(
                    id=5,
                    title="Cross-Functional Team Leadership & Delivery Excellence",
                    category="Leadership & Program Management",
                    description="Established governance frameworks, built high-performing engineering teams, and implemented structured delivery processes to improve organizational efficiency and team performance.",
                    achievements=[
                        "30% improvement in delivery efficiency through structured program planning",
                        "40% improvement in cross-functional team productivity",
                        "Built and mentored high-performing engineering teams",
                        "Simplified complex delivery processes improving release governance"
                    ],
                    technologies=["Agile Program Management", "Team Leadership", "JIRA", "Azure DevOps", "Governance Frameworks"],
                    impact="Created scalable delivery excellence through team leadership and structured governance frameworks.",
                    metrics={
                        "deliveryEfficiency": "30%",
                        "productivity": "40%",
                        "teamPerformance": "High"
                    }
                )
            ],
            certifications=[
                "ISB Certified Product Manager",
                "Project Management Professional (PMP) - Google Accredited",
                "Professional Scrum Product Owner (PSPO) - Scrum.org",
                "Professional Scrum Master (PSM) - Scrum.org", 
                "Scaled Professional Scrum (SPS) - Scrum.org",
                "Google Certified AI Professional - Google AI Essentials"
            ],
            achievements=[
                Achievement(
                    title="Philips Client Recognition",
                    description="Awarded by client (Philips) for error-free data transfer within timelines"
                ),
                Achievement(
                    title="Serco Pulse Award - Best Employee",
                    description="Honored 'Serco Pulse Award – Best Employee (India) of the year' by Serco Global Services"
                ),
                Achievement(
                    title="Tech PMx Junction Newsletter Author",
                    description="Author of Tech PMx Junction newsletter dedicated to real-world lessons in product, project, and program management with strategic vision insights"
                ),
                Achievement(
                    title="Director/Head Level Leadership Position",
                    description="Positioned for Director/Head of Product/Head of Program leadership roles based on strategic vision and execution excellence"
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