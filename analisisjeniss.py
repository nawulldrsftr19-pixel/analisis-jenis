import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- FUNGSI VISUAL ---
def tube_viz(liq_color, p_color=None, p_height=0):
    p_html = f'<div style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div style="width:55px;height:160px;border:2px solid #333;border-radius:0 0 30px 30px;position:relative;background:rgba(255,255,255,0.4);overflow:hidden;"><div style="position:absolute;bottom:0;width:100%;height:75%;background:{liq_color};opacity:0.6;"></div>{p_html}</div>', unsafe_allow_html=True)

def flame_viz(color):
    st.markdown(f'<div style="width:35px;height:35px;border-radius:50%;background:{color};box-shadow:0 0 20px {color};margin:10px;"></div>', unsafe_allow_html=True)

# --- UI UTAMA ---
st.title("🧪 Virtual Lab — Analisis Kualitatif Kation & Anion")

tab1, tab2, tab3 = st.tabs(["📊 Bagan Alir", "🔹 Analisis Kation", "🧪 Analisis Anion"])

# --- TAB 2: ANALISIS KATION ---
with tab2:
    st.subheader("🛠️ Simulasi Pemisahan Kation")
    gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol == "Golongan I":
        st.info("Penambahan HCl encer untuk memisahkan Ag+, Pb2+, Hg2^2+.")
        if st.button("Uji Golongan I"):
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}")
            st.latex(r"Hg_2^{2+} + 2Cl^- \rightarrow Hg_2Cl_2(s) \downarrow \text{ (Putih)}")
            tube_viz("lightblue", "white", 40)

    elif gol == "Golongan III":
        st.info("Penambahan NH4OH untuk memisahkan Fe3+ & Al3+.")
        if st.button("Uji Besi (Fe3+)"):
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3(aq) \text{ (Merah Darah)}")
            tube_viz("#b71c1c")
        if st.button("Uji Aluminium (Al3+)"):
            st.latex(r"Al^{3+} + 3OH^- \rightarrow Al(OH)_3(s) \downarrow \text{ (Putih)}")
            tube_viz("lightblue", "white", 35)

    elif gol == "Golongan IV":
        st.info("Identifikasi Ba2+, Sr2+, Ca2+ melalui uji nyala & pengendapan.")
        
        # Ditampilkan baris ke bawah
        st.markdown("### 🔬 Barium (Ba²⁺)")
        flame_viz("#adff2f")  # Hijau Apel
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        st.write("Uji Nyala: Hijau Apel")

        st.markdown("### 🔬 Stronsium (Sr²⁺)")
        flame_viz("#ff0000")  # Merah Tua
        st.latex(r"Sr^{2+} + CO_3^{2-} \rightarrow SrCO_3(s) \downarrow \text{ (Putih)}")
        st.write("Uji Nyala: Merah Karmin")

        st.markdown("### 🔬 Kalsium (Ca²⁺)")
        flame_viz("#ff4500")  # Merah Bata
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")
        st.write("Uji Nyala: Merah Bata")

# --- TAB 3: ANALISIS ANION ---
with tab3:
    st.subheader("📝 Identifikasi Anion Spesifik")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl-)", "Iodida (I-)", "Karbonat (CO3 2-)", "Sulfat (SO4 2-)"])
    
    if anion == "Klorida (Cl-)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        tube_viz("lightblue", "white", 35)
    elif anion == "Iodida (I-)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}")
        st.write("Jika KI berlebih → (HgI_4)^{2-} (Larutan Kuning).")
        tube_viz("yellow", "red", 35)
    elif anion == "Karbonat (CO3 2-)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
        st.write("Uji: gelembung gas CO₂ terbentuk.")
    elif anion == "Sulfat (SO4 2-)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
        tube_viz("lightblue", "white", 35)
