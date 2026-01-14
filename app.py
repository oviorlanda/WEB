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
html, body {
    background-color: #1E90FF !important;
}

/* ROOT */
.stApp {
    background-color: #1E90FF !important;
    color: white;
}

/* CONTENT */
.block-container {
    padding-top: 0rem;
}

/* ===== HEADER ===== */
.header {
    background: linear-gradient(135deg, #1b6fe5, #2d8cff);
    padding: 25px 50px;
    border-bottom-left-radius: 60px;
    border-bottom-right-radius: 60px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

/* ===== NAV CONTAINER ===== */
.nav-container {
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: flex-start;
    margin-left: -20px;
}

/* ===== BUTTON ===== */
button[kind="secondary"] {
    background: transparent !important;
    color: white !important;
    border: none !important;
    font-size: 15px;
    font-weight: 600;
    padding: 8px 12px;
}

button[kind="secondary"]:hover {
    color: #cce4ff !important;
}

/* ===== TEXT ===== */
.subtitle {
    color: #dbeafe;
    font-weight: 700;
    letter-spacing: 1.2px;
}

.section-title {
    font-size: 36px;
    font-weight: 800;
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

</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown('<div class="header">', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 8.5])

with col1:
    if os.path.exists("ocl_logo.png.png"):
        st.image("ocl_logo.png.png", width=200)

with col2:
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)

    if st.button("About Us"):
        st.session_state.page = "about"
    if st.button("Our Teams"):
        st.session_state.page = "team"
    if st.button("Our Activity"):
        st.session_state.page = "activity"
    if st.button("Informations"):
        st.session_state.page = "info"

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# ======================
# CONTENT
# ======================
if st.session_state.page == "home":

    st.markdown("""
    <div style="padding:40px">
        <p class="subtitle">WELCOME</p>
        <h2 class="section-title">Optical Communication Laboratory</h2>
        <p style="font-size:18px; max-width:900px; line-height:1.7;">
        This website provides academic, practical, and research information
        related to optical and photonic communication systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "about":

    st.markdown("""
    <div style="padding:40px">
        <p class="subtitle">ABOUT US</p>
        <h2 class="section-title">Optical Communication Laboratory (OCL)</h2>

        <p style="font-size:18px; max-width:1000px; line-height:1.8;">
        Laboratorium Komunikasi Optik (Optical Communication Laboratory)
        di Telkom University merupakan fasilitas riset dan pembelajaran
        di bawah Fakultas Teknik Elektro (FTE) yang berfokus pada teknologi
        transmisi data berbasis cahaya.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>📡 Focus</h3>
        <p>Fiber Optic, FTTH, DWDM, VLC, dan sistem komunikasi optik modern.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🔬 Facilities</h3>
        <p>Fusion Splicer, OTDR, Optical Power Meter, dan software simulasi.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h3>🏭 Industry</h3>
        <p>Mendukung kebutuhan industri ISP, vendor telekomunikasi, dan riset.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "team":
    st.markdown("""
    <div style="padding:40px">
        <h2 class="section-title">Our Teams</h2>
        <p>Dosen, laboran, asisten, dan mahasiswa peneliti.</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "activity":
    st.markdown("""
    <div style="padding:40px">
        <h2 class="section-title">Our Activity</h2>
        <p>Praktikum, penelitian, sertifikasi, dan kolaborasi industri.</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "info":

    st.markdown("""
    <div style="padding:40px">
        <p class="subtitle">ACADEMIC INFORMATION</p>
        <h2 class="section-title">Our Modules</h2>
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
