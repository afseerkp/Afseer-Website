"""Single source of truth for the CV. Both build_docx.py and build_pdf.py read this."""

NAME = "AFSEER KP"
NAME_DISPLAY = "Afseer KP"   # mixed-case form used on the website
HEADLINE = "IT Team Lead  |  DevOps & Cloud (Azure / AWS)  |  Founder & Developer, BizApp365 ERP"
CONTACT = ("Dubai, United Arab Emirates  |  +971 58 288 5633  |  "
           "mail@afseer.com  |  bizapp365.com")

SUMMARY = (
    "IT Team Lead with over 15 years of experience in IT infrastructure, systems administration, "
    "networking and end-user support, currently leading the IT function at OMNIX International LLC in Dubai. "
    "Microsoft Certified DevOps Engineer Expert (AZ-400) and AWS Certified DevOps Engineer - Professional, "
    "with hands-on experience building CI/CD pipelines, automating infrastructure and administering "
    "Azure and AWS environments. Independently designed and built BizApp365, a multi-tenant cloud ERP "
    "platform for small and medium businesses covering accounting, inventory, CRM, HR and VAN sales. "
    "Specialises in integrating AI-driven automation into IT service workflows to reduce manual effort and "
    "shorten resolution times, and combines hands-on software development with proven strength in leading "
    "technical teams, managing vendors and standardising infrastructure across multi-site operations."
)

COMPETENCIES = [
    "IT Team Leadership & Mentoring",
    "DevOps & CI/CD Pipeline Delivery",
    "Cloud Administration (Azure, AWS)",
    "SaaS Product Development",
    "Full-Stack Web Development",
    "AI-Driven Process Automation",
    "ERP Implementation & Support",
    "Incident, Problem & Change Management",
    "Windows Server & Active Directory",
    "Network & Firewall Administration",
    "Virtualisation (VMware, Hyper-V)",
    "Microsoft 365 Administration",
    "Backup, Recovery & Business Continuity",
    "Vendor & Asset Lifecycle Management",
    "IT Projects, Rollouts & Migrations",
]

SKILLS = [
    ("Cloud & DevOps",
     "Microsoft Azure, Amazon Web Services (AWS), Azure DevOps, CI/CD pipeline design, Git & version control, "
     "Infrastructure as Code (ARM templates, AWS CloudFormation), containers (Docker), release management, "
     "monitoring & alerting (Azure Monitor, AWS CloudWatch), identity & access management (Entra ID, AWS IAM)"),
    ("Software Development",
     "Full-stack web application development, React, Vite, JavaScript, HTML5 and CSS3, responsive UI design, "
     "REST API design and integration, multi-tenant SaaS architecture, relational database design, "
     "role-based access control, bilingual (English / Arabic) interfaces, Git and version control"),
    ("Automation & AI",
     "AI-driven automation of IT workflows, Microsoft Power Automate, PowerShell scripting, Bash, "
     "automated ticket triage & routing, automated user onboarding/offboarding, scripted reporting, "
     "AI assistants and agent-based task automation"),
    ("Servers & Virtualisation",
     "Windows Server 2012/2016/2019/2022, Active Directory & ADC, DNS, DHCP, Group Policy, File & Print Services, "
     "Microsoft Exchange Server, VMware ESXi, Microsoft Hyper-V, QNAP NAS, server hardware & RAID"),
    ("Networking",
     "LAN / WAN, Cisco routers & switches, routing & switching, VLANs, structured cabling, "
     "wireless access points & controllers, VPN & site-to-site connectivity, network printing"),
    ("Security & Infrastructure",
     "Sophos and Fortinet FortiGate firewalls, endpoint protection, patch management, backup & disaster recovery, "
     "IP CCTV & enterprise NVR, biometric and door access control systems, time & attendance systems"),
    ("End-User & Voice",
     "Windows client OS deployment & imaging, Microsoft 365 and Outlook, desktop/laptop/peripheral support, "
     "PABX & IP PBX, IP telephony, enterprise Xerox multifunction devices, GPS vehicle tracking, remote support tools"),
]

EXPERIENCE = [
    {
        "company": "BIZAPP365 (bizapp365.com)",
        "display": "BizApp365",
        "location": "Own Product - Dubai, United Arab Emirates",
        "title": "Founder & Full-Stack Developer",
        "dates": "Ongoing",
        "note": None,
        "bullets": [
            "Independently designed, built and launched BizApp365, a multi-tenant cloud ERP platform for small "
            "and medium businesses, covering accounting, inventory, CRM, HR, VAN sales and silent printing.",
            "Architected the multi-tenant data model and role-based access control so that multiple client "
            "organisations run securely on shared infrastructure with isolated data.",
            "Developed the full application front to back, building a responsive React and Vite interface with "
            "bilingual English and Arabic support for the regional market.",
            "Built and integrated REST APIs across accounting, stock, sales and payroll modules, including "
            "document and invoice generation with direct silent printing for high-volume counter operations.",
            "Own the complete product lifecycle: cloud hosting and deployment, release management, database "
            "administration, performance tuning, security, customer onboarding and ongoing support.",
        ],
    },
    {
        "company": "OMNIX INTERNATIONAL LLC",
        "display": "OMNIX International LLC",
        "location": "Dubai, United Arab Emirates",
        "title": "IT Team Lead",
        "dates": "September 2021 - Present",
        "note": "Promoted from IT Engineer",
        "bullets": [
            "Lead the IT support team, allocating workload, defining SLAs and escalation paths, and mentoring "
            "engineers across infrastructure, networking and cloud practices.",
            "Own daily operation and availability of Windows Server, Active Directory, Microsoft 365 and "
            "virtualised VMware and Hyper-V environments across internal and client sites.",
            "Design and maintain CI/CD pipelines and deployment automation in Azure DevOps, standardising "
            "release processes and removing manual deployment steps.",
            "Administer Azure and AWS resources including virtual machines, storage, networking, identity and "
            "access management, backup policies and monitoring and alerting.",
            "Integrate AI-driven automation into IT service workflows using Power Automate, PowerShell and AI "
            "assistants, automating ticket triage, routine service requests, user onboarding and offboarding, "
            "and management reporting.",
            "Act as the final escalation point for complex incidents spanning servers, networks, Sophos and "
            "Fortinet firewalls, and end-user computing.",
            "Plan and deliver infrastructure projects including server and network upgrades, new office IT "
            "fit-outs, Microsoft 365 and Azure migrations, and CCTV and access control deployments.",
            "Manage vendors, procurement, licence renewals and IT asset lifecycle, and author the SOPs and "
            "runbooks that improved first-time fix rates across the team.",
        ],
    },
    {
        "company": "GULF AND SAFA DAIRIES",
        "display": "Gulf and Safa Dairies",
        "location": "Abu Dhabi, United Arab Emirates",
        "title": "IT Engineer",
        "dates": "May 2020 - August 2021",
        "note": None,
        "bullets": [
            "Maintained servers, network and end-user systems for a large-scale dairy production and distribution "
            "business, safeguarding availability of business-critical systems.",
            "Administered Active Directory, DNS, DHCP, file and print services, and Exchange and Outlook client "
            "configuration.",
            "Configured and supported Cisco switches and routers, wireless access points and site-to-site links "
            "across plant and office locations.",
            "Deployed and maintained IP CCTV and enterprise NVR, biometric time-attendance and door access "
            "control systems, and managed backups, patching and end-user hardware support.",
        ],
    },
    {
        "company": "AL MANARA PRIVATE SCHOOL",
        "display": "Al Manara Private School",
        "location": "Al Shamkha, Abu Dhabi, United Arab Emirates",
        "title": "IT Manager",
        "dates": "January 2020 - May 2020",
        "note": None,
        "bullets": [
            "Managed the school IT function covering servers, network infrastructure, computer labs, classroom "
            "technology and user support.",
            "Enabled the transition to remote learning by rolling out online platforms and secure remote access "
            "for staff and students.",
            "Maintained wireless coverage, network equipment, CCTV and access control across the campus.",
        ],
    },
    {
        "company": "SPEED PLUS (IT Solution Provider)",
        "display": "Speed Plus (IT Solution Provider)",
        "location": "Kasaragod, India",
        "title": "IT Support Engineer",
        "dates": "October 2017 - January 2020",
        "note": None,
        "bullets": [
            "Delivered on-site and remote IT support to a portfolio of SME clients across retail, education and "
            "healthcare sectors.",
            "Installed and configured Windows Server roles, virtual machines, networking equipment, firewalls and "
            "QNAP NAS storage.",
            "Implemented CCTV and NVR, access control, PABX and IP PBX, GPS vehicle tracking and home automation "
            "solutions, and delivered preventive maintenance and client training.",
        ],
    },
    {
        "company": "STARLINE",
        "display": "Starline",
        "location": "Al Rigga, Dubai, United Arab Emirates",
        "title": "IT Support Engineer",
        "dates": "June 2014 - August 2016",
        "note": None,
        "bullets": [
            "Provided first and second line support for desktops, laptops, printers, network connectivity and "
            "email issues.",
            "Assisted with server maintenance, user account administration, structured cabling and IP telephony "
            "setup.",
        ],
    },
    {
        "company": "VIJAY CISCO SYSTEMS",
        "display": "Vijay Cisco Systems",
        "location": "Bangalore, India",
        "title": "IT Support Engineer",
        "dates": "March 2010 - June 2014",
        "note": None,
        "bullets": [
            "Supported LAN and WAN environments, Cisco routing and switching, and mainframe terminal connectivity.",
            "Built, imaged and deployed desktops and laptops, and resolved hardware, operating system and "
            "application faults.",
        ],
    },
]

CERTIFICATIONS = [
    "Microsoft Certified: DevOps Engineer Expert (AZ-400)",
    "AWS Certified DevOps Engineer - Professional",
    "MCITP - Microsoft Certified IT Professional",
    "Microsoft Exchange Server 2007",
    "Diploma in Computer Hardware and Networking - IIHT, Bangalore (2006)",
    "Advanced Networking - Government ITI, Kasaragod",
]

EDUCATION = [
    "Bachelor of Commerce (B.Com) - Kannur University, India",
    "Diploma in Electronics and Communication Engineering (3 Years) - India",
]

LANGUAGES = "English  |  Hindi  |  Malayalam"
