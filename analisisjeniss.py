import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Lab Virtual: Analisis Kualitatif Terpadu", layout="wide")

# --- CSS: ESTETIKA MODERN, ANIMASI API & SENTRIFUGASI ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #ffffff 100%); }
    .main-title { color: #075985; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-bottom: 5px solid #0ea5e9; margin-bottom: 25px; }
    .center-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    
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
    
    /* Animasi Api (Flicker) */
    .flame-box { display: flex; justify-content: center; align-items: flex-end; height: 60px; }
    .flame {
        width: 30px; height: 30px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.2); opacity: 0.9; } }

    /* Gaya Mind Map Node */
    .node { padding: 12px; border-radius: 10px; border: 2px solid #0369a1; background: #e0f2fe; text-align: center; margin: 10px 0; font-weight: bold; font-size: 0.95rem; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI & VISUAL ---
def play_centrifuge():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        st.write("<center><b>🌀 Sentrifugasi 3000 rpm sedang berlangsung...</b></center>", unsafe_allow_html=True)
        time.sleep(2)
    placeholder.empty()

def render_tube(liq_color, p_color=None, p_height=0, mixed=False):
    op = "0.5" if mixed else "0.8"
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-container"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-box"><div class="flame" style="background:{color}; box-shadow:0 0 15px {color};"></div></div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🔬 Kontrol Lab Virtual")
menu = st.sidebar.radio("Pilih Menu Sidebar:", ["Sidebar 1: Bagan Interaktif", "Sidebar 2: Kation (Per Golongan)", "Sidebar 3: Anion (Per Ion)"])

# --- HEADER UTAMA ---
st.markdown('<h1 class="main-title">Aplikasi Analisis Kualitatif Ion Pro</h1>', unsafe_allow_html=True)

# --- AREA UTAMA (TENGAH) ---
_, col_main, _ = st.columns([0.1, 0.8, 0.1])

with col_main:
    st.markdown('<div class="center-card">', unsafe_allow_html=True)

    # --- MENU 1: BAGAN INTERAKTIF (Berdasarkan Sumber 4) ---
    if menu == "Sidebar 1: Bagan Interaktif":
        st.subheader("📍 Bagan Pemisahan Campuran Kation (Hingga Akhir)")
        tab_gol1, tab_gol3, tab_gol4 = st.tabs(["🔹 Alur Golongan I", "🔹 Alur Golongan III", "🔹 Alur Golongan IV"])

        with tab_gol1:
            st.markdown('<div class="node">Campuran Contoh Gol I - V</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + HCl Encer</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Endapan Gol I (AgCl, PbCl2, Hg2Cl2)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + H2O Panas</center>", unsafe_allow_html=True)
            col_pb, col_res = st.columns(2)
            with col_pb:
                st.markdown('<div class="node" style="border-color:#facc15;">Larutan Pb2+</div>', unsafe_allow_html=True)
                st.write("Identifikasi: + K2CrO4 → 🟡 Kuning")
            with col_res:
                st.markdown('<div class="node" style="border-color:#64748b;">Residu AgCl, Hg2Cl2</div>', unsafe_allow_html=True)
                st.write("Identifikasi: + NH4OH Berlebih → ⚫ Hg Hitam / Ag+ Larut")

        with tab_gol3:
            st.markdown('<div class="node">Larutan Filtrat Gol I</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + NH4OH Berlebih</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Endapan Gol III (Al(OH)3, Fe(OH)3)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + NaOH</center>", unsafe_allow_html=True)
            c_fe, c_al = st.columns(2)
            with c_fe:
                st.markdown('<div class="node" style="border-color:#991b1b;">Fe(OH)3</div>', unsafe_allow_html=True)
                st.write("Identifikasi: + SCN- → 🔴 Merah Darah")
            with c_al:
                st.markdown('<div class="node" style="border-color:#f1f5f9;">[Al(OH)4]-</div>', unsafe_allow_html=True)
                st.write("Identifikasi: + HCl → ⚪ Putih Gelatin")

        with tab_gol4:
            st.markdown('<div class="node">Larutan Filtrat Gol III</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ + K2CrO4</center>", unsafe_allow_html=True)
            st.markdown('<div class="node" style="border-color:#facc15;">BaCrO4 (Kuning)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ Larutan Sr2+, Ca2+</center>", unsafe_allow_html=True)
            st.markdown('<div class="node">Identifikasi Akhir Nyala Api</div>', unsafe_allow_html=True)

    # --- MENU 2: KATION PER GOLONGAN (Berdasarkan Sumber 1, 2) ---
    elif menu == "Sidebar 2: Kation (Per Golongan)":
        gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I", "Golongan III", "Golongan IV"])
        
        if gol == "Golongan I":
            st.info("Pemisahan Ag+, Pb2+, Hg2^2+ dengan HCl.")
            if st.button("Simulasikan Sentrifugasi Gol I"):
                render_tube("white", mixed=True)
                play_centrifuge()
                st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow")
                render_tube("rgba(200,230,255,0.3)", "white", 45)
        
        elif gol == "Golongan III":
            st.info("Uji Spesifik Besi (Fe3+) & Aluminium (Al3+).")
            if st.button("Uji Besi (Fe3+)"):
                st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah)}")
                render_tube("#991b1b")

        elif gol == "Golongan IV":
            st.info("Identifikasi Ba2+, Sr2+, Ca2+ (Penyajian Baris ke Bawah)")
            # PENYAJIAN VERTIKAL (BARIS KE BAWAH)
            st.markdown("### 1. Barium (Ba2+)")
            render_flame("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
            
            st.markdown("---")
            st.markdown("### 2. Stronsium (Sr2+)")
            render_flame("#ef4444")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
            
            st.markdown("---")
            st.markdown("### 3. Kalsium (Ca2+)")
            render_flame("#f97316")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \text{ (Putih)}")

    # --- MENU 3: ANION PER ION (Berdasarkan Sumber 5) ---
    elif menu == "Sidebar 3: Anion (Per Ion)":
        st.subheader("Identifikasi Anion Spesifik (Tabel 6.1)")
        an_tab = st.tabs(["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
        
        with an_tab:
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow + NO_3^-")
            if st.button("Uji Cl-"):
                render_tube("rgba(255,255,255,0.2)", "white", 35)
                st.write("Hasil: **Endapan Putih**.")
        
        with an_tab[3]:
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow + 2Cl^-")
            if st.button("Uji I-"):
                render_tube("yellow", "#ef4444", 40)
                st.write("Hasil: **Endapan Merah Jingga**. Larut menjadi kuning jika KI berlebih.")

        with an_tab[4]:
            st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
            st.write("Hasil: **Terbentuk gas** (Gelembung).")

        with an_tab[5]:
            st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
            if st.button("Uji SO4 2-"):
                render_tube("rgba(200,230,255,0.2)", "white", 40)
                st.write("Hasil: **Endapan Putih**.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER SIDEBAR ---
st.sidebar.divider()
st.sidebar.info("💡 **Catatan**: Sentrifugasi dilakukan pada 3000 rpm selama 1-2 menit untuk pemisahan sempurna [3, 5].")
