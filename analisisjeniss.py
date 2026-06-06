import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif Terintegrasi", layout="wide")

# --- CSS: TEMA BIRU & ANIMASI NYATA ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #ffffff 100%); }
    .main-title { color: #075985; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-bottom: 5px solid #0ea5e9; }
    
    /* Animasi Centrifuge */
    .centrifuge-spin {
        width: 70px; height: 70px; border: 6px dashed #0284c7;
        border-radius: 50%; animation: spin 0.8s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi Realistis */
    .tube-container { display: flex; flex-direction: column; align-items: center; margin: 20px 0; }
    .tube {
        width: 60px; height: 180px; border: 3px solid #334155;
        border-radius: 0 0 30px 30px; position: relative;
        background: rgba(255,255,255,0.4); overflow: hidden;
        box-shadow: inset 5px 0 10px rgba(255,255,255,0.5);
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 25px 25px; transition: all 1.5s ease; }
    
    /* Animasi Api */
    .flame-box { display: flex; justify-content: center; align-items: flex-end; height: 60px; }
    .flame {
        width: 30px; height: 30px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.2); opacity: 0.9; } }

    /* Gaya Mind Map Node */
    .node { padding: 12px; border-radius: 10px; border: 2px solid #0369a1; background: #e0f2fe; text-align: center; margin: 10px 0; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI & VISUALISASI ---
def play_centrifuge():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        st.write("<center><b>🌀 Sentrifugasi 3000 rpm (Sesuai Prosedur)...</b></center>", unsafe_allow_html=True)
        time.sleep(2)
    placeholder.empty()

def render_tube(liq_color, p_color=None, p_height=0, mixed=False):
    op = "0.5" if mixed else "0.8"
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-container"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-box"><div class="flame" style="background:{color}; box-shadow:0 0 15px {color};"></div></div>', unsafe_allow_html=True)

# --- HEADER UTAMA ---
st.markdown('<h1 class="main-title">🧪 Aplikasi Lab Virtual: Analisis Kation & Anion</h1>', unsafe_allow_html=True)

# --- SIDEBAR 1: BAGAN/MIND MAP INTERAKTIF ---
st.sidebar.title("📍 Sidebar 1: Bagan Alir")
menu_bagan = st.sidebar.radio("Pilih Alur Bagan:", ["Golongan I", "Golongan III", "Golongan IV"])

# --- MENU UTAMA DI TENGAH ---
_, col_center, _ = st.columns([2, 3, 2])

with col_center:
    if menu_bagan == "Golongan I":
        st.subheader("Bagan Alir Pemisahan Golongan I")
        tab_a, tab_b = st.tabs(["Langkah 1: Pengendapan", "Langkah 2: Pemisahan Pb, Ag, Hg"])
        
        with tab_a:
            st.markdown('<div class="node">Campuran Gol I - V</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + HCl Encer</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Endapan Gol I (AgCl, PbCl2, Hg2Cl2)</div>', unsafe_allow_html=True)
            if st.button("Simulasi Sentrifugasi Gol I"):
                play_centrifuge()
                render_tube("rgba(200,230,255,0.3)", "white", 45)
                st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow")

        with tab_b:
            st.markdown('<div class="node">Endapan Gol I</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + H2O Panas</center>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.success("**Pb2+** (Larutan)")
                st.write("Identifikasi: + K2CrO4 → 🟡 Kuning")
            with col2:
                st.error("**Residu AgCl, Hg2Cl2**")
                st.write("Identifikasi: + NH4OH Berlebih → Hg (Hitam) & Ag+ (Larut)")

    elif menu_bagan == "Golongan III":
        st.subheader("Bagan Alir Pemisahan Golongan III")
        st.markdown('<div class="node">Larutan dari Gol I</div>', unsafe_allow_html=True)
        st.write("<center>⬇️ + NH4OH Berlebih</center>", unsafe_allow_html=True)
        st.markdown('<div class="node">Endapan Gol III (Al(OH)3, Fe(OH)3)</div>', unsafe_allow_html=True)
        
        if st.button("Uji Spesifik Fe3+"):
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah)}")
            render_tube("#b91c1c")
            st.write("Hasil: Larutan Merah Darah [3].")

    elif menu_bagan == "Golongan IV":
        st.subheader("Bagan Alir Pemisahan Golongan IV")
        st.info("Penyajian Baris ke Bawah (Vertikal) sesuai permintaan.")
        
        st.markdown('<div class="node">Larutan Gol IV (Ba2+, Sr2+, Ca2+)</div>', unsafe_allow_html=True)
        st.write("<center>⬇️ Penambahan Pereaksi Spesifik</center>", unsafe_allow_html=True)
        
        # PENYAJIAN BARIS KE BAWAH (VERTIKAL)
        st.markdown("---")
        st.markdown("**1. Barium (Ba2+)**")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
        render_flame("#adff2f")
        st.write("Identifikasi: Endapan Kuning & Nyala Hijau Apel [3].")
        
        st.markdown("---")
        st.markdown("**2. Stronsium (Sr2+)**")
        st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
        render_flame("#ef4444")
        st.write("Identifikasi: Endapan Putih & Nyala Merah Tua [1, 3].")
        
        st.markdown("---")
        st.markdown("**3. Kalsium (Ca2+)**")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \text{ (Putih)}")
        render_flame("#f97316")
        st.write("Identifikasi: Endapan Putih & Nyala Merah Bata [1, 3].")

# --- SIDEBAR TAMBAHAN (REAKSI ANION) ---
st.sidebar.divider()
st.sidebar.title("🧪 Sidebar 2: Reaksi Anion")
anion_tab = st.sidebar.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)"])

if anion_tab == "Iodida (I-)":
    st.sidebar.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow")
    st.sidebar.write("Hasil: Endapan Merah [4].")
elif anion_tab == "Klorida (Cl-)":
    st.sidebar.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow")
    st.sidebar.write("Hasil: Endapan Putih [4].")
