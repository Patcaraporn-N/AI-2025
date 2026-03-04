import streamlit as st
import time
 
st.title("🌸 Pastel AI Health Screening Project")
# ----------------------------
# ตั้งค่าเพจ
# ----------------------------
st.set_page_config(
    page_title="Pastel AI Health Project",
    page_icon="🌸",
    layout="centered"
)
 
# ----------------------------
# CSS ธีมพาสเทล
# ----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #FDEFF4, #E3F2FD);
}
 
h1, h2, h3 {
    text-align: center;
    color: #5D6D7E;
}
 
.stButton>button {
    background-color: #A8DADC;
    color: black;
    border-radius: 15px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
 
.card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}
 
.footer {
    text-align: center;
    font-size: 12px;
    color: gray;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)
 
# ----------------------------
# Session state คุมหน้า
# ----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
 
# ============================
# หน้าแรก (Landing Page)
# ============================
if st.session_state.page == "home":
 
    st.markdown('<div class="card">', unsafe_allow_html=True)
 
    st.markdown("## 🩺 AI Health Screening Project")
    st.markdown("### 🌸 ระบบคัดกรองสุขภาพเบื้องต้น")
 
 
    st.markdown("""
    💡 **วัตถุประสงค์ของเว็บไซต์นี้**
 
    เว็บไซต์นี้ถูกพัฒนาขึ้นเพื่อการศึกษาในรายวิชา  
    เกี่ยวกับ Data Science และปัญญาประดิษฐ์  
 
    ระบบนี้เป็นเพียงการจำลองการวิเคราะห์อาการเบื้องต้น  
    ไม่มีการจัดเก็บ เผยแพร่ หรือใช้ข้อมูลในเชิงพาณิชย์
    """)
 
    st.info("⚠️ ใช้เพื่อการศึกษาเท่านั้น ไม่สามารถใช้แทนการวินิจฉัยทางการแพทย์ได้")
 
    if st.button("🌷 เข้าสู่ระบบคัดกรองสุขภาพ"):
        st.session_state.page = "app"
        st.rerun()
 
    st.markdown('</div>', unsafe_allow_html=True)
 
# ============================
# หน้าแอพคัดกรอง
# ============================
elif st.session_state.page == "app":
 
    st.title("🌸 ระบบคัดกรองสุขภาพเบื้องต้นด้วย AI")
    st.markdown("ระบบนี้ใช้เพื่อประเมินเบื้องต้นเท่านั้น")
 
    if st.button("← กลับหน้าแรก"):
        st.session_state.page = "home"
        st.rerun()
 
    st.divider()
 
    # ฟอร์ม
    with st.form("health_form"):
 
        col1, col2 = st.columns(2)
 
        with col1:
            age = st.number_input("🎂 อายุ", 1, 120, 25)
            temperature = st.slider("🌡 อุณหภูมิร่างกาย (°C)", 35.0, 42.0, 36.5)
            chronic = st.selectbox("💊 โรคประจำตัว", ["ไม่มี", "เบาหวาน", "ความดัน", "โรคหัวใจ"])
 
        with col2:
            fever = st.checkbox("🤒 มีไข้")
            cough = st.checkbox("😷 ไอ")
            sore_throat = st.checkbox("🗣 เจ็บคอ")
            headache = st.checkbox("🤕 ปวดหัว")
            chest_pain = st.checkbox("❤️ เจ็บหน้าอก")
            fatigue = st.checkbox("😴 อ่อนเพลีย")
 
        other_symptoms = st.text_area("📝 อาการเพิ่มเติม")
 
        submitted = st.form_submit_button("🔍 วิเคราะห์สุขภาพ")
 
    # วิเคราะห์
    def analyze():
        score = 0
        disease = "ยังไม่สามารถระบุได้ชัดเจน"
 
        if fever: score += 1
        if cough: score += 1
        if sore_throat: score += 1
        if headache: score += 1
        if chest_pain: score += 2
        if fatigue: score += 1
        if temperature > 38: score += 1
 
        if fever and cough and sore_throat:
            disease = "ไข้หวัด / ไข้หวัดใหญ่"
 
        if chest_pain and chronic == "โรคหัวใจ":
            disease = "ภาวะเสี่ยงโรคหัวใจ"
 
        risk_percent = min(score * 15, 100)
        return disease, risk_percent
 
    def recommend_specialist(disease):
        if "หัวใจ" in disease:
            return "👨‍⚕️ แพทย์โรคหัวใจ"
        elif "ไข้หวัด" in disease:
            return "👩‍⚕️ แพทย์ทั่วไป"
        else:
            return "👨‍⚕️ แพทย์ทั่วไป"
 
    # แสดงผล
    if submitted:
 
        with st.spinner("🤖 AI กำลังวิเคราะห์..."):
            time.sleep(1.5)
 
        disease, risk = analyze()
        specialist = recommend_specialist(disease)
 
        st.markdown('<div class="card">', unsafe_allow_html=True)
 
        st.subheader("📊 ผลการวิเคราะห์เบื้องต้น")
        st.write(f"🔎 โรคที่เป็นไปได้: **{disease}**")
        st.write(f"{specialist}")
 
        st.write("📈 ระดับความเสี่ยง")
        st.progress(risk)
        st.write(f"{risk}%")
 
        if other_symptoms:
            st.markdown("### 📝 อาการเพิ่มเติม")
            st.write(other_symptoms)
 
        if risk >= 60:
            st.warning("⚠️ อาการค่อนข้างรุนแรง ควรพบแพทย์โดยเร็ว")
        else:
            st.info("🌼 ควรพักผ่อนและสังเกตอาการเพิ่มเติม")
 
        st.markdown("""
        🏥 หากมีอาการเจ็บหน้าอกรุนแรง หายใจลำบาก หน้ามืด  
        ควรไปโรงพยาบาลทันที
        """)
 
        st.markdown('</div>', unsafe_allow_html=True)
 
    st.markdown('<div class="footer">Pastel AI Health Screening | Educational Project Only</div>', unsafe_allow_html=True)

