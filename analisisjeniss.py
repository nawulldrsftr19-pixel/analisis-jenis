import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Vibrant Lab: Analisis Ion Pro", layout="wide")

# --- CSS: VIBRANT, HIDE WHITE SPACE, & ANIMASI ---
st.markdown("""
    <style>
    /* Menghilangkan celah putih di bawah judul & padding berlebih */
    .block-container { padding-top: 1rem; }
    header { visibility: hidden; } /* Menyembunyikan toolbar default Streamlit */
    
    /* Tema Warna Vibrant */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 15px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 0px; 
    }
    
    /* Styling Tabs agar menarik */
    div.stTabs [data-baseweb="tab-list"] { 
        gap: 10px; padding: 10px; background-color: rgba(255, 255, 255, 0.5); 
        border-radius: 10px; margin-top: 10px;
    }
    div.stTabs [data-baseweb="tab"] {
        background-color: white; border-radius: 8px; padding: 10px 20px; 
        font-weight: bold; color: #0369a1; border: 1px solid #bae6fd;
    }
    div.stTabs [aria-selected="true"] { background-color: #0284c7; color: white; }

    /* Gaya Node Bagan */
    .node { 
        padding: 12px; border-radius: 12px; border: 2px solid #0369a1; 
        background: #f0f9ff; text-align: center; margin: 10px 0; 
        font-weight: bold; font-size: 1rem; color: #0c4a6e; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .result-node { background: #dcfce7; border-color: #16a34a; color: #166534; border-style: double; border-width: 4px; }
    
    /* Simulator Tabung */
    .tube-body {
        width: 60px; height: 180px; border: 4px solid #334155; border-radius: 0 0 35px 35px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 20px auto;
    }
    .liquid-fill { position: absolute; bottom: 0; width: 100%; transition: all 1.8s ease-in-out; }
    .pellet-fill { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 30px 30px; transition: all 1.8s ease-in-out; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI HELPER ---
def render_tube(liq, pel=None, h=0):
    p_html = f'<div class="pellet-fill" style="height:{h}px; background:{pel};"></div>' if pel else ""
    st.markdown(f'<div class="tube-body"><div class="liquid-fill" style="height:75%; background:{liq}; opacity:0.7;"></div>{p_html}</div>', unsafe_allow_html=True)

# --- HEADER UTAMA ---
st.markdown('<h1 class="main-title">🧪 Aplikasi Lab Virtual: Analisis Kualitatif Ion</h1>', unsafe_allow_html=True)

# --- SISTEM TAB NAVIGASI ---
tab1, tab2, tab3 = st.tabs(["📍 Bagan Pemisahan (Mind Map)", "🧪 Simulasi & Reaksi Kation", "📝 Analisis Anion"])

# --- TAB 1: MIND MAP INTERAKTIF (LENGKAP HINGGA AKHIR) ---
with tab1:
    st.info("Klik tombol pada setiap tahap untuk menelusuri alur bagan hingga uji spesifik kation [1].")
    
    # Root: Campuran Contoh
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
                    # LEVEL 3 GOL I: NH4OH Berlebih
                    if st.button("➕ Tambahkan NH₄OH Berlebih", key="g1_nh4"):
                        st.markdown('<div class="node result-node">HASIL: Hg(NH₂)Cl + Hg (Putih + Hitam ⚫)</div>', unsafe_allow_html=True)
                        st.markdown('<div class="node">Filtrat Ag(NH₃)₂⁺ Cl⁻</div>', unsafe_allow_html=True)
                        if st.button("⚪ Uji Ag⁺ (+ HNO₃)", key="test_ag"):
                            st.markdown('<div class="node result-node">IDENTIFIKASI: AgCl (Endapan Putih ⚪)</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="node" style="background:#dcfce7;">Larutan Filtrat (Gol III, IV, V)</div>', unsafe_allow_html=True)
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
                            if st.button("⚪ Uji Al³⁺ (+ HCl)", key="test_al"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: Al(OH)₃ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Al³⁺ (+ Na₂CO₃)", key="test_al2"):
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
                            # LEVEL 4 GOL IV: Sr & Ca
                            if st.button("⚪ Identifikasi Sr²⁺ (+ Na₂CO₃)", key="test_sr"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: SrCO₃ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)
                            if st.button("⚪ Identifikasi Ca²⁺ (+ Asam/NH₄OH/Oksalat)", key="test_ca"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: CaC₂O₄ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)

# --- TAB 2: SIMULASI & REAKSI KATION ---
with tab2:
    st.subheader("🧪 Simulasi Pengendapan Kation Golongan 1-4")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol == "Golongan I":
        st.markdown('<div class="node">Alur: Sampel → HCl → Sentrifugasi → Endapan Putih [1]</div>', unsafe_allow_html=True)
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("🔥 Jalankan Simulasi"):
            render_tube("rgba(200,230,255,0.4)", "white", 45)
            st.success("Terbentuk endapan putih klorida.")

    elif gol == "Golongan III":
        st.markdown('<div class="node">Alur: Filtrat → NH₄OH → NaOH → HNO₃ + SCN⁻ [1]</div>', unsafe_allow_html=True)
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
        if st.button("🔴 Uji Spesifik Fe³⁺"):
            render_tube("#991b1b")
            st.info("Larutan berubah menjadi merah darah.")

    elif gol == "Golongan IV":
        st.warning("Identifikasi Golongan IV (Penyajian Baris Vertikal sesuai [1]):")
        st.write("### 1. Barium (Ba²⁺)")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        render_tube("rgba(255,255,224,0.3)", "yellow", 40)
        st.write("---")
        st.write("### 2. Stronsium (Sr²⁺)")
        st.latex(r"Sr^{2+} + CO_3^{2-} \rightarrow SrCO_3(s) \downarrow \text{ (Putih)}")
        st.write("---")
        st.write("### 3. Kalsium (Ca²⁺)")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

# --- TAB 3: ANALISIS ANION ---
with tab3:
    st.subheader("📝 Analisis Anion Spesifik")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(255,255,255,0.2)", "white", 35)
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)}")
        st.caption("Jika KI berlebih: HgI₂ + 2I⁻ → [HgI₄]²⁻ (Larutan Kuning)")
        render_tube("yellow", "#ef4444", 45)
    elif anion == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("Hasil: Terbentuk gelembung gas CO₂.")
    elif anion == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(200,230,255,0.2)", "white", 40)
