import streamlit as st
import pandas as pd
from data import PATIENTS

def render():
    st.markdown('<h2 class="section-title">Patient Management</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p class="page-intro">View, add, and update patient records. '
        'All patient information is managed centrally for quick access.</p>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(["📋  All Patients", "➕  Add Patient", "✏️  Update Patient"])

    # ── Tab 1: All Patients ───────────────────────────────────────────────
    with tab1:
        # Filters
        fc1, fc2, fc3, fc4 = st.columns(4)
        with fc1:
            search = st.text_input("🔍 Search by name / ID", placeholder="e.g. Ramesh or P001")
        with fc2:
            filter_status = st.selectbox("Filter by Status", ["All", "Critical", "Stable", "Improving", "Post-Op", "Under Treatment"])
        with fc3:
            filter_gender = st.selectbox("Filter by Gender", ["All", "Male", "Female"])
        with fc4:
            filter_dept = st.selectbox("Filter by Department", ["All"] + sorted(set(p["dept"] for p in PATIENTS)))

        filtered = PATIENTS[:]
        if search:
            q = search.lower()
            filtered = [p for p in filtered if q in p["name"].lower() or q in p["id"].lower()]
        if filter_status != "All":
            filtered = [p for p in filtered if p["status"] == filter_status]
        if filter_gender != "All":
            filtered = [p for p in filtered if p["gender"] == filter_gender]
        if filter_dept != "All":
            filtered = [p for p in filtered if p["dept"] == filter_dept]

        st.markdown(f"<p style='font-size:0.82rem;color:#7f8c9a;margin-bottom:0.8rem;'>Showing <b>{len(filtered)}</b> of {len(PATIENTS)} patients</p>", unsafe_allow_html=True)

        if not filtered:
            st.info("No patients match the selected filters.")
        else:
            for p in filtered:
                badge_cls = {
                    "Critical": "badge-critical", "Stable": "badge-stable",
                    "Improving": "badge-improving", "Post-Op": "badge-post-op",
                    "Under Treatment": "badge-under-treatment"
                }.get(p["status"], "badge-stable")
                card_cls = {
                    "Critical": "critical", "Stable": "stable",
                    "Improving": "improving"
                }.get(p["status"], "")

                with st.expander(f"🧑‍⚕️  {p['name']}  ·  {p['id']}  ·  {p['room']}  ·  {p['status']}", expanded=False):
                    r1, r2, r3 = st.columns(3)
                    with r1:
                        st.markdown(f"""
                        <div style="line-height:2;">
                            <b>Patient ID:</b> {p['id']}<br>
                            <b>Name:</b> {p['name']}<br>
                            <b>Age:</b> {p['age']} years<br>
                            <b>Gender:</b> {p['gender']}<br>
                            <b>Blood Group:</b> {p['blood']}<br>
                        </div>
                        """, unsafe_allow_html=True)
                    with r2:
                        st.markdown(f"""
                        <div style="line-height:2;">
                            <b>Disease:</b> {p['disease']}<br>
                            <b>Department:</b> {p['dept']}<br>
                            <b>Doctor:</b> {p['doctor']}<br>
                            <b>Room:</b> {p['room']}<br>
                            <b>Admission Date:</b> {p['admission']}<br>
                        </div>
                        """, unsafe_allow_html=True)
                    with r3:
                        st.markdown(f"""
                        <div style="line-height:2;">
                            <b>Contact:</b> {p['contact']}<br>
                            <b>Status:</b> <span class="badge {badge_cls}">{p['status']}</span>
                        </div>
                        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📊 Patient Table View")
        df = pd.DataFrame([{
            "ID": p["id"], "Name": p["name"], "Age": p["age"],
            "Gender": p["gender"], "Blood": p["blood"],
            "Disease": p["disease"], "Dept": p["dept"],
            "Doctor": p["doctor"], "Room": p["room"],
            "Admitted": p["admission"], "Status": p["status"]
        } for p in filtered])
        st.dataframe(df, use_container_width=True, hide_index=True)

    # ── Tab 2: Add Patient ────────────────────────────────────────────────
    with tab2:
        st.markdown("### 🆕 Register New Patient")
        st.markdown("Fill in the details below to add a new patient record.")

        with st.form("add_patient_form"):
            a1, a2, a3 = st.columns(3)
            with a1:
                new_name    = st.text_input("Full Name *", placeholder="e.g. Rahul Sharma")
                new_age     = st.number_input("Age *", min_value=0, max_value=120, value=30)
                new_gender  = st.selectbox("Gender *", ["Male", "Female", "Other"])
                new_blood   = st.selectbox("Blood Group", ["A+","A-","B+","B-","O+","O-","AB+","AB-"])
            with a2:
                new_disease = st.text_input("Disease / Diagnosis *", placeholder="e.g. Hypertension")
                new_dept    = st.selectbox("Department *", sorted(set(p["dept"] for p in PATIENTS)))
                new_doctor  = st.text_input("Attending Doctor *", placeholder="e.g. Dr. Arjun Mehta")
                new_room    = st.text_input("Room Number *", placeholder="e.g. GEN-11")
            with a3:
                new_admission = st.date_input("Admission Date *")
                new_status    = st.selectbox("Status *", ["Stable", "Critical", "Improving", "Post-Op", "Under Treatment"])
                new_contact   = st.text_input("Contact Number *", placeholder="+91-XXXXX-XXXXX")

            submitted = st.form_submit_button("✅ Register Patient", use_container_width=True)
            if submitted:
                if not new_name or not new_disease or not new_contact:
                    st.error("Please fill all required fields (*).")
                else:
                    new_id = f"P{str(len(PATIENTS) + 1).zfill(3)}"
                    st.success(f"✅ Patient **{new_name}** registered successfully with ID **{new_id}**.")
                    st.info("ℹ️ In a live deployment, this record would be saved to the database. This demo uses hard-coded data.")
                    st.markdown(f"""
                    <div class="card" style="margin-top:1rem;">
                        <h4 style="color:#0d1b2a;">📋 New Patient Preview</h4>
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;line-height:2;">
                            <span><b>ID:</b> {new_id}</span>
                            <span><b>Name:</b> {new_name}</span>
                            <span><b>Age:</b> {new_age}</span>
                            <span><b>Gender:</b> {new_gender}</span>
                            <span><b>Blood:</b> {new_blood}</span>
                            <span><b>Disease:</b> {new_disease}</span>
                            <span><b>Doctor:</b> {new_doctor}</span>
                            <span><b>Room:</b> {new_room}</span>
                            <span><b>Status:</b> {new_status}</span>
                            <span><b>Admitted:</b> {new_admission}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # ── Tab 3: Update Patient ─────────────────────────────────────────────
    with tab3:
        st.markdown("### ✏️ Update Existing Patient Record")
        patient_ids = [f"{p['id']} – {p['name']}" for p in PATIENTS]
        selected    = st.selectbox("Select Patient", patient_ids)
        pid         = selected.split(" – ")[0]
        patient     = next(p for p in PATIENTS if p["id"] == pid)

        with st.form("update_patient_form"):
            u1, u2, u3 = st.columns(3)
            with u1:
                u_name    = st.text_input("Full Name", value=patient["name"])
                u_age     = st.number_input("Age", min_value=0, max_value=120, value=patient["age"])
                u_gender  = st.selectbox("Gender", ["Male", "Female", "Other"],
                                         index=["Male","Female","Other"].index(patient["gender"]))
                u_blood   = st.selectbox("Blood Group", ["A+","A-","B+","B-","O+","O-","AB+","AB-"],
                                         index=["A+","A-","B+","B-","O+","O-","AB+","AB-"].index(patient["blood"]))
            with u2:
                u_disease = st.text_input("Disease / Diagnosis", value=patient["disease"])
                u_doctor  = st.text_input("Attending Doctor", value=patient["doctor"])
                u_room    = st.text_input("Room Number", value=patient["room"])
                u_contact = st.text_input("Contact Number", value=patient["contact"])
            with u3:
                statuses = ["Stable", "Critical", "Improving", "Post-Op", "Under Treatment"]
                u_status = st.selectbox("Status", statuses,
                                        index=statuses.index(patient["status"]) if patient["status"] in statuses else 0)
                st.markdown(f"**Current Admission:** {patient['admission']}")
                st.markdown(f"**Department:** {patient['dept']}")

            update_submitted = st.form_submit_button("💾 Save Changes", use_container_width=True)
            if update_submitted:
                st.success(f"✅ Patient **{u_name}** ({pid}) record updated successfully!")
                st.info("ℹ️ In a live deployment, changes would persist to the database.")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Before:**")
                    st.markdown(f"Name: {patient['name']} | Age: {patient['age']} | Status: {patient['status']}")
                with col2:
                    st.markdown("**After:**")
                    st.markdown(f"Name: {u_name} | Age: {u_age} | Status: {u_status}")
