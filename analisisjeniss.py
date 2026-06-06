import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Interactive Cation Analysis Pro", layout="wide")

# --- CSS: VIBRANT & PENGHILANGAN CELAH PUTIH ---
st.markdown("""
    <style>
    /* Menghilangkan padding putih di bagian atas agar judul rapat ke atas */
    .block-container { padding-top: 1rem; }
    
    /* Tema Warna Vibrant */
    .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fff7ed 50%, #f0fdf4 100%); }
    
    /* Header Utama */
    .main-title { 
        color: white; text-align: center; background: linear-gradient(90deg, #0284c7, #3b82f6); 
        padding: 20px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        border-bottom: 5px solid #0c4a6e; margin-bottom: 20px;
    }
    
    /* Styling Tabs */
    div.stTabs [data-baseweb="tab-list"] { gap: 15px; }
    div.stTabs [data-baseweb="tab"] {
        background-color: white; border-radius: 10px; padding: 10px 25px; 
        font-weight: bold; color: #0369a1; border: 1px solid #bae6fd;
    }
    div.stTabs [aria-selected="true"] { background-color: #0284c7; color: white; }

    /* Gaya Node Bagan (Flowchart) */
    .node { 
        padding: 12px; border-radius: 10px; border: 2px solid #0369a1; 
        background: #f0f9ff; text-align: center; margin: 10px 0; 
        font-weight: bold; font-size: 0.95rem; color: #0c4a6e;
    }
    .result-node { background: #dcfce7; border-color: #16a34a; color: #166534; border-style: double; border-width: 4px; }
    .step-arrow { text-align: center; font-size: 24px; color: #64748b; margin: -10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI VISUALISASI ---
def render_tube(liq_color, pellet_color=None, p_height=0):
    p_html = f'<div style="position:absolute; bottom:0; width:100%; height:{p_height}px; background:{pellet_color}; border-radius:0 0 20px 20px;"></div>' if pellet_color else ""
    st.markdown(f"""
        <div style="display:flex; justify-content:center; margin:10px;">
            <div style="width:50px; height:150px; border:3px solid #334155; border-radius:0 0 25px 25px; position:relative; background:rgba(255,255,255,0.4); overflow:hidden;">
                <div style="position:absolute; bottom:0; width:100%; height:70%; background:{liq_color}; opacity:0.6;"></div>
                {p_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- JUDUL UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Bagan Pemisahan Kation Terpadu</h1>', unsafe_allow_html=True)

# --- NAVIGASI TAB ---
tab1, tab2 = st.tabs(["📍 Bagan Interaktif (Full Path)", "🧪 Reaksi & Simulasi"])

# --- TAB 1: BAGAN INTERAKTIF LENGKAP (SOURCE 5) ---
with tab1:
    st.info("Klik tombol pereaksi untuk menelusuri alur bagan secara interaktif hingga uji spesifik kation.")
    
    # Root Node
    st.markdown('<div class="node">Campuran Contoh Gol I - V</div>', unsafe_allow_html=True)
    
    # Langkah 1: HCl Encer
    if st.button("➕ Tambahkan HCl Encer", key="step1", type="primary"):
        st.markdown('<div class="step-arrow">⬇️</div>', unsafe_allow_html=True)
        col_g1, col_filtrat = st.columns(2)
        
        with col_g1:
            st.markdown('<div class="node" style="background:#fee2e2;">Endapan Gol I (AgCl, PbCl₂, Hg₂Cl₂)</div>', unsafe_allow_html=True)
            
            # Langkah 2 Gol I: H2O Panas
            if st.button("➕ Tambahkan H₂O Panas", key="g1_hot"):
                st.write("---")
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="node">Larutan Pb²⁺</div>', unsafe_allow_html=True)
                    if st.button("🟡 Uji Pb²⁺ (+ K₂CrO₄)", key="final_pb"):
                        st.markdown('<div class="node result-node">IDENTIFIKASI: PbCrO₄ (Kuning 🟡)</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown('<div class="node">Residu AgCl, Hg₂Cl₂</div>', unsafe_allow_html=True)
                    if st.button("➕ Tambahkan NH₄OH Berlebih", key="g1_nh4"):
                        st.markdown('<div class="node result-node">HASIL: Hg(NH₂)Cl + Hg (Putih + Hitam ⚫)</div>', unsafe_allow_html=True)
                        if st.button("⚪ Uji Ag⁺ (+ HNO₃)", key="final_ag"):
                            st.markdown('<div class="node result-node">IDENTIFIKASI: AgCl (Putih ⚪)</div>', unsafe_allow_html=True)

        with col_filtrat:
            st.markdown('<div class="node" style="background:#dcfce7;">Larutan (Al³⁺, Fe³⁺, Ba²⁺, Sr²⁺, Ca²⁺)</div>', unsafe_allow_html=True)
            
            # Langkah 2 Gol III: NH4OH Berlebih
            if st.button("➕ Tambahkan NH₄OH Berlebih", key="step2_filtrat"):
                st.write("---")
                col_g3, col_g4 = st.columns(2)
                
                with col_g3:
                    st.markdown('<div class="node">Endapan Gol III (Al(OH)₃, Fe(OH)₃)</div>', unsafe_allow_html=True)
                    # Langkah 3 Gol III: NaOH
                    if st.button("➕ Tambahkan NaOH", key="g3_naoh"):
                        st.write("---")
                        c3a, c3b = st.columns(2)
                        with c3a:
                            st.markdown('<div class="node">Residu Fe(OH)₃</div>', unsafe_allow_html=True)
                            if st.button("🔴 Uji Fe³⁺ (+ HNO₃ + SCN⁻)", key="final_fe"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: Fe(SCN)₃ (Larutan Merah 🔴)</div>', unsafe_allow_html=True)
                        with c3b:
                            st.markdown('<div class="node">Filtrat Al(OH)₄⁻</div>', unsafe_allow_html=True)
                            if st.button("⚪ Uji Al³⁺ (+ HCl / Na₂CO₃)", key="final_al"):
                                st.markdown('<div class="node result-node">IDENTIFIKASI: Al(OH)₃ (Endapan Putih ⚪)</div>', unsafe_allow_html=True)

                with col_g4:
                    st.markdown('<div class="node">Larutan Gol IV (Ba²⁺, Sr²⁺, Ca²⁺)</div>', unsafe_allow_html=True)
                    # Langkah 3 Gol IV: K2CrO4
                    if st.button("➕ Tambahkan K₂CrO₄", key="g4_k2cr"):
                        st.write("---")
                        c4a, c4b = st.columns(2)
                        with c4a:
                            st.markdown('<div class="node result-node">IDENTIFIKASI: BaCrO₄ (Endapan Kuning 🟡)</div>', unsafe_allow_html=True)
                        with c4b:
                            st.markdown('<div class="node">Larutan Sr²⁺, Ca²⁺</div>', unsafe_allow_html=True)
                            if st.button("➕ Uji Spesifik Sr & Ca", key="final_srca"):
                                st.markdown('<div class="node result-node">Sr²⁺ (+ Na₂CO₃ → SrCO₃ Putih ⚪)</div>', unsafe_allow_html=True)
                                st.markdown('<div class="node result-node">Ca²⁺ (+ CH₃COOH + H₂C₂O₄ + NH₄OH → CaC₂O₄ Putih ⚪)</div>', unsafe_allow_html=True)

# --- TAB 2: REAKSI & SIMULASI ---
with tab2:
    st.subheader("🧪 Simulasi Tabung Reaksi & Stoikiometri")
    pilih_gol = st.selectbox("Pilih Golongan untuk Simulasi:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if pilih_gol == "Golongan I":
        st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        st.latex(r"Pb^{2+} + CrO_4^{2-} \rightarrow PbCrO_4(s) \downarrow \text{ (Kuning)}")
        render_tube("rgba(200,230,255,0.3)", "white", 45)
        st.write("**Catatan:** PbCl₂ larut dalam air panas, sedangkan AgCl dan Hg₂Cl₂ tetap mengendap [1].")

    elif pilih_gol == "Golongan III":
        st.latex(r"Fe^{3+} + 3SCN^- \rightarrow [Fe(SCN)]_3 \text{ (Larutan Merah)}")
        st.latex(r"Al(OH)_3 + NaOH \rightarrow Al(OH)_4^- \text{ (Larut)}")
        render_tube("#991b1b")
        st.write("**Catatan:** Penambahan NaOH memisahkan Fe(OH)₃ (residu) dari Al(OH)₄⁻ (filtrat) [1].")

    elif pilih_gol == "Golongan IV":
        st.write("### Identifikasi Vertikal Golongan IV:")
        st.markdown("1. **Barium (Ba²⁺)**: $+ K_2CrO_4 \rightarrow BaCrO_4 \downarrow$ (Kuning 🟡)")
        st.markdown("2. **Stronsium (Sr²⁺)**: $+ Na_2CO_3 \rightarrow SrCO_3 \downarrow$ (Putih ⚪)")
        st.markdown("3. **Kalsium (Ca²⁺)**: $+ H_2C_2O_4 + NH_4OH \rightarrow CaC_2O_4 \downarrow$ (Putih ⚪)")
        render_tube("rgba(255,255,224,0.3)", "yellow", 35)
