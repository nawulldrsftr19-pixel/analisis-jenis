import streamlit as st

st.set_page_config(page_title="Bagan Analisis Kation", page_icon="⚗️", layout="wide")

st.title("🧪 Laboratorium Virtual — Bagan Analisis Kualitatif Kation Gol I–V")
st.write("Klik setiap node bagan untuk membuka langkah reaksi berikutnya.")

# ─── BAGAN UTAMA ───────────────────────────────────────────────────────────────
with st.expander("Campuran Contoh Gol I–V"):
    st.info("Larutan awal mengandung campuran kation Golongan I–V.")
    
    # Cabang Golongan I
    with st.expander("+ HCl Encer → Endapan Golongan I (Ag, Pb, Hg)"):
        st.success("Endapan putih klorida terbentuk.")
        
        with st.expander("+ H₂O Panas → Pb²⁺ Larut"):
            st.info("Pb²⁺ larut → uji lanjut.")
            st.button("Pb²⁺ + K₂CrO₄ → PbCrO₄ (Kuning)")
        
        with st.expander("Endapan AgCl & Hg₂Cl₂ + NH₄OH"):
            st.warning("Hg(NH₂)Cl + Hg (Putih/Hitam), Ag(NH₃)₂⁺ larut.")
            st.button("Ag(NH₃)₂⁺ + HNO₃ → AgCl (Putih)")
    
    # Cabang Golongan III
    with st.expander("Filtrat (Al, Fe, Ba, Sr, Ca) + NH₄OH Berlebih"):
        st.info("Endapan hidroksida terbentuk (Al, Fe).")
        
        with st.expander("Fe(OH)₃ Endapan"):
            st.button("Fe³⁺ + SCN⁻ → Fe(SCN)₃ (Merah)")
        
        with st.expander("Al(OH)₄⁻ Larutan"):
            st.button("Al(OH)₄⁻ + HCl/Na₂CO₃ → Al(OH)₃ (Putih)")
        
        # Cabang Golongan IV
        with st.expander("Filtrat (Ba, Sr, Ca) + K₂CrO₄"):
            st.success("Ba²⁺ → Endapan kuning BaCrO₄.")
            
            with st.expander("Filtrat (Sr, Ca)"):
                st.button("Sr²⁺ + Na₂CO₃ → SrCO₃ (Putih)")
                st.button("Ca²⁺ + H₂C₂O₄ + NH₄OH → CaC₂O₄ (Putih)")


