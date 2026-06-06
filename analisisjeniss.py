import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Kation Pro", layout="wide")

# --- CSS: TEMA, POSISI TENGAH, & ANIMASI BERGERAK ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ff; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .center-box { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-top: 20px; }
    
    /* Animasi Api (Flame Test) */
    .flame-container { display: flex; justify-content: center; align-items: flex-end; height: 80px; margin: 10px; }
    .flame {
        width: 35px; height: 35px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); opacity: 0.8; } 100% { transform: rotate(-45deg) scale(1.15); opacity: 1; } }
    
    /* Animasi Sentrifugasi Berputar */
    .spin-loader {
        border: 8px solid #f3f3f3; border-top: 8px solid #1565c0;
        border-radius: 50%; width: 60px; height: 60px;
        animation: spin 1s linear infinite; margin: 20px auto;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi */
    .tube-wrapper { display: flex; justify-content: center; margin: 15px 0; }
    .tube {
        width: 50px; height: 160px; border: 3px solid #333; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: height 1s; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def render_flame(color):
    st.markdown(f'<div class="flame-container"><div class="flame" style="background:{color}; box-shadow:0 0 15px {color};"></div></div>', unsafe_allow_html=True)

def show_tube(liq_color, pellet_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{pellet_color};"></div>' if pellet_color else ""
    st.markdown(f'<div class="tube-wrapper"><div class="tube"><div class="liquid" style="height:70%; background:{liq_color}; opacity:0.6;"></div>{p_html}</div></div>', unsafe_allow_html=True)

def play_sentrifugasi():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="spin-loader"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 Menyeimbangkan tabung dan memutar pada 3000 rpm...</center>", unsafe_allow_html=True)
        time.sleep(2)
    placeholder.empty()
    st.success("✅ Pemisahan Selesai!")

# --- UI UTAMA (DISETTING KE TENGAH) ---
st.markdown('<h1 class="main-title">🧪 Aplikasi Lab Virtual: Analisis Kation Pro</h1>', unsafe_allow_html=True)

# PERBAIKAN ERROR: Menyamakan jumlah variabel (3) dengan jumlah kolom (3) [2]
col_side_l, col_center, col_side_r = st.columns([1, 2])

with col_center:
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    
    # 1. TAMPILAN MIND MAP (Source 1)
    st.subheader("📍 Mind Map Alur Pemisahan")
    try:
        # Ganti nama file sesuai dengan file image Anda
        st.image("NotebookLM Mind Map (1).png", caption="Bagan Alir Pemisahan Kation Gol I - V", use_column_width=True)
    except:
        st.warning("⚠️ File gambar 'NotebookLM Mind Map (1).png' tidak ditemukan.")

    st.write("---")
    
    # 2. TOOLS INTERAKTIF
    st.subheader("🛠️ Alat Analisis & Simulasi Reaksi")
    tab1, tab2, tab3, tab4 = st.tabs(["🔹 Gol I", "🔹 Gol III", "🔥 Gol IV", "🧪 Anion"])

    with tab1:
        st.info("Pemisahan Golongan I menggunakan HCl encer.")
        if st.button("Uji Golongan I"):
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \text{ (Endapan Putih)}")
            play_sentrifugasi()
            st.write("Hasil: Terbentuk **pellet putih** (AgCl, PbCl₂, Hg₂Cl₂).")
            show_tube("rgba(200,230,255,0.3)", "white", 40)
            
    with tab2:
        st.info("Pemisahan Golongan III (Fe³⁺, Al³⁺) menggunakan NH₄OH.")
        if st.button("Uji Besi (Fe3+)"):
            # Berdasarkan Mind Map [1]
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
            st.write("Hasil: Larutan berubah warna menjadi **merah darah**.")
            show_tube("#b71c1c", tinggi_pellet=0)

    with tab3:
        st.info("Uji Nyala dan Identifikasi Golongan IV (Ba²⁺, Sr²⁺, Ca²⁺).")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.caption("Barium (Ba2+)")
            render_flame("#adff2f") # Hijau Apel
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4 \text{ (Kuning)}")
        with c2:
            st.caption("Stronsium (Sr2+)")
            render_flame("#ff0000") # Merah Tua
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4 \text{ (Putih)}")
        with c3:
            st.caption("Kalsium (Ca2+)")
            render_flame("#ff4500") # Merah Bata
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4 \text{ (Putih)}")

    with tab4:
        st.info("Identifikasi Anion Spesifik.")
        anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)"])
        if anion == "Iodida (I-)":
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \text{ (Endapan Merah)}")
            show_tube("rgba(255,255,255,0.3)", "red", 30)
        elif anion == "Klorida (Cl-)":
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \text{ (Endapan Putih)}")
            show_tube("rgba(255,255,255,0.3)", "white", 30)

    st.markdown('</div>', unsafe_allow_html=True)
