import streamlit as st

st.set_page_config(
    page_title="Optical Communication Laboratory",
    page_icon="🔵",
    layout="wide"
)

# ===============================
# STATE
# ===============================
if "mode" not in st.session_state:
    st.session_state.mode = "info"

# ===============================
# CSS
# ===============================
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }

    .header {
        background-color: #1E90FF;
        padding: 35px 20px;
        border-radius: 0px 0px 25px 25px;
    }

    .lab-title {
        font-size: 36px;
        font-weight: 700;
        color: white;
        margin-bottom: 5px;
    }

    .lab-subtitle {
        font-size: 16px;
        color: #eaf3ff;
    }

    .content-box {
        padding: 30px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-top: 25px;
    }

    .stButton>button {
        background-color: #ffffff;
        color: #1E90FF;
        border-radius: 8px;
        border: none;
        padding: 6px 14px;
        font-weight: 600;
    }

    .stButton>button:hover {
        background-color: #eaf3ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===============================
# HEADER
# ===============================
st.markdown('<div class="header">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 4])

with col1:
    st.image("ocl_logo.png.png", width=140)

with col2:
    st.markdown('<div class="lab-title">Optical Communication Laboratory</div>', unsafe_allow_html=True)
    st.markdown('<div class="lab-subtitle">Research • Education • Innovation</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# NAVBAR (TOP)
# ===============================
menu_cols = st.columns(7)

menus = [
    "HOME",
    "ABOUT US",
    "OUR TEAM",
    "OUR ACTIVITY",
    "INFORMATIONS",
    "AI MODE",
    "RESET"
]

clicked = None
for i, m in enumerate(menus):
    if menu_cols[i].button(m):
        clicked = m

if clicked == "AI MODE":
    st.session_state.mode = "ai"

if clicked == "RESET":
    st.session_state.mode = "info"

# ===============================
# CONTENT
# ===============================
st.markdown('<div class="content-box">', unsafe_allow_html=True)

if st.session_state.mode == "info":

    if clicked == "ABOUT US":
        st.header("About Us")
        st.write(
            "Optical Communication Laboratory (OCL) focuses on research, education, "
            "and experimentation in fiber optic communication systems."
        )

    elif clicked == "OUR TEAM":
        st.header("Our Team")
        st.write("Consists of lecturers, researchers, and students in optical communication.")

    elif clicked == "OUR ACTIVITY":
        st.header("Our Activity")
        st.write("Research, practicum sessions, publications, and laboratory development.")

    elif clicked == "INFORMATIONS":
        st.header("Informations")
        st.write("Latest news, schedules, and announcements related to OCL.")

    else:
        st.header("Welcome")
        st.write(
            "Welcome to the Optical Communication Laboratory website.\n\n"
            "Explore research, facilities, and innovations in optical communications."
        )

else:
    st.header("🔍 Optical Signal Quality Detection (Demo)")
    st.write(
        "This is a **demo AI feature**.\n\n"
        "In future development, this section can analyze:\n"
        "- Signal attenuation\n"
        "- Noise impact\n"
        "- BER estimation\n"
        "- Fiber quality assessment"
    )

    st.info("This AI feature is currently illustrative (no model required).")

st.markdown("</div>", unsafe_allow_html=True)
