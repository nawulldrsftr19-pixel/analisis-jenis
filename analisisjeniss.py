import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif Pro", layout="wide")

# --- CSS: ESTETIKA MODERN & ANIMASI NYATA ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%); }
    .main-title { color: #0369a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 8px solid #0284c7; margin-bottom: 25px; }
    .center-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    
    /* Animasi Centrifuge */
    .centrifuge-spin {
        width: 70px; height: 70px; border: 6px dashed #0284c7;
        border-radius: 50%; animation: spin 0.8s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi (Pellet & Supernatan) */
    .tube-container { display: flex; flex-direction: column; align-items: center; margin: 20px 0; }
    .tube {
        width: 60px; height: 180px; border: 3px solid #334155;
        border-radius: 0 0 30px 30px; position: relative;
        background: rgba(255,255,255,0.4); overflow: hidden;
        box-shadow: inset 5px 0 10px rgba(255,255,255,0.5);
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease-in-out; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 25px 25px; transition: all 1.5s ease-in-out; }
    
    /* Animasi Api (Uji Nyala) */
    .flame-box { display: flex; justify-content: center; align-items: flex-end; height: 60px; }
    .flame {
        width: 30px; height: 30px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg); animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker { 0% { transform: rotate(-45deg) scale(1); } 100% { transform: rotate(-45deg) scale(1.2); opacity: 0.9; } }

    /* Gaya Bagan (Flowchart Node) */
    .node { padding: 12px; border-radius: 10px; border: 2px solid #0369a1; background: #e0f2fe; text-align: center; margin: 10px 0; font-weight: bold; font-size: 0.95rem; color: #0c4a6e; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def play_centrifuge():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        st.write("<center>🌀 <b>Sentrifugasi 3000 rpm berlangsung...</b></center>", unsafe_allow_html=True)
        time.sleep(2)
    placeholder.empty()

def render_tube(liq_color, p_color=None, p_height=0, mixed=False):
    op = "0.5" if mixed else "0.8"
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube-container"><div class="tube"><div class="liquid" style="height:75%; background:{liq_color}; opacity:{op};"></div>{p_html}</div></div>', unsafe_allow_html=True)

def render_flame(color):
    st.markdown(f'<div class="flame-box"><div class="flame" style="background:{color}; box-shadow:0 0 15px {color};"></div></div>', unsafe_allow_html=True)

# --- SIDEBAR: SEMUA DIAGRAM ALIR INTERAKTIF ---
st.sidebar.title("📍 Diagram Alir Pemisahan")
st.sidebar.info("Klik alur di bawah untuk melihat detail setiap langkah pemisahan.")

# Alur Utama yang bisa di-klik
main_step = st.sidebar.radio("Pilih Tahapan Utama:", ["Campuran Sampel", "Golongan I (Endapan)", "Golongan III (Filtrat)", "Golongan IV (Filtrat)"])

# Sub-Alur (Detail Diagram)
sub_step = None
if main_step == "Golongan I (Endapan)":
    sub_step = st.sidebar.selectbox("Detail Pemisahan Gol I:", ["Langkah Awal (+HCl)", "Pemisahan Timbal (Pb)", "Identifikasi Ag & Hg"])
elif main_step == "Golongan III (Filtrat)":
    sub_step = st.sidebar.selectbox("Detail Pemisahan Gol III:", ["Pengendapan Hidroksida", "Uji Besi (Fe3+) & Aluminium (Al3+)"])
elif main_step == "Golongan IV (Filtrat)":
    sub_step = st.sidebar.selectbox("Detail Identifikasi Gol IV:", ["Penyajian Vertikal"])

st.sidebar.divider()
anion_mode = st.sidebar.checkbox("Buka Panel Analisis Anion")

# --- AREA UTAMA TERPUSAT ---
st.markdown('<h1 class="main-title">Lab Virtual: Analisis Kualitatif Kation & Anion</h1>', unsafe_allow_html=True)
_, col_main, _ = st.columns([0.1, 0.8, 0.1])

with col_main:
    st.markdown('<div class="center-card">', unsafe_allow_html=True)

    # LOGIKA NAVIGASI DIAGRAM ALIR
    if not anion_mode:
        if main_step == "Campuran Sampel":
            st.subheader("Prinsip Awal: Pemisahan Campuran Gol I - V")
            st.markdown('<div class="node">Campuran Contoh Kation (Gol I - V)</div>', unsafe_allow_html=True)
            st.write("<center>⬇️ <b>+ HCl Encer</b></center>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="node" style="border-color:#ef4444;">Endapan Golongan I</div>', unsafe_allow_html=True)
                st.caption("AgCl, PbCl₂, Hg₂Cl₂ (Putih) [1, 2]")
            with c2:
                st.markdown('<div class="node" style="border-color:#10b981;">Larutan Gol III, IV, V</div>', unsafe_allow_html=True)
                st.caption("Filtrat untuk analisis tahap berikutnya [2]")

        elif main_step == "Golongan I (Endapan)":
            st.subheader(f"Analisis Golongan I: {sub_step}")
            if sub_step == "Langkah Awal (+HCl)":
                st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
                if st.button("Simulasi Sentrifugasi"):
                    play_centrifuge()
                    render_tube("rgba(200,230,255,0.3)", "white", 45)
            elif sub_step == "Pemisahan Timbal (Pb)":
                st.write("Endapan ditambahkan air panas untuk melarutkan $PbCl_2$ [2].")
                st.latex(r"Pb^{2+}(aq) + CrO_4^{2-}(aq) \rightarrow PbCrO_4(s) \downarrow \text{ (Kuning)}")
                render_tube("rgba(255,255,224,0.3)", "#facc15", 35)
            elif sub_step == "Identifikasi Ag & Hg":
                st.write("Residu ditambahkan $NH_4OH$ berlebih [2].")
                st.markdown("- **Hg:** Terbentuk endapan hitam ($Hg + Hg(NH_2)Cl$) [2].")
                st.markdown("- **Ag:** Perak larut sebagai kompleks $[Ag(NH_3)_2]^+$ [2].")

        elif main_step == "Golongan III (Filtrat)":
            st.subheader(f"Analisis Golongan III: {sub_step}")
            if sub_step == "Pengendapan Hidroksida":
                st.write("Ditambahkan $NH_4OH$ berlebih untuk mengendapkan kation golongan III [2, 3].")
                st.markdown('<div class="node">Endapan Gol III (Al(OH)₃, Fe(OH)₃)</div>', unsafe_allow_html=True)
            elif sub_step == "Uji Besi (Fe3+) & Aluminium (Al3+)":
                st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Merah Darah)}")
                render_tube("#991b1b")
                st.latex(r"Al(OH)_3 + NaOH \rightarrow [Al(OH)_4]^- \text{ (Larut)}")

        elif main_step == "Golongan IV (Filtrat)":
            st.subheader("Identifikasi Golongan IV (Penyajian Vertikal)")
            st.markdown("### 1. Barium (Ba²⁺)")
            render_api("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4(s) \downarrow \text{ (Kuning)}")
            
            st.markdown("---")
            st.markdown("### 2. Stronsium (Sr²⁺)")
            render_api("#ef4444")
            st.latex(r"Sr^{2+} + SO_4^{2-} \rightarrow SrSO_4(s) \downarrow \text{ (Putih)}")
            
            st.markdown("---")
            st.markdown("### 3. Kalsium (Ca²⁺)")
            render_api("#f97316")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4(s) \downarrow \text{ (Putih)}")

    # --- PANEL ANALISIS ANION (Sesuai Tabel 6.1) ---
    else:
        st.subheader("Identifikasi Anion Spesifik")
        an_tab = st.tabs(["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
        
        with an_tab:
            st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            if st.button("Uji Cl⁻"): render_tube("rgba(255,255,255,0.2)", "white", 35)
        
        with an_tab[1]:
            st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah Jingga)}")
            if st.button("Uji I⁻"): render_tube("yellow", "#ef4444", 40)
            st.caption("Catatan: Kelebihan KI melarutkan endapan menjadi kompleks kuning [4].")

        with an_tab[3]:
            st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O + 2Cl^-")
            st.write("Hasil: Terbentuk gas (gelembung) [4].")

        with an_tab[5]:
            st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow \text{ (Putih)}")
            if st.button("Uji SO₄²⁻"): render_tube("rgba(200,230,255,0.2)", "white", 40)

    st.markdown('</div>', unsafe_allow_html=True)
