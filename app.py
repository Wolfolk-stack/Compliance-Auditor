import streamlit as st
import google.generativeai as genai
import PyPDF2

# Securely load the API key we just saved in Streamlit Settings
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("📄 AI Compliance Auditor")
st.markdown("Specify your audit parameters and upload your Draft SOP.")

st.subheader("1. Regulatory Guidelines")
framework = st.selectbox("Framework:", ["Good Laboratory Practice (GLP)", "ISO 9001", "FDA 21 CFR Part 11"])

st.subheader("2. Target Process")
process = st.text_input("Process:", "Dialysis QC")

st.subheader("3. Upload Draft Document")
uploaded_file = st.file_uploader("Upload SOP", type=["pdf"])

if st.button("Run Compliance Check"):
    if uploaded_file is not None:
        with st.spinner("AI is reading and analyzing the document..."):
            try:
                # Extract text from the uploaded PDF
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                document_text = ""
                for page in pdf_reader.pages:
                    document_text += page.extract_text() + "\n"

                # Initialize the Google Gemini AI Model
                model = genai.GenerativeModel('gemini-pro')
                
                # Tell the AI exactly what its job is
                prompt = f"""
                You are an expert regulatory compliance auditor.
                Review the following Standard Operating Procedure (SOP) for the process: '{process}'.
                Evaluate its compliance against the '{framework}' regulatory framework.
                
                Provide a structured Gap Analysis Report including:
                1. An overall Compliance Score (Percentage).
                2. NON-COMPLIANT areas (critical gaps or missing elements).
                3. PARTIAL MATCH areas (needs improvement or more detail).
                4. COMPLIANT areas (well-defined and accurate).
                
                Document Text to Analyze:
                {document_text}
                """

                # Send the prompt to the AI and get the report back
                response = model.generate_content(prompt)
                
                # Display the AI's report on the website
                st.success("Audit Complete!")
                st.subheader("🔍 Gap Analysis Report")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload a PDF document first.")
