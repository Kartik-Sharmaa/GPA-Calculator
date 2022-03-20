import streamlit as st

st.set_page_config("GPA Calculator")
st.title("Calculate GPA")
st.subheader("Semester GPA Calculater For B.tech(ECE)")
Name = st.text_input("Write your name")
if Name:
    st.write("Hello " + Name + "!")
Sem = st.selectbox("Enter your semester", (1, 2, 3, 4, 5, 6, 7, 8))
st.subheader("Enter Your Marks!")


def Grade(Marks):
    if Marks >= 90:
        grade = 10
    elif Marks >= 75:
        grade = 9
    elif Marks >= 65:
        grade = 8
    elif Marks >= 55:
        grade = 7
    elif Marks >= 50:
        grade = 6
    elif Marks >= 45:
        grade = 5
    elif Marks >= 40:
        grade = 4
    else:
        grade = 0

    return grade

Subs = {}
Labs = {}
GPA = 0
Flag = 0
Credits = 0
col1, col2 = st.columns(2)

if Sem == 1:
    Subs = {"Applied Maths-I": 4, "Applied Physics-I": 3, "Manufacturing Processes": 3, "Electrical Technology": 3, "Human Values": 1, "Fundamentals of Computing": 2, "Applied Chemistry": 3}
    Labs = {"Applied Physics Lab-I": 1, "Elecrical Technology Lab": 1, "Workshop practice": 2, "Engineering Graphics Lab": 2, "FOC Lab": 1, "Applied Chemistry Lab": 1}
    Credits = 27

elif Sem == 2:
    Subs = {"Applied Maths-II": 4, "Applied Physics-II": 3, "Electronic Devices": 3, "Intro To Programming": 3, "Engineering Mechanics": 3, "Communication Skills": 3, "Environmental Studies": 3}
    Labs = {"Applied Physics Lab-II": 1, "Programming Lab": 1, "Electronic Devices Lab": 1, "Engineering Mechanics Lab": 1, "EVS Lab": 1}
    Credits = 27

elif Sem == 3:
    Subs = {"Applied Maths-III": 4, "Analog Electronics-I": 4, "Switching Theory & Logic Design": 4, "Electronic Instruments and Measurements": 4, "Data Structures": 4, "Signals and Systems": 4, }
    Labs = {"Analog Electronics Lab": 1, "STLD Lab": 1, "EIM Lab": 1, "DS Lab": 1, "SS Lab": 1}
    Credits = 29

elif Sem == 4:
    Subs = {"Applied Maths-IV": 4, "Analog Electronics-II": 4, "Network Analysis and Synthesis": 4, "Communication Systems": 4, "Electromagnetic Field Theory": 3, "Computer Organisation and Architecture": 3}
    Labs = {"Applied Maths Lab": 1, "NAS Lab": 1, "CS Lab": 1, "AE-II Lab": 1, "LPA Lab": 1, "NSS": 1}
    Credits = 28

elif Sem == 5:
    Subs = {"Communication skills": 1, "Digital Communication": 4, "Microprocessors and Microcontrollers": 4, "Control Systems": 4, "Digital System Design": 4, "Industrial Management": 3}
    Labs = {"Communication skills Lab": 1, "Digital System Design Lab": 1, "Control Systems Lab": 1, "Microprocessors and Microcontrollers Lab": 1, "Digital Communication Lab": 1, "Industrial Training Workshop": 1}
    Credits = 26

elif Sem == 6:
    Subs = {"Microwave Engineering": 4, "Information Theory and Coding": 4, "Digital Signal Processing": 4, "VLSI design": 4, "Data Communication and Networks": 4, "Antenna and Wave Propagation": 4, }
    Labs = {"Microwave Engineering Lab": 1, "VLSI design Lab": 1, "Digital Signal Processing Lab": 1, "Data Communication and Networks Lab": 1, "Industrial Training Lab": 1}
    Credits = 29
elif Sem == 7:
    Subs = {"Embedded Systems": 4, "OOC": 4, "Wireless Communication": 4, "RF devices and Circuits": 3, "Radar and Navigation": 3}
    Labs = {"OOC Lab": 1, "Embedded Systems Lab": 1, "RF and RN Lab": 1, "Seminar": 1, "Minor Project": 3, "Industrial Training": 1}
    Credits = 26
elif Sem == 8:
    Subs = {"Human Values": 1, "Satellite Communication": 4, "Ad Hoc and Sensor Networks": 3, "ASIC design": 3, "Adaptive Signal Processing": 3}
    Labs = {"Satellite and Antenna Lab": 1, "ASIC or ASP Lab": 1, "Major Project": 8}
    Credits = 24

with col1:
    with st.expander("Theory Subjects"):
        for Sub in Subs:
            Marks = st.number_input("{}:".format(Sub), 0, 100)
            if Marks == 0:
                Flag = 1
            num = Grade(Marks)
            GPA += num * Subs[Sub]

with col2:
    with st.expander("Practical Subjects"):
        for Lab in Labs:
            Marks = st.number_input("{}:".format(Lab), 0, 100)
            if Marks == 0:
                Flag = 1
            num = Grade(Marks)
            GPA += num * Labs[Lab]

if Flag:
    st.warning("You haven't entered the marks of all subjects!")

GPA = GPA / Credits

End = st.button("Submit")

if End:
    txt = "Your GPA: {}".format(str(round(GPA, 2)))
    st.markdown(f"<h3 style='text-align: center; '>{txt}</h3>", unsafe_allow_html=True)
    if GPA >= 8.0:
        st.balloons()
    elif GPA >= 5.0:
        st.info("Try Harder Next Time!")
