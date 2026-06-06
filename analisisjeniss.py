import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Anion & Kation", layout="wide")

# --- CSS: TEMA, POSISI TENGAH, & ANIMASI ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f4f8; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 30px; }
    .center-box { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    
    /* Gaya Kotak Bagan (Mind Map Nodes) */
    .node-container { display: flex; flex-direction: column; align-items: center; margin: 10px 0; }
    .node { padding: 12px; border-radius: 8px; border: 2px solid #1a73e8; background: #e8f0fe; font-weight: bold; min-width: 180px; text-align: center; }
    .node-reagent { background: #fff3e0; border-color: #ff9800; }
    .node-result { background: #e8f5e9; border-color: #4caf50; }
    .arrow { font-size: 20px; margin: 5px 0; color: #555; }

    /* Tabung Reaksi & Animasi Cairan */
    .tube-wrapper { display: flex; justify-content: center; margin: 20px 0; }
    .tube {
        width: 55px; height: 160px; border: 3px solid #333; border-radius: 0 0 30px 30px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 27px 27px; transition: height 1s; }
    
    /* Animasi Centrifuge */
    .spinner {
        border: 6px dashed #1a73e8; border-radius: 50%; width: 50px; height: 50px;
        animation: spin 1s linear infinite; margin: 10px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def render_node(text, style="node"):
    st.markdown(f'<div class="node-container"><div class="{style}">{text}</div></div>', unsafe_allow_html=True)

def render_arrow():
    st.markdown('<div class="node-container"><div class="arrow">↓</div></div>', unsafe_allow_html=True)

def render_tube(liq_color, p_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-wrapper"><div class="tube"><div class="liquid" style="height:70%; background:{liq_color}; opacity:0.6;"></div>{p_html}</div></div>', unsafe_allow_html=True)

def play_centrifuge():
    with st.spinner("🌀 Sentrifugasi 3000 rpm berlangsung..."):
        st.markdown('<div class="spinner"></div>', unsafe_allow_html=True)
        time.sleep(2)
    st.success("✅ Sentrifugasi Selesai (Berdasarkan Sumber [2])")

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Bagan Analisis Per Anion</h1>', unsafe_allow_html=True)

# Layout Tengah
_, col_main, _ = st.columns([2, 3])

with col_main:
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    
    # BAGAN PER ANION DENGAN TAB (Sumber [1])
    st.subheader("📍 Bagan Alir Identifikasi Anion")
    st.write("Klik setiap tab untuk melihat bagan alur reaksi spesifik per anion.")
    
    t1, t2, t3, t4 = st.tabs(["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])

    with t1:
        render_node("Larutan Sampel (Cl⁻)")
        render_arrow()
        render_node("+ AgNO₃ + HNO₃", "node node-reagent")
        if st.button("Jalankan Reaksi Cl⁻"):
            render_arrow()
            render_node("Endapan AgCl (Putih)", "node node-result")
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow + NO_3^-")
            play_centrifuge()
            render_tube("rgba(200,230,255,0.3)", "white", 40)
            st.info("Pengamatan: Terbentuk endapan putih (Sumber [1])")

    with t2:
        render_node("Larutan Sampel (I⁻)")
        render_arrow()
        render_node("+ HgCl₂ + KI", "node node-reagent")
        if st.button("Jalankan Reaksi I⁻"):
            render_arrow()
            render_node("Endapan HgI₂ (Merah Jingga)", "node node-result")
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow + 2Cl^-")
            play_centrifuge()
            render_tube("yellow", "red", 40)
            st.warning("Catatan: Jika KI berlebih, endapan larut menjadi larutan kuning (HgI₄)²⁻ (Sumber [1])")

    with t3:
        render_node("Larutan Sampel (CO₃²⁻)")
        render_arrow()
        render_node("+ HCl atau BaCl₂", "node node-reagent")
        if st.button("Jalankan Reaksi CO₃²⁻"):
            render_arrow()
            render_node("Gas CO₂ / Endapan BaCO₃", "node node-result")
            st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
            st.write("Hasil: Terbentuk gelembung gas (Sumber [1])")

    with t4:
        render_node("Larutan Sampel (SO₄²⁻)")
        render_arrow()
        render_node("+ BaCl₂", "node node-reagent")
        if st.button("Jalankan Reaksi SO₄²⁻"):
            render_arrow()
            render_node("Endapan BaSO₄ (Putih)", "node node-result")
            st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
            play_centrifuge()
            render_tube("rgba(200,230,255,0.2)", "white", 45)

    st.markdown('</div>', unsafe_allow_html=True)

# --- SIDEBAR: REAKSI KATION (Sumber [2-4]) ---
st.sidebar.title("🧪 Kontrol Kation")
if st.sidebar.checkbox("Tampilkan Reaksi Kation"):
    kat = st.sidebar.selectbox("Pilih Kation:", ["Ag+", "Pb2+", "Hg2 2+", "Fe3+", "Ba2+"])
    if kat == "Ag+":
        st.sidebar.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s)")
        st.sidebar.write("Hasil: Endapan putih klorida [2]")
    elif kat == "Fe3+":
        st.sidebar.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3")
        st.sidebar.write("Hasil: Warna merah darah [4]")

st.sidebar.divider()
st.sidebar.info("💡 **Prinsip**: Sentrifugasi memisahkan pellet dan supernatan dengan gaya putar 3000 rpm [2].")
