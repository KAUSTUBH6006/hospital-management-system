def get_styles():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --navy:    #0d1b2a;
    --teal:    #1a7a6e;
    --teal-lt: #22a99a;
    --red:     #e74c3c;
    --gold:    #f0a500;
    --white:   #ffffff;
    --off-white: #f4f7f9;
    --text:    #2c3e50;
    --muted:   #7f8c9a;
    --border:  #dce4ec;
}

/* ── Reset & Base ─────────────────────────────────────── */
body, .stApp { background: var(--off-white) !important; color: var(--text) !important; }
h1,h2,h3,h4,h5 { font-family: 'Playfair Display', serif !important; }
p,span,div,label,button { font-family: 'DM Sans', sans-serif !important; }
.stApp > header { display: none !important; }

/* ── Hospital Header ──────────────────────────────────── */
.hospital-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg, var(--navy) 0%, #1b3a5c 100%);
    color: white;
    padding: 1.1rem 2rem;
    border-radius: 0 0 18px 18px;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 24px rgba(13,27,42,0.25);
}
.header-left { display: flex; align-items: center; gap: 1rem; }
.hospital-logo {
    font-size: 2.6rem;
    background: var(--red);
    width: 56px; height: 56px;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 900;
    box-shadow: 0 4px 14px rgba(231,76,60,0.45);
}
.hospital-name { font-size: 1.7rem !important; margin: 0 !important; color: white !important; letter-spacing: 0.5px; }
.hospital-tagline { margin: 0 !important; font-size: 0.78rem !important; color: rgba(255,255,255,0.65); letter-spacing: 1px; text-transform: uppercase; }
.header-right { text-align: right; }
.header-contact { display: flex; flex-direction: column; gap: 3px; }
.header-contact span { font-size: 0.78rem; color: rgba(255,255,255,0.8); }
.header-badge {
    display: inline-block;
    background: var(--gold);
    color: var(--navy);
    font-weight: 700;
    font-size: 0.7rem;
    padding: 2px 10px;
    border-radius: 20px;
    margin-top: 5px;
    letter-spacing: 1px;
}

/* ── Sidebar ──────────────────────────────────────────── */
.stSidebar { background: var(--navy) !important; }
.stSidebar > div { background: var(--navy) !important; }
.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0.5rem 0;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.2rem;
    font-weight: 700;
    color: white;
}
.sidebar-icon {
    background: var(--red);
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    font-weight: 900;
}
.nav-label {
    font-size: 0.65rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    color: rgba(255,255,255,0.4) !important;
    margin: 0.5rem 0 0.3rem 0 !important;
}
.stSidebar .stButton button {
    background: rgba(255,255,255,0.06) !important;
    color: rgba(255,255,255,0.8) !important;
    border: none !important;
    border-radius: 10px !important;
    text-align: left !important;
    padding: 0.55rem 1rem !important;
    margin: 2px 0 !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    transition: all 0.2s !important;
}
.stSidebar .stButton button:hover {
    background: rgba(26,122,110,0.35) !important;
    color: white !important;
}
.sidebar-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin: 6px 0;
}
.stat-item {
    background: rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 10px 8px;
    text-align: center;
}
.stat-item.icu { background: rgba(231,76,60,0.2); }
.stat-num { display: block; font-size: 1.5rem; font-weight: 700; color: var(--teal-lt); font-family: 'Playfair Display', serif !important; }
.stat-item.icu .stat-num { color: #ff8f85; }
.stat-lbl { display: block; font-size: 0.65rem; color: rgba(255,255,255,0.55); margin-top: 2px; text-transform: uppercase; letter-spacing: 0.5px; }
.sidebar-footer { text-align: center; padding: 4px 0; }
.sidebar-footer p { font-size: 0.78rem; color: rgba(255,255,255,0.55); margin: 3px 0 !important; }

/* ── Cards ────────────────────────────────────────────── */
.card {
    background: white;
    border-radius: 16px;
    padding: 1.4rem 1.5rem;
    box-shadow: 0 2px 14px rgba(0,0,0,0.06);
    border: 1px solid var(--border);
    height: 100%;
    transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover { transform: translateY(-3px); box-shadow: 0 6px 22px rgba(0,0,0,0.1); }

.metric-card {
    background: white;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    border-left: 5px solid var(--teal);
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    display: flex;
    align-items: center;
    gap: 1rem;
}
.metric-icon { font-size: 2.2rem; }
.metric-value { font-size: 2rem; font-weight: 700; color: var(--navy); font-family: 'Playfair Display', serif !important; line-height: 1; }
.metric-label { font-size: 0.78rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 3px; }

/* ── Section headings ─────────────────────────────────── */
.section-title {
    font-size: 1.6rem !important;
    font-family: 'Playfair Display', serif !important;
    color: var(--navy);
    border-bottom: 3px solid var(--teal);
    padding-bottom: 6px;
    margin-bottom: 1.2rem !important;
    display: inline-block;
}
.page-intro {
    font-size: 0.88rem;
    color: var(--muted);
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

/* ── Patient Card ─────────────────────────────────────── */
.patient-card {
    background: white;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border: 1px solid var(--border);
    margin-bottom: 0.8rem;
    position: relative;
    overflow: hidden;
}
.patient-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 5px;
    background: var(--teal);
}
.patient-card.critical::before { background: var(--red); }
.patient-card.stable::before { background: #27ae60; }
.patient-card.improving::before { background: var(--gold); }
.badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.badge-critical { background: #fdecea; color: var(--red); }
.badge-stable   { background: #eafaf1; color: #27ae60; }
.badge-improving{ background: #fef9e7; color: #d4a017; }
.badge-post-op  { background: #eaf0fb; color: #2980b9; }
.badge-under-treatment { background: #f4ecf7; color: #8e44ad; }
.badge-icu      { background: #fdecea; color: var(--red); }
.badge-general  { background: #eaf0fb; color: #2980b9; }
.badge-private  { background: #fef9e7; color: #d4a017; }
.badge-available { background: #eafaf1; color: #27ae60; }
.badge-occupied { background: #fdecea; color: var(--red); }

/* ── Room Card ────────────────────────────────────────── */
.room-card {
    background: white;
    border-radius: 14px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    border: 1px solid var(--border);
    text-align: center;
    position: relative;
}
.room-card.available { border-top: 4px solid #27ae60; }
.room-card.occupied  { border-top: 4px solid var(--red); }
.room-number { font-size: 1.2rem; font-weight: 700; color: var(--navy); }
.room-type-tag {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 700;
    color: var(--muted);
    margin-top: 2px;
}

/* ── Info Box ─────────────────────────────────────────── */
.info-box {
    background: linear-gradient(135deg, var(--navy), #1b3a5c);
    color: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(13,27,42,0.2);
}
.info-box h3 { color: var(--gold) !important; margin-bottom: 0.8rem !important; }

/* ── Department Card ──────────────────────────────────── */
.dept-card {
    background: white;
    border-radius: 12px;
    padding: 1rem 1.1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
.dept-icon { font-size: 1.8rem; }
.dept-name { font-weight: 700; font-size: 0.9rem; color: var(--navy); }
.dept-head { font-size: 0.75rem; color: var(--muted); }

/* ── Service Card ─────────────────────────────────────── */
.service-card {
    background: white;
    border-radius: 12px;
    padding: 1.1rem;
    text-align: center;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.service-icon { font-size: 2rem; margin-bottom: 6px; }
.service-name { font-weight: 700; font-size: 0.85rem; color: var(--navy); }
.service-desc { font-size: 0.72rem; color: var(--muted); margin-top: 3px; line-height: 1.4; }

/* ── Doctor Card ──────────────────────────────────────── */
.doctor-card {
    background: white;
    border-radius: 14px;
    padding: 1.2rem;
    border: 1px solid var(--border);
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.doctor-avatar {
    width: 48px; height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--teal), var(--teal-lt));
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    color: white;
    font-weight: 700;
    margin-bottom: 8px;
}
.doctor-name { font-weight: 700; color: var(--navy); font-size: 0.92rem; }
.doctor-dept { font-size: 0.72rem; color: var(--teal); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
.doctor-qual { font-size: 0.72rem; color: var(--muted); margin-top: 4px; }

/* ── Footer ───────────────────────────────────────────── */
.hospital-footer {
    background: linear-gradient(135deg, var(--navy), #1b3a5c);
    color: rgba(255,255,255,0.75);
    border-radius: 18px 18px 0 0;
    padding: 2.5rem 2rem 0;
    margin-top: 3rem;
}
.footer-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid rgba(255,255,255,0.12);
}
.footer-col h4 {
    color: white !important;
    font-size: 1rem !important;
    margin-bottom: 0.7rem !important;
}
.footer-col p { font-size: 0.8rem; margin: 4px 0 !important; }
.footer-bottom {
    text-align: center;
    padding: 1rem 0;
    font-size: 0.75rem;
    color: rgba(255,255,255,0.4);
}

/* ── Streamlit Tweaks ─────────────────────────────────── */
.stTextInput input, .stSelectbox select, .stNumberInput input {
    border-radius: 10px !important;
    border: 1.5px solid var(--border) !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stButton > button {
    background: var(--teal) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    font-size: 0.9rem !important;
}
.stButton > button:hover { background: var(--teal-lt) !important; }
.stSuccess { border-radius: 10px !important; }
div[data-testid="stMetricValue"] { font-family: 'Playfair Display', serif !important; color: var(--navy) !important; }
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }
.stTabs [data-baseweb="tab"] { font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important; }
.stTabs [aria-selected="true"] { color: var(--teal) !important; border-bottom-color: var(--teal) !important; }
</style>
"""
