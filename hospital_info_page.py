import streamlit as st
from data import HOSPITAL_INFO, DEPARTMENTS, SERVICES, DOCTORS

def render():
    st.markdown('<h2 class="section-title">Hospital Information</h2>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🏥  About Us", "🏢  Departments", "⚕️  Services", "👨‍⚕️  Medical Team"])

    # ── Tab 1: About ─────────────────────────────────────────────────────
    with tab1:
        c1, c2 = st.columns([1.4, 1])

        with c1:
            st.markdown(f"""
            <div class="info-box">
                <h3>✚ {HOSPITAL_INFO['name']}</h3>
                <p style="font-size:0.88rem;line-height:1.8;color:rgba(255,255,255,0.85);">
                    {HOSPITAL_INFO['description']}
                </p>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.7rem;margin-top:1.2rem;">
                    <div style="background:rgba(255,255,255,0.08);border-radius:10px;padding:0.8rem;">
                        <div style="font-size:1.6rem;font-family:'Playfair Display',serif;font-weight:700;color:#f0a500;">{HOSPITAL_INFO['beds']}+</div>
                        <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,0.55);">Beds</div>
                    </div>
                    <div style="background:rgba(255,255,255,0.08);border-radius:10px;padding:0.8rem;">
                        <div style="font-size:1.6rem;font-family:'Playfair Display',serif;font-weight:700;color:#f0a500;">{HOSPITAL_INFO['doctors']}+</div>
                        <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,0.55);">Specialists</div>
                    </div>
                    <div style="background:rgba(255,255,255,0.08);border-radius:10px;padding:0.8rem;">
                        <div style="font-size:1.6rem;font-family:'Playfair Display',serif;font-weight:700;color:#f0a500;">{HOSPITAL_INFO['specialties']}</div>
                        <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,0.55);">Departments</div>
                    </div>
                    <div style="background:rgba(255,255,255,0.08);border-radius:10px;padding:0.8rem;">
                        <div style="font-size:1rem;font-family:'Playfair Display',serif;font-weight:700;color:#f0a500;">27 yrs</div>
                        <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,0.55);">Of Excellence</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card" style="height:100%;">
                <h4 style="color:#0d1b2a;border-bottom:2px solid #1a7a6e;padding-bottom:8px;">📞 Contact Directory</h4>
            """, unsafe_allow_html=True)

            contact_items = [
                ("📍", "Address",          HOSPITAL_INFO["address"] + ", " + HOSPITAL_INFO["city"]),
                ("📞", "Main Line",        HOSPITAL_INFO["phone"]),
                ("📱", "Mobile",           HOSPITAL_INFO["mobile"]),
                ("✉️", "Email",            HOSPITAL_INFO["email"]),
                ("🌐", "Website",          HOSPITAL_INFO["website"]),
                ("🚨", "Emergency",        HOSPITAL_INFO["emergency"]),
                ("🚑", "Ambulance",        HOSPITAL_INFO["ambulance"]),
                ("🕐", "OPD Timings",      HOSPITAL_INFO["timing"]),
                ("🏅", "Accreditation",    HOSPITAL_INFO["accreditation"]),
                ("📅", "Established",      HOSPITAL_INFO["established"]),
            ]
            for icon, label, value in contact_items:
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid #f0f0f0;">
                    <span style="font-size:1rem;min-width:22px;">{icon}</span>
                    <div>
                        <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1px;color:#7f8c9a;">{label}</div>
                        <div style="font-size:0.85rem;color:#2c3e50;font-weight:500;">{value}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Accreditation / Awards strip
        st.markdown("""
        <div style="background:linear-gradient(135deg,#1a7a6e,#22a99a);border-radius:14px;padding:1.2rem 2rem;display:flex;align-items:center;justify-content:space-between;color:white;">
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">🏅</div>
                <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin-top:4px;">NABH Accredited</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">🎖️</div>
                <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin-top:4px;">ISO 9001:2015</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">⭐</div>
                <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin-top:4px;">Best Hospital MP 2024</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">🩺</div>
                <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin-top:4px;">1,20,000+ Patients/yr</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">💊</div>
                <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin-top:4px;">NABL Lab</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;">🤖</div>
                <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;opacity:0.8;margin-top:4px;">Robotic Surgery</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Tab 2: Departments ───────────────────────────────────────────────
    with tab2:
        st.markdown(f"### 🏢 Our {len(DEPARTMENTS)} Clinical Departments")
        st.markdown('<p class="page-intro">Each department is led by a senior specialist with decades of expertise.</p>', unsafe_allow_html=True)

        cols = st.columns(3)
        for i, dept in enumerate(DEPARTMENTS):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="dept-card" style="margin-bottom:12px;">
                    <div class="dept-icon">{dept['icon']}</div>
                    <div>
                        <div class="dept-name">{dept['name']}</div>
                        <div class="dept-head">🩺 {dept['head']}</div>
                        <div style="font-size:0.7rem;color:#7f8c9a;margin-top:3px;">📞 Ext. {dept['ext']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            if (i + 1) % 3 == 0 and i + 1 < len(DEPARTMENTS):
                cols = st.columns(3)

    # ── Tab 3: Services ──────────────────────────────────────────────────
    with tab3:
        st.markdown("### ⚕️ Our Clinical Services")
        st.markdown('<p class="page-intro">World-class services available 24×7 for our patients and their families.</p>', unsafe_allow_html=True)

        cols = st.columns(4)
        for i, svc in enumerate(SERVICES):
            with cols[i % 4]:
                st.markdown(f"""
                <div class="service-card" style="margin-bottom:12px;">
                    <div class="service-icon">{svc['icon']}</div>
                    <div class="service-name">{svc['name']}</div>
                    <div class="service-desc">{svc['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
            if (i + 1) % 4 == 0 and i + 1 < len(SERVICES):
                cols = st.columns(4)

    # ── Tab 4: Medical Team ───────────────────────────────────────────────
    with tab4:
        st.markdown("### 👨‍⚕️ Senior Medical Team")
        st.markdown('<p class="page-intro">Our doctors bring decades of clinical expertise and compassionate care.</p>', unsafe_allow_html=True)

        cols = st.columns(5)
        for i, doc in enumerate(DOCTORS):
            initials = "".join([n[0] for n in doc["name"].replace("Dr. ", "").split()[:2]])
            status_color = {"Available": "#27ae60", "In OT": "#e74c3c", "On Leave": "#95a5a6"}.get(doc["status"], "#7f8c9a")
            with cols[i % 5]:
                st.markdown(f"""
                <div class="doctor-card" style="margin-bottom:14px;">
                    <div class="doctor-avatar">{initials}</div>
                    <div class="doctor-name">{doc['name']}</div>
                    <div class="doctor-dept">{doc['dept']}</div>
                    <div class="doctor-qual">{doc['qual']}</div>
                    <div style="font-size:0.72rem;color:#7f8c9a;margin-top:4px;">🎓 {doc['exp']} yrs experience</div>
                    <div style="margin-top:6px;">
                        <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:{status_color};margin-right:5px;"></span>
                        <span style="font-size:0.72rem;color:{status_color};font-weight:600;">{doc['status']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            if (i + 1) % 5 == 0 and i + 1 < len(DOCTORS):
                cols = st.columns(5)
