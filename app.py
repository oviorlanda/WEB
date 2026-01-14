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

/* ===== NAV ===== */
.nav-container {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    margin-top: 12px;
}

/* NAV BUTTON */
button[kind="secondary"] {
    background: transparent !important;
    color: #ffffff !important;
    border: none !important;
    font-size: 15px;
    font-weight: 600;
    padding: 8px 14px;
}

button[kind="secondary"]:hover {
    color: #cce4ff !important;
    text-decoration: underline;
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
    .nav-container {
        justify-content: center;
        flex-wrap: wrap;
    }
}

</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown('<div class="header">', unsafe_allow_html=True)

col1, col2 = st.columns([2, 8])

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
    <div style="padding:40px;">
        <h2 class="section-title">Welcome to Optical Communication Laboratory</h2>
        <p style="max-width:900px;font-size:18px;line-height:1.7;">
        This website provides academic, laboratory, and research information
        related to optical and photonic communication systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "about":
    st.markdown("""
    <div style="padding:40px;">
        <p class="subtitle">ABOUT US</p>
        <h2 class="section-title">Optical Communication Laboratory</h2>

        <p style="max-width:1000px;font-size:18px;line-height:1.8;margin-top:20px;">
        Laboratorium Komunikasi Optik (Optical Communication Laboratory) di Telkom University
        merupakan fasilitas pembelajaran dan riset di bawah Fakultas Teknik Elektro (FTE).
        Laboratorium ini berfokus pada teknologi transmisi data berbasis cahaya
        yang menjadi tulang punggung telekomunikasi modern.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>📡 Education</h3>
        <p>Praktikum sistem komunikasi serat optik, FTTH, dan jaringan akses optik.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🔬 Research</h3>
        <p>Riset DWDM, VLC (Li-Fi), Optical Network, dan Free Space Optics.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h3>🏭 Industry Relevance</h3>
        <p>Kompetensi industri untuk ISP, Telco, dan infrastruktur broadband.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "team":
    st.header("Our Teams")
    st.write("Lecturers, laboratory assistants, and student researchers.")

elif st.session_state.page == "activity":
    st.header("Our Activity")
    st.write("Practicum sessions, academic research, and industrial collaboration.")

elif st.session_state.page == "info":
    st.markdown("""
    <div style="padding:40px;">
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
        <p>Wavelength Division Multiplexing experiments.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h4>Optical Network</h4>
        <p>Access & backbone optical network module.</p>
        </div>
        """, unsafe_allow_html=True)
