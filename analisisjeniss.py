import streamlit as st

st.set_page_config(page_title="Analisis Kualitatif Kation", page_icon="⚗️", layout="wide")

st.title("Laboratorium Virtual — Analisis Kualitatif Kation Gol I–V")
st.write("Simulasi interaktif berdasarkan bagan analisis kation.")

# ─── TAB MENU ───────────────────────────────────────────────────────────────
tab_g1, tab_g3, tab_g4, tab_g5 = st.tabs([
    "Golongan I (Ag, Pb, Hg)",
    "Golongan III (Al, Fe)",
    "Golongan IV (Ba, Sr, Ca)",
    "Ringkasan"
])

# 📌 TAB GOLONGAN I
with tab_g1:
    st.subheader("Pengendapan Golongan I")
    step = st.radio("Pilih langkah:", [
        "Campuran + HCl Encer",
        "Endapan Pb²⁺ + H₂O Panas",
        "Pb²⁺ + K₂CrO₄ → PbCrO₄ (Kuning)",
        "Endapan AgCl & Hg₂Cl₂ + NH₄OH",
        "Hg(NH₂)Cl + Hg (Putih/Hitam)",
        "Ag(NH₃)₂⁺ + HNO₃ → AgCl (Putih)"
    ])
    if "PbCrO₄" in step:
        st.success("Terbentuk endapan kuning PbCrO₄")
    elif "AgCl" in step:
        st.info("Terbentuk endapan putih AgCl")
    elif "Hg" in step:
        st.warning("Terbentuk endapan putih/ hitam Hg(NH₂)Cl + Hg")
    else:
        st.write("Langkah dipilih:", step)

# 📌 TAB GOLONGAN III
with tab_g3:
    st.subheader("Pengendapan Golongan III")
    step = st.radio("Pilih langkah:", [
        "Filtrat + NH₄OH → Endapan (Al, Fe)",
        "Fe(OH)₃ Endapan",
        "Fe³⁺ + SCN⁻ → Fe(SCN)₃ (Merah)",
        "Al(OH)₄⁻ Larutan",
        "Al(OH)₃ Endapan Putih"
    ])
    if "Fe(SCN)₃" in step:
        st.success("Larutan merah darah terbentuk (Fe(SCN)₃)")
    elif "Al(OH)₃" in step:
        st.info("Endapan putih Al(OH)₃ terbentuk")
    else:
        st.write("Langkah dipilih:", step)

# 📌 TAB GOLONGAN IV
with tab_g4:
    st.subheader("Pengendapan Golongan IV")
    step = st.radio("Pilih langkah:", [
        "Filtrat (Ba, Sr, Ca) + K₂CrO₄",
        "Ba²⁺ → BaCrO₄ (Kuning)",
        "Sr²⁺ + Na₂CO₃ → SrCO₃ (Putih)",
        "Ca²⁺ + H₂C₂O₄ + NH₄OH → CaC₂O₄ (Putih)"
    ])
    if "BaCrO₄" in step:
        st.success("Endapan kuning BaCrO₄ terbentuk")
    elif "SrCO₃" in step:
        st.info("Endapan putih SrCO₃ terbentuk")
    elif "CaC₂O₄" in step:
        st.warning("Endapan putih CaC₂O₄ terbentuk")
    else:
        st.write("Langkah dipilih:", step)

# 📌 TAB RINGKASAN
with tab_g5:
    st.subheader("Ringkasan Analisis")
    st.write("""
    - **Gol I**: Ag, Pb, Hg dipisahkan dengan HCl → endapan klorida.
    - **Gol III**: Al, Fe dipisahkan dengan NH₄OH → endapan hidroksida.
    - **Gol IV**: Ba, Sr, Ca dipisahkan dengan K₂CrO₄, Na₂CO₃, H₂C₂O₄.
    """)
