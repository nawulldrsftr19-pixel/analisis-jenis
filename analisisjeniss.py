import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Lab Virtual Sentrifugasi", layout="wide")

# --- CSS: TEMA BIRU, ANIMASI API, & TABUNG ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f4f8; }
    .center-box { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    .main-header { color: #1a73e8; text-align: center; font-family: 'Arial', sans-serif; }
    
    /* Animasi Api Bergerak */
    .flame-box { display: flex; justify-content: center; align-items: flex-end; height: 70px; }
    .flame {
        width: 30px; height: 30px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.2); opacity: 0.8; } }
    
    /* Visualisasi Tabung Reaksi */
    .tube-wrapper { display: flex; justify-content: center; margin: 20px 0; }
    .tube {
        width: 50px; height: 160px; border: 3px solid #333; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s, background-color 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: height 1s; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI KOMPONEN ---
def render_tube(liq_color, pellet_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{pellet_color};"></div>' if pellet_color else ""
    st.markdown(f'<div class="tube-wrapper"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:0.6;"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-box"><div class="flame" style="background:{color}; box-shadow: 0 0 15px {color};"></div></div>', unsafe_allow_html=True)

def play_centrifuge():
    with st.spinner("🌀 Sedang Sentrifugasi (3000 rpm)..."):
        p = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            p.progress(i + 1)
    st.success("✅ Pemisahan Berhasil!")

# --- UI UTAMA (DIBUAT DI TENGAH) ---
st.markdown('<h1 class="main-title">🧪 Aplikasi Analisis Kualitatif Terpadu</h1>', unsafe_allow_html=True)

# Layout Tengah (Space-Content-Space)
col_l, col_main, col_r = st.columns([1, 2])

with col_main:
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    
    # 1. TAMPILAN MIND MAP & BAGAN
    st.subheader("📊 Alur Pemisahan & Hasil Percobaan")
    map_tab, table_tab = st.tabs(["📍 Mind Map Kation", "📝 Tabel Anion"])
    
    with map_tab:
        try:
            st.image("NotebookLM Mind Map.png", caption="Alur Pemisahan Campuran Gol I-V [1]", use_column_width=True)
        except:
            st.error("Gambar 'NotebookLM Mind Map.png' tidak ditemukan.")
            
    with table_tab:
        try:
            st.image("ef5bf4a7-66fb-4ef1-ac42-491909eb0ee4.jpeg", caption="Hasil Pengamatan Identifikasi Anion [3]", use_column_width=True)
        except:
            st.error("Gambar Tabel Anion tidak ditemukan.")

    st.divider()

    # 2. TOOLS INTERAKTIF
    st.subheader("🛠️ Tools Analisis & Reaksi Stoikiometri")
    tab1, tab2, tab3, tab4 = st.tabs(["🔹 Gol I", "🔹 Gol III", "🔥 Gol IV", "🧪 Anion"])

    with tab1:
        st.write("**Pemisahan Golongan I (Ag+, Pb2+, Hg2^2+)** [4]")
        if st.button("Reaksi + HCl"):
            render_tube("white")
            play_centrifuge()
            st.write("Hasil: Endapan Putih klorida.")
            render_tube("rgba(200,230,255,0.3)", "white", 40)
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow")
            st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow")
            st.latex(r"Hg_2^{2+} + 2Cl^- \rightarrow Hg_2Cl_2(s) \downarrow")

    with tab2:
        st.write("**Pemisahan Golongan III (Fe3+, Al3+)** [5]")
        if st.button("Uji Besi (Fe3+)"):
            st.write("Hasil: 🔴 Larutan Merah Darah dengan SCN-.")
            render_tube("#b71c1c")
            st.latex(r"Fe^{3+}(aq) + 3SCN^-(aq) \rightarrow [Fe(SCN)]_3(aq)")

    with tab3:
        st.write("**Uji Nyala & Reaksi Golongan IV** [5]")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.caption("Barium (Ba2+)")
            render_flame("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s)")
        with c2:
            st.caption("Stronsium (Sr2+)")
            render_flame("#ff0000")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s)")
        with c3:
            st.caption("Kalsium (Ca2+)")
            render_flame("#ff4500")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s)")

    with tab4:
        st.write("**Analisis Anion (Stoikiometri)** [3]")
        anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
        if anion == "Iodida (I-)":
            st.latex(r"2I^-(aq) + HgCl_2(aq) \rightarrow HgI_2(s) \downarrow + 2Cl^-(aq)")
            st.write("Hasil: **Endapan Merah (HgI2)**. Jika KI berlebih menjadi larutan kuning.")
            render_tube("yellow", "red", 30)
        elif anion == "Klorida (Cl-)":
            st.latex(r"Cl^-(aq) + AgNO_3(aq) \rightarrow AgCl(s) \downarrow + NO_3^-(aq)")
            render_tube("rgba(255,255,255,0.2)", "white", 35)

    st.markdown('</div>', unsafe_allow_html=True)
