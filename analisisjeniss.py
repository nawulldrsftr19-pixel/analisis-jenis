import streamlit as st

st.set_page_config(page_title="Mind Map Analisis Kation", page_icon="⚗️", layout="wide")

st.title("🧪 Mind Map Interaktif — Analisis Kualitatif Kation Gol I–V")
st.write("Klik node di bawah untuk membuka detail reaksi.")

# ─── BAGAN MIND MAP ─────────────────────────────────────────────────────────────
st.subheader("Bagan Alur Analisis")
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
    "AgCl &
    """)
