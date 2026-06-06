import streamlit as st

st.set_page_config(page_title="Mind Map Analisis Kation", page_icon="⚗️", layout="wide")

st.title("🧪 Mind Map Interaktif — Analisis Kualitatif Kation Gol I–V")

# ─── BAGAN VISUAL ─────────────────────────────────────────────────────────────
st.graphviz_chart("""
digraph {
    node [shape=box, style=filled, color=lightblue, fontname="Helvetica"];
    "Campuran Gol I–V" -> "Tambah HCl Encer";
    "Tambah HCl Encer" -> "Endapan Gol I (Ag, Pb, Hg)";
    "Tambah HCl Encer" -> "Filtrat (Al, Fe, Ba, Sr, Ca)";
    
    "Endapan Gol I (Ag, Pb, Hg)" -> "Pb²⁺ + H₂O Panas";
    "Pb²⁺ + H₂O Panas" -> "Pb²⁺ + K₂CrO₄ → PbCrO₄ (Kuning)";
    "Endapan Gol I (Ag, Pb, Hg)" -> "AgCl & Hg₂Cl₂ + NH₄OH";
    "AgCl & Hg₂Cl₂ + NH₄OH" -> "Hg(NH₂)Cl + Hg (Putih/Hitam)";
    "AgCl & Hg₂Cl₂ + NH₄OH" -> "Ag(NH₃)₂⁺ + HNO₃ → AgCl (Putih)";
    
    "Filtrat (Al, Fe, Ba, Sr, Ca)" -> "Tambah NH₄OH Berlebih";
    "Tambah NH₄OH Berlebih" -> "Endapan (Al, Fe)";
    "Endapan (Al, Fe)" -> "Fe³⁺ + SCN⁻ → Fe(SCN)₃ (Merah)";
    "Endapan (Al, Fe)" -> "Al(OH)₄⁻ → Al(OH)₃ (Putih)";
    
    "Tambah NH₄OH Berlebih" -> "Filtrat (Ba, Sr, Ca)";
    "Filtrat (Ba, Sr, Ca)" -> "Ba²⁺ + K₂CrO₄ → BaCrO₄ (Kuning)";
    "Filtrat (Ba, Sr, Ca)" -> "Sr²⁺ + Na₂CO₃ → SrCO₃ (Putih)";
    "Filtrat (Ba, Sr, Ca)" -> "Ca²⁺ + H₂C₂O₄ + NH₄OH → CaC₂O₄ (Putih)";
}
""")

# ─── NODE DETAIL ─────────────────────────────────────────────────────────────
st.subheader("🔍 Klik node di bawah untuk detail reaksi")

with st.expander("Campuran Gol I–V"):
    st.info("Larutan awal mengandung campuran kation Golongan I–V.")

with st.expander("Endapan Gol I (Ag, Pb, Hg")
