import streamlit as st
import time
import graphviz

st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

st.title("🧪 Virtual Lab — Analisis Kualitatif Kation & Anion")

# --- FUNGSI VISUAL ---
def tube_viz(liq_color, p_color=None, p_height=0):
    p_html = f'<div style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div style="width:55px;height:160px;border:2px solid #333;border-radius:0 0 30px 30px;position:relative;background:rgba(255,255,255,0.4);overflow:hidden;"><div style="position:absolute;bottom:0;width:100%;height:75%;background:{liq_color};opacity:0.6;"></div>{p_html}</div>', unsafe_allow_html=True)

def flame_viz(color):
    st.markdown(f'<div style="width:35px;height:35px;border-radius:50%;background:{color};box-shadow:0 0 20px {color};margin:10px;"></div>', unsafe_allow_html=True)

# --- TAB MENU ---
tab1, tab2, tab3 = st.tabs(["📊 Bagan Alir (Mind Map)", "🔹 Analisis Kation", "🧪 Analisis Anion"])

# --- TAB 1: BAGAN ALIR ---
with tab1:
    st.subheader("📊 Bagan Pemisahan Kation (Mind Map)")
    if 'langkah' not in st.session_state:
        st.session_state.langkah = 0

    def buat_bagan(step):
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB', size='10,10')  # TB = top to bottom

        dot.node('start', 'Campuran Gol I–V', style='filled', color='lavender')
        if step >= 1:
            dot.node('hcl', '+ HCl encer')
            dot.edge('start', 'hcl')
            dot.node('gol1', 'Endapan Gol I (Ag, Pb, Hg)', style='filled', color='lightblue')
            dot.node('larutan1', 'Larutan (Al, Fe, Ba, Sr, Ca)', style='filled', color='lightblue')
            dot.edge('hcl', 'gol1')
            dot.edge('hcl', 'larutan1')
        if step >= 2:
            dot.node('h2o', '+ H2O Panas')
            dot.edge('gol1', 'h2o')
            dot.node('pb', 'Pb²⁺')
            dot.node('residu', 'Residu AgCl, Hg₂Cl₂')
            dot.edge('h2o', 'pb')
            dot.edge('h2o', 'residu')
            dot.node('nh4oh', '+ NH₄OH berlebih')
            dot.edge('larutan1', 'nh4oh')
            dot.node('gol3', 'Endapan Gol III (Al, Fe)')
            dot.node('gol4', 'Larutan Gol IV (Ba, Sr, Ca)')
            dot.edge('nh4oh', 'gol3')
            dot.edge('nh4oh', 'gol4')
        if step >= 3:
            dot.node('k2cro4_pb', '+ K₂CrO₄')
            dot.edge('pb', 'k2cro4_pb')
            dot.node('hasil_pb', 'PbCrO₄ (Kuning)')
            dot.edge('k2cro4_pb', 'hasil_pb')
            dot.node('naoh', '+ NaOH')
            dot.edge('gol3', 'naoh')
            dot.node('fe', 'Fe(OH)₃')
            dot.node('al', 'Al(OH)₄⁻')
            dot.edge('naoh', 'fe')
            dot.edge('naoh', 'al')
            dot.node('k2cro4_iv', '+ K₂CrO₄')
            dot.edge('gol4', 'k2cro4_iv')
            dot.node('ba', 'BaCrO₄ (Kuning)')
            dot.node('sr_ca', 'Larutan Sr²⁺, Ca²⁺')
            dot.edge('k2cro4_iv', 'ba')
            dot.edge('k2cro4_iv', 'sr_ca')
        if step >= 4:
            dot.edge('fe', 'Fe(SCN)₃ (Merah)', label='+ SCN⁻')
            dot.edge('al', 'Al(OH)₃ (Putih)', label='+ HCl/Na₂CO₃')
            dot.edge('sr_ca', 'SrCO₃ (Putih)', label='+ Na₂CO₃')
            dot.edge('sr_ca', 'CaC₂O₄ (Putih)', label='+ H₂C₂O₄ + NH₄OH')
        return dot

    st.graphviz_chart(buat_bagan(st.session_state.langkah))

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Langkah Berikutnya"):
            if st.session_state.langkah < 4:
                st.session_state.langkah += 1
                st.rerun()
    with col2:
        if st.button("🔄 Reset"):
            st.session_state.langkah = 0
            st.rerun()

# --- TAB 2: ANALISIS KATION ---
with tab2:
    st.subheader("🛠️ Simulasi Pemisahan Kation")
    gol = st.selectbox("Pilih Golongan Kation:", ["Golongan I", "Golongan III", "Golongan IV"])
    if gol == "Golongan IV":
        st.info("Identifikasi Ba²⁺, Sr²⁺, Ca²⁺ melalui uji nyala & pengendapan.")
        st.markdown("### 🔬 Barium (Ba²⁺)")
        flame_viz("#adff2f")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
        st.write("Uji Nyala: Hijau Apel")
        st.markdown("### 🔬 Stronsium (Sr²⁺)")
        flame_viz("#ff0000")
        st.latex(r"Sr^{2+} + CO_3^{2-} \rightarrow SrCO_3(s) \downarrow \text{ (Putih)}")
        st.write("Uji Nyala: Merah Karmin")
        st.markdown("### 🔬 Kalsium (Ca²⁺)")
        flame_viz("#ff4500")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")
        st.write("Uji Nyala: Merah Bata")

# --- TAB 3: ANALISIS ANION ---
with tab3:
    st.subheader("📝 Identifikasi Anion Spesifik")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        tube_viz("lightblue", "white", 35)
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}")
        st.write("Jika KI berlebih → (HgI₄)²⁻ (Larutan Kuning).")
        tube_viz("yellow", "red", 35)
    elif anion == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
        st.write("Uji: gelembung gas CO₂ terbentuk.")
    elif anion == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
        tube_viz("lightblue", "white", 35)
