import streamlit as st
import google.generativeai as genai
import pypdf
import io

# 1. Page Configuration
st.set_page_config(
    page_title="Wolfolk Compliance Auditor",
    page_icon="🐺",
    layout="wide"
)

# Custom styling for a cleaner look
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: bold; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 1.1rem; color: #4B5563; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 2. Brand Header & Logo
col1, col2 = st.columns([1, 5])

with col1:
    # This pulls the logo you just uploaded to GitHub
    st.image("wolfolk_logo.png", width=120)

with col2:
    st.markdown('<div class="main-title">Wolfolk Compliance Auditor</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Automated Gap Analysis & Regulatory Readiness for MSME & Cottage Industries</div>', unsafe_allow_html=True)

# 3. The Pitch & Value Proposition
with st.expander("📖 Why use the Wolfolk Auditor?", expanded=True):
    st.markdown("""
    **Transforming Compliance with AI-Assisted Auditing**
    
    Navigating complex regulatory frameworks can be overwhelming. The Wolfolk Compliance Auditor is designed to make enterprise-grade compliance accessible, fast, and highly accurate.
    
    * 🌍 **Global & Local Alignment:** Cross-reference your Standard Operating Procedures (SOPs) against International (ISO, cGMP), National (BIS, FSSAI), and State requirements.
    * 🤝 **The Perfect Hybrid System:** We combine the exhaustive, high-speed processing of Artificial Intelligence with your human expertise. The AI acts as your vigilant Co-Pilot—flagging missing clauses and blind spots—while you retain total control over the final audit decisions.
    """)

# 4. The Privacy & Trust Guarantee
st.info("🔒 **Strict Confidentiality Guaranteed:** Uploaded documents are processed entirely in-memory and deleted immediately. No data is stored or used for model training.")

st.divider()

# 5. Two-Column Layout for Controls
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("1. Industry & Standards Setup")
    
    industry = st.selectbox("Industry Sector:", [
        "Manufacturing & Packaging (MSME)", 
        "Food, Agro & Cottage Industries",
        "Life Sciences & Medical",
        "General Quality Management"
    ])

    if industry == "Manufacturing & Packaging (MSME)":
        framework_options = [
            "BIS IS 2771 (Corrugated Fibreboard Boxes)",
            "BIS IS 1397 (Kraft Paper for Packing)",
            "ISO 9001:2015 (Quality Management)",
            "ISO 45001:2018 (Occupational Health & Safety)",
            "Other (Specify custom standard below)"
        ]
    elif industry == "Food, Agro & Cottage Industries":
        framework_options = [
            "ISO 22000 (Food Safety Management / HACCP)",
            "FSSAI General Hygiene & Sanitary Practices",
            "BIS IS 10500 (Drinking Water Specifications)",
            "Other (Specify custom standard below)"
        ]
    elif industry == "Life Sciences & Medical":
        framework_options = [
            "Good Laboratory Practice (GLP)",
            "ISO 13485:2016 (Medical Devices)",
            "Good Manufacturing Practice (cGMP)",
            "Other (Specify custom standard below)"
        ]
    else:
        framework_options = [
            "ISO 9001:2015 (Quality Management)",
            "ISO 27001 (Information Security)",
            "Other (Specify custom standard below)"
        ]

    selected_framework = st.selectbox("Compliance Standard:", framework_options)

    if selected_framework == "Other (Specify custom standard below)":
        framework = st.text_input("Enter exact standard (e.g., BIS IS 1848):", "BIS IS 1848")
    else:
        framework = selected_framework

    st.subheader("2. Secure Audit Access")
    user_email = st.text_input("Work / Business Email:", placeholder="manager@factory.com")

with col_right:
    st.subheader("3. Document Intake")
    uploaded_file = st.file_uploader("Upload Draft SOP or Manual (PDF)", type=["pdf"])

    audit_ready = bool(user_email and uploaded_file)
    
    if not user_email and uploaded_file:
        st.warning("Please provide your business email on the left to initiate the audit.")

    if st.button("🚀 Run Compliance Check", disabled=not audit_ready, use_container_width=True):
        st.success("System ready to process document...")
        # Your Gemini processing code will execute here
          
