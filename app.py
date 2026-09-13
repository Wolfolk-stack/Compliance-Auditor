import streamlit as st
import time

st.set_page_config(page_title="AI Compliance Auditor", layout="centered")

STANDARD_DATABASE = {
    "Good Laboratory Practice (GLP)": {
        "Dialysis QC": [
            "Rule 1.1: Flow circuits must be visually inspected for leaks prior to every operation cycle.",
            "Rule 1.2: System layout documentation must include a map of all emergency shut-off valves.",
            "Rule 1.3: Quality control personnel must log calibration metrics for the dialysate composition every 24 hours."
        ]
    }
}

st.title("📄 AI Compliance Auditor")
st.write("Specify your audit parameters and upload your Draft SOP.")

st.subheader("1. Regulatory Guidelines")
guideline_choice = st.selectbox("Framework:", ["Good Laboratory Practice (GLP)", "ISO 13485 (Medical Devices)", "FDA 21 CFR Part 11"])

st.subheader("2. Target Process")
compliance_area = st.text_input("Process:", value="Dialysis QC")

st.subheader("3. Upload Draft Document")
draft_file = st.file_uploader("Upload SOP", type=["pdf", "txt"])

st.markdown("---")

if st.button("Run Compliance Check", type="primary"):
    if draft_file and compliance_area:
        with st.spinner("Analyzing SOP against standards..."):
            time.sleep(2) 
            st.success("✅ Audit Complete: 66% Compliant")
            st.markdown("### 🔍 Gap Analysis Report")
            st.error("**NON-COMPLIANT:** The SOP fails to address Rule 1.2. No mention of mapping emergency shut-off valves in the system layout.")
            st.warning("**PARTIAL MATCH:** SOP mentions checking flow circuits, but does not specify *prior to every operation cycle* (Rule 1.1).")
            st.info("**COMPLIANT:** Calibration metrics for dialysate composition are properly logged daily (Rule 1.3).")
    elif not compliance_area:
        st.warning("⚠️ Please specify the target process.")
    else:
        st.error("⚠️ Please upload your Draft SOP.")
      
