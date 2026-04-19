HOSPITAL_INFO = {
    "name": "MediCare Plus Hospital",
    "tagline": "Compassionate Care · Advanced Medicine · Trusted Healing",
    "address": "42, Rajwada Road, Palasia Square",
    "city": "Indore, Madhya Pradesh – 452001",
    "phone": "+91-731-400-1234",
    "mobile": "+91-98765-43210",
    "email": "info@medicareplus.in",
    "website": "www.medicareplus.in",
    "emergency": "100-MEDI",
    "ambulance": "+91-731-400-9999",
    "established": "1998",
    "beds": 250,
    "doctors": 85,
    "specialties": 18,
    "accreditation": "NABH · ISO 9001:2015",
    "timing": "OPD: Mon–Sat, 8 AM – 8 PM  |  Emergency: 24 × 7",
    "description": (
        "MediCare Plus Hospital has been a cornerstone of healthcare excellence "
        "in Indore since 1998. With 250 beds, 85 specialist doctors, and 18 clinical "
        "departments, we deliver compassionate, evidence-based care to over 1,20,000 "
        "patients every year. Our state-of-the-art infrastructure—including a Level-III "
        "ICU, robotic surgery suite, and advanced diagnostics—ensures that every patient "
        "receives world-class treatment close to home."
    ),
}

DEPARTMENTS = [
    {"name": "Cardiology",       "head": "Dr. Arjun Mehta",    "ext": "101", "icon": "❤️"},
    {"name": "Neurology",        "head": "Dr. Priya Sharma",   "ext": "102", "icon": "🧠"},
    {"name": "Orthopaedics",     "head": "Dr. Rajesh Verma",   "ext": "103", "icon": "🦴"},
    {"name": "Paediatrics",      "head": "Dr. Sunita Joshi",   "ext": "104", "icon": "👶"},
    {"name": "Oncology",         "head": "Dr. Vivek Gupta",    "ext": "105", "icon": "🎗️"},
    {"name": "Gynaecology",      "head": "Dr. Anita Singh",    "ext": "106", "icon": "🌸"},
    {"name": "General Surgery",  "head": "Dr. Karan Patel",    "ext": "107", "icon": "🔬"},
    {"name": "Dermatology",      "head": "Dr. Neha Kulkarni",  "ext": "108", "icon": "🧬"},
    {"name": "Ophthalmology",    "head": "Dr. Ramesh Tiwari",  "ext": "109", "icon": "👁️"},
    {"name": "ENT",              "head": "Dr. Seema Dubey",    "ext": "110", "icon": "👂"},
    {"name": "Pulmonology",      "head": "Dr. Anil Shukla",    "ext": "111", "icon": "🫁"},
    {"name": "Nephrology",       "head": "Dr. Pooja Yadav",    "ext": "112", "icon": "🫘"},
    {"name": "Gastroenterology", "head": "Dr. Suresh Mishra",  "ext": "113", "icon": "🏥"},
    {"name": "Psychiatry",       "head": "Dr. Rina Agarwal",   "ext": "114", "icon": "🧩"},
    {"name": "Radiology",        "head": "Dr. Manish Saxena",  "ext": "115", "icon": "📡"},
    {"name": "Anaesthesiology",  "head": "Dr. Deepa Pandey",   "ext": "116", "icon": "💉"},
    {"name": "Physiotherapy",    "head": "Dr. Gaurav Rathore", "ext": "117", "icon": "🏃"},
    {"name": "Emergency Med.",   "head": "Dr. Rohit Bhatt",    "ext": "118", "icon": "🚨"},
]

DOCTORS = [
    {"id": "D001", "name": "Dr. Arjun Mehta",    "dept": "Cardiology",       "qual": "MD, DM (Cardiology)",         "exp": 22, "status": "Available"},
    {"id": "D002", "name": "Dr. Priya Sharma",   "dept": "Neurology",        "qual": "MD, DM (Neurology)",          "exp": 18, "status": "In OT"},
    {"id": "D003", "name": "Dr. Rajesh Verma",   "dept": "Orthopaedics",     "qual": "MS (Ortho), Fellowship UK",   "exp": 25, "status": "Available"},
    {"id": "D004", "name": "Dr. Sunita Joshi",   "dept": "Paediatrics",      "qual": "MD (Paediatrics)",            "exp": 15, "status": "Available"},
    {"id": "D005", "name": "Dr. Vivek Gupta",    "dept": "Oncology",         "qual": "MD, DM (Oncology)",           "exp": 20, "status": "On Leave"},
    {"id": "D006", "name": "Dr. Anita Singh",    "dept": "Gynaecology",      "qual": "MS (Obs & Gynae)",            "exp": 17, "status": "Available"},
    {"id": "D007", "name": "Dr. Karan Patel",    "dept": "General Surgery",  "qual": "MS (Surgery), FIAGES",        "exp": 19, "status": "In OT"},
    {"id": "D008", "name": "Dr. Neha Kulkarni",  "dept": "Dermatology",      "qual": "MD (Dermatology)",            "exp": 12, "status": "Available"},
    {"id": "D009", "name": "Dr. Rohit Bhatt",    "dept": "Emergency Med.",    "qual": "MD (Emergency Medicine)",     "exp": 14, "status": "Available"},
    {"id": "D010", "name": "Dr. Deepa Pandey",   "dept": "Anaesthesiology",  "qual": "MD (Anaesthesia)",            "exp": 16, "status": "In OT"},
]

PATIENTS = [
    {
        "id": "P001", "name": "Ramesh Sharma",    "age": 58, "gender": "Male",
        "disease": "Acute Myocardial Infarction", "dept": "Cardiology",
        "doctor": "Dr. Arjun Mehta",  "room": "ICU-01",
        "admission": "2025-07-01",    "status": "Critical",
        "blood": "B+", "contact": "+91-98100-11111",
    },
    {
        "id": "P002", "name": "Sunita Patel",     "age": 34, "gender": "Female",
        "disease": "Normal Delivery",              "dept": "Gynaecology",
        "doctor": "Dr. Anita Singh",  "room": "PVT-05",
        "admission": "2025-07-03",    "status": "Stable",
        "blood": "O+", "contact": "+91-98100-22222",
    },
    {
        "id": "P003", "name": "Vikram Joshi",     "age": 45, "gender": "Male",
        "disease": "Lumbar Disc Herniation",       "dept": "Orthopaedics",
        "doctor": "Dr. Rajesh Verma", "room": "GEN-12",
        "admission": "2025-07-02",    "status": "Stable",
        "blood": "A+", "contact": "+91-98100-33333",
    },
    {
        "id": "P004", "name": "Ananya Gupta",     "age": 7,  "gender": "Female",
        "disease": "Viral Pneumonia",              "dept": "Paediatrics",
        "doctor": "Dr. Sunita Joshi", "room": "GEN-08",
        "admission": "2025-07-04",    "status": "Improving",
        "blood": "AB-", "contact": "+91-98100-44444",
    },
    {
        "id": "P005", "name": "Mohammed Hussain", "age": 62, "gender": "Male",
        "disease": "Type-2 Diabetes with Nephropathy", "dept": "Nephrology",
        "doctor": "Dr. Pooja Yadav",  "room": "PVT-02",
        "admission": "2025-06-28",    "status": "Stable",
        "blood": "O-", "contact": "+91-98100-55555",
    },
    {
        "id": "P006", "name": "Kavita Mishra",    "age": 52, "gender": "Female",
        "disease": "Breast Carcinoma Stage II",    "dept": "Oncology",
        "doctor": "Dr. Vivek Gupta",  "room": "PVT-07",
        "admission": "2025-06-25",    "status": "Under Treatment",
        "blood": "B-", "contact": "+91-98100-66666",
    },
    {
        "id": "P007", "name": "Deepak Rajput",    "age": 38, "gender": "Male",
        "disease": "Acute Appendicitis",           "dept": "General Surgery",
        "doctor": "Dr. Karan Patel",  "room": "GEN-15",
        "admission": "2025-07-05",    "status": "Post-Op",
        "blood": "A-", "contact": "+91-98100-77777",
    },
    {
        "id": "P008", "name": "Geeta Verma",      "age": 71, "gender": "Female",
        "disease": "Ischaemic Stroke",             "dept": "Neurology",
        "doctor": "Dr. Priya Sharma", "room": "ICU-03",
        "admission": "2025-07-04",    "status": "Critical",
        "blood": "AB+", "contact": "+91-98100-88888",
    },
    {
        "id": "P009", "name": "Akash Tiwari",     "age": 29, "gender": "Male",
        "disease": "Road Traffic Accident – Polytrauma", "dept": "Emergency Med.",
        "doctor": "Dr. Rohit Bhatt",  "room": "ICU-02",
        "admission": "2025-07-05",    "status": "Critical",
        "blood": "B+", "contact": "+91-98100-99999",
    },
    {
        "id": "P010", "name": "Pooja Agarwal",    "age": 41, "gender": "Female",
        "disease": "Hyperthyroidism",              "dept": "General Surgery",
        "doctor": "Dr. Karan Patel",  "room": "GEN-20",
        "admission": "2025-07-03",    "status": "Stable",
        "blood": "O+", "contact": "+91-98100-10101",
    },
    {
        "id": "P011", "name": "Suresh Yadav",     "age": 55, "gender": "Male",
        "disease": "Chronic Obstructive Pulmonary Disease", "dept": "Pulmonology",
        "doctor": "Dr. Anil Shukla",  "room": "GEN-18",
        "admission": "2025-06-30",    "status": "Improving",
        "blood": "A+", "contact": "+91-98100-11122",
    },
    {
        "id": "P012", "name": "Ritu Saxena",      "age": 26, "gender": "Female",
        "disease": "Urinary Tract Infection",      "dept": "Nephrology",
        "doctor": "Dr. Pooja Yadav",  "room": "GEN-06",
        "admission": "2025-07-05",    "status": "Stable",
        "blood": "B+", "contact": "+91-98100-22233",
    },
]

ROOMS = [
    # ICU Rooms
    {"room_no": "ICU-01", "type": "ICU",     "floor": 1, "capacity": 1, "status": "Occupied",  "patient": "P001", "nurse": "Nurse Kavita",  "rate": 8000},
    {"room_no": "ICU-02", "type": "ICU",     "floor": 1, "capacity": 1, "status": "Occupied",  "patient": "P009", "nurse": "Nurse Pradeep", "rate": 8000},
    {"room_no": "ICU-03", "type": "ICU",     "floor": 1, "capacity": 1, "status": "Occupied",  "patient": "P008", "nurse": "Nurse Rina",    "rate": 8000},
    {"room_no": "ICU-04", "type": "ICU",     "floor": 1, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Suresh",  "rate": 8000},
    {"room_no": "ICU-05", "type": "ICU",     "floor": 1, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Meena",   "rate": 8000},
    # Private Rooms
    {"room_no": "PVT-01", "type": "Private", "floor": 2, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Anjali",  "rate": 4500},
    {"room_no": "PVT-02", "type": "Private", "floor": 2, "capacity": 1, "status": "Occupied",  "patient": "P005", "nurse": "Nurse Deepa",   "rate": 4500},
    {"room_no": "PVT-03", "type": "Private", "floor": 2, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Rahul",   "rate": 4500},
    {"room_no": "PVT-04", "type": "Private", "floor": 2, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Shalini", "rate": 4500},
    {"room_no": "PVT-05", "type": "Private", "floor": 2, "capacity": 1, "status": "Occupied",  "patient": "P002", "nurse": "Nurse Preeti",  "rate": 4500},
    {"room_no": "PVT-06", "type": "Private", "floor": 3, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Arun",    "rate": 4500},
    {"room_no": "PVT-07", "type": "Private", "floor": 3, "capacity": 1, "status": "Occupied",  "patient": "P006", "nurse": "Nurse Vandana", "rate": 4500},
    {"room_no": "PVT-08", "type": "Private", "floor": 3, "capacity": 1, "status": "Available", "patient": None,   "nurse": "Nurse Lokesh",  "rate": 4500},
    # General Rooms
    {"room_no": "GEN-01", "type": "General", "floor": 4, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Sangita", "rate": 1500},
    {"room_no": "GEN-02", "type": "General", "floor": 4, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Vinod",   "rate": 1500},
    {"room_no": "GEN-03", "type": "General", "floor": 4, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Geeta",   "rate": 1500},
    {"room_no": "GEN-04", "type": "General", "floor": 4, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Brijesh", "rate": 1500},
    {"room_no": "GEN-05", "type": "General", "floor": 4, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Nidhi",   "rate": 1500},
    {"room_no": "GEN-06", "type": "General", "floor": 5, "capacity": 4, "status": "Occupied",  "patient": "P012", "nurse": "Nurse Sharda",  "rate": 1500},
    {"room_no": "GEN-07", "type": "General", "floor": 5, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Tarun",   "rate": 1500},
    {"room_no": "GEN-08", "type": "General", "floor": 5, "capacity": 4, "status": "Occupied",  "patient": "P004", "nurse": "Nurse Kaveri",  "rate": 1500},
    {"room_no": "GEN-09", "type": "General", "floor": 5, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Dilip",   "rate": 1500},
    {"room_no": "GEN-10", "type": "General", "floor": 5, "capacity": 4, "status": "Available", "patient": None,   "nurse": "Nurse Rekha",   "rate": 1500},
    {"room_no": "GEN-12", "type": "General", "floor": 6, "capacity": 4, "status": "Occupied",  "patient": "P003", "nurse": "Nurse Pradeep", "rate": 1500},
    {"room_no": "GEN-15", "type": "General", "floor": 6, "capacity": 4, "status": "Occupied",  "patient": "P007", "nurse": "Nurse Smita",   "rate": 1500},
    {"room_no": "GEN-18", "type": "General", "floor": 6, "capacity": 4, "status": "Occupied",  "patient": "P011", "nurse": "Nurse Harish",  "rate": 1500},
    {"room_no": "GEN-20", "type": "General", "floor": 6, "capacity": 4, "status": "Occupied",  "patient": "P010", "nurse": "Nurse Usha",    "rate": 1500},
]

SERVICES = [
    {"name": "24×7 Emergency",      "icon": "🚨", "desc": "Round-the-clock trauma and critical care"},
    {"name": "Advanced ICU",         "icon": "🫀", "desc": "Level-III ICU with ventilator support"},
    {"name": "Robotic Surgery",      "icon": "🤖", "desc": "Minimally invasive precision procedures"},
    {"name": "Digital Radiology",    "icon": "📡", "desc": "MRI, CT, PET-CT, and Ultrasound"},
    {"name": "Blood Bank",           "icon": "🩸", "desc": "24×7 component blood therapy"},
    {"name": "Pharmacy",             "icon": "💊", "desc": "In-house pharmacy & home delivery"},
    {"name": "Ambulance",            "icon": "🚑", "desc": "GPS-equipped ALS ambulances"},
    {"name": "Telemedicine",         "icon": "💻", "desc": "Virtual consultations from home"},
    {"name": "Physiotherapy",        "icon": "🏃", "desc": "Rehabilitation & sports medicine"},
    {"name": "Diagnostics Lab",      "icon": "🔬", "desc": "NABL-accredited pathology services"},
    {"name": "Neonatal ICU (NICU)",  "icon": "👶", "desc": "Level-III NICU for preterm infants"},
    {"name": "Dialysis Centre",      "icon": "🫘", "desc": "Haemodialysis & peritoneal dialysis"},
]
