import streamlit as st
from data import HOSPITAL_INFO, PATIENTS, ROOMS
from pages import patients_page, rooms_page, hospital_info_page
from styles import get_styles

st.set_page_config(
    page_title="MediCare Plus Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(get_styles(), unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hospital-header">
    <div class="header-left">
        <div class="hospital-logo">✚</div>
        <div class="header-text">
            <h1 class="hospital-name">{HOSPITAL_INFO['name']}</h1>
            <p class="hospital-tagline">{HOSPITAL_INFO['tagline']}</p>
        </div>
    </div>
    <div class="header-right">
        <div class="header-contact">
            <span>📍 {HOSPITAL_INFO['address']}</span>
            <span>📞 {HOSPITAL_INFO['phone']}</span>
            <span>✉️ {HOSPITAL_INFO['email']}</span>
        </div>
        <div class="header-badge">Est. {HOSPITAL_INFO['established']}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-icon">✚</div>
        <span>MediCare Plus</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p class="nav-label">NAVIGATION</p>', unsafe_allow_html=True)

    nav_options = {
        "🏠  Dashboard": "Dashboard",
        "👥  Patients": "Patients",
        "🛏️  Rooms": "Rooms",
        "🏥  Hospital Info": "Hospital Info",
    }

    if "page" not in st.session_state:
        st.session_state.page = "Dashboard"

    for label, page in nav_options.items():
        is_active = st.session_state.page == page
        btn_class = "nav-btn-active" if is_active else "nav-btn"
        if st.button(label, key=f"nav_{page}", use_container_width=True):
            st.session_state.page = page
            st.rerun()

    st.markdown("---")

    # Quick stats in sidebar
    total_patients = len(PATIENTS)
    occupied_rooms = sum(1 for r in ROOMS if r["status"] == "Occupied")
    available_rooms = sum(1 for r in ROOMS if r["status"] == "Available")
    icu_patients = sum(1 for r in ROOMS if r["type"] == "ICU" and r["status"] == "Occupied")

    st.markdown('<p class="nav-label">QUICK STATS</p>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="sidebar-stats">
        <div class="stat-item">
            <span class="stat-num">{total_patients}</span>
            <span class="stat-lbl">Patients</span>
        </div>
        <div class="stat-item">
            <span class="stat-num">{occupied_rooms}</span>
            <span class="stat-lbl">Occupied</span>
        </div>
        <div class="stat-item">
            <span class="stat-num">{available_rooms}</span>
            <span class="stat-lbl">Available</span>
        </div>
        <div class="stat-item icu">
            <span class="stat-num">{icu_patients}</span>
            <span class="stat-lbl">ICU Active</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <div class="sidebar-footer">
        <p>🕐 24/7 Emergency</p>
        <p style="font-weight:700;color:#e74c3c;">{HOSPITAL_INFO['emergency']}</p>
    </div>
    """, unsafe_allow_html=True)

# ── Page Routing ─────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "Dashboard":
    from pages import dashboard_page
    dashboard_page.render()
elif page == "Patients":
    patients_page.render()
elif page == "Rooms":
    rooms_page.render()
elif page == "Hospital Info":
    hospital_info_page.render()

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hospital-footer">
    <div class="footer-grid">
        <div class="footer-col">
            <h4>✚ {HOSPITAL_INFO['name']}</h4>
            <p>{HOSPITAL_INFO['tagline']}</p>
            <p>Est. {HOSPITAL_INFO['established']}</p>
        </div>
        <div class="footer-col">
            <h4>Contact Us</h4>
            <p>📞 {HOSPITAL_INFO['phone']}</p>
            <p>📱 {HOSPITAL_INFO['mobile']}</p>
            <p>✉️ {HOSPITAL_INFO['email']}</p>
            <p>🌐 {HOSPITAL_INFO['website']}</p>
        </div>
        <div class="footer-col">
            <h4>Location</h4>
            <p>📍 {HOSPITAL_INFO['address']}</p>
            <p>{HOSPITAL_INFO['city']}</p>
        </div>
        <div class="footer-col">
            <h4>Emergency</h4>
            <p style="font-size:1.4rem;font-weight:700;color:#e74c3c;">🚨 {HOSPITAL_INFO['emergency']}</p>
            <p>Available 24 × 7</p>
            <p>Ambulance: {HOSPITAL_INFO['ambulance']}</p>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2025 {HOSPITAL_INFO['name']} · All Rights Reserved · NABH Accredited · ISO 9001:2015 Certified</p>
    </div>
</div>
""", unsafe_allow_html=True)
