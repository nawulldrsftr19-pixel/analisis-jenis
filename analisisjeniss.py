import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Pro-Lab: Analisis Ion Terpadu", layout="wide")

# --- CSS: ESTETIKA & ANIMASI REALISTIK ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); }
    .main-title { color: #0369a1; text-align: center; background: white; padding: 25px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-left: 10px solid #0284c7; }
    .content-card { background: white; padding: 35px; border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    
    /* Animasi Centrifuge */
    .centrifuge-spin {
        width: 80px; height: 80px; border: 8px dashed #0ea5e9;
        border-radius: 50%; animation: spin 0.7s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi */
    .tube-container { display: flex; flex-direction: column; align-items: center; margin: 25px 0; }
    .tube {
        width: 65px; height: 200px; border: 4px solid #334155;
        border-radius: 0 0 35px 35px; position: relative;
        background: rgba(255,255,255,0.4); overflow: hidden;
        box-shadow: inset 8px 0 15px rgba(255,255,255,0.5);
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.8s ease-in-out; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 30px 30px; transition: all 1.8s ease-in-out; }
    
    /* Animasi Api Flicker */
    .flame-box { display: flex; justify-content: center; align-items: flex-end; height: 80px; margin-bottom: 10px; }
    .flame {
        width: 35px; height: 35px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.4s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.3); opacity: 0.8; } }

    /* Gaya Mind Map Node */
    .node { padding: 15px; border-radius: 12px; border: 2px solid #0284c7; background: #f0f9ff; text-align: center; margin: 10px 0; font-weight: bold; font-size: 1rem; color: #0c4a6e; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI KOMPONEN ---
def animasi_sentrifugasi():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 rpm Sedang Berlangsung...</b></center>", unsafe_allow_html=True)
        time.sleep(2.5)
    placeholder.empty()

def render_tabung(liq_color, p_color=None, p_height=0, keruh=False):
    op = "0.4" if keruh else "0.8"
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-container"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_api(color):
    st.markdown(f'<div class="flame-box"><div class="flame" style="background:{color}; box-shadow:0 0 20px {color};"></div></div>', unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<h1 class="main-title">🧪 Aplikasi Lab Virtual: Analisis Kualitatif Lengkap</h1>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🔬 Menu Laboratorium")
nav = st.sidebar.radio("Pilih Analisis:", ["📍 Bagan Alir Lengkap", "🧪 Kation Per Golongan", "🧪 Anion Per Ion"])

# --- AREA UTAMA TERPUSAT ---
_, col_main, _ = st.columns([0.1, 0.8, 0.1])

with col_main:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)

    # --- MENU 1: BAGAN ALIR (Mind Map Hingga Akhir) ---
    if nav == "📍 Bagan Alir Lengkap":
        st.subheader("📍 Mind Map Pemisahan Kation (Source 4)")
        tab_g1, tab_g3, tab_g4 = st.tabs(["Golongan I", "Golongan III", "Golongan IV"])

        with tab_g1:
            st.markdown('<div class="node">Campuran Sampel (Gol I-V)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + HCl Encer</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Endapan Putih (AgCl, PbCl₂, Hg₂Cl₂)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + Air Panas</center>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="node" style="border-color:#eab308;">Pb²⁺ (Larutan)</div>', unsafe_allow_html=True)
                st.caption("Identifikasi: + K₂CrO₄ → Endapan Kuning 🟡")
            with c2:
                st.markdown('<div class="node">Residu AgCl, Hg₂Cl₂</div>', unsafe_allow_html=True)
                st.write("<center>⬇️ + NH₄OH Berlebih</center>", unsafe_allow_html=True)
                st.write("**Hg(NH₂)Cl + Hg** (Putih+Hitam ⚫) & **[Ag(NH₃)₂]⁺** (Larut)")

        with tab_g3:
            st.markdown('<div class="node">Filtrat dari Gol I</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + NH₄OH Berlebih</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Endapan Gol III (Fe(OH)₃, Al(OH)₃)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + NaOH</center>", unsafe_allow_html=True)
            st.columns(2).markdown('<div class="node" style="border-color:#b91c1c;">Fe(OH)₃ (Coklat)</div>', unsafe_allow_html=True)
            st.columns(2)[1].markdown('<div class="node" style="border-color:#cbd5e1;">[Al(OH)₄]⁻ (Larut)</div>', unsafe_allow_html=True)

        with tab_g4:
            st.markdown('<div class="node">Filtrat dari Gol III</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + K₂CrO₄</center>", unsafe_allow_html=True)
            st.markdown('<div class="node" style="border-color:#eab308;">BaCrO₄ (Kuning)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ Larutan Sr²⁺, Ca²⁺</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Identifikasi Akhir Uji Nyala</div>', unsafe_allow_html=True)

    # --- MENU 2: KATION PER GOLONGAN ---
    elif nav == "🧪 Kation Per Golongan":
        st.subheader("Pemisahan & Reaksi Stoikiometri Kation")
        pilih_gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])

        if pilih_gol == "Golongan I":
            st.info("Penambahan HCl encer (Source 1)")
            if st.button("Jalankan Sentrifugasi Gol I"):
                render_tabung("white", keruh=True)
                animasi_sentrifugasi()
                st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
                st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}")
                render_tabung("rgba(200,230,255,0.3)", "white", 45)

        elif pilih_gol == "Golongan III":
            st.info("Penambahan NH₄OH & SCN⁻ (Source 2)")
            if st.button("Uji Besi (Fe³⁺)"):
                st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
                render_tabung("#991b1b")

        elif pilih_gol == "Golongan IV":
            st.info("Penyajian Baris Vertikal (Source 2 & 4)")
            st.markdown("### 1. Barium (Ba²⁺)")
            render_api("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
            
            st.markdown("---")
            st.markdown("### 2. Stronsium (Sr²⁺)")
            render_api("#ef4444")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
            
            st.markdown("---")
            st.markdown("### 3. Kalsium (Ca²⁺)")
            render_api("#f97316")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \text{ (Putih)}")

    # --- MENU 3: ANION PER ION ---
    elif nav == "🧪 Anion Per Ion":
        st.subheader("Identifikasi Anion (Tabel 6.1 - Source 5)")
        an_tab = st.tabs(["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
        
        with an_tab:
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)} + NO_3^-")
            if st.button("Uji Cl⁻"):
                render_tabung("rgba(255,255,255,0.2)", "white", 35)

        with an_tab[1]:
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)} + 2Cl^-")
            if st.button("Uji I⁻"):
                render_tabung("yellow", "#ef4444", 40)
                st.caption("Jika KI berlebih: HgI₂ + 2I⁻ → [HgI₄]²⁻ (Larutan Kuning)")

        with an_tab[2]:
            st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
            st.write("Hasil: Terbentuk gelembung gas CO₂.")

        with an_tab[3]:
            st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)} + 2Cl^-")
            if st.button("Uji SO₄²⁻"):
                render_tabung("rgba(200,230,255,0.2)", "white", 40)

    st.markdown('</div>', unsafe_allow_html=True)
