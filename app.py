import streamlit as st
import os

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Optical Communication Laboratory",
    layout="wide",
)

# ======================
# STATE
# ======================
if "page" not in st.session_state:
    st.session_state.page = "home"

# ======================
# GLOBAL CSS
# ======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');

* { font-family: 'Inter', sans-serif; }

html, body, [class*="css"] {
    background-color: #020617;
}

/* HEADER */
.header {
    background: linear-gradient(135deg, #1E90FF, #2563EB);
    padding: 30px 50px;
    border-bottom-left-radius: 50px;
    border-bottom-right-radius: 50px;
}

/* NAV BUTTON */
button[kind="secondary"] {
    background: transparent !important;
    border: none !important;
    color: white !important;
    font-weight: 600;
}

button[kind="secondary"]:hover {
    color: #DBEAFE !important;
}

/* HERO */
.hero-wrapper {
    display: flex;
    height: 88vh;
}

.hero-left {
    width: 50%;
    padding: 80px;
    background: linear-gradient(135deg, #1E90FF, #2563EB);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.hero-title {
    font-size: 56px;
    font-weight: 900;
    line-height: 1.1;
}

.hero-subtitle {
    font-size: 18px;
    margin-top: 20px;
    max-width: 520px;
    opacity: 0.95;
}

.hero-btn {
    margin-top: 35px;
}

.hero-btn a {
    text-decoration: none;
    background: white;
    color: #1E3A8A;
    padding: 14px 36px;
    border-radius: 40px;
    font-weight: 700;
}

.hero-right {
    width: 50%;
    background: #020617;
    display: flex;
    align-items: center;
    justify-content: center;
}

.glass-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    padding: 40px;
    border-radius: 22px;
    color: white;
    max-width: 420px;
    border: 1px solid rgba(255,255,255,0.2);
}

.glass-card h3 {
    color: #38BDF8;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown('<div class="header">', unsafe_allow_html=True)

col1, col2 = st.columns([2, 6])

with col1:
    if os.path.exists("ocl_logo.png.png"):
        st.image("ocl_logo.png.png", width=160)

with col2:
    nav1, nav2, nav3, nav4 = st.columns([1,1,1,1])
    with nav1:
        if st.button("Home"):
            st.session_state.page = "home"
    with nav2:
        if st.button("About Us"):
            st.session_state.page = "about"
    with nav3:
        if st.button("Our Team"):
            st.session_state.page = "team"
    with nav4:
        if st.button("Activity"):
            st.session_state.page = "activity"

st.markdown('</div>', unsafe_allow_html=True)

# ======================
# CONTENT
# ======================
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero-wrapper">
        <div class="hero-left">
            <div class="hero-title">
                Lighting the Future<br>of Connectivity
            </div>
            <div class="hero-subtitle">
                Optical Communication Laboratory focuses on fiber optics,
                photonics, and high-speed communication technologies
                for education, research, and innovation.
            </div>
            <div class="hero-btn">
                <a href="#">Explore Our Lab</a>
            </div>
        </div>

        <div class="hero-right">
            <div class="glass-card">
                <h3>Optical Communication Lab</h3>
                <p>
                    A research-driven laboratory dedicated to optical fiber,
                    laser communication, and photonic systems.
                </p>
                <ul>
                    <li>🔹 Fiber Optic Systems</li>
                    <li>🔹 Photonic Technology</li>
                    <li>🔹 High-Speed Networks</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "about":
    st.header("About Us")
    st.write("Optical Communication Laboratory focuses on optical and photonic education and research.")

elif st.session_state.page == "team":
    st.header("Our Team")
    st.write("Lecturers, laboratory assistants, and researchers.")

elif st.session_state.page == "activity":
    st.header("Our Activity")
    st.write("Practical sessions, experiments, and collaborative research.")
