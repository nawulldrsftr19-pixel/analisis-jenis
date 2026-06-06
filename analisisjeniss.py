import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Lab Virtual: Analisis Kualitatif", layout="wide")

# --- CUSTOM CSS (TEMA BIRU & ANIMASI) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f7ff; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .section-box { background: white; padding: 20px; border-radius: 12px; border-left: 8px solid #1976d2; margin-bottom: 20px; }
    .tube-container { display: flex; justify-content: center; margin: 20px 0; }
    .tube {
        width: 60px; height: 180px; border: 3px solid #555; border-radius: 0 0 30px 30px;
        position: relative; background: rgba(255,255,255,0.5); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1s ease; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 25px 25px; transition: all 1s ease; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI & VISUAL ---
def visualisasi_reaksi(warna_larutan, warna_endapan=None, tinggi_endapan=0):
    pellet_html = f'<div class="pellet" style="height:{tinggi_endapan}px; background:{warna_endapan};"></div>' if warna_endapan else ""
    st.markdown(f"""
        <div class="tube-container">
            <div class="tube">
                <div class="liquid" style="height:80%; background:{warna_larutan}; opacity:0.7;"></div>
                {pellet_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

def animasi_sentrifugasi():
    with st.spinner("🌀 Memutar pada 3000 rpm (Sesuai Prosedur)..."):
        p = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            p.progress(i + 1)
    st.success("✅ Pemisahan Selesai! Pellet (bawah) dan Supernatan (atas) terpisah.")

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Analisis Kation & Anion</h1>', unsafe_allow_html=True)

menu = st.sidebar.selectbox("Pilih Menu Utama:", ["Bagan Alir Interaktif", "Analisis Kation (Prosedur)", "Analisis Anion", "Uji Nyala Kation"])

# --- MENU 1: BAGAN ALIR INTERAKTIF (Berdasarkan Source 4) ---
if menu == "Bagan Alir Interaktif":
    st.header("📋 Bagan Pemisahan Kation (Source 4)")
    st.info("Klik tab di bawah untuk melihat detail pemisahan dari campuran sampel.")
    
    tab1, tab2, tab3 = st.tabs(["Golongan I (HCl)", "Golongan III (NH4OH)", "Golongan IV ((NH4)2CO3)"])
    
    with tab1:
        st.subheader("Pemisahan Golongan I")
        st.write("Sampel + **HCl encer** → Endapan Putih (AgCl, PbCl2, Hg2Cl2)")
        if st.button("Lihat Hasil Reaksi Gol I"):
            st.code("AgCl + NH4OH -> [Ag(NH3)2]+ (Larut)\nPb2+ + K2CrO4 -> PbCrO4 (Kuning)\nHg2Cl2 + NH4OH -> Hg + Hg(NH2)Cl (Hitam)")
            visualisasi_reaksi("rgba(255,255,255,0.8)", "white", 40)
            
    with tab2:
        st.subheader("Pemisahan Golongan III")
        st.write("Supernatan + **NH4OH** → Endapan Fe(OH)3 & Al(OH)3")
        if st.button("Lihat Hasil Reaksi Gol III"):
            st.code("Fe3+ + SCN- -> [Fe(SCN)]2+ (Merah Darah)\nAl(OH)3 + NaOH -> [Al(OH)4]- (Larut)")
            visualisasi_reaksi("rgba(139, 0, 0, 0.8)", "#8B4513", 40)

    with tab3:
        st.subheader("Pemisahan Golongan IV")
        st.write("Supernatan + **(NH4)2CO3** → Endapan BaCO3, SrCO3, CaCO3")
        if st.button("Lihat Hasil Reaksi Gol IV"):
            st.code("Ba2+ + CrO4^2- -> BaCrO4 (Kuning)\nSr2+ + SO4^2- -> SrSO4 (Putih)\nCa2+ + C2O4^2- -> CaC2O4 (Putih)")
            visualisasi_reaksi("yellow", "yellow", 40)

# --- MENU 2: ANALISIS KATION (Prosedur Source 1 & 2) ---
elif menu == "Analisis Kation (Prosedur)":
    st.header("🔬 Prosedur Sentrifugasi")
    st.warning("⚠️ Catatan: Pastikan tabung seimbang sebelum sentrifugasi [5].")
    
    opsi_kation = st.selectbox("Pilih Kation Uji:", ["Ag+", "Pb2+", "Hg2^2+", "Fe3+", "Ba2+"])
    
    if st.button("Jalankan Prosedur Lab"):
        if opsi_kation in ["Ag+", "Pb2+", "Hg2^2+"]:
            st.write("1. Menambahkan HCl encer...")
            animasi_sentrifugasi()
            if opsi_kation == "Pb2+":
                st.write("2. Menambahkan K2CrO4 → 🟡 Endapan Kuning [1]")
                visualisasi_reaksi("rgba(255,255,224,0.5)", "yellow", 40)
            elif opsi_kation == "Hg2^2+":
                st.write("2. Menambahkan NH4OH → ⚫ Endapan Hitam [1]")
                visualisasi_reaksi("rgba(0,0,0,0.2)", "black", 40)
        
        elif opsi_kation == "Fe3+":
            st.write("1. Menambahkan NH4OH, lalu SCN-...")
            animasi_sentrifugasi()
            st.write("2. Hasil: 🔴 Larutan Merah Darah [2]")
            visualisasi_reaksi("#b71c1c", tinggi_endapan=0)

# --- MENU 3: ANALISIS ANION (Berdasarkan Source 5) ---
elif menu == "Analisis Anion":
    st.header("🧪 Identifikasi Anion (Source 5)")
    anion = st.selectbox("Pilih Anion:", ["Cl- (Klorida)", "I- (Iodida)", "CO3^2- (Karbonat)", "SO4^2- (Sulfat)"])
    
    if anion == "Cl- (Klorida)":
        st.write("**Pereaksi:** AgNO3 + HNO3")
        st.write("**Hasil:** ⚪ Endapan Putih")
        visualisasi_reaksi("rgba(255,255,255,0.5)", "white", 30)
    elif anion == "I- (Iodida)":
        st.write("**Pereaksi:** HgCl2")
        st.write("**Hasil:** 🔴 Endapan Merah (HgI2), jika KI berlebih → Larutan Kuning")
        visualisasi_reaksi("yellow", "red", 30)
    elif anion == "CO3^2- (Karbonat)":
        st.write("**Pereaksi:** BaCl2 / HCl")
        st.write("**Hasil:** ⚪ Endapan Putih BaCO3 / Terbentuk gas CO2")
        visualisasi_reaksi("rgba(255,255,255,0.3)", "white", 30)
    elif anion == "SO4^2- (Sulfat)":
        st.write("**Pereaksi:** BaCl2")
        st.write("**Hasil:** ⚪ Endapan Putih BaSO4")
        visualisasi_reaksi("rgba(255,255,255,0.3)", "white", 30)

# --- MENU 4: UJI NYALA (Informasi Tambahan) ---
elif menu == "Uji Nyala Kation":
    st.header("🔥 Simulasi Uji Nyala")
    st.info("Visualisasi warna nyala untuk kation Golongan IV (Berdasarkan standar kimia umum).")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Barium (Ba2+)")
        st.markdown("<div style='background:#adff2f; height:100px; border-radius:10px; display:flex; align-items:center; justify-content:center; color:black;'><b>Hijau Apel</b></div>", unsafe_allow_html=True)
    with col2:
        st.subheader("Stronsium (Sr2+)")
        st.markdown("<div style='background:#ff0000; height:100px; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white;'><b>Merah Tua</b></div>", unsafe_allow_html=True)
    with col3:
        st.subheader("Kalsium (Ca2+)")
        st.markdown("<div style='background:#ff4500; height:100px; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white;'><b>Merah Bata</b></div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.caption("Sumber Data: analisis_kation_sentrifugasi.pdf & Tabel Anion")
