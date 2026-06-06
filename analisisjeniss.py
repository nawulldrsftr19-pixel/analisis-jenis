import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Lab Virtual: Analisis Ion Lengkap", layout="wide")

# --- CSS: VIBRANT, NO PADDING, & ANIMASI REALISTIK ---
st.markdown("""
    <style>
    /* Menghilangkan celah putih di bawah judul */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    
    /* Background Vibrant */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    
    /* Header Utama */
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 20px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 20px;
    }
    
    /* Gaya Node Bagan (Mind Map) */
    .node { 
        padding: 10px; border-radius: 8px; border: 2px solid #0369a1; 
        background: #f0f9ff; text-align: center; margin: 8px 0; 
        font-weight: bold; font-size: 0.9rem; color: #0c4a6e;
    }
    .result-node { background: #dcfce7; border-color: #16a34a; color: #166534; border-style: double; }
    
    /* Animasi Centrifuge */
    .spin-vibrant {
        width: 60px; height: 60px; border: 6px dashed #0284c7; border-top: 6px solid #f43f5e;
        border-radius: 50%; animation: spin 0.8s linear infinite; margin: 15px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Simulator Tabung */
    .tube-body {
        width: 50px; height: 160px; border: 3px solid #334155; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 10px auto;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: all 1.5s ease-in-out; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def play_centrifuge():
    p = st.empty()
    with p.container():
        st.markdown('<div class="spin-vibrant"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 RPM Sedang Berlangsung...</b></center>", unsafe_allow_html=True)
        time.sleep(1.5)
    p.empty()

def render_tube(liq, pel=None, h=0):
    p_html = f'<div class="pellet" style="height:{h}px; background:{pel};"></div>' if pel else ""
    st.markdown(f'<div class="tube-body"><div class="liquid" style="height:70%; background:{liq}; opacity:0.6;"></div>{p_html}</div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🎨 Menu Pro-Lab")
page = st.sidebar.radio("Pilih Halaman:", ["Halaman 1: Mind Map Interaktif", "Halaman 2: Kation (Reaksi & Animasi)", "Halaman 3: Analisis Anion"])

st.markdown('<h1 class="main-title">Aplikasi Lab Virtual Analisis Ion</h1>', unsafe_allow_html=True)

# --- HALAMAN 1: MIND MAP INTERAKTIF (LENGKAP HINGGA AKHIR) ---
if page == "Halaman 1: Mind Map Interaktif":
    st.subheader("📍 Diagram Alir Pemisahan Kation (Sampai Uji Spesifik)")
    st.info("Klik setiap tombol untuk menelusuri alur bagan hingga hasil akhir [1].")
    
    st.markdown('<div class="node">Campuran Contoh Gol I - V</div>', unsafe_allow_html=True)
    
    # LEVEL 1: HCl Encer
    if st.button("🔵 Tambahkan HCl Encer", key="lvl1", type="primary"):
        st.write("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="node" style="background:#fee2e2;">Endapan Gol I (AgCl, PbCl₂, Hg₂Cl₂)</div>', unsafe_allow_html=True)
            # LEVEL 2 GOL I: H2O Panas
            if st.button("➕ Tambahkan H₂O Panas", key="g1_h2o"):
                st.write("---")
                c1a, c1b = st.columns(2)
                with c1a:
                    st.markdown('<div class="node">Larutan Pb²⁺</div>', unsafe_allow_html=True)
                    if st.button("🟡 Uji Pb²⁺ (+K₂CrO₄)", key="final_pb"):
                        st.markdown('<div class="node result-node">HASIL: PbCrO₄ (Kuning 🟡)</div>', unsafe_allow_html=True)
                with c1b:
                    st.markdown('<div class="node">Residu AgCl, Hg₂Cl₂</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan NH₄OH Berlebih", key="g1_nh4oh"):
                        st.markdown('<div class="node result-node">HASIL: Hg(NH₂)Cl + Hg (Putih + Hitam ⚫)</div>', unsafe_allow_html=True)
                        if st.button("⚪ Uji Ag⁺ (+HNO₃)", key="final_ag"):
                            st.markdown('<div class="node result-node">HASIL: AgCl (Putih ⚪)</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="node" style="background:#dcfce7;">Larutan Filtrat (Gol III, IV, V)</div>', unsafe_allow_html=True)
            # LEVEL 2 GOL III: NH4OH Berlebih
            if st.button("➕ Tambahkan NH₄OH Berlebih", key="lvl2_filtrat"):
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
                            if st.button("🔴 Uji Fe³⁺ (+HNO₃ + SCN⁻)", key="final_fe"):
                                st.markdown('<div class="node result-node">HASIL: Fe(SCN)₃ (Merah Darah 🔴)</div>', unsafe_allow_html=True)
                        with c2a2:
                            st.markdown('<div class="node">Filtrat Al(OH)₄⁻</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Al³⁺ (+HCl)", key="final_al"):
                                st.markdown('<div class="node result-node">HASIL: Al(OH)₃ (Putih ⚪)</div>', unsafe_allow_html=True)
                
                with c2b:
                    st.markdown('<div class="node">Larutan Gol IV (Ba²⁺, Sr²⁺, Ca²⁺)</div>', unsafe_allow_html=True)
                    # LEVEL 3 GOL IV: K2CrO4
                    if st.button("➕ Tambahkan K₂CrO₄", key="g4_k2cro4"):
                        st.write("---")
                        c2b1, c2b2 = st.columns(2)
                        with c2b1:
                            st.markdown('<div class="node result-node">HASIL: BaCrO₄ (Kuning 🟡)</div>', unsafe_allow_html=True)
                        with c2b2:
                            st.markdown('<div class="node">Larutan Sr²⁺, Ca²⁺</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Sr²⁺ & Ca²⁺", key="final_srca"):
                                st.markdown('<div class="node result-node">Sr²⁺ (+Na₂CO₃ → SrCO₃ Putih ⚪)</div>', unsafe_allow_html=True)
                                st.markdown('<div class="node result-node">Ca²⁺ (+H₂C₂O₄ → CaC₂O₄ Putih ⚪)</div>', unsafe_allow_html=True)

# --- HALAMAN 2: SIMULASI KATION ---
elif page == "Halaman 2: Kation (Reaksi & Animasi)":
    st.subheader("🧪 Simulasi Pengendapan Kation")
    gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    # Menampilkan ulang ringkasan bagan per golongan
    if gol == "Golongan I":
        st.markdown('<div class="node">Alur: Sampel → HCl → Sentrifugasi → Endapan Putih [2]</div>', unsafe_allow_html=True)
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("🔥 Jalankan Sentrifugasi"):
            play_centrifuge()
            render_tube("rgba(200,230,255,0.4)", "white", 45)
            st.success("Endapan Gol I terpisah dari supernatan.")

    elif gol == "Golongan III":
        st.markdown('<div class="node">Alur: Filtrat → NH₄OH → NaOH → Uji Spesifik [3]</div>', unsafe_allow_html=True)
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
        if st.button("🔴 Uji Fe³⁺"):
            render_tube("#991b1b")
            st.info("Larutan berubah menjadi merah darah.")

    elif gol == "Golongan IV":
        st.warning("Identifikasi Golongan IV (Penyajian Baris Vertikal [3]):")
        st.write("### 1. Barium (Ba²⁺)")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        render_tube("rgba(255,255,224,0.3)", "yellow", 35)
        
        st.write("### 2. Stronsium (Sr²⁺)")
        st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
        
        st.write("### 3. Kalsium (Ca²⁺)")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

# --- HALAMAN 3: ANALISIS ANION ---
elif page == "Halaman 3: Analisis Anion":
    st.subheader("📝 Identifikasi Anion Spesifik (Berdasarkan Tabel 6.1 [4])")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(255,255,255,0.2)", "white", 35)
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)}")
        st.caption("Jika KI berlebih: HgI₂ + 2I⁻ → [HgI₄]²⁻ (Larutan Kuning)")
        render_tube("yellow", "#ef4444", 40)
    elif anion == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("Hasil: Terbentuk gas (gelembung).")
    elif anion == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(200,230,255,0.2)", "white", 40)

    with st.expander("📸 Lihat Tabel Hasil Percobaan Asli"):
        st.image("ef5bf4a7-66fb-4ef1-ac42-491909eb0ee4.jpeg", use_column_width=True)
