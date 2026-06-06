import streamlit as st
import time

# --- KONFIGURASI HALAMAN & CSS ---
st.set_page_config(page_title="Pro-Lab: Analisis Ion Interaktif", layout="wide")

st.markdown("""
    <style>
    /* Menghilangkan padding putih di bawah judul */
    .block-container { padding-top: 1.5rem; padding-bottom: 1rem; }
    
    /* Background Vibrant & Menarik */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    
    /* Header Utama */
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 20px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 20px;
    }
    
    /* Gaya Kotak Bagan (Nodes) */
    .node { 
        padding: 12px; border-radius: 10px; border: 2px solid #0369a1; 
        background: #f0f9ff; text-align: center; margin: 10px 0; 
        font-weight: bold; font-size: 0.95rem; color: #0c4a6e;
    }
    .result-node { background: #dcfce7; border-color: #16a34a; color: #166534; border-style: double; }
    .reagent-btn { background: #fef3c7 !important; border-color: #d97706 !important; }
    
    /* Simulator Tabung & Animasi */
    .tube-body {
        width: 50px; height: 160px; border: 3px solid #334155; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 15px auto;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: all 1.5s ease-in-out; }
    
    .spin-loader {
        width: 60px; height: 60px; border: 6px dashed #0284c7; border-top: 6px solid #f43f5e;
        border-radius: 50%; animation: spin 0.8s linear infinite; margin: 15px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def play_centrifuge():
    p = st.empty()
    with p.container():
        st.markdown('<div class="spin-loader"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 RPM (Pemisahan Pellet & Supernatan)...</b></center>", unsafe_allow_html=True)
        time.sleep(1.5)
    p.empty()

def render_tube(liq_color, p_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-body"><div class="liquid" style="height:70%; background:{liq_color}; opacity:0.6;"></div>{p_html}</div>', unsafe_allow_html=True)

# --- NAVIGASI SIDEBAR ---
st.sidebar.title("🎨 Menu Laboratorium")
page = st.sidebar.radio("Navigasi Halaman:", ["Halaman 1: Mind Map Interaktif", "Halaman 2: Simulasi Kation", "Halaman 3: Analisis Anion"])

st.markdown('<h1 class="main-title">Aplikasi Lab Virtual: Analisis Kualitatif Ion</h1>', unsafe_allow_html=True)

# --- HALAMAN 1: MIND MAP INTERAKTIF (LENGKAP HINGGA AKHIR) ---
if page == "Halaman 1: Mind Map Interaktif":
    st.subheader("📍 Diagram Alir Pemisahan Kation (Bisa Diklik)")
    st.info("Klik tombol pereaksi untuk menelusuri bagan hingga hasil uji spesifik setiap kation.")
    
    # Root Node
    st.markdown('<div class="node">Campuran Contoh Kation (Gol I - V)</div>', unsafe_allow_html=True)
    
    # LEVEL 1: HCl Encer
    if st.button("➕ Tambahkan HCl Encer", key="gol1", type="primary"):
        st.divider()
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="node" style="background:#fee2e2;">Endapan Gol I (AgCl, PbCl₂, Hg₂Cl₂)</div>', unsafe_allow_html=True)
            # LEVEL 2: H2O Panas
            if st.button("➕ Tambahkan H₂O Panas", key="h2o_hot"):
                st.write("---")
                c1a, c1b = st.columns(2)
                with c1a:
                    st.markdown('<div class="node">Larutan Pb²⁺</div>', unsafe_allow_html=True)
                    if st.button("🟡 Uji Spesifik Pb²⁺ (+K₂CrO₄)", key="test_pb"):
                        st.markdown('<div class="node result-node">HASIL AKHIR: PbCrO₄ (Endapan Kuning 🟡)</div>', unsafe_allow_html=True)
                with c1b:
                    st.markdown('<div class="node">Residu AgCl, Hg₂Cl₂</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan NH₄OH Berlebih", key="nh4oh_gol1"):
                        st.markdown('<div class="node result-node">HASIL: Hg(NH₂)Cl + Hg (Putih + Hitam ⚫)</div>', unsafe_allow_html=True)
                        st.markdown('<div class="node result-node">HASIL: Ag(NH₃)₂⁺ (+HNO₃ → AgCl Putih ⚪)</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="node" style="background:#dcfce7;">Larutan Filtrat (Gol III, IV, V)</div>', unsafe_allow_html=True)
            # LEVEL 2: NH4OH Berlebih
            if st.button("➕ Tambahkan NH₄OH Berlebih", key="gol3"):
                st.write("---")
                c2a, c2b = st.columns(2)
                with c2a:
                    st.markdown('<div class="node">Endapan Gol III (Al(OH)₃, Fe(OH)₃)</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan NaOH", key="naoh_gol3"):
                        st.write("---")
                        c2a1, c2a2 = st.columns(2)
                        with c2a1:
                            st.markdown('<div class="node">Residu Fe(OH)₃</div>', unsafe_allow_html=True)
                            if st.button("🔴 Uji Spesifik Fe³⁺ (+HNO₃ + SCN⁻)", key="test_fe"):
                                st.markdown('<div class="node result-node">HASIL AKHIR: Fe(SCN)₃ (Larutan Merah Darah 🔴)</div>', unsafe_allow_html=True)
                        with c2a2:
                            st.markdown('<div class="node">Filtrat Al(OH)₄⁻</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Spesifik Al³⁺ (+HCl)", key="test_al"):
                                st.markdown('<div class="node result-node">HASIL AKHIR: Al(OH)₃ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)
                
                with c2b:
                    st.markdown('<div class="node">Larutan Gol IV (Ba²⁺, Sr²⁺, Ca²⁺)</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan K₂CrO₄", key="gol4"):
                        st.write("---")
                        c2b1, c2b2 = st.columns(2)
                        with c2b1:
                            st.markdown('<div class="node result-node">HASIL AKHIR: BaCrO₄ (Endapan Kuning 🟡)</div>', unsafe_allow_html=True)
                        with c2b2:
                            st.markdown('<div class="node">Larutan Sr²⁺, Ca²⁺</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Spesifik Sr & Ca", key="test_srca"):
                                st.markdown('<div class="node result-node">Sr²⁺ (+Na₂CO₃ → SrCO₃ Putih ⚪)</div>', unsafe_allow_html=True)
                                st.markdown('<div class="node result-node">Ca²⁺ (+H₂C₂O₄ → CaC₂O₄ Putih ⚪)</div>', unsafe_allow_html=True)

# --- HALAMAN 2: SIMULASI KATION ---
elif page == "Halaman 2: Simulasi Kation":
    st.subheader("🧪 Simulasi Pengendapan & Reaksi Kation")
    gol_pilih = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    # Kembali menampilkan cuplikan bagan per golongan [1]
    if gol_pilih == "Golongan I":
        st.markdown('<div class="node">Alur: Sampel → HCl → Sentrifugasi → Pellet Putih</div>', unsafe_allow_html=True)
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("Jalankan Pemisahan"):
            play_centrifuge()
            tube_viz("rgba(200,230,255,0.4)", "white", 45)
            st.success("Endapan klorida (AgCl, PbCl2, Hg2Cl2) terpisah sempurna [2].")

    elif gol_pilih == "Golongan III":
        st.markdown('<div class="node">Alur: Filtrat → NH4OH → NaOH → Fe(SCN)3 (Merah)</div>', unsafe_allow_html=True)
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
        if st.button("Uji Spesifik Fe3+"):
            tube_viz("#991b1b")
            st.info("Hasil pengamatan menunjukkan warna merah darah [1, 3].")

    elif gol_pilih == "Golongan IV":
        st.warning("Penyajian Identifikasi Golongan IV (Vertikal):")
        st.markdown("### 1. Barium (Ba²⁺)")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        tube_viz("rgba(255,255,224,0.3)", "yellow", 35)
        
        st.markdown("---")
        st.markdown("### 2. Stronsium (Sr²⁺)")
        st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
        
        st.markdown("---")
        st.markdown("### 3. Kalsium (Ca²⁺)")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

# --- HALAMAN 3: ANALISIS ANION ---
elif page == "Halaman 3: Analisis Anion":
    st.subheader("📝 Identifikasi Anion Spesifik (Tabel 6.1)")
    an_pilih = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    
    if an_pilih == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        tube_viz("rgba(255,255,255,0.2)", "white", 35)
    elif an_pilih == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)}")
        st.write("Catatan: Jika KI berlebih, endapan larut menjadi larutan kuning [4].")
        tube_viz("yellow", "#ef4444", 40)
    elif an_pilih == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("Hasil: Terbentuk gas (gelembung) [4].")
    elif an_pilih == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
        tube_viz("rgba(200,230,255,0.2)", "white", 40)

    with st.expander("📸 Lihat Tabel Hasil Percobaan Asli"):
        st.image("ef5bf4a7-66fb-4ef1-ac42-491909eb0ee4.jpeg", use_column_width=True)
