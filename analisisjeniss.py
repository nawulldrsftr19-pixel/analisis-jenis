import streamlit as st
import time
import graphviz

st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- CSS untuk animasi ---
st.markdown("""
<style>
.spin-icon {
    border: 8px solid #f3f3f3; border-top: 8px solid #1565c0;
    border-radius: 50%; width: 50px; height: 50px;
    animation: spin 1s linear infinite; margin: 10px auto;
}
@keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
.flame { width:35px; height:35px; border-radius:50%; margin:10px; }
.tube { width:55px; height:160px; border:2px solid #333; border-radius:0 0 30px 30px;
        position:relative; background:rgba(255,255,255,0.4); overflow:hidden; margin:10px;}
.liquid { position:absolute; bottom:0; width:100%; opacity:0.6;}
.pellet { position:absolute; bottom:0; width:100%; border-radius:0 0 27px 27px;}
</style>
""", unsafe_allow_html=True)

# --- Fungsi visual ---
def tube_viz(liq_color, p_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube"><div class="liquid" style="height:75%; background:{liq_color};"></div>{p_html}</div>', unsafe_allow_html=True)

def flame_viz(color):
    st.markdown(f'<div class="flame" style="background:{color}; box-shadow:0 0 20px {color};"></div>', unsafe_allow_html=True)

def centrifuge_action():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="spin-icon"></div>', unsafe_allow_html=True)
        st.write("🌀 Memutar pada 3000 rpm...")
        time.sleep(2)
    placeholder.empty()
    st.success("✅ Pemisahan selesai!")

# --- Tab menu ---
tab1, tab2, tab3 = st.tabs(["📊 Bagan Alir (Mind Map)", "🔹 Analisis Kation", "🧪 Analisis Anion"])

# --- TAB 1: BAGAN (tetap ada, jangan diubah) ---
with tab1:
    st.subheader("📊 Bagan Pemisahan Kation")
    if 'langkah' not in st.session_state:
        st.session_state.langkah = 0
    def buat_bagan(step):
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        dot.node('start','Campuran Gol I–V',style='filled',color='lavender')
        if step>=1:
            dot.node('hcl','+ HCl encer')
            dot.edge('start','hcl')
            dot.node('gol1','Endapan Gol I',style='filled',color='lightblue')
            dot.node('larutan','Larutan (Al,Fe,Ba,Sr,Ca)',style='filled',color='lightblue')
            dot.edge('hcl','gol1'); dot.edge('hcl','larutan')
        if step>=2:
            dot.node('h2o','+ H2O Panas'); dot.edge('gol1','h2o')
            dot.node('pb','Pb²⁺'); dot.node('residu','Residu Ag/Hg')
            dot.edge('h2o','pb'); dot.edge('h2o','residu')
            dot.node('nh4oh','+ NH₄OH'); dot.edge('larutan','nh4oh')
            dot.node('gol3','Endapan Gol III'); dot.node('gol4','Larutan Gol IV')
            dot.edge('nh4oh','gol3'); dot.edge('nh4oh','gol4')
        if step>=3:
            dot.edge('pb','PbCrO₄ (Kuning)',label='+ K₂CrO₄')
            dot.edge('gol3','Fe(OH)₃'); dot.edge('gol3','Al(OH)₄⁻')
            dot.edge('gol4','BaCrO₄ (Kuning)',label='+ K₂CrO₄')
            dot.edge('gol4','Sr²⁺, Ca²⁺')
        if step>=4:
            dot.edge('Fe(OH)₃','Fe(SCN)₃ (Merah)',label='+ SCN⁻')
            dot.edge('Al(OH)₄⁻','Al(OH)₃ (Putih)',label='+ HCl/Na₂CO₃')
