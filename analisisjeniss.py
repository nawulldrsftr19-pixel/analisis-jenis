import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif Pro", layout="wide")

# --- CSS: ESTETIKA MODERN & ANIMASI NYATA ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #e0f2fe, #ffffff); }
    .main-title { color: #0c4a6e; text-align: center; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-bottom: 6px solid #0284c7; }
    
    /* Animasi Centrifuge Bergerak */
    .centrifuge-spin {
        width: 80px; height: 80px; border: 6px dashed #0284c7;
        border-radius: 50%; animation: spin 0.8s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi (Pellet & Supernatan) */
    .tube-container { display: flex; flex-direction: column; align-items: center; margin: 25px 0; }
    .tube {
        width: 65px; height: 190px; border: 4px solid #334155;
        border-radius: 0 0 35px 35px; position: relative;
        background: rgba(255,255,255,0.3); overflow: hidden;
        box-shadow: inset 5px 0 15px rgba(255,255,255,0.6);
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 30px 30px; transition: all 1.5s ease-in-out; }
    
    /* Animasi Api (Uji Nyala) */
    .flame-container { display: flex; justify-content: center; align-items: flex-end; height: 90px; }
    .flame {
        width: 40px; height: 40px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.4s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.25); opacity: 0.9; } }

    /* Gaya Bagan (Mind Map Nodes) */
    .node { padding: 12px; border-radius: 12px; border: 2px solid #0369a1; background: #f0f9ff; text-align: center; margin: 10px 0; font-weight: bold; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI ---
def centrifuge_simulation():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 rpm (1-2 menit)...</b></center>", unsafe_allow_html=True)
        time.sleep(2.5)
    placeholder.empty()

def render_tube(liq_color, p_color=None, p_height=0, is_mixed=False):
    op = "0.5" if is_mixed else "0.8"
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-container"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-container"><div class="flame" style="background:{color}; box-shadow:0 0 25px {color};"></div></div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGASI BERDASARKAN GOLONGAN ---
st.sidebar.title("🔬 Navigasi Laboratorium")
menu = st.sidebar.radio("Pilih Analisis:", ["📍 Bagan Pemisahan (Mind Map)", "🧪 Kation (Per Golongan)", "🧪 Anion (Per Ion)"])

st.markdown('<h1 class="main-title">Virtual Lab: Analisis Kualitatif Terintegrasi</h1>', unsafe_allow_html=True)

# --- KONTEN TENGAH (CENTERED TOOLS) ---
_, col_center, _ = st.columns([1, 3])

with col_center:
    # --- BAGIAN 1: BAGAN INTERAKTIF ---
    if menu == "📍 Bagan Pemisahan (Mind Map)":
        st.subheader("Bagan Alir Pemisahan Kation (Source 4)")
        st.markdown('<div class="node">Campuran Contoh Gol I - V</div>', unsafe_allow_html=True)
        st.write("<center>⬇️ + HCl Encer</center>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="node" style="border-color:#ef4444;">Endapan Gol I (Putih)</div>', unsafe_allow_html=True)
            st.caption("AgCl, PbCl2, Hg2Cl2")
        with c2:
            st.markdown('<div class="node" style="border-color:#10b981;">Larutan Gol III, IV, V</div>', unsafe_allow_html=True)
            st.caption("Al3+, Fe3+, Ba2+, Sr2+, Ca2+")
        
        st.divider()
        st.info("Gunakan menu sidebar untuk menjalankan simulasi reaksi spesifik.")

    # --- BAGIAN 2: KATION PER GOLONGAN ---
    elif menu == "🧪 Kation (Per Golongan)":
        gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I (HCl)", "Golongan III (NH4OH)", "Golongan IV (Karbonat)"])
        
        if gol == "Golongan I (HCl)":
            st.write("### Pemisahan Ag+, Pb2+, Hg2^2+")
            if st.button("Jalankan Uji Gol I"):
                render_tube("white", is_mixed=True)
                centrifuge_simulation()
                st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
                render_tube("rgba(200,230,255,0.4)", "white", 45)
                st.success("Pb2+ diidentifikasi dengan K2CrO4 menghasilkan endapan kuning 🟡")
        
        elif gol == "Golongan III (NH4OH)":
            st.write("### Pemisahan Fe3+ & Al3+")
            if st.button("Uji Besi (Fe3+)"):
                st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
                render_tube("#b91c1c")
        
        elif gol == "Golongan IV (Karbonat)":
            st.write("### Identifikasi Ba2+, Sr2+, Ca2+")
            k1, k2, k3 = st.columns(3)
            with k1:
                st.caption("Barium (Ba2+)")
                render_flame("#adff2f") # Hijau Apel
                st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \text{ (Kuning)}")
            with k2:
                st.caption("Stronsium (Sr2+)")
                render_flame("#ef4444") # Merah Tua
                st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \text{ (Putih)}")
            with k3:
                st.caption("Kalsium (Ca2+)")
                render_flame("#f97316") # Merah Bata
                st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \text{ (Putih)}")

    # --- BAGIAN 3: ANION PER ION (TABS) ---
    elif menu == "🧪 Anion (Per Ion)":
        st.subheader("Identifikasi Anion Spesifik (Source 5)")
        an_tab1, an_tab2, an_tab3, an_tab4 = st.tabs(["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
        
        with an_tab1:
            st.latex(r"Cl^-(aq) + AgNO_3(aq) \rightarrow AgCl(s) \downarrow + NO_3^-(aq)")
            if st.button("Simulasikan Reaksi Cl-"):
                render_tube("rgba(255,255,255,0.2)", "white", 35)
                st.write("Hasil: **Endapan Putih**")
        
        with an_tab2:
            st.latex(r"2I^-(aq) + HgCl_2(aq) \rightarrow HgI_2(s) \downarrow + 2Cl^-(aq)")
            if st.button("Simulasikan Reaksi I-"):
                render_tube("yellow", "#ef4444", 40)
                st.warning("Catatan: Jika KI berlebih, terbentuk larutan kuning kompleks [HgI4]2-")
        
        with an_tab3:
            st.latex(r"CO_3^{2-}(aq) + 2HCl(aq) \rightarrow CO_2(g) \uparrow + H_2O(l) + 2Cl^-(aq)")
            st.write("Hasil: **Terbentuk gas CO2** dan endapan putih dengan BaCl2.")
            
        with an_tab4:
            st.latex(r"SO_4^{2-}(aq) + BaCl_2(aq) \rightarrow BaSO_4(s) \downarrow + 2Cl^-(aq)")
            if st.button("Simulasikan Reaksi SO4 2-"):
                render_tube("rgba(200,230,255,0.2)", "white", 40)

