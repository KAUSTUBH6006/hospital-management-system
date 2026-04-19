# 🏥 MediCare Plus — Hospital Management System

A fully functional, beautifully designed **Hospital Management System** built with **Python + Streamlit**. No database required — all data is hard-coded for a clean, portable demo.

---

## ✨ Features

| Module | Highlights |
|---|---|
| **Dashboard** | KPI metrics, room occupancy bars, patient status charts, doctor cards |
| **Patient Management** | Search/filter patients, expandable detail cards, add new patient form, update existing records |
| **Room Allocation** | Visual room grid (ICU / Private / General), assign & discharge rooms |
| **Hospital Info** | About, 18 departments, 12 services, senior medical team |
| **Header & Footer** | Hospital name, address, phone, email visible on every page |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/hospital-management-system.git
cd hospital-management-system

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app will open automatically at **http://localhost:8501**

---

## 📁 Project Structure

```
hospital-management-system/
│
├── app.py                  # Main entry point — header, sidebar, routing, footer
├── data.py                 # All hard-coded data (hospital info, patients, rooms, doctors)
├── styles.py               # Custom CSS (fonts, colors, cards, badges)
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
└── pages/
    ├── __init__.py
    ├── dashboard_page.py   # Dashboard with KPIs & charts
    ├── patients_page.py    # Patient list, add & update forms
    ├── rooms_page.py       # Room grid, allocation, table view
    └── hospital_info_page.py # About, departments, services, team
```

---

## 🏥 Hospital Details (Demo Data)

| Field | Value |
|---|---|
| Hospital | MediCare Plus Hospital |
| Location | 42, Rajwada Road, Indore, MP — 452001 |
| Phone | +91-731-400-1234 |
| Email | info@medicareplus.in |
| Emergency | 100-MEDI |
| Beds | 250+ |
| Doctors | 85+ |
| Departments | 18 |

---

## 🌐 Deploy on Streamlit Cloud (Free)

1. Push this repository to GitHub.
2. Visit [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **"New app"** → select your repo → set **Main file path** to `app.py`.
4. Click **Deploy** — your app goes live in ~60 seconds!

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** — UI framework
- **Pandas** — tabular data display
- **Google Fonts** — Playfair Display + DM Sans

---

## 📝 Notes

- This project uses **hard-coded in-memory data** (no database). Form submissions show a preview/confirmation but do not permanently mutate data — ideal for demos and portfolio projects.
- To wire up a real database, replace the lists in `data.py` with SQLite / PostgreSQL queries.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built with ❤️ for learning and portfolio purposes.*
