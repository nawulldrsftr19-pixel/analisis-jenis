import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Analisis Kualitatif Virtual Lab", layout="wide")

# --- GAYA VISUAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #eef2f6; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    
    /* Animasi Api Flicker */
    .flame-container { display: flex; justify-content: center; align-items: flex-end; height: 80px; margin: 10px; }
    .flame {
        width: 35px; height: 35px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.6s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); opacity: 0.8; } 100% { transform: rotate(-45deg) scale(1.15); opacity: 1; } }
    
    /* Tabung Reaksi & Animasi Cairan */
    .tube-center { display: flex; justify-content: center; margin: 15px 0; }
    .tube {
        width: 55px; height: 160px; border: 3px solid #333; border-radius: 0 0 30px 30px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 27px 27px; transition: height 1s; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def animasi_sentrifugasi():
    with st.spinner("🌀 Memutar tabung pada 3000 rpm (Sesuai Prosedur)..."):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.015)
            bar.progress(i + 1)
    st.success("✅ Sentrifugasi Selesai! Pellet dan Supernatan terpisah.")

def render_tube(warna_liq, warna_pel=None, h_pel=0):
    pel_html = f'<div class="pellet" style="height:{h_pel}px; background:{warna_pel};"></div>' if warna_pel else ""
    st.markdown(f'<div class="tube-center"><div class="tube"><div class="liquid" style="height:70%; background:{warna_liq}; opacity:0.6;"></div>{pel_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-container"><div class="flame" style="background:{color}; box-shadow:0 0 20px {color};"></div></div>', unsafe_allow_html=True)

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Analisis Kation & Anion</h1>', unsafe_allow_html=True)

# Mengatur Konten di Tengah
left, center, right = st.columns([1, 2])

with center:
    st.write("### 📍 Alur Pemisahan (Mind Map)")
    # Pastikan file gambar sesuai dengan nama di notebook state
    try:
        st.image("NotebookLM Mind Map.png", caption="Alur Pemisahan Campuran Gol I-V (Source 1)", use_column_width=True)
    except:
        st.warning("⚠️ File 'NotebookLM Mind Map.png' tidak ditemukan di direktori.")

    st.write("---")
    st.write("### 🛠️ Alat Analisis Interaktif")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔹 Golongan I", "🔹 Golongan III", "🔥 Golongan IV", "🧪 Anion Spesifik"])

    with tab1:
        st.info("**Pemisahan Golongan I**: Penambahan HCl encer.")
        if st.button("Jalankan Uji Gol I"):
            animasi_sentrifugasi()
            render_tube("rgba(200,230,255,0.3)", "white", 40)
            st.markdown("**Reaksi Stoikiometri:**")
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}")
            st.latex(r"Hg_2^{2+} + 2Cl^- \rightarrow Hg_2Cl_2(s) \downarrow \text{ (Putih)}")

    with tab2:
        st.info("**Pemisahan Golongan III**: Penambahan NH4OH.")
        if st.button("Uji Besi (Fe3+)"):
            st.write("Hasil: Larutan Merah Darah (Source 3)")
            render_tube("#b71c1c")
            st.latex(r"Fe^{3+}(aq) + 3SCN^-(aq) \rightarrow [Fe(SCN)]_3(aq)")

    with tab3:
        st.info("**Identifikasi Golongan IV & Uji Nyala**")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.caption("Barium (Ba2+)")
            render_flame("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        with c2:
            st.caption("Stronsium (Sr2+)")
            render_flame("#ff0000")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
        with c3:
            st.caption("Kalsium (Ca2+)")
            render_flame("#ff4500")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

    with tab4:
        st.info("**Analisis Anion (Berdasarkan Tabel Source 5)**")
        anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
        
        if anion == "Klorida (Cl-)":
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow + NO_3^-")
            st.write("Hasil: **Endapan Putih**")
            render_tube("rgba(255,255,255,0.2)", "white", 30)
        elif anion == "Iodida (I-)":
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow + 2Cl^-")
            st.write("Hasil: **Endapan Merah**")
            render_tube("rgba(255,255,255,0.2)", "red", 30)
        elif anion == "Karbonat (CO3 2-)":
            st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
            st.write("Hasil: **Terbentuk Gas CO2**")
        elif anion == "Sulfat (SO4 2-)":
            st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
            st.write("Hasil: **Endapan Putih**")
            render_tube("rgba(255,255,255,0.2)", "white", 30)
