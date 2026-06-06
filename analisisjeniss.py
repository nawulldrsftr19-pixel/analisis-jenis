import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Pro-Lab: Analisis Kualitatif Terpadu", layout="wide")

# --- CSS: ESTETIKA MODERN, ANIMASI API & SENTRIFUGASI REALISTIK ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%); }
    .main-title { color: #075985; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 10px solid #0284c7; margin-bottom: 25px; }
    .center-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    
    /* Animasi Centrifuge Bergerak */
    .centrifuge-spin {
        width: 80px; height: 80px; border: 8px dashed #0284c7;
        border-radius: 50%; animation: spin 0.7s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi (Pellet & Supernatan) */
    .tube-container { display: flex; flex-direction: column; align-items: center; margin: 25px 0; }
    .tube {
        width: 65px; height: 190px; border: 4px solid #334155;
        border-radius: 0 0 35px 35px; position: relative;
        background: rgba(255,255,255,0.3); overflow: hidden;
        box-shadow: inset 8px 0 15px rgba(255,255,255,0.5);
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.8s ease-in-out; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 30px 30px; transition: all 1.8s ease-in-out; }
    
    /* Animasi Api (Flicker) */
    .flame-box { display: flex; justify-content: center; align-items: flex-end; height: 75px; margin-bottom: 10px; }
    .flame {
        width: 35px; height: 35px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.4s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.3); opacity: 0.8; } }

    /* Gaya Mind Map Node */
    .node { padding: 12px; border-radius: 12px; border: 2px solid #0369a1; background: #e0f2fe; text-align: center; margin: 10px 0; font-weight: bold; font-size: 1rem; color: #0c4a6e; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI ---
def play_centrifuge():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 rpm Sedang Berlangsung...</b></center>", unsafe_allow_html=True)
        time.sleep(2.5)
    placeholder.empty()

def render_tube(liq_color, p_color=None, p_height=0, keruh=False):
    op = "0.4" if keruh else "0.8"
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-container"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-box"><div class="flame" style="background:{color}; box-shadow:0 0 20px {color};"></div></div>', unsafe_allow_html=True)

# --- SIDEBAR: DIAGRAM ALIR INTERAKTIF (MIND MAP) ---
st.sidebar.title("📍 Mind Map Pemisahan")
st.sidebar.info("Klik tahapan bagan di bawah untuk menelusuri pemisahan kation [1].")

# Navigasi Bagan Utama
step_1 = st.sidebar.selectbox("Langkah Utama:", ["Campuran Gol I-V", "Golongan I (Endapan)", "Filtrat (Gol III & IV)"])

detail_bagan = None
if step_1 == "Golongan I (Endapan)":
    detail_bagan = st.sidebar.radio("Telusuri Alur Gol I:", ["Awal (+HCl)", "Pemisahan Pb2+", "Identifikasi Ag & Hg"])
elif step_1 == "Filtrat (Gol III & IV)":
    detail_bagan = st.sidebar.radio("Telusuri Alur Filtrat:", ["Pemisahan Gol III", "Identifikasi Gol IV (Baris)"])

st.sidebar.divider()
st.sidebar.title("🧪 Analisis Anion")
mode_anion = st.sidebar.checkbox("Buka Simulator Anion")

# --- AREA UTAMA TERPUSAT ---
st.markdown('<h1 class="main-title">Aplikasi Lab Virtual: Analisis Kualitatif Ion</h1>', unsafe_allow_html=True)
_, col_main, _ = st.columns([0.1, 0.8, 0.1])

with col_main:
    st.markdown('<div class="center-card">', unsafe_allow_html=True)

    if not mode_anion:
        # LOGIKA DIAGRAM ALIR KATION
        if step_1 == "Campuran Gol I-V":
            st.subheader("Bagan Tahap Awal: Pemisahan Campuran")
            st.markdown('<div class="node">Campuran Contoh Kation (Gol I - V)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ <b>+ HCl Encer</b></center>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="node" style="border-color:#ef4444;">Endapan Golongan I</div>', unsafe_allow_html=True)
                st.caption("AgCl, PbCl₂, Hg₂Cl₂ (Putih) [2]")
            with c2:
                st.markdown('<div class="node" style="border-color:#10b981;">Filtrat (Gol III, IV, V)</div>', unsafe_allow_html=True)
                st.caption("Larutan untuk analisis selanjutnya [1]")

        elif detail_bagan == "Awal (+HCl)":
            st.subheader("Langkah 1: Pengendapan Golongan I")
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            if st.button("Jalankan Sentrifugasi 3000 rpm"):
                render_tube("white", keruh=True)
                play_centrifuge()
                render_tube("rgba(200,230,255,0.3)", "white", 45)
                st.success("Endapan (Pellet) dan Larutan (Supernatan) terpisah sempurna [2].")

        elif detail_bagan == "Pemisahan Pb2+":
            st.subheader("Identifikasi Timbal (Pb2+)")
            st.write("Endapan ditambahkan air panas untuk melarutkan PbCl₂ [1].")
            st.latex(r"Pb^{2+}(aq) + CrO_4^{2-}(aq) \rightarrow PbCrO_4(s) \downarrow \text{ (Kuning)}")
            render_tube("rgba(255,255,224,0.3)", "#eab308", 40)

        elif detail_bagan == "Pemisahan Gol III":
            st.subheader("Analisis Golongan III: Besi & Aluminium")
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
            if st.button("Uji Spesifik Fe3+"):
                render_tube("#991b1b")
                st.info("Larutan berubah menjadi merah darah [3].")

        elif detail_bagan == "Identifikasi Gol IV (Baris)":
            st.subheader("Identifikasi Golongan IV (Penyajian Vertikal)")
            # PENYAJIAN BARIS KE BAWAH (VERTIKAL)
            st.markdown("### 1. Barium (Ba²⁺)")
            render_api("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
            
            st.markdown("---")
            st.markdown("### 2. Stronsium (Sr²⁺)")
            render_api("#ef4444")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
            
            st.markdown("---")
            st.markdown("### 3. Kalsium (Ca²⁺)")
            render_api("#f97316")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

    else:
        # PANEL ANION (REAKSI STOIKIOMETRI LENGKAP)
        st.subheader("Identifikasi Anion (Berdasarkan Tabel 6.1)")
        tabs_anion = st.tabs(["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
        
        with tabs_anion:
            st.latex(r"Cl^-(aq) + AgNO_3(aq) \rightarrow AgCl(s) \downarrow \text{ (Putih)} + NO_3^-(aq)")
            if st.button("Uji Cl⁻"): render_tube("rgba(255,255,255,0.2)", "white", 35)

        with tabs_anion[2]:
            st.latex(r"2I^-(aq) + HgCl_2(aq) \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)} + 2Cl^-(aq)")
            if st.button("Uji I⁻"): 
                render_tube("yellow", "#ef4444", 40)
                st.warning("Catatan: Kelebihan KI melarutkan endapan menjadi kompleks kuning [4].")

        with tabs_anion[3]:
            st.latex(r"CO_3^{2-}(aq) + 2HCl(aq) \rightarrow CO_2(g) \uparrow + H_2O(l) + 2Cl^-(aq)")
            st.write("Hasil: Terbentuk gelembung gas CO₂ [4].")

        with tabs_anion[5]:
            st.latex(r"SO_4^{2-}(aq) + BaCl_2(aq) \rightarrow BaSO_4(s) \downarrow \text{ (Putih)} + 2Cl^-(aq)")
            if st.button("Uji SO₄²⁻"): render_tube("rgba(200,230,255,0.2)", "white", 40)

    st.markdown('</div>', unsafe_allow_html=True)
