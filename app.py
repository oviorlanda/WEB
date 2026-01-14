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

/* RESET */
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

/* HEADER */
.header {
    background: linear-gradient(135deg, #1b6fe5, #2d8cff);
    padding: 30px 60px;
    border-bottom-left-radius: 60px;
    border-bottom-right-radius: 60px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

/* NAV BUTTON */
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

/* TEXT */
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

/* CARD */
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

col1, col2 = st.columns([2, 6])

with col1:
    if os.path.exists("ocl_logo.png.png"):
        st.image("ocl_logo.png.png", width=160)

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
    <div style="padding:40px;">
        <h1>Welcome to Optical Communication Laboratory</h1>
        <p style="font-size:18px; max-width:850px;">
        This website provides academic, research, and laboratory information
        related to optical and photonic communication systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========= ABOUT =========
elif st.session_state.page == "about":
    st.markdown("""
    <div style="padding:40px;">
        <p class="subtitle">ABOUT OCL</p>
        <h2 class="section-title">Optical Communication Laboratory</h2>

        <p style="margin-top:20px; max-width:900px; font-size:18px; line-height:1.7;">
        Optical Communication Laboratory (OCL) is an academic laboratory dedicated
        to education, research, and innovation in optical and photonic communication
        systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h3>📡 Education</h3>
            <p>Hands-on practicum modules and laboratory-based learning.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h3>🔬 Research</h3>
            <p>Fiber optics, WDM, optical network performance analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h3>🌐 Innovation</h3>
            <p>Experimental platforms for future photonic technologies.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:40px;">
        <h3>Focus Areas</h3>
        <ul style="font-size:17px; line-height:1.8;">
            <li>Fiber Optic Communication</li>
            <li>WDM Systems</li>
            <li>Optical Access Networks</li>
            <li>Photonic Devices</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ========= TEAM =========
elif st.session_state.page == "team":
    st.header("Our Teams")
    st.write("Lecturers, laboratory assistants, and student researchers.")

# ========= ACTIVITY =========
elif st.session_state.page == "activity":
    st.header("Our Activity")
    st.write("Practical classes, research projects, and collaborations.")

# ========= INFORMATION =========
elif st.session_state.page == "info":
    st.markdown("""
    <div style="padding:40px;">
        <p class="subtitle">ACADEMIC INFORMATION</p>
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
            <p>Wavelength Division Multiplexing experiments.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h4>Optical Network</h4>
            <p>Access & backbone optical networks.</p>
        </div>
        """, unsafe_allow_html=True)
