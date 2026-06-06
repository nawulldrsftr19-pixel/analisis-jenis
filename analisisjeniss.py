import streamlit as st
import time

# --- KONFIGURASI HALAMAN & TEMA ---
st.set_page_config(page_title="Lab Virtual: Analisis Kualitatif Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    .main-title { color: #0d47a1; text-align: center; padding: 15px; background: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    .tube-box { display: flex; justify-content: center; margin: 20px 0; }
    .tube {
        width: 60px; height: 180px; border: 3px solid #333; border-radius: 0 0 30px 30px;
        position: relative; background: rgba(255,255,255,0.4); overflow: hidden;
    }
    .supernatant { position: absolute; bottom: 0; width: 100%; transition: all 1.5s ease; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 25px 25px; transition: all 1.5s ease; }
    .flame-box { height: 80px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: bold; color: white; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI ANIMASI & VISUALISASI ---
def visualisasi_tabung(warna_sup, tinggi_sup=80, warna_pel=None, tinggi_pel=0):
    pellet_html = f'<div class="pellet" style="height:{tinggi_pel}px; background:{warna_pel};"></div>' if warna_pel else ""
    st.markdown(f"""
        <div class="tube-box">
            <div class="tube">
                <div class="supernatant" style="height:{tinggi_sup}%; background:{warna_sup}; opacity:0.7;"></div>
                {pellet_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

def animasi_sentrifugasi():
    with st.spinner("🌀 Sedang memutar pada 3000 rpm (1-2 menit)..."):
        p = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            p.progress(i + 1)
    st.success("✅ Sentrifugasi Selesai! Pellet (bawah) dan Supernatan (atas) terpisah.")

# --- HEADER ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Bagan Alir Analisis Kualitatif</h1>', unsafe_allow_html=True)

# --- BAGAN ALIR DENGAN TAB (Berdasarkan Sumber 4 & 5) ---
st.write("### 📋 Bagan Alir Pemisahan")
tab1, tab2, tab3, tab4 = st.tabs(["🔹 Golongan I", "🔹 Golongan III", "🔹 Golongan IV", "🔸 Analisis Anion"])

with tab1:
    st.info("Campuran Sampel + HCl encer → Endapan Putih (AgCl, PbCl2, Hg2Cl2) [1, 2]")
    if st.button("Jalankan Pemisahan Gol I"):
        visualisasi_tabung("rgba(255,255,255,0.8)") # Keruh sebelum sentrifugasi
        animasi_sentrifugasi()
        visualisasi_tabung("rgba(200,230,255,0.3)", tinggi_sup=60, warna_pel="white", tinggi_pel=40)
        
        st.subheader("Hasil Identifikasi Spesifik:")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Perak (Ag+)**")
            st.write("AgCl + NH4OH → Larut")
            st.write("+ HNO3 → ⚪ Putih [1]")
        with c2:
            st.markdown("**Timbal (Pb2+)**")
            st.write("+ K2CrO4 → 🟡 Kuning [1, 2]")
            st.markdown("<div class='flame-box' style='background:#add8e6; color:black;'>🔥 Nyala: Putih-Biru*</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("**Merkuri (Hg2^2+)**")
            st.write("+ NH4OH → ⚫ Hitam [1, 2]")

with tab2:
    st.info("Supernatan + NH4OH → Endapan Coklat/Putih (Fe(OH)3, Al(OH)3) [2, 3]")
    if st.button("Jalankan Pemisahan Gol III"):
        animasi_sentrifugasi()
        st.subheader("Hasil Identifikasi:")
        k1, k2 = st.columns(2)
        with k1:
            st.error("**Besi (Fe3+)**")
            st.write("+ SCN- → 🔴 Merah [2, 3]")
            visualisasi_tabung("#b71c1c", tinggi_sup=80)
        with k2:
            st.success("**Aluminium (Al3+)**")
            st.write("+ NaOH → Larut")
            st.write("+ HCl → ⚪ Putih Gelatin [2, 3]")

with tab3:
    st.info("Supernatan + (NH4)2CO3 → Endapan Putih (BaCO3, SrCO3, CaCO3) [2, 3]")
    if st.button("Jalankan Pemisahan Gol IV"):
        animasi_sentrifugasi()
        st.subheader("Uji Nyala & Reaksi Warna:")
        j1, j2, j3 = st.columns(3)
        with j1:
            st.write("**Barium (Ba2+)**")
            st.write("+ CrO4^2- → 🟡 Kuning [3]")
            st.markdown("<div class='flame-box' style='background:#adff2f; color:black;'>🔥 Hijau Apel*</div>", unsafe_allow_html=True)
        with j2:
            st.write("**Stronsium (Sr2+)**")
            st.write("+ SO4^2- → ⚪ Putih [3]")
            st.markdown("<div class='flame-box' style='background:#ff0000;'>🔥 Merah Tua*</div>", unsafe_allow_html=True)
        with j3:
            st.write("**Kalsium (Ca2+)**")
            st.write("+ C2O4^2- → ⚪ Putih [3]")
            st.markdown("<div class='flame-box' style='background:#ff4500;'>🔥 Merah Bata*</div>", unsafe_allow_html=True)

with tab4:
    st.header("🧪 Identifikasi Anion (Source 5)")
    anion_pilih = st.selectbox("Pilih Anion:", ["Cl-", "I-", "CO3^2-", "SO4^2-"])
    
    if anion_pilih == "Cl-":
        st.write("**Pereaksi:** AgNO3 + HNO3 → ⚪ Putih [4]")
        visualisasi_tabung("rgba(255,255,255,0.3)", warna_pel="white", tinggi_pel=30)
    elif anion_pilih == "I-":
        st.write("**Pereaksi:** HgCl2 → 🔴 Merah (HgI2) [4]")
        st.write("Jika KI berlebih → 🟡 Larutan Kuning [4]")
        visualisasi_tabung("yellow", warna_pel="red", tinggi_pel=30)
    elif anion_pilih == "CO3^2-":
        st.write("**Pereaksi:** HCl → Terbentuk Gas CO2 [4]")
        st.write("**Pereaksi:** BaCl2 → ⚪ Putih (BaCO3) [4]")
    elif anion_pilih == "SO4^2-":
        st.write("**Pereaksi:** BaCl2 → ⚪ Putih (BaSO4) [4]")
        visualisasi_tabung("rgba(255,255,255,0.2)", warna_pel="white", tinggi_pel=35)
