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
    color: #dbeafe !important;
}

/* SECTION */
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
        st.image("ocl_logo.png.png", width=140)

with col2:
    n1, n2, n3, n4 = st.columns(4)

    with n1:
        if st.button("About Us"):
            st.session_state.page = "about"
    with n2:
        if st.button("Our Teams"):
            st.session_state.page = "team"
    with n3:
        if st.button("Our Activity"):
            st.session_state.page = "activity"
    with n4:
        if st.button("Informations"):
            st.session_state.page = "info"

st.markdown("</div><br><br>", unsafe_allow_html=True)

# ======================
# CONTENT
# ======================
if st.session_state.page == "home":
    st.header("Welcome to Optical Communication Laboratory")
    st.write(
        "This platform provides academic, laboratory, and research information "
        "related to optical and photonic communication systems."
    )

# ======================
# ABOUT US
# ======================
elif st.session_state.page == "about":

    st.markdown("""
    <div style="padding:50px;">
        <p class="subtitle">ABOUT US</p>
        <h2 class="section-title">Optical Communication Laboratory</h2>

        <p style="margin-top:20px; max-width:1000px; font-size:18px; line-height:1.8;">
        Laboratorium Komunikasi Optik (Optical Communication Laboratory) di 
        <b>Telkom University</b> merupakan salah satu fasilitas riset dan pembelajaran
        utama di bawah <b>Fakultas Teknik Elektro (FTE)</b>. Laboratorium ini berfokus
        pada teknologi transmisi data menggunakan media cahaya yang menjadi
        tulang punggung sistem telekomunikasi modern.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='padding:40px;'><h3>🔹 Focus Area</h3></div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown('<div class="card"><h4>SKSO</h4><p>Sistem komunikasi serat optik.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h4>FTTH</h4><p>Fiber to the Home networks.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><h4>DWDM</h4><p>Multi-wavelength transmission.</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="card"><h4>VLC</h4><p>Visible Light Communication.</p></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:40px;">
        <h3>🔬 Facilities & Equipment</h3>
        <ul>
            <li>Fusion Splicer</li>
            <li>OTDR</li>
            <li>Optical Power Meter</li>
            <li>OptiSystem Simulation Software</li>
        </ul>

        <h3 style="margin-top:25px;">🎓 Academic & Research</h3>
        <ul>
            <li>Fiber optic practicum & measurements</li>
            <li>Industry certification & training</li>
            <li>Optical sensor and FSO research</li>
        </ul>

        <h3 style="margin-top:25px;">🏭 Industry Relevance</h3>
        <p>
        Graduates gain industry-ready skills demanded by ISPs, network vendors,
        and telecommunication infrastructure companies.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ======================
# OTHER PAGES
# ======================
elif st.session_state.page == "team":
    st.header("Our Teams")
    st.write("Lecturers, assistants, and student researchers.")

elif st.session_state.page == "activity":
    st.header("Our Activity")
    st.write("Practicum sessions, research, and collaborations.")

elif st.session_state.page == "info":
    st.header("Informations")
    st.write("Academic modules and laboratory information.")
