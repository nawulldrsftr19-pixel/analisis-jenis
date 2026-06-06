import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Vibrant Lab: Analisis Kualitatif Pro", layout="wide")

# --- CSS: VIBRANT, NO TOP PADDING, & FLOWCHART STYLE ---
st.markdown("""
    <style>
    /* Menghilangkan celah putih di bawah judul */
    .block-container { padding-top: 1rem; }
    
    /* Tema Warna Vibrant */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 20px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 20px;
    }
    
    /* Gaya Node Bagan (Mind Map) */
    .node { 
        padding: 12px; border-radius: 10px; border: 2px solid #0369a1; 
        background: #f0f9ff; text-align: center; margin: 10px 0; 
        font-weight: bold; font-size: 0.95rem; color: #0c4a6e;
    }
    .result-node { background: #dcfce7; border-color: #16a34a; color: #166534; border-style: double; border-width: 4px; }
    .arrow { text-align: center; font-size: 22px; color: #64748b; margin: -5px 0; }

    /* Simulator Tabung */
    .tube-body {
        width: 50px; height: 160px; border: 3px solid #334155; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 10px auto;
    }
    .liquid-fill { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet-fill { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: all 1.5s ease-in-out; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI HELPER ---
def render_tube(liq, pel=None, h=0):
    p_html = f'<div class="pellet-fill" style="height:{h}px; background:{pel};"></div>' if pel else ""
    st.markdown(f'<div class="tube-body"><div class="liquid-fill" style="height:70%; background:{liq}; opacity:0.7;"></div>{p_html}</div>', unsafe_allow_html=True)

# --- NAVIGASI SIDEBAR ---
st.sidebar.title("🎨 Menu Laboratorium")
page = st.sidebar.radio("Navigasi Halaman:", ["Halaman 1: Bagan Interaktif", "Halaman 2: Simulasi Kation", "Halaman 3: Analisis Anion"])

st.markdown('<h1 class="main-title">Aplikasi Analisis Kualitatif Ion Interaktif</h1>', unsafe_allow_html=True)

# --- HALAMAN 1: BAGAN INTERAKTIF LENGKAP (SOURCE 5 & 6) ---
if page == "Halaman 1: Bagan Interaktif":
    st.subheader("📍 Diagram Alir Pemisahan Kation (Berdasarkan Sumber)")
    st.info("Klik tombol pereaksi untuk menelusuri langkah identifikasi spesifik setiap kation.")
    
    # ROOT: Campuran Contoh
    st.markdown('<div class="node">Campuran Contoh Gol I - V</div>', unsafe_allow_html=True)
    
    # LEVEL 1: HCl Encer
    if st.button("➕ Tambahkan HCl Encer", key="start", type="primary"):
        st.write("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="node" style="background:#fee2e2;">Endapan Gol I (AgCl, PbCl₂, Hg₂Cl₂)</div>', unsafe_allow_html=True)
            
            # LEVEL 2 GOL I: Pencucian H2O Panas
            if st.button("🧼 Cuci dengan H₂O Panas", key="g1_h2o"):
                st.write("---")
                c1a, c1b = st.columns(2)
                with c1a:
                    st.markdown('<div class="node">Larutan Pb²⁺</div>', unsafe_allow_html=True)
                    if st.button("🟡 Uji Pb²⁺ (+ K₂CrO₄)", key="test_pb"):
                        st.markdown('<div class="node result-node">IDENTIFIKASI: PbCrO₄ (Endapan Kuning 🟡)</div>', unsafe_allow_html=True)
                with c1b:
                    st.markdown('<div class="node">Residu AgCl, Hg₂Cl₂</div>', unsafe_allow_html=True)
                    # LEVEL 3 GOL I: NH4OH
                    if st.button("➕ Tambahkan NH₄OH Berlebih", key="g1_nh4"):
                        st.markdown('<div class="node result-node">HASIL: Hg(NH₂)Cl + Hg (Putih + Hitam ⚫)</div>', unsafe_allow_html=True)
                        st.markdown('<div class="node">Filtrat Ag(NH₃)₂⁺ Cl⁻</div>', unsafe_allow_html=True)
                        if st.button("⚪ Uji Ag⁺ (+ HNO₃)", key="test_ag"):
                            st.markdown('<div class="node result-node">IDENTIFIKASI: AgCl (Endapan Putih ⚪)</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="node" style="background:#dcfce7;">Larutan (Al³⁺, Fe³⁺, Ba²⁺, Sr²⁺, Ca²⁺)</div>', unsafe_allow_html=True)
            
            # LEVEL 2 GOL III/IV: NH4OH Berlebih
            if st.button("➕ Tambahkan NH₄OH Berlebih", key="lvl2"):
                st.write("---")
                c2a, c2b = st.columns(2)
                
                with c2a:
                    st.markdown('<div class="node">Endapan Gol III (Al(OH)₃, Fe(OH)₃)</div>', unsafe_allow_html=True)
                    # LEVEL 3 GOL III: NaOH
                    if st.button("➕ Tambahkan NaOH", key="g3_naoh"):
                        st.write("---")
                        c2a1, c2a2 = st.columns(2)
                        with c2a1:
                            st.markdown('<div class="node">Residu Fe(OH)₃</div>', unsafe_allow_html=True)
                            if st.button("➕ Larutkan dengan HNO₃", key="fe_hno"):
                                st.markdown('<div class="node">Larutan Fe³⁺</div>', unsafe_allow_html=True)
                                if st.button("🔴 Uji Fe³⁺ (+ SCN⁻)", key="test_fe"):
                                    st.markdown('<div class="node result-node">IDENTIFIKASI: Fe(SCN)₃ (Larutan Merah 🔴)</div>', unsafe_allow_html=True)
                        with c2a2:
                            st.markdown('<div class="node">Filtrat Al(OH)₄⁻</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Al³⁺ (+ HCl / Na₂CO₃)", key="test_al"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: Al(OH)₃ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)

                with c2b:
                    st.markdown('<div class="node">Larutan Gol IV (Ba²⁺, Sr²⁺, Ca²⁺)</div>', unsafe_allow_html=True)
                    # LEVEL 3 GOL IV: K2CrO4
                    if st.button("➕ Tambahkan K₂CrO₄", key="g4_k2cr"):
                        st.write("---")
                        c2b1, c2b2 = st.columns(2)
                        with c2b1:
                            st.markdown('<div class="node result-node">IDENTIFIKASI: BaCrO₄ (Endapan Kuning 🟡)</div>', unsafe_allow_html=True)
                        with c2b2:
                            st.markdown('<div class="node">Larutan Sr²⁺, Ca²⁺</div>', unsafe_allow_html=True)
                            # LEVEL 4 GOL IV: Identifikasi Spesifik Sr & Ca
                            if st.button("➕ Tambahkan Na₂CO₃", key="g4_na2co"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: SrCO₃ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)
                            if st.button("➕ Tambahkan CH₃COOH + H₂C₂O₄ + NH₄OH", key="g4_ca"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: CaC₂O₄ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)

# --- HALAMAN 2: SIMULASI KATION ---
elif page == "Halaman 2: Simulasi Kation":
    st.subheader("🧪 Simulasi Reaksi & Pengendapan Kation")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol == "Golongan I":
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("Jalankan Simulasi"):
            render_tube("rgba(200,230,255,0.4)", "white", 45)
            st.success("Terbentuk Pellet Putih sesuai alur bagan [1].")

    elif gol == "Golongan III":
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah)}")
        if st.button("Jalankan Simulasi"):
            render_tube("#991b1b")
            st.info("Hasil identifikasi besi menghasilkan larutan merah darah [2].")

    elif gol == "Golongan IV":
        st.write("### Identifikasi Baris Vertikal:")
        st.markdown("1. **Ba²⁺**: $+ K_2CrO_4 \rightarrow BaCrO_4$ (Kuning 🟡)")
        st.markdown("2. **Sr²⁺**: $+ Na_2CO_3 \rightarrow SrCO_3$ (Putih ⚪)")
        st.markdown("3. **Ca²⁺**: $+ CH_3COOH + H_2C_2O_4 + NH_4OH \rightarrow CaC_2O_4$ (Putih ⚪)")

# --- HALAMAN 3: ANALISIS ANION ---
elif page == "Halaman 3: Analisis Anion":
    st.subheader("📝 Analisis Anion (Berdasarkan Tabel 6.1) [3]")
    anion = st.selectbox("Pilih Ion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(255,255,255,0.2)", "white", 35)
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}")
        render_tube("yellow", "#ef4444", 45)
