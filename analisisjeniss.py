import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Analisis Kualitatif Pro", layout="wide")

# --- CSS KHUSUS (TEMA, API, & LAYOUT TENGAH) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ff; }
    .center-content { display: flex; flex-direction: column; align-items: center; text-align: center; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    
    /* Animasi Api */
    .flame-container { display: flex; justify-content: center; align-items: flex-end; height: 80px; margin: 10px; }
    .flame {
        width: 30px; height: 30px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.1); } }
    
    /* Tabung Reaksi */
    .tube {
        width: 50px; height: 150px; border: 3px solid #444; border-radius: 0 0 25px 25px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden; margin: 10px auto;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: height 1s; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI VISUAL ---
def render_flame(color):
    st.markdown(f'<div class="flame-container"><div class="flame" style="background:{color}; box-shadow:0 0 15px {color};"></div></div>', unsafe_allow_html=True)

def show_tube(liq_color, pellet_color=None, pellet_height=0):
    p_html = f'<div class="pellet" style="height:{pellet_height}px; background:{pellet_color};"></div>' if pellet_color else ""
    st.markdown(f'<div class="tube"><div class="liquid" style="height:70%; background:{liq_color}; opacity:0.6;"></div>{p_html}</div>', unsafe_allow_html=True)

def animasi_sentrifugasi():
    with st.spinner("🌀 Sentrifugasi 3000 rpm..."):
        p = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            p.progress(i + 1)

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Analisis Kation & Anion</h1>', unsafe_allow_html=True)

# Layout Tengah Menggunakan Columns
left_space, center_col, right_space = st.columns([1, 2])

with center_col:
    # 1. TAMPILAN MIND MAP (Source 1)
    st.subheader("📍 Mind Map Pemisahan")
    try:
        st.image("NotebookLM Mind Map.png", caption="Alur Pemisahan Campuran Kation Gol I - V", use_column_width=True)
    except:
        st.warning("⚠️ File 'NotebookLM Mind Map.png' tidak ditemukan.")

    # 2. TOOLS INTERAKTIF DENGAN TAB
    st.write("### 🛠️ Tools Analisis & Reaksi Stoikiometri")
    tab1, tab2, tab3, tab4 = st.tabs(["🔹 Golongan I", "🔹 Golongan III", "🔥 Golongan IV", "🧪 Analisis Anion"])

    with tab1:
        st.info("Penambahan HCl encer untuk memisahkan Ag+, Pb2+, Hg2^2+ [1, 3]")
        if st.button("Uji Golongan I"):
            animasi_sentrifugasi()
            show_tube("rgba(200,230,255,0.3)", "white", 40)
            st.markdown("""
            **Persamaan Stoikiometri:**
            - $Ag^+(aq) + Cl^-(aq) \\rightarrow AgCl(s)$ (Putih)
            - $Pb^{2+}(aq) + 2Cl^-(aq) \\rightarrow PbCl_2(s)$ (Putih)
            - $Hg_2^{2+}(aq) + 2Cl^-(aq) \\rightarrow Hg_2Cl_2(s)$ (Putih)
            """)

    with tab2:
        st.info("Penambahan NH4OH untuk memisahkan Fe3+ & Al3+ [2]")
        if st.button("Uji Golongan III"):
            st.write("**Identifikasi Besi (Fe3+):**")
            show_tube("#b71c1c")
            st.latex(r"Fe^{3+}(aq) + 3SCN^-(aq) \rightarrow [Fe(SCN)]_3(aq) \text{ (Merah Darah)}")

    with tab3:
        st.info("Uji Nyala & Identifikasi Kation alkali tanah [2]")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.caption("Barium (Ba2+)")
            render_flame("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
        with c2:
            st.caption("Stronsium (Sr2+)")
            render_flame("#ff0000")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
        with c3:
            st.caption("Kalsium (Ca2+)")
            render_flame("#ff4500")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \text{ (Putih)}")

    with tab4:
        st.info("Identifikasi Anion berdasarkan tabel hasil percobaan [4]")
        anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
        
        if anion == "Klorida (Cl-)":
            st.latex(r"Cl^-(aq) + AgNO_3(aq) \rightarrow AgCl(s) \downarrow + NO_3^-(aq)")
            st.write("Hasil: Endapan Putih [4]")
        elif anion == "Iodida (I-)":
            st.latex(r"2I^-(aq) + HgCl_2(aq) \rightarrow HgI_2(s) \downarrow + 2Cl^-(aq)")
            st.write("Hasil: Endapan Merah (HgI2) [4]")
        elif anion == "Karbonat (CO3 2-)":
            st.latex(r"CO_3^{2-}(aq) + 2HCl(aq) \rightarrow CO_2(g) \uparrow + H_2O(l) + 2Cl^-(aq)")
            st.write("Hasil: Terbentuk gas CO2 [4]")
        elif anion == "Sulfat (SO4 2-)":
            st.latex(r"SO_4^{2-}(aq) + BaCl_2(aq) \rightarrow BaSO_4(s) \downarrow + 2Cl^-(aq)")
            st.write("Hasil: Endapan Putih [4]")
