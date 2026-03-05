import streamlit as st

st.set_page_config(
    page_title="Health Screening",
    page_icon="🩺",
    layout="centered"
)

# ---------- THEME ----------

st.markdown("""
<style>

.stApp{
background-color:#dff3ff;
}

.title{
text-align:center;
color:#0f6f8f;
}

.subtitle{
text-align:center;
color:#3a7f97;
margin-bottom:25px;
}

.box{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0px 2px 8px rgba(0,0,0,0.1);
margin-bottom:20px;
}

.notice{
background:#e9f7ff;
padding:15px;
border-left:6px solid #3aa7c9;
border-radius:8px;
}

.result{
background:#f4fbff;
padding:20px;
border-radius:10px;
border:1px solid #cfeaf5;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("<h1 class='title'>🩺 ระบบคัดกรองอาการเบื้องต้น</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI Health Symptom Screening</p>", unsafe_allow_html=True)

# ---------- NOTICE ----------

st.markdown("""
<div class="notice">

เว็บไซต์นี้ใช้สำหรับ **การศึกษาเท่านั้น**

ผลการวิเคราะห์เป็นเพียงแนวทางด้านสุขภาพเบื้องต้น  
ไม่สามารถใช้แทนการวินิจฉัยจากแพทย์ได้

This website is for educational purposes only.

</div>
""", unsafe_allow_html=True)

# ---------- วิเคราะห์อาการ ----------

def analyze(symptom):

    text = symptom.lower()

    result = ""

    if "ไข้" in text or "ไอ" in text or "เจ็บคอ" in text:
        result += """
**โรคที่อาจเกี่ยวข้อง : ไข้หวัด / ไข้หวัดใหญ่**

คำอธิบาย  
เป็นการติดเชื้อไวรัสในระบบทางเดินหายใจ ทำให้มีไข้ ไอ เจ็บคอ อ่อนเพลีย

อาการที่พบบ่อย  
- มีไข้  
- ไอ  
- เจ็บคอ  
- อ่อนเพลีย

คำแนะนำเบื้องต้น  
พักผ่อน ดื่มน้ำมาก ๆ และสังเกตอาการ หากไข้สูงควรพบแพทย์

---
"""

    if "ปวดหัว" in text or "ปวดศีรษะ" in text:
        result += """
**โรคที่อาจเกี่ยวข้อง : อาการปวดศีรษะจากความเครียด**

คำอธิบาย  
มักเกิดจากการพักผ่อนไม่เพียงพอ ความเครียด หรือการใช้สายตานาน

อาการที่พบบ่อย  
- ปวดศีรษะ  
- ตึงบริเวณศีรษะ  
- รู้สึกล้า

คำแนะนำ  
พักผ่อนให้เพียงพอ และลดการใช้หน้าจอ

---
"""

    if "เวียนหัว" in text or "หน้ามืด" in text:
        result += """
**โรคที่อาจเกี่ยวข้อง : อาการเวียนศีรษะ**

คำอธิบาย  
อาจเกิดจากความดันโลหิตต่ำ พักผ่อนไม่พอ หรือร่างกายอ่อนเพลีย

อาการที่พบบ่อย  
- เวียนศีรษะ  
- หน้ามืด  
- รู้สึกโคลงเคลง

คำแนะนำ  
นั่งพัก ดื่มน้ำ และหลีกเลี่ยงการลุกขึ้นเร็ว

---
"""

    if "กลืน" in text or "กลืนน้ำลาย" in text:
        result += """
**โรคที่อาจเกี่ยวข้อง : คออักเสบ**

คำอธิบาย  
การอักเสบของลำคอจากการติดเชื้อ ทำให้รู้สึกเจ็บเวลาพูดหรือกลืน

อาการที่พบบ่อย  
- เจ็บคอ  
- กลืนลำบาก  
- ระคายคอ

คำแนะนำ  
ดื่มน้ำอุ่น พักเสียง และหลีกเลี่ยงอาหารเผ็ดจัด

---
"""

    if result == "":
        result = """
ไม่สามารถประเมินอาการได้ชัดเจนจากข้อมูลที่กรอก

คำแนะนำ  
- สังเกตอาการเพิ่มเติม  
- พักผ่อนให้เพียงพอ  
- หากมีอาการรุนแรงควรพบแพทย์
"""

    result += "\n⚠️ นี่เป็นเพียงการประเมินเบื้องต้น ไม่ใช่การวินิจฉัยโรค"

    return result


# ---------- INPUT ----------

symptom = st.text_area(
"กรอกอาการของคุณ",
placeholder="เช่น ปวดหัว มีไข้ เวียนหัว กลืนน้ำลายแล้วเจ็บ"
)

# ---------- BUTTON ----------

if st.button("วิเคราะห์อาการ"):

    if symptom == "":
        st.warning("กรุณากรอกอาการก่อน")

    else:

        st.markdown("<div class='result'>", unsafe_allow_html=True)

        st.subheader("ผลการวิเคราะห์เบื้องต้น")

        st.write(analyze(symptom))

        st.markdown("</div>", unsafe_allow_html=True)