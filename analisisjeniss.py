import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Interactive Kation MindMap", layout="wide")

# --- CSS CUSTOM UNTUK TAMPILAN BAGAN (MIND MAP STYLE) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .center-col { display: flex; flex-direction: column; align-items: center; }
    
    /* Gaya Kotak Bagan (Nodes) */
    .node {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
        min-width: 200px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        border: 2px solid #333;
    }
    .node-start { background-color: #e1bee7; color: #4a148c; } /* Ungu */
    .node-reagent { background-color: #bbdefb; color: #0d47a1; } /* Biru */
    .node-result { background-color: #c8e6c9; color: #1b5e20; } /* Hijau */
    .node-final { background-color: #fff9c4; color: #f57f17; border: 2px dashed #f57f17; } /* Kuning */
    
    /* Panah Penghubung */
    .arrow { font-size: 24px; color: #333; margin: -5px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- UI UTAMA (SEMUA DI TENGAH) ---
st.markdown("<h1 style='text-align: center; color: #0d47a1;'>🧪 Bagan Alir Pemisahan Kation Interaktif</h1>", unsafe_allow_html=True)
st.write("<center>Berdasarkan bagan pemisahan kation Gol I - V</center>", unsafe_allow_html=True)

# Layout Tengah
_, col_center, _ = st.columns([1])

with col_center:
    # Komponen awal yang selalu muncul
    st.markdown('<div class="center-col"><div class="node node-start">Campuran Contoh Gol I - V</div><div class="arrow">↓</div><div class="node node-reagent">+ HCl Encer</div></div>', unsafe_allow_html=True)
    
    st.divider()
    
    # TABS UNTUK TIAP CABANG BAGAN
    tab1, tab2, tab3 = st.tabs(["🔹 Golongan I (Endapan)", "🔹 Golongan III (Endapan)", "🔹 Golongan IV (Larutan)"])

    # --- TAB GOLONGAN I ---
    with tab1:
        st.info("Eksplorasi pemisahan dari Endapan Gol I (AgCl, PbCl2, Hg2Cl2)")
        sub_step_gol1 = st.radio("Pilih Tahapan Identifikasi:", ["Awal", "Pemisahan Pb", "Pemisahan Ag & Hg"], horizontal=True)
        
        st.markdown('<div class="center-col">', unsafe_allow_html=True)
        st.markdown('<div class="node node-result">Endapan Gol I (AgCl, PbCl2, Hg2Cl2)</div>', unsafe_allow_html=True)
        
        if sub_step_gol1 != "Awal":
            st.markdown('<div class="arrow">↓</div><div class="node node-reagent">+ H2O Panas</div>', unsafe_allow_html=True)
            
            if sub_step_gol1 == "Pemisahan Pb":
                st.markdown('<div class="arrow">↓</div><div class="node node-final">Pb2+<br>(+ K2CrO4 -> PbCrO4 Kuning 🟡)</div>', unsafe_allow_html=True)
            
            elif sub_step_gol1 == "Pemisahan Ag & Hg":
                st.markdown('<div class="arrow">↓</div><div class="node node-result">Residu AgCl, Hg2Cl2</div>', unsafe_allow_html=True)
                st.markdown('<div class="arrow">↓</div><div class="node node-reagent">+ NH4OH Berlebih</div>', unsafe_allow_html=True)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown('<div class="node node-final">Hg(NH2)Cl + Hg<br>(Putih + Hitam ⚫)</div>', unsafe_allow_html=True)
                with col_b:
                    st.markdown('<div class="node node-final">Ag(NH3)2+ Cl-<br>(+ HNO3 -> AgCl Putih ⚪)</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- TAB GOLONGAN III ---
    with tab2:
        st.info("Eksplorasi pemisahan dari Larutan (Al3+, Fe3+)")
        if st.checkbox("Tampilkan Alur Pemisahan Gol III"):
            st.markdown('<div class="center-col">', unsafe_allow_html=True)
            st.markdown('<div class="node node-result">Larutan (Al3+, Fe3+, Ba2+, Sr2+, Ca2+)</div>', unsafe_allow_html=True)
            st.markdown('<div class="arrow">↓</div><div class="node node-reagent">+ NH4OH Berlebih</div>', unsafe_allow_html=True)
            st.markdown('<div class="arrow">↓</div><div class="node node-result">Endapan Gol III (Al(OH)3, Fe(OH)3)</div>', unsafe_allow_html=True)
            st.markdown('<div class="arrow">↓</div><div class="node node-reagent">+ NaOH</div>', unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="node node-final">Fe(OH)3<br>(+ SCN- -> Merah Darah 🔴)</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="node node-final">Al(OH)4-<br>(+ HCl -> Al(OH)3 Putih ⚪)</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- TAB GOLONGAN IV ---
    with tab3:
        st.info("Eksplorasi pemisahan untuk kation alkali tanah")
        if st.button("Lihat Bagan Golongan IV"):
            st.markdown('<div class="center-col">', unsafe_allow_html=True)
            st.markdown('<div class="node node-result">Larutan Gol IV (Ba2+, Sr2+, Ca2+)</div>', unsafe_allow_html=True)
            st.markdown('<div class="arrow">↓</div><div class="node node-reagent">+ K2CrO4</div>', unsafe_allow_html=True)
            
            # Percabangan Ba vs Sr/Ca
            ca1, ca2 = st.columns(2)
            with ca1:
                st.markdown('<div class="node node-final">BaCrO4 (Kuning 🟡)</div>', unsafe_allow_html=True)
            with ca2:
                st.markdown('<div class="node node-result">Larutan Sr2+, Ca2+</div>', unsafe_allow_html=True)
                st.markdown('<div class="arrow">↓</div><div class="node node-reagent">+ Na2CO3 / H2C2O4</div>', unsafe_allow_html=True)
                st.markdown('<div class="node node-final">Endapan Putih (Sr/Ca) ⚪</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
