import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Vibrant Lab: Analisis Kation & Anion", layout="wide")

# --- CSS: VIBRANT & HIDE TOP PADDING ---
st.markdown("""
    <style>
    /* Menghilangkan padding putih di bawah judul */
    .block-container { padding-top: 1rem; }
    
    /* Background Vibrant */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    
    /* Header Utama */
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 20px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 20px;
    }
    
    /* Gaya Node Bagan */
    .node { 
        padding: 10px; border-radius: 8px; border: 2px solid #0369a1; 
        background: #f0f9ff; text-align: center; margin: 5px 0; 
        font-weight: bold; font-size: 0.9rem;
    }
    .result-node { background: #dcfce7; border-color: #16a34a; color: #166534; }
    
    /* Animasi Centrifuge */
    .spin-vibrant {
        width: 60px; height: 60px; border: 6px dashed #0284c7; border-top: 6px solid #f43f5e;
        border-radius: 50%; animation: spin 0.8s linear infinite; margin: 15px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Simulator Tabung */
    .tube-body {
        width: 50px; height: 150px; border: 3px solid #334155; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 10px auto;
    }
    .liquid-fill { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease; }
    .pellet-fill { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: all 1.5s ease; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI ---
def centrifuge_anim():
    p = st.empty()
    with p.container():
        st.markdown('<div class="spin-vibrant"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 RPM Berlangsung...</b></center>", unsafe_allow_html=True)
        time.sleep(1.5)
    p.empty()

def tube_viz(liq, pel=None, h=0):
    p_html = f'<div class="pellet-fill" style="height:{h}px; background:{pel};"></div>' if pel else ""
    st.markdown(f'<div class="tube-body"><div class="liquid-fill" style="height:70%; background:{liq}; opacity:0.6;"></div>{p_html}</div>', unsafe_allow_html=True)

# --- NAVIGASI ---
st.sidebar.title("🎨 Menu Pro-Lab")
page = st.sidebar.radio("Navigasi:", ["Halaman 1: Bagan Interaktif", "Halaman 2: Kation (Simulasi)", "Halaman 3: Anion (Analisis)"])

st.markdown('<h1 class="main-title">Aplikasi Lab Virtual Analisis Ion</h1>', unsafe_allow_html=True)

# --- HALAMAN 1: BAGAN INTERAKTIF (LENGKAP SAMPAI AKHIR) ---
if page == "Halaman 1: Bagan Interaktif":
    st.subheader("📍 Mind Map Interaktif: Telusuri Alur Hingga Akhir")
    st.info("Klik tombol di setiap langkah untuk membuka percabangan analisis [1].")
    
    st.markdown('<div class="node">Campuran Contoh Gol I - V</div>', unsafe_allow_html=True)
    
    if st.button("🔵 Tambahkan HCl encer"):
        st.write("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="node" style="background:#fee2e2;">Endapan Gol I (AgCl, PbCl2, Hg2Cl2)</div>', unsafe_allow_html=True)
            if st.button("➕ Tambahkan H2O Panas"):
                st.write("---")
                c1a, c1b = st.columns(2)
                with c1a:
                    st.markdown('<div class="node">Larutan Pb2+</div>', unsafe_allow_html=True)
                    if st.button("🟡 Uji Pb2+ (+K2CrO4)"):
                        st.markdown('<div class="node result-node">HASIL: PbCrO4 (Endapan Kuning)</div>', unsafe_allow_html=True)
                with c1b:
                    st.markdown('<div class="node">Residu AgCl, Hg2Cl2</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan NH4OH Berlebih"):
                        st.markdown('<div class="node result-node">HASIL: Hg(NH2)Cl + Hg (Putih + Hitam)</div>', unsafe_allow_html=True)
                        st.markdown('<div class="node result-node">HASIL: Ag(NH3)2+ Cl- (+HNO3 -> AgCl Putih)</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="node" style="background:#dcfce7;">Larutan Filtrat (Gol III, IV, V)</div>', unsafe_allow_html=True)
            if st.button("🟢 Tambahkan NH4OH Berlebih"):
                st.write("---")
                c2a, c2b = st.columns(2)
                with c2a:
                    st.markdown('<div class="node">Endapan Gol III (Al(OH)3, Fe(OH)3)</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan NaOH"):
                        st.write("---")
                        c2a1, c2a2 = st.columns(2)
                        with c2a1:
                            st.markdown('<div class="node">Residu Fe(OH)3</div>', unsafe_allow_html=True)
                            if st.button("🔴 Uji Fe3+ (+SCN-)"):
                                st.markdown('<div class="node result-node">HASIL: Fe(SCN)3 (Merah Darah)</div>', unsafe_allow_html=True)
                        with c2a2:
                            st.markdown('<div class="node">Filtrat Al(OH)4-</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Al3+ (+HCl)"):
                                st.markdown('<div class="node result-node">HASIL: Al(OH)3 (Putih)</div>', unsafe_allow_html=True)
                with c2b:
                    st.markdown('<div class="node">Larutan Gol IV (Ba2+, Sr2+, Ca2+)</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan K2CrO4"):
                        st.write("---")
                        c2b1, c2b2 = st.columns(2)
                        with c2b1:
                            st.markdown('<div class="node result-node">HASIL: BaCrO4 (Kuning)</div>', unsafe_allow_html=True)
                        with c2b2:
                            st.markdown('<div class="node">Larutan Sr2+, Ca2+</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Akhir Sr & Ca"):
                                st.markdown('<div class="node result-node">Sr2+ -> SrCO3 (Putih)</div>', unsafe_allow_html=True)
                                st.markdown('<div class="node result-node">Ca2+ -> CaC2O4 (Putih)</div>', unsafe_allow_html=True)

# --- HALAMAN 2: KATION SIMULASI ---
elif page == "Halaman 2: Kation (Simulasi)":
    st.subheader("🧪 Simulasi Pengendapan & Reaksi Kation")
    gol_pilih = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol_pilih == "Golongan I":
        st.markdown('<div class="node">Alur: Sampel → HCl → Sentrifugasi [2]</div>', unsafe_allow_html=True)
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("Jalankan Pemisahan"):
            centrifuge_anim()
            tube_viz("rgba(200,230,255,0.4)", "white", 45)
            st.success("Endapan Gol I terpisah dari supernatan.")

    elif gol_pilih == "Golongan III":
        st.markdown('<div class="node">Alur: Filtrat → NH4OH → NaOH [1, 3]</div>', unsafe_allow_html=True)
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
        if st.button("Uji Fe3+"):
            tube_viz("#991b1b")
            st.write("Larutan berubah menjadi merah darah.")

    elif gol_pilih == "Golongan IV":
        st.info("Identifikasi Golongan IV (Penyajian Baris Vertikal) [3]:")
        st.markdown("### 1. Barium (Ba2+)")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
        tube_viz("rgba(255,255,224,0.4)", "yellow", 35)
        
        st.markdown("---")
        st.markdown("### 2. Stronsium (Sr2+)")
        st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
        
        st.markdown("---")
        st.markdown("### 3. Kalsium (Ca2+)")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \text{ (Putih)}")

# --- HALAMAN 3: ANION ---
elif page == "Halaman 3: Analisis Anion":
    st.subheader("📝 Analisis Anion Berdasarkan Tabel 6.1 [4]")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
    
    if anion == "Klorida (Cl-)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        tube_viz("rgba(255,255,255,0.2)", "white", 35)
    elif anion == "Iodida (I-)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}")
        st.info("Kelebihan KI melarutkan endapan menjadi kompleks kuning.")
        tube_viz("yellow", "#ef4444", 40)
    elif anion == "Karbonat (CO3 2-)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
    elif anion == "Sulfat (SO4 2-)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
        tube_viz("rgba(200,230,255,0.2)", "white", 40)

    with st.expander("📸 Lihat Tabel Hasil Percobaan"):
        st.image("ef5bf4a7-66fb-4ef1-ac42-491909eb0ee4.jpeg", use_column_width=True)
