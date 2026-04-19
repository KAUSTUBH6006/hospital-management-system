import streamlit as st
from data import PATIENTS, ROOMS, HOSPITAL_INFO, DOCTORS, DEPARTMENTS

def render():
    st.markdown('<h2 class="section-title">Dashboard Overview</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="page-intro">Welcome to MediCare Plus Hospital Management System. '
        'Here is a real-time snapshot of hospital operations.</p>',
        unsafe_allow_html=True
    )

    # ── KPI Metrics ──────────────────────────────────────────────────────────
    total_patients  = len(PATIENTS)
    occupied_rooms  = sum(1 for r in ROOMS if r["status"] == "Occupied")
    available_rooms = sum(1 for r in ROOMS if r["status"] == "Available")
    icu_active      = sum(1 for r in ROOMS if r["type"] == "ICU" and r["status"] == "Occupied")
    critical_pts    = sum(1 for p in PATIENTS if p["status"] == "Critical")
    total_doctors   = len(DOCTORS)

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    metrics = [
        (c1, "👥", total_patients,  "Total Patients", "#1a7a6e"),
        (c2, "🛏️", occupied_rooms, "Occupied Rooms",  "#e74c3c"),
        (c3, "✅", available_rooms, "Available Rooms", "#27ae60"),
        (c4, "🚨", icu_active,      "ICU Active",      "#e74c3c"),
        (c5, "⚠️", critical_pts,   "Critical Cases",  "#e67e22"),
        (c6, "👨‍⚕️", total_doctors,  "Doctors on Staff","#2980b9"),
    ]
    for col, icon, val, label, color in metrics:
        with col:
            st.markdown(f"""
            <div class="metric-card" style="border-left-color:{color}">
                <div class="metric-icon">{icon}</div>
                <div>
                    <div class="metric-value">{val}</div>
                    <div class="metric-label">{label}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Room Summary Bar ─────────────────────────────────────────────────────
    icu_total   = sum(1 for r in ROOMS if r["type"] == "ICU")
    pvt_total   = sum(1 for r in ROOMS if r["type"] == "Private")
    gen_total   = sum(1 for r in ROOMS if r["type"] == "General")
    icu_occ     = sum(1 for r in ROOMS if r["type"] == "ICU"     and r["status"] == "Occupied")
    pvt_occ     = sum(1 for r in ROOMS if r["type"] == "Private" and r["status"] == "Occupied")
    gen_occ     = sum(1 for r in ROOMS if r["type"] == "General" and r["status"] == "Occupied")

    st.markdown('<h3 style="font-family:Playfair Display,serif;color:#0d1b2a;font-size:1.2rem;">🏨 Room Occupancy at a Glance</h3>', unsafe_allow_html=True)
    rc1, rc2, rc3 = st.columns(3)
    for col, label, occ, total, color, icon in [
        (rc1, "ICU Rooms",     icu_occ, icu_total, "#e74c3c", "🔴"),
        (rc2, "Private Rooms", pvt_occ, pvt_total, "#f0a500", "🟡"),
        (rc3, "General Rooms", gen_occ, gen_total, "#1a7a6e", "🟢"),
    ]:
        pct = int((occ / total) * 100) if total else 0
        with col:
            st.markdown(f"""
            <div class="card">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.7rem;">
                    <span style="font-weight:700;color:#0d1b2a;">{icon} {label}</span>
                    <span style="font-size:0.8rem;color:#7f8c9a;">{occ}/{total} occupied</span>
                </div>
                <div style="height:10px;background:#eee;border-radius:6px;overflow:hidden;">
                    <div style="height:100%;width:{pct}%;background:{color};border-radius:6px;transition:width 0.5s;"></div>
                </div>
                <div style="text-align:right;font-size:0.75rem;color:{color};margin-top:4px;font-weight:700;">{pct}%</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Patient Status Distribution + Recent Patients ─────────────────────
    left, right = st.columns([1, 1.6])

    with left:
        st.markdown('<h3 style="font-family:Playfair Display,serif;color:#0d1b2a;font-size:1.2rem;">📊 Patient Status</h3>', unsafe_allow_html=True)
        statuses = {}
        for p in PATIENTS:
            statuses[p["status"]] = statuses.get(p["status"], 0) + 1
        colors_map = {
            "Critical": "#e74c3c", "Stable": "#27ae60",
            "Improving": "#f0a500", "Post-Op": "#2980b9",
            "Under Treatment": "#8e44ad"
        }
        for status, count in sorted(statuses.items(), key=lambda x: -x[1]):
            color = colors_map.get(status, "#95a5a6")
            pct = int((count / total_patients) * 100)
            st.markdown(f"""
            <div style="margin-bottom:10px;">
                <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                    <span style="font-size:0.82rem;font-weight:600;color:#2c3e50;">{status}</span>
                    <span style="font-size:0.8rem;color:#7f8c9a;">{count} patient{'s' if count>1 else ''}</span>
                </div>
                <div style="height:8px;background:#eee;border-radius:4px;overflow:hidden;">
                    <div style="height:100%;width:{pct}%;background:{color};border-radius:4px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<h3 style="font-family:Playfair Display,serif;color:#0d1b2a;font-size:1.2rem;">🆕 Recent Admissions</h3>', unsafe_allow_html=True)
        sorted_pts = sorted(PATIENTS, key=lambda x: x["admission"], reverse=True)[:5]
        for p in sorted_pts:
            badge_cls = {
                "Critical": "badge-critical", "Stable": "badge-stable",
                "Improving": "badge-improving", "Post-Op": "badge-post-op",
                "Under Treatment": "badge-under-treatment"
            }.get(p["status"], "badge-stable")
            st.markdown(f"""
            <div class="patient-card {p['status'].lower().replace(' ','-').replace('-op','').replace('under-treatment','')}">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div>
                        <div style="font-weight:700;color:#0d1b2a;font-size:0.95rem;">{p['name']} <span style="color:#7f8c9a;font-weight:400;font-size:0.8rem;">· {p['id']}</span></div>
                        <div style="font-size:0.78rem;color:#7f8c9a;margin-top:2px;">{p['disease']} · {p['room']} · {p['doctor']}</div>
                    </div>
                    <div style="text-align:right;">
                        <span class="badge {badge_cls}">{p['status']}</span>
                        <div style="font-size:0.7rem;color:#7f8c9a;margin-top:4px;">{p['admission']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Doctors On Duty ───────────────────────────────────────────────────
    st.markdown('<h3 style="font-family:Playfair Display,serif;color:#0d1b2a;font-size:1.2rem;">👨‍⚕️ Doctors On Duty Today</h3>', unsafe_allow_html=True)
    cols = st.columns(5)
    for i, doc in enumerate(DOCTORS):
        initials = "".join([n[0] for n in doc["name"].replace("Dr. ", "").split()[:2]])
        status_color = {"Available": "#27ae60", "In OT": "#e74c3c", "On Leave": "#95a5a6"}.get(doc["status"], "#7f8c9a")
        with cols[i % 5]:
            st.markdown(f"""
            <div class="doctor-card">
                <div class="doctor-avatar">{initials}</div>
                <div class="doctor-name">{doc['name']}</div>
                <div class="doctor-dept">{doc['dept']}</div>
                <div class="doctor-qual">{doc['qual']}</div>
                <div style="margin-top:6px;">
                    <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:{status_color};margin-right:5px;"></span>
                    <span style="font-size:0.72rem;color:{status_color};font-weight:600;">{doc['status']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if (i + 1) % 5 == 0 and i + 1 < len(DOCTORS):
            cols = st.columns(5)
