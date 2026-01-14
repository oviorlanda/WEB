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

/* ===== RESET ===== */
html, body, [class*="css"] {
    background-color: #1E90FF !important;
}

/* ROOT */
.stApp {
    background-color: #1E90FF !important;
    color: #ffffff;
}

/* CONTENT */
.block-container {
    padding-top: 0rem;
    background-color: #1E90FF !important;
}

/* ===== HEADER ===== */
.header {
    background: linear-gradient(135deg, #1b6fe5, #2d8cff);
    padding: 30px 60px;
    border-bottom-left-radius: 60px;
    border-bottom-right-radius: 60px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

/* LOGO */
.logo img {
    border-radius: 12px;
}

/* ===== NAV BUTTON ===== */
button[kind="secondary"] {
    background: transparent !important;
    color: #ffffff !important;
    border: none !important;
    font-size: 15px;
    font-weight: 600;
    padding: 10px 16px;
}

button[kind="secondary"]:hover {
    color: #cce4ff !important;
}

/* ===== SECTION ===== */
.subtitle {
    color: #dbeafe;
    font-weight: 700;
    letter-spacing: 1.2px;
}

.section-title {
    font-size: 36px;
    font-weight: 800;
    margin-top: 5px;
}

/* ===== CARD ===== */
.card {
    background: #2d7ff0;
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.35);
    transition: 0.3s ease-in-out;
}

.card:hover {
    transform: translateY(-8px);
    background: #3b91ff;
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .header {
        padding: 20px 25px;
        text-align: center;
    }
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
        st.image("ocl_logo.png.png", width=90)

with col2:
    nav1, nav2, nav3, nav4 = st.columns(4)

    with nav1:
        if st.button("About Us"):
            st.session_state.page = "about"
    with nav2:
        if st.button("Our Teams"):
            st.session_state.page = "team"
    with nav3:
        if st.button("Our Activity"):
            st.session_state.page = "activity"
    with nav4:
        if st.button("Informations"):
            st.session_state.page = "info"

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# ======================
# CONTENT
# ======================
if st.session_state.page == "home":

    st.markdown("""
    <div style="padding: 40px;">
        <p class="subtitle">MODULE</p>
        <h2 class="section-title">Our Module</h2>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h4>Optical Fiber</h4>
            <p>Basic optical fiber transmission module.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h4>WDM System</h4>
            <p>Wavelength Division Multiplexing experiment.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h4>Optical Network</h4>
            <p>Optical access & backbone network module.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "about":
    st.header("About Us")
    st.write("Optical Communication Laboratory focuses on optical & photonic education and research.")

elif st.session_state.page == "team":
    st.header("Our Teams")
    st.write("Our lecturers, assistants, and researchers.")

elif st.session_state.page == "activity":
    st.header("Our Activity")
    st.write("Practical sessions, research, and collaborations.")

elif st.session_state.page == "info":
    st.header("Informations")
    st.write("Announcements and laboratory information.")

