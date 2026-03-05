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
 