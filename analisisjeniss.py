import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Vibrant Virtual Lab: Ion Analysis", layout="wide")

# --- CSS: TEMA PENUH WARNA & ANIMASI NYATA ---
st.markdown("""
    <style>
    /* Background Gradient Vibrant */
    .stApp { background: linear-gradient(120deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    
    /* Header Utama yang Menarik */
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 30px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 8px solid #0c4a6e; font-family: 'Arial Black', sans-serif;
    }
    
    /* Kartu Konten Berwarna */
    .glass-card { background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); padding: 30px; border-radius: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 2px solid #bae6fd; }

    /* Animasi Centrifuge */
    .spin-vibrant {
        width: 80px; height: 80px; border: 8px dashed #0284c7; border-top: 8px solid #f43f5e;
        border-radius: 50%; animation: spin 0.6s linear infinite; margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Simulator Tabung Reaksi */
    .tube-box { display: flex; flex-direction: column; align-items: center; margin: 20px 0; }
    .tube-body {
        width: 65px; height: 190px; border: 4px solid #334155; border-radius: 0 0 35px 35px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .liquid-fill { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet-fill { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 30px 30px; transition: all 1.5s ease-in-out; }
    
    /* Animasi Api Flicker */
    .flame-vibrant {
        width: 40px; height: 40px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.4s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.3); opacity: 0.8; } }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI KOMPONEN ---
def tube_simulator(liq_color, p_color=None, p_height=0, is_cloudy=False):
    op = "0.5" if is_cloudy else "0.8"
    p_html = f'<div class="pellet-fill" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-box"><div class="tube-body"><div class="liquid-fill" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def play_centrifuge():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="spin-vibrant"></div>', unsafe_allow_html=True)
        st.write("<center><b>🌀 Memutar pada 3000 RPM (Pemisahan Pellet & Supernatan)...</b></center>", unsafe_allow_html=True)
        time.sleep(2)
    placeholder.empty()

# --- SIDEBAR NAVIGASI ---
st.sidebar.markdown("<h2 style='text-align: center;'>🎨 Virtual Lab Menu</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigasi Halaman:", ["Halaman 1: Full Mind Map", "Halaman 2: Kation (Animasi & Reaksi)", "Halaman 3: Analisis Anion"])

st.markdown('<h1 class="main-title">Interactive Qualitative Analysis Pro</h1>', unsafe_allow_html=True)

# --- HALAMAN 1: FULL MIND MAP ---
if page == "Halaman 1: Full Mind Map":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📍 Bagan Pemisahan Kation Lengkap (Awal - Akhir)")
    try:
        # Menampilkan bagan alir dari sumber [1]
        st.image("bagan pemisahan kation.png", use_column_width=True, caption="Mind Map Pemisahan Campuran Kation Gol I - V")
    except:
        st.error("Gagal memuat gambar 'bagan pemisahan kation.png'.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- HALAMAN 2: KATION (ANIMASI & REAKSI) ---
elif page == "Halaman 2: Kation (Animasi & Reaksi)":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧪 Simulator Pengendapan Kation Golongan 1-5")
    
    gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol == "Golongan I":
        st.write("**Prosedur:** Penambahan HCl encer untuk memisahkan Ag⁺, Pb²⁺, Hg₂²⁺ [2].")
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        if st.button("🔥 Jalankan Sentrifugasi 3000 RPM"):
            play_centrifuge()
            st.success("✅ Terbentuk Pellet Putih!")
            tube_simulator("rgba(200,230,255,0.4)", "white", 45) # Pellet putih [2]

    elif gol == "Golongan III":
        st.write("**Prosedur:** Penambahan NH₄OH berlebih menghasilkan endapan hidroksida [1, 3].")
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
        if st.button("🔴 Uji Spesifik Fe3+"):
            tube_simulator("#991b1b") # Merah darah [3]
            st.write("Hasil: Larutan berubah menjadi Merah Darah.")

    elif gol == "Golongan IV":
        st.write("**Identifikasi Baris ke Bawah (Uji Nyala & Endapan) [3]:**")
        st.markdown("### 1. Barium (Ba²⁺)")
        st.markdown('<div class="flame-vibrant" style="background:#adff2f; box-shadow:0 0 15px #adff2f;"></div>', unsafe_allow_html=True)
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
        
        st.divider()
        st.markdown("### 2. Stronsium (Sr²⁺)")
        st.markdown('<div class="flame-vibrant" style="background:#f43f5e; box-shadow:0 0 15px #f43f5e;"></div>', unsafe_allow_html=True)
        st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- HALAMAN 3: ANALISIS ANION ---
elif page == "Halaman 3: Analisis Anion":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧪 Identifikasi Anion Berdasarkan Tabel 6.1")
    
    anion = st.tabs(["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    
    with anion:
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        st.write("Pengamatan: Endapan Putih [4].")
        tube_simulator("rgba(255,255,255,0.2)", "white", 35)

    with anion[2]:
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)}")
        st.write("Pengamatan: Endapan Merah Jingga. Kelebihan KI melarutkan endapan [4].")
        tube_simulator("yellow", "#ef4444", 40) # Merah HgI2 [4]

    with anion[3]:
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("Pengamatan: Terbentuk gelembung gas [4].")

    with anion[5]:
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
        st.write("Pengamatan: Endapan Putih [4].")
        tube_simulator("rgba(200,230,255,0.2)", "white", 40)

    st.markdown('</div>', unsafe_allow_html=True)
    
    # Menampilkan tabel pengamatan anion asli [4]
    with st.expander("🖼️ Lihat Data Tabel Pengamatan Asli"):
        st.image("ef5bf4a7-66fb-4ef1-ac42-491909eb0ee4.jpeg", use_column_width=True)
