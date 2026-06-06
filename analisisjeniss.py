import streamlit as st

st.set_page_config(page_title="Analisis Kualitatif Kation", page_icon="⚗️", layout="wide")

st.title("🧪 Laboratorium Virtual — Analisis Kualitatif Kation Gol I–V")
st.write("Klik tab dan langkah untuk melihat hasil reaksi sesuai bagan analisis.")

# ─── TAB MENU ───────────────────────────────────────────────────────────────
tab_g1, tab_g3, tab_g4, tab_summary = st.tabs([
    "Golongan I (Ag, Pb, Hg)",
    "Golongan III (Al, Fe)",
    "Golongan IV (Ba, Sr, Ca)",
    "📖 Ringkasan"
])

# 📌 TAB GOLONGAN I
with tab_g1:
    st.header("Golongan I — Ag, Pb, Hg")
    with st.expander("Campuran + HCl Encer"):
        st.info("Terbentuk endapan putih klorida (AgCl, PbCl₂, Hg₂Cl₂).")
    with st.expander("Pb²⁺ + H₂O Panas"):
        st.success("Pb²⁺ larut → lanjut uji dengan K₂CrO₄.")
    with st.expander("Pb²⁺ + K₂CrO₄"):
        st.markdown("**Endapan kuning PbCrO₄ terbentuk.**")
    with st.expander("AgCl & Hg₂Cl₂ + NH₄OH"):
        st.warning("Hg(NH₂)Cl + Hg (putih/hitam), Ag(NH₃)₂⁺ larut.")
    with st.expander("Ag(NH₃)₂⁺ + HNO₃"):
        st.info("Endapan putih AgCl kembali terbentuk.")

# 📌 TAB GOLONGAN III
with tab_g3:
    st.header("Golongan III — Al, Fe")
    with st.expander("Filtrat + NH₄OH"):
        st.info("Endapan hidroksida terbentuk (Al(OH)₃, Fe(OH)₃).")
    with st.expander("Fe(OH)₃ + HNO₃ + SCN⁻"):
        st.success("Larutan merah darah Fe(SCN)₃ terbentuk.")
    with st.expander("Al(OH)₄⁻ Larutan"):
        st.write("Al(OH)₄⁻ tetap larut dalam NaOH berlebih.")
    with st.expander("Al(OH)₃ Endapan"):
        st.info("Endapan putih Al(OH)₃ terbentuk kembali.")

# 📌 TAB GOLONGAN IV
with tab_g4:
    st.header("Golongan IV — Ba, Sr, Ca")
    with st.expander("Filtrat (Ba, Sr, Ca) + K₂CrO₄"):
        st.success("Ba²⁺ → Endapan kuning BaCrO₄.")
    with st.expander("Sr²⁺ + Na₂CO₃"):
        st.info("Endapan putih SrCO₃ terbentuk.")
    with st.expander("Ca²⁺ + H₂C₂O₄ + NH₄OH"):
        st.warning("Endapan putih CaC₂O₄ terbentuk.")

# 📌 TAB RINGKASAN
with tab_summary:
    st.header("Ringkasan Analisis Golongan I–IV")
    st.markdown("""
    - **Gol I**: Ag, Pb, Hg → endapan kl
    """)
