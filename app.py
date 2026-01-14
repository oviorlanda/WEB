if st.session_state.page == "home":

    with st.container():
        st.markdown("### 🔬 Optical Communication Laboratory")
        st.markdown(
            """
            ## Lighting the Future of Connectivity
            """
        )

        st.markdown(
            """
            Optical Communication Laboratory (OCL) at Telkom University
            focuses on education, research, and innovation in optical
            and photonic communication technologies that support
            modern telecommunication infrastructure.
            """
        )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📡 Education")
        st.write(
            "Hands-on laboratory practicum covering fiber optic "
            "transmission, measurement, and system design."
        )

    with col2:
        st.markdown("### 🔬 Research")
        st.write(
            "Research activities in WDM systems, FTTH networks, "
            "and optical performance analysis."
        )

    with col3:
        st.markdown("### 🌐 Innovation")
        st.write(
            "Development of future communication technologies such "
            "as photonic devices and optical access networks."
        )

    st.markdown("---")

    st.markdown("### 📊 Laboratory Highlights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Research Projects", "10+")
    with c2:
        st.metric("Active Modules", "5")
    with c3:
        st.metric("Certified Equipment", "Industry Standard")
