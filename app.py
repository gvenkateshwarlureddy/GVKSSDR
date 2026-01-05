import streamlit as st
from modules.video_generator import generate_video
from modules.resume_parser import extract_resume_data
from modules.resume_rewriter import rewrite_resume
from modules.resume_exporter import export_docx, export_pdf

st.set_page_config(page_title="GVKSSDR Smart Desk", layout="wide")
st.title("GVKSSDR SMART DESK")

tab1, tab2 = st.tabs(["🎥 Video Generator", "📄 Resume Engine"])

# VIDEO TAB
with tab1:
    script = st.text_area("Paste Video Script")
    if st.button("Generate Video"):
        generate_video(script, "content/bg_videos", "content/output_videos/video.mp4")
        st.success("Video generated successfully")

# RESUME TAB
with tab2:
    raw_resume = st.text_area("Paste Raw Resume", height=300)
    country = st.selectbox("Target Country", ["Luxembourg", "Germany", "Poland", "Czech Republic"])

    if st.button("Process Resume"):
        data = extract_resume_data(raw_resume)
        rewritten = rewrite_resume(data, raw_resume, country)

        st.subheader("Extracted Data")
        st.json(data)

        st.subheader("Rewritten ATS Resume")
        st.text_area("", rewritten, height=400)

    if st.button("Export DOCX"):
            export_docx(rewritten, "resumes/rewritten/resume.docx")

    if st.button("Export PDF"):
            export_pdf(rewritten, "resumes/rewritten/resume.pdf")
