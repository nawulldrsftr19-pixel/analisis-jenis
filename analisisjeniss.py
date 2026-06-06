import streamlit as st
import time
import graphviz

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- CSS: TEMA BIRU, LAYOUT TENGAH & ANIMASI ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ff; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .center-container { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-top: 20px; }
    
    /* Animasi Api (Flame Test) */
    .flame-wrapper { display: flex; justify-content: center; align-items: flex-end; height: 80px; margin: 10px; }
    .flame {
        width: 35px; height: 35px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.6s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); opacity: 0.8; } 100% { transform: rotate(-45deg) scale(1.2); opacity: 1; } }
    
    /* Animasi Tabung Reaksi */
    .tube-box { display: flex; justify-content: center; margin: 20px 0; }
    .tube {
        width: 55px; height: 160px; border: 3px solid #333; border-radius: 0 0 30px 30px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 27px 27px; transition: height 1s; }
    
    /* Centrifuge Spinner */
    .spin-icon {
        border: 8px solid #f3f3f3; border-top: 8px solid #1565c0;
        border-radius: 50%; width: 50px; height: 50px;
        animation: spin 1s linear infinite; margin: 10px auto;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def tube_viz(liq_color, p_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-box"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:0.6;"></div>{p_html}</div></div>', unsafe_allow_html=True)

def flame_viz(color):
    st.markdown(f'<div class="flame-wrapper"><div class="flame" style="background:{color}; box-shadow:0 0 20px {color};"></div></div>', unsafe_allow_html=True)

def centrifuge_action():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="spin-icon"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 Memutar pada 3000 rpm (Sesuai Prosedur)...</center>", unsafe_allow_html=True)
        time.sleep(2)
    placeholder.empty()
    st.success("✅ Pemisahan Pellet & Supernatan Selesai [2]!")

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Analisis Kation & Anion Terpadu</h1>', unsafe_allow_html=True)

# Layout Tengah (Space - Content - Space)
_, col_center, _ = st.columns([1, 5, 1])

with col_center:
    st.markdown('<div class="center-container">', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Bagan Alir (Mind Map)", "🔹 Analisis Kation", "🧪 Analisis Anion"])

    # --- TAB 1: BAGAN ALIR ---
# Judul aplikasi berdasarkan sumber [1]
st.title("Analisis Kualitatif Kation (Golongan I-V)")
st.write("Klik tombol di bawah untuk melihat langkah-langkah pemisahan kation secara bertahap.")

# Pengaturan halaman
st.set_page_config(page_title="Analisis Kation Golongan I-V", layout="wide")

st.title("🔬 Bagan Pemisahan Kation (Golongan I-V)")
st.write("Navigasikan tab di bawah untuk melihat alur pemisahan kation secara bertahap berdasarkan bagan analisis kualitatif.")

# Membuat sistem Tab untuk navigasi antar langkah
tab1, tab2, tab3, tab4 = st.tabs([
    "Step 1: HCl (Gol I)", 
    "Step 2: H2O Panas & NH4OH", 
    "Step 3: NaOH & K2CrO4", 
    "Step 4: Identifikasi Akhir"
])

# Fungsi untuk merender bagan menggunakan Graphviz
def render_flowchart(step):
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', size='12,12')
    
    # Titik awal: Campuran Contoh
    dot.node('start', 'Campuran Contoh Gol I - V', style='filled', color='lavender')

    # Logika visualisasi bertahap berdasarkan data dari sumber [1]
    if step >= 1:
        dot.node('hcl', '+ HCl encer', shape='plaintext')
        dot.edge('start', 'hcl')
        dot.node('gol1', 'Endapan Gol I\n(AgCl, PbCl2, Hg2Cl2)', style='filled', color='lightblue')
        dot.node('larutan1', 'Larutan\n(Al3+, Fe3+, Ba2+, Sr2+, Ca2+)', style='filled', color='lightblue')
        dot.edge('hcl', 'gol1')
        dot.edge('hcl', 'larutan1')

    if step >= 2:
        # Jalur Endapan Gol I
        dot.node('hot_water', '+ H2O Panas', shape='plaintext')
        dot.edge('gol1', 'hot_water')
        dot.node('pb_sol', 'Pb2+', style='filled', color='lightgreen')
        dot.node('residu1', 'Residu AgCl, Hg2Cl2', style='filled', color='lightgreen')
        dot.edge('hot_water', 'pb_sol')
        dot.edge('hot_water', 'residu1')
        
        # Jalur Larutan (Gol III & IV)
        dot.node('nh4oh', '+ NH4OH Berlebih', shape='plaintext')
        dot.edge('larutan1', 'nh4oh')
        dot.node('gol3', 'Endapan Gol III\n(Al(OH)3, Fe(OH)3)', style='filled', color='lightgreen')
        dot.node('gol4', 'Larutan Gol IV\n(Ba2+, Sr2+, Ca2+)', style='filled', color='lightgreen')
        dot.edge('nh4oh', 'gol3')
        dot.edge('nh4oh', 'gol4')

    if step >= 3:
        # Identifikasi Pb & Hg
        dot.edge('pb_sol', 'PbCrO4 (Kuning)', label='+ K2CrO4')
        dot.node('nh4oh_res', '+ NH4OH Berlebih', shape='plaintext')
        dot.edge('residu1', 'nh4oh_res')
        dot.node('hg_res', 'Hg(NH2)Cl + Hg (Hitam)', style='filled', color='grey')
        dot.node('ag_complex', 'Ag(NH3)2+ Cl-', style='filled', color='lightgreen')
        dot.edge('nh4oh_res', 'hg_res')
        dot.edge('nh4oh_res', 'ag_complex')

        # Identifikasi Gol III & IV
        dot.edge('gol3', 'Fe(OH)3 & Al(OH)4-', label='+ NaOH')
        dot.edge('gol4', 'BaCrO4 (Kuning)', label='+ K2CrO4')

    if step >= 4:
        # Hasil Konfirmasi Akhir
        dot.edge('ag_complex', 'AgCl (Putih)', label='+ HNO3')
        dot.edge('al_oh4', 'Al(OH)3 (Putih)', label='Netralisasi')
        dot.node('final', 'Kation Teridentifikasi:\nAg+, Pb2+, Hg2 2+,\nAl3+, Fe3+, Ba2+', shape='doublecircle', color='orange')
        dot.edge('start', 'final', style='dotted')

    return dot

# Mengisi Konten untuk Setiap Tab
with tab1:
    st.subheader("Pemisahan Golongan I")
    st.info("Pada tahap ini, HCl encer digunakan untuk mengendapkan Ag+, Pb2+, dan Hg2 2+ sebagai garam klorida [1].")
    st.graphviz_chart(render_flowchart(1))

with tab2:
    st.subheader("Pemisahan Golongan I, III, dan IV")
    st.info("Kation dipisahkan menggunakan air panas (untuk Pb) dan NH4OH berlebih untuk memisahkan Golongan III dari Golongan IV [1].")
    st.graphviz_chart(render_flowchart(2))

with tab3:
    st.subheader("Identifikasi Spesifik")
    st.info("Tahap ini melibatkan penambahan K2CrO4 untuk identifikasi Pb dan Ba, serta NaOH untuk memisahkan besi dan aluminium [1].")
    st.graphviz_chart(render_flowchart(3))

with tab4:
    st.subheader("Hasil Analisis Akhir")
    st.success("Seluruh kation dari Golongan I hingga IV telah berhasil dipisahkan dan diidentifikasi melalui reaksi konfirmasi [1].")
    st.graphviz_chart(render_flowchart(4))

    # --- TAB 2: ANALISIS KATION ---
with tab2:
        st.subheader("🛠️ Simulasi Pemisahan Kation [2, 3]")
        gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I", "Golongan III", "Golongan IV"])
        
        if gol == "Golongan I":
            st.info("Penambahan HCl encer untuk memisahkan Ag+, Pb2+, Hg2^2+.")
            if st.button("Jalankan Uji Gol I"):
                st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
                st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}")
                centrifuge_action()
                tube_viz("rgba(173,216,230,0.3)", "white", 40)
        
        elif gol == "Golongan III":
            st.info("Penambahan NH4OH untuk memisahkan Fe3+ & Al3+.")
            if st.button("Uji Besi (Fe3+)"):
                st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3(aq) \text{ (Merah Darah)}")
                tube_viz("#b71c1c")
        
        elif gol == "Golongan IV":
            st.info("Identifikasi Ba2+, Sr2+, Ca2+ melalui Uji Nyala & Pengendapan.")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.caption("Barium (Ba2+)")
                flame_viz("#adff2f") # Hijau Apel
                st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
            with c2:
                st.caption("Stronsium (Sr2+)")
                flame_viz("#ff0000") # Merah Tua
                st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
            with c3:
                st.caption("Kalsium (Ca2+)")
                flame_viz("#ff4500") # Merah Bata
                st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

    # --- TAB 3: ANALISIS ANION ---
with tab3:
        st.subheader("📝 Identifikasi Anion Spesifik [4]")
        anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
        
        if anion == "Iodida (I-)":
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Endapan Merah)}")
            st.write("Catatan: Jika KI berlebih $\\rightarrow (HgI_4)^{2-}$ (Larutan Kuning) [4].")
            tube_viz("yellow", "red", 35)
        elif anion == "Klorida (Cl-)":
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Endapan Putih)}")
            tube_viz("rgba(255,255,255,0.2)", "white", 35)
        elif anion == "Karbonat (CO3 2-)":
            st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
            st.write("Hasil: Terbentuk gas dan endapan putih dengan $Ba(OH)_2$ [4].")
        elif anion == "Sulfat (SO4 2-)":
            st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
            tube_viz("rgba(255,255,255,0.2)", "white", 35)

            st.markdown('</div>', unsafe_allow_html=True)
