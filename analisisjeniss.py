import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Vibrant Virtual Lab Ion", layout="wide")

# --- CSS: VIBRANT, HIDE PADDING, & ANIMASI ---
st.markdown("""
    <style>
    /* Menghilangkan spasi putih di bawah judul & padding berlebih */
    .block-container { padding-top: 2rem; padding-bottom: 0rem; }
    div.stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    
    /* Tema Warna Vibrant */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 20px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 0px; 
    }
    
    /* Gaya Bagan (Flowchart Node) */
    .node { 
        padding: 12px; border-radius: 10px; border: 2px solid #0369a1; 
        background: #e0f2fe; text-align: center; margin: 5px 0; 
        font-weight: bold; cursor: pointer; transition: 0.3s;
    }
    .node:hover { background: #bae6fd; transform: scale(1.02); }
    .arrow { text-align: center; font-size: 20px; color: #64748b; margin: -5px 0; }

    /* Animasi Centrifuge */
    .spin-loader {
        width: 60px; height: 60px; border: 6px dashed #0284c7; border-top: 6px solid #f43f5e;
        border-radius: 50%; animation: spin 0.8s linear infinite; margin: 15px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Simulator Tabung Reaksi */
    .tube-body {
        width: 55px; height: 160px; border: 3px solid #334155; border-radius: 0 0 30px 30px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 10px auto;
    }
    .liquid-fill { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet-fill { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 25px 25px; transition: all 1.5s ease-in-out; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI HELPER ---
def show_centrifuge():
    p = st.empty()
    with p.container():
        st.markdown('<div class="spin-loader"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 RPM (1-2 Menit)...</b></center>", unsafe_allow_html=True)
        time.sleep(2)
    p.empty()

def render_tube(liq, pel=None, h=0):
    p_html = f'<div class="pellet-fill" style="height:{h}px; background:{pel};"></div>' if pel else ""
    st.markdown(f'<div class="tube-body"><div class="liquid-fill" style="height:75%; background:{liq}; opacity:0.7;"></div>{p_html}</div>', unsafe_allow_html=True)

# --- NAVIGASI SIDEBAR ---
st.sidebar.title("🎨 Menu Navigasi")
hal = st.sidebar.radio("Pilih Halaman:", ["Bagan Interaktif", "Kation: Reaksi & Animasi", "Anion: Reaksi & Tabel"])

st.markdown('<h1 class="main-title">Virtual Lab: Analisis Kualitatif Ion</h1>', unsafe_allow_html=True)

# --- HALAMAN 1: BAGAN INTERAKTIF (MIND MAP) ---
if hal == "Bagan Interaktif":
    st.subheader("📍 Diagram Alir Pemisahan Kation (Bisa Diklik)")
    st.info("Klik tombol pada setiap tahap untuk melihat detail prosesnya.")
    
    # Root
    if st.button("🧬 Campuran Contoh Gol I - V"):
        st.markdown('<div class="node">Input: Larutan Sampel Campuran</div>', unsafe_allow_html=True)
        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🟦 + HCl encer (Gol I)"):
                st.markdown('<div class="node" style="background:#fecaca;">Endapan Gol I (AgCl, PbCl2, Hg2Cl2)</div>', unsafe_allow_html=True)
                st.write("Hasil: Endapan Putih [1].")
        with c2:
            if st.button("🟩 + NH4OH (Gol III & IV)"):
                st.markdown('<div class="node" style="background:#bbf7d0;">Larutan (Al3+, Fe3+, Ba2+, Sr2+, Ca2+)</div>', unsafe_allow_html=True)
                st.write("Filtrat dilanjutkan ke pemisahan berikutnya [2].")

    st.divider()
    st.image("bagan pemisahan kation.png", caption="Referensi Mind Map Lengkap (Source 5)", use_column_width=True)

# --- HALAMAN 2: KATION (REAKSI & ANIMASI) ---
elif hal == "Kation: Reaksi & Animasi":
    st.subheader("🧪 Simulasi Pengendapan Kation Golongan 1-5")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    # Menampilkan potongan bagan per golongan
    if gol == "Golongan I":
        st.markdown('<div class="node">Bagan: Sampel → +HCl → Pellet Putih</div>', unsafe_allow_html=True)
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("🔥 Jalankan Sentrifugasi"):
            show_centrifuge()
            render_tube("rgba(200,230,255,0.4)", "white", 45)
            st.success("Endapan AgCl, PbCl2, Hg2Cl2 terbentuk di bawah tabung [1].")

    elif gol == "Golongan III":
        st.markdown('<div class="node">Bagan: Supernatan → +NH4OH → Fe(OH)3 & Al(OH)3</div>', unsafe_allow_html=True)
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
        if st.button("🔴 Uji Besi (Fe3+)"):
            render_tube("#991b1b")
            st.write("Terbentuk kompleks warna merah darah [2].")

    elif gol == "Golongan IV":
        st.markdown('<div class="node">Bagan: Larutan → +K2CrO4 → BaCrO4 (Kuning)</div>', unsafe_allow_html=True)
        st.warning("Identifikasi Golongan IV (Lengkap & Vertikal sesuai Source 4 & 5):")
        
        # Penjelasan Vertikal Lengkap
        st.write("### 1. Barium (Ba2+)")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        st.write("Hasil: Endapan Kuning [2].")
        
        st.write("### 2. Stronsium (Sr2+)")
        st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
        st.write("Atau dengan $Na_2CO_3 \\rightarrow SrCO_3$ (Putih) [3].")
        
        st.write("### 3. Kalsium (Ca2+)")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")
        st.write("Menggunakan pereaksi $H_2C_2O_4$ dan $NH_4OH$ [3].")

# --- HALAMAN 3: ANION (REAKSI & TABEL) ---
elif hal == "Anion: Reaksi & Tabel":
    st.subheader("📝 Analisis Anion (Berdasarkan Tabel 6.1)")
    
    anion_pilih = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
    
    if anion_pilih == "Klorida (Cl-)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(255,255,255,0.2)", "white", 35)
    
    elif anion_pilih == "Iodida (I-)":
        # Perbaikan Stoikiometri sesuai Source 5
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)}")
        st.latex(r"HgI_2 + 2I^- \rightarrow [HgI_4]^{2-} \text{ (Larutan Kuning)}")
        st.info("Catatan: Jika KI berlebih, endapan merah larut kembali menjadi kuning [4].")
        render_tube("yellow", "#ef4444", 40)
        
    elif anion_pilih == "Karbonat (CO3 2-)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("Pengamatan: Terbentuk gelembung gas [4].")
        
    elif anion_pilih == "Sulfat (SO4 2-)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
        render_tube("rgba(200,230,255,0.2)", "white", 40)

    st.divider()
    with st.expander("📸 Lihat Tabel Hasil Percobaan Asli (Source 7)"):
        st.image("ef5bf4a7-66fb-4ef1-ac42-491909eb0ee4.jpeg", use_column_width=True)
        
