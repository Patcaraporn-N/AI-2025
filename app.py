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
 
    # -------- SVG การ์ตูนหมอ --------
    st.markdown("""
    <div style="text-align:center;">
    <svg width="150" height="150" viewBox="0 0 200 200">
        <circle cx="100" cy="80" r="40" fill="#FFE0E9"/>
        <circle cx="85" cy="70" r="5" fill="#5D6D7E"/>
        <circle cx="115" cy="70" r="5" fill="#5D6D7E"/>
        <path d="M85 95 Q100 110 115 95" stroke="#5D6D7E" stroke-width="3" fill="none"/>
        <rect x="60" y="120" width="80" height="50" rx="15" fill="#FFFFFF" stroke="#A8DADC" stroke-width="3"/>
        <line x1="100" y1="135" x2="100" y2="155" stroke="#FFAFCC" stroke-width="4"/>
        <line x1="90" y1="145" x2="110" y2="145" stroke="#FFAFCC" stroke-width="4"/>
    </svg>
    </div>
    """, unsafe_allow_html=True)
 
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

import streamlit as st
 
# ---------------- PAGE ----------------
 
st.set_page_config(
    page_title="AI Health Screening",
    page_icon="🩺",
    layout="centered"
)
 
# ---------------- STYLE ----------------
 
st.markdown("""
<style>
 
.stApp{
background-color:#eaf4f8;
}
 
.title{
text-align:center;
color:#0b6e79;
}
 
.subtitle{
text-align:center;
color:#3c8d96;
}
 
.notice{
background:#e6f6f8;
padding:18px;
border-radius:10px;
border-left:6px solid #2aa5a0;
margin-bottom:20px;
}
 
.privacy{
background:#f4fbff;
padding:12px;
border-radius:8px;
font-size:14px;
margin-bottom:20px;
}
 
.result{
background:#f2fbff;
padding:20px;
border-radius:10px;
border:1px solid #cce7ef;
margin-top:20px;
}
 
button {
background-color:#0b7285 !important;
color:white !important;
border-radius:8px !important;
height:45px !important;
font-size:16px !important;
border:none !important;
}
 
</style>
""", unsafe_allow_html=True)
 
# ---------------- HEADER ----------------
 
st.markdown("<h1 class='title'>👩‍⚕️ ระบบคัดกรองโรคเบื้องต้น</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI Health Symptom Screening System</p>", unsafe_allow_html=True)
 
# ---------------- NOTICE ----------------
 
st.markdown("""
<div class="notice">
 
**ประกาศ / Notice**
 
เว็บไซต์นี้จัดทำขึ้นเพื่อใช้ในการศึกษาและสาธิตระบบเท่านั้น  
ผลลัพธ์เป็นเพียงการประเมินอาการเบื้องต้น ไม่สามารถใช้แทนการวินิจฉัยของแพทย์ได้  
 
หากมีอาการรุนแรงควรพบแพทย์
 
This website is for educational purposes only.
 
</div>
""", unsafe_allow_html=True)
 
# ---------------- PRIVACY ----------------
 
st.markdown("""
<div class="privacy">
 
🔒 **นโยบายความเป็นส่วนตัว**
 
ระบบนี้ไม่บันทึกข้อมูลผู้ใช้งาน  
อาการที่กรอกจะใช้เพื่อการวิเคราะห์ในหน้านี้เท่านั้น
 
</div>
""", unsafe_allow_html=True)
 
# ---------------- INPUT ----------------
 
symptom = st.text_area(
"กรอกอาการของคุณ",
placeholder="ตัวอย่าง: ปวดหัว มีไข้ เวียนหัว เจ็บคอ กลืนน้ำลายแล้วเจ็บ เหนื่อยง่าย..."
)
 
# ---------------- DATABASE ----------------
 
disease_db = {
 
"ไข้หวัด":{
"symptoms":["ไข้","ไอ","เจ็บคอ","คัดจมูก","น้ำมูก","จาม"],
"doctor":"แพทย์ทั่วไป",
"advice":"พักผ่อน ดื่มน้ำมาก ๆ และหลีกเลี่ยงอากาศเย็น"
},
 
"ไข้หวัดใหญ่":{
"symptoms":["ไข้สูง","ปวดเมื่อย","หนาวสั่น","อ่อนเพลีย","ไอ"],
"doctor":"แพทย์ทั่วไป",
"advice":"พักผ่อนมาก ๆ ดื่มน้ำ และหากไข้สูงควรพบแพทย์"
},
 
"คออักเสบ":{
"symptoms":["เจ็บคอ","กลืนลำบาก","กลืนน้ำลายเจ็บ"],
"doctor":"แพทย์หูคอจมูก",
"advice":"หลีกเลี่ยงอาหารเผ็ดและเครื่องดื่มเย็น"
},
 
"ไมเกรน":{
"symptoms":["ปวดหัว","คลื่นไส้","แพ้แสง","เวียนหัว"],
"doctor":"แพทย์ระบบประสาท",
"advice":"พักผ่อนในที่เงียบ ลดการใช้สายตา"
},
 
"กระเพาะอาหารอักเสบ":{
"symptoms":["ปวดท้อง","จุกท้อง","แสบท้อง","คลื่นไส้"],
"doctor":"แพทย์ระบบทางเดินอาหาร",
"advice":"หลีกเลี่ยงอาหารรสจัดและกาแฟ"
},
 
"อาหารเป็นพิษ":{
"symptoms":["ท้องเสีย","ปวดท้อง","อาเจียน","คลื่นไส้"],
"doctor":"แพทย์ทั่วไป",
"advice":"ดื่มเกลือแร่และพักผ่อน"
},
 
"กรดไหลย้อน":{
"symptoms":["แสบร้อนหน้าอก","เรอเปรี้ยว","จุกคอ"],
"doctor":"แพทย์ระบบทางเดินอาหาร",
"advice":"หลีกเลี่ยงอาหารมันและไม่ควรนอนทันทีหลังทานอาหาร"
},
 
"ไซนัสอักเสบ":{
"symptoms":["ปวดหัว","คัดจมูก","น้ำมูก","ปวดหน้า"],
"doctor":"แพทย์หูคอจมูก",
"advice":"พักผ่อนและหลีกเลี่ยงฝุ่น"
},
 
"ความดันต่ำ":{
"symptoms":["เวียนหัว","หน้ามืด","อ่อนแรง"],
"doctor":"แพทย์ทั่วไป",
"advice":"ดื่มน้ำมากขึ้นและพักผ่อน"
},
 
"หัวใจขาดเลือด":{
"symptoms":["แน่นหน้าอก","หายใจลำบาก","เหนื่อยง่าย"],
"doctor":"แพทย์โรคหัวใจ",
"advice":"ควรพบแพทย์ทันที"
},
 
"ไส้ติ่งอักเสบ":{
"symptoms":["ปวดท้องขวา","คลื่นไส้","ไข้"],
"doctor":"ศัลยแพทย์",
"advice":"ควรพบแพทย์ทันที"
},
 
"ภูมิแพ้":{
"symptoms":["จาม","คัดจมูก","น้ำมูก","คันตา"],
"doctor":"แพทย์ทั่วไป",
"advice":"หลีกเลี่ยงฝุ่นและสารก่อภูมิแพ้"
},
 
"หลอดลมอักเสบ":{
"symptoms":["ไอ","หายใจลำบาก","เจ็บหน้าอก"],
"doctor":"แพทย์ระบบทางเดินหายใจ",
"advice":"พักผ่อนและหลีกเลี่ยงควัน"
},
 
"อ่อนเพลีย":{
"symptoms":["เหนื่อยง่าย","อ่อนแรง","ง่วง"],
"doctor":"แพทย์ทั่วไป",
"advice":"พักผ่อนให้เพียงพอ"
}
 
}
 
# ---------------- ANALYSIS ----------------
 
def analyze(symptom):
 
    s = symptom.lower()
 
    result = []
 
    for disease,data in disease_db.items():
 
        score = 0
 
        for sym in data["symptoms"]:
            if sym in s:
                score += 1
 
        if score > 0:
            result.append((disease,score,data))
 
    result.sort(key=lambda x:x[1],reverse=True)
 
    return result[:3]
 
# ---------------- BUTTON ----------------
 
if st.button("🔍 วิเคราะห์อาการ"):
 
    if symptom.strip()=="":
        st.warning("กรุณากรอกอาการก่อน")
 
    else:
 
        results = analyze(symptom)
 
        st.markdown("<div class='result'>", unsafe_allow_html=True)
 
        st.subheader("📋 ผลการประเมินเบื้องต้น")
 
        if results:
 
            for disease,score,data in results:
 
                st.write("###",disease)
 
                st.write("**อาการที่เกี่ยวข้อง:**")
                st.write(", ".join(data["symptoms"]))
 
                st.write("**คำแนะนำเบื้องต้น:**")
                st.write(data["advice"])
 
                st.write("**แพทย์ที่แนะนำ:**",data["doctor"])
 
                st.write("---")
 
        else:
 
            st.write("ไม่สามารถประเมินโรคจากอาการที่กรอกได้")
 
        st.info("นี่เป็นเพียงการประเมินเบื้องต้น ไม่ใช่การวินิจฉัยโรค")
 
        st.markdown("</div>", unsafe_allow_html=True)
 
# ---------------- FOOTER ----------------
 
st.markdown("---")
st.caption("AI Health Screening | Student Project")
 
