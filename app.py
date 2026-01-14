import streamlit as st

# ========================
# CONFIG
# ========================
st.set_page_config(
    page_title="Optical Communication Laboratory",
    layout="wide"
)

# ========================
# STATE MODE
# ========================
if "mode" not in st.session_state:
    st.session_state.mode = "OCL"


# ========================
# CSS MODE OCL
# ========================
def ocl_style():
    st.markdown("""
    <style>
    .stApp {
        background-color: white;
    }

    .ocl-header {
        background: linear-gradient(135deg, #1E90FF, #187bcd);
        padding: 40px 20px;
        border-radius: 0 0 30px 30px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }

    .ocl-title {
        font-size: 38px;
        font-weight: 800;
        margin-top: 10px;
    }

    .ocl-subtitle {
        font-size: 18px;
        opacity: 0.9;
    }

    .menu-box {
        background-color: #f7f9fc;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)


# ========================
# MODE SWITCH BUTTON
# ========================
col1, col2 = st.columns([8, 2])

with col2:
    if st.session_state.mode == "OCL":
        if st.button("🔁 Default Mode"):
            st.session_state.mode = "DEFAULT"
            st.rerun()
    else:
        if st.button("🎨 OCL Mode"):
            st.session_state.mode = "OCL"
            st.rerun()

# ========================
# APPLY STYLE
# ========================
if st.session_state.mode == "OCL":
    ocl_style()

# ========================
# HEADER
# ========================
if st.session_state.mode == "OCL":
    st.markdown("""
    <div class="ocl-header">
        <img src="ocl_logo.png.png" width="160">
        <div class="ocl-title">Optical Communication Laboratory</div>
        <div class="ocl-subtitle">Research • Education • Innovation</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.image("ocl_logo.png.png", width=160)
    st.title("Optical Communication Laboratory")
    st.write("Research • Education • Innovation")

# ========================
# NAVIGATION
# ========================
menu = st.tabs([
    "🏠 Home",
    "👥 About Us",
    "🧑‍🔬 Our Team",
    "🔬 Our Activity",
    "ℹ️ Informations",
    "🤖 AI Feature"
])

# ========================
# CONTENT
# ========================
with menu[0]:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.write("Welcome to the Optical Communication Laboratory web platform.")
    st.markdown("</div>", unsafe_allow_html=True)

with menu[1]:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.write("OCL focuses on optical fiber systems, photonics, and communication research.")
    st.markdown("</div>", unsafe_allow_html=True)

with menu[2]:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.write("Our team consists of lecturers, researchers, and students.")
    st.markdown("</div>", unsafe_allow_html=True)

with menu[3]:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.write("Laboratory experiments, research projects, and student practicums.")
    st.markdown("</div>", unsafe_allow_html=True)

with menu[4]:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.write("Announcements, schedules, and lab regulations.")
    st.markdown("</div>", unsafe_allow_html=True)

with menu[5]:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.subheader("Optical Signal Quality Detection (Demo)")
    snr = st.slider("SNR (dB)", 0, 40, 25)
    if snr >= 25:
        st.success("✅ Signal Quality: GOOD")
    elif snr >= 15:
        st.warning("⚠️ Signal Quality: FAIR")
    else:
        st.error("❌ Signal Quality: POOR")
    st.markdown("</div>", unsafe_allow_html=True)
