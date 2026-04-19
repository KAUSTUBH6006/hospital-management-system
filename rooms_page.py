import streamlit as st
import pandas as pd
from data import ROOMS, PATIENTS

def render():
    st.markdown('<h2 class="section-title">Room Allocation</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="page-intro">Manage room assignments and monitor bed availability '
        'across ICU, Private, and General wards.</p>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(["🗺️  Room Overview", "🛏️  Allocate Room", "📊  Summary Table"])

    # ── Tab 1: Room Overview ─────────────────────────────────────────────
    with tab1:
        # Filter bar
        fc1, fc2 = st.columns(2)
        with fc1:
            filter_type = st.selectbox("Filter by Room Type", ["All", "ICU", "Private", "General"])
        with fc2:
            filter_status = st.selectbox("Filter by Status", ["All", "Available", "Occupied"])

        filtered = ROOMS[:]
        if filter_type != "All":
            filtered = [r for r in filtered if r["type"] == filter_type]
        if filter_status != "All":
            filtered = [r for r in filtered if r["status"] == filter_status]

        # Group rooms by type
        for room_type in ["ICU", "Private", "General"]:
            type_rooms = [r for r in filtered if r["type"] == room_type]
            if not type_rooms:
                continue

            type_icons = {"ICU": "🔴", "Private": "🟡", "General": "🟢"}
            occ_count  = sum(1 for r in type_rooms if r["status"] == "Occupied")
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:0.7rem;margin:1.2rem 0 0.7rem 0;">
                <span style="font-size:1.5rem;">{type_icons[room_type]}</span>
                <h3 style="font-family:'Playfair Display',serif;color:#0d1b2a;margin:0;font-size:1.15rem;">
                    {room_type} Ward
                </h3>
                <span style="font-size:0.78rem;color:#7f8c9a;background:#f4f7f9;padding:3px 10px;border-radius:20px;">
                    {occ_count}/{len(type_rooms)} occupied
                </span>
            </div>
            """, unsafe_allow_html=True)

            cols = st.columns(5)
            for i, room in enumerate(type_rooms):
                patient_name = "—"
                if room["patient"]:
                    pt = next((p for p in PATIENTS if p["id"] == room["patient"]), None)
                    patient_name = pt["name"] if pt else room["patient"]

                is_occ   = room["status"] == "Occupied"
                card_cls = "occupied" if is_occ else "available"
                rate_str = f"₹{room['rate']:,}/day"

                with cols[i % 5]:
                    st.markdown(f"""
                    <div class="room-card {card_cls}" style="margin-bottom:12px;">
                        <div class="room-number">{room['room_no']}</div>
                        <div class="room-type-tag">{room['type']} · Floor {room['floor']}</div>
                        <hr style="margin:8px 0;border-color:#eee;">
                        <div style="font-size:0.72rem;color:{'#e74c3c' if is_occ else '#27ae60'};font-weight:700;margin-bottom:4px;">
                            {'🔴 Occupied' if is_occ else '🟢 Available'}
                        </div>
                        <div style="font-size:0.7rem;color:#7f8c9a;">
                            {'👤 ' + patient_name if is_occ else '—'}
                        </div>
                        <div style="font-size:0.68rem;color:#95a5a6;margin-top:4px;">
                            👩‍⚕️ {room['nurse']}
                        </div>
                        <div style="font-size:0.72rem;font-weight:700;color:#0d1b2a;margin-top:5px;">{rate_str}</div>
                    </div>
                    """, unsafe_allow_html=True)
                if (i + 1) % 5 == 0 and i + 1 < len(type_rooms):
                    cols = st.columns(5)

    # ── Tab 2: Allocate Room ─────────────────────────────────────────────
    with tab2:
        st.markdown("### 🛏️ Room Allocation / De-allocation")
        col_l, col_r = st.columns(2)

        with col_l:
            st.markdown("#### ➕ Assign Room to Patient")
            avail_rooms  = [r for r in ROOMS if r["status"] == "Available"]
            unassigned_pts = [p for p in PATIENTS if not any(r["patient"] == p["id"] for r in ROOMS if r["status"] == "Occupied")]

            if not avail_rooms:
                st.warning("⚠️ No rooms currently available.")
            else:
                with st.form("allocate_form"):
                    sel_room = st.selectbox(
                        "Select Available Room",
                        [f"{r['room_no']} ({r['type']}, Floor {r['floor']}, ₹{r['rate']:,}/day)" for r in avail_rooms]
                    )
                    sel_patient = st.selectbox(
                        "Select Patient",
                        [f"{p['id']} – {p['name']}" for p in PATIENTS]
                    )
                    alloc_btn = st.form_submit_button("✅ Assign Room", use_container_width=True)
                    if alloc_btn:
                        room_no  = sel_room.split(" ")[0]
                        pt_id    = sel_patient.split(" – ")[0]
                        pt_name  = sel_patient.split(" – ")[1]
                        st.success(f"✅ Room **{room_no}** successfully assigned to **{pt_name}** ({pt_id}).")
                        st.info("ℹ️ In a live system, this would update the database in real time.")

        with col_r:
            st.markdown("#### ➖ Discharge Patient / Free Room")
            occupied_rooms = [r for r in ROOMS if r["status"] == "Occupied"]
            if not occupied_rooms:
                st.info("No occupied rooms to discharge.")
            else:
                with st.form("discharge_form"):
                    occ_options = []
                    for r in occupied_rooms:
                        pt = next((p for p in PATIENTS if p["id"] == r["patient"]), None)
                        pt_name = pt["name"] if pt else r["patient"]
                        occ_options.append(f"{r['room_no']} – {pt_name} ({r['patient']})")

                    sel_occ = st.selectbox("Select Occupied Room", occ_options)
                    discharge_btn = st.form_submit_button("🚪 Mark as Discharged", use_container_width=True)
                    if discharge_btn:
                        room_no = sel_occ.split(" – ")[0]
                        st.success(f"✅ Room **{room_no}** is now marked as Available.")
                        st.info("ℹ️ In a live system, patient would be discharged and billing finalised.")

    # ── Tab 3: Summary Table ─────────────────────────────────────────────
    with tab3:
        st.markdown("### 📊 Complete Room List")
        rows = []
        for r in ROOMS:
            pt = next((p for p in PATIENTS if p["id"] == r["patient"]), None)
            rows.append({
                "Room No":  r["room_no"],
                "Type":     r["type"],
                "Floor":    r["floor"],
                "Capacity": r["capacity"],
                "Status":   r["status"],
                "Patient":  pt["name"] if pt else "—",
                "Nurse":    r["nurse"],
                "Rate/Day": f"₹{r['rate']:,}",
            })
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Summary metrics
        sm1, sm2, sm3, sm4 = st.columns(4)
        total_rooms = len(ROOMS)
        total_occ   = sum(1 for r in ROOMS if r["status"] == "Occupied")
        total_avail = sum(1 for r in ROOMS if r["status"] == "Available")
        occ_pct     = round((total_occ / total_rooms) * 100, 1)

        for col, label, val in [
            (sm1, "Total Rooms",    total_rooms),
            (sm2, "Occupied",       total_occ),
            (sm3, "Available",      total_avail),
            (sm4, "Occupancy Rate", f"{occ_pct}%"),
        ]:
            with col:
                st.metric(label, val)
