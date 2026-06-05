import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Lab Virtual: Analisis Kation", layout="wide")

# --- GAYA VISUAL (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; }
    .test-tube {
        border: 2px solid #333;
        border-radius: 0 0 25px 25px;
        width: 60px;
        height: 150px;
        margin: 10px auto;
        position: relative;
        background: #e0e0e0;
    }
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        border-radius: 0 0 22px 22px;
        transition: height 1s, background-color 1s;
    }
    .pellet {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 20px;
        border-radius: 0 0 22px 22px;
        background-color: #555;
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def visualisasi_tabung(warna_larutan="rgba(255,255,255,0.5)", tinggi_isi="70%", ada_pellet=False, warna_pellet="#fff"):
    pellet_display = "block" if ada_pellet else "none"
    st.markdown(f"""
        <div class="test-tube">
            <div class="liquid" style="height: {tinggi_isi}; background-color: {warna_larutan};"></div>
            <div class="pellet" style="display: {pellet_display}; background-color: {warna_pellet};"></div>
        </div>
    """, unsafe_allow_html=True)

def animasi_sentrifugasi():
    with st.spinner('🔄 Menyeimbangkan tabung dan memutar pada 3000 rpm...'):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.03)
            bar.progress(i + 1)
    st.success("✅ Sentrifugasi Selesai (1-2 menit). Pellet dan Supernatan terpisah!")

# --- UI UTAMA ---
st.title("🧪 Simulasi Analisis Kualitatif Kation")
st.caption("Berdasarkan Metode Sentrifugasi (Ag+, Pb2+, Hg2^2+, Fe3+, Al3+, Ba2+, Sr2+, Ca2+)")

menu = st.sidebar.selectbox("Pilih Tahapan Analisis:", 
    ["Pendahuluan", "Golongan I (HCl)", "Golongan III (NH4OH)", "Golongan IV ((NH4)2CO3)"])

# --- HALAMAN: PENDAHULUAN ---
if menu == "Pendahuluan":
    st.header("📍 Prinsip Dasar")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        **Sentrifugasi** digunakan untuk memisahkan:
        1. **Pellet (Endapan)**: Partikel padat di bawah tabung [1].
        2. **Supernatan (Larutan)**: Cairan bening di atas pellet [1].
        """)
        visualisasi_tabung(warna_larutan="rgba(173, 216, 230, 0.5)", ada_pellet=True, warna_pellet="#f0f0f0")
    with col2:
        st.warning("**Catatan Penting:**\n- Pastikan tabung seimbang saat sentrifugasi.\n- Ambil supernatan dengan hati-hati agar tidak mengganggu pellet [2].")

# --- HALAMAN: GOLONGAN I ---
elif menu == "Golongan I (HCl)":
    st.header("🧪 Pemisahan Golongan I")
    st.write("Sampel + **HCl encer**")
    
    if st.button("Jalankan Reaksi & Sentrifugasi"):
        visualisasi_tabung(warna_larutan="white", tinggi_isi="80%")
        st.info("Terbentuk endapan putih AgCl, PbCl2, dan Hg2Cl2 [1].")
        animasi_sentrifugasi()
        
        st.subheader("Uji Identifikasi Spesifik:")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Perak (Ag+)**")
            st.write("AgCl + NH4OH → Larut")
            visualisasi_tabung(warna_larutan="rgba(255,255,255,0.8)")
        with c2:
            st.markdown("**Timbal (Pb2+)**")
            st.write("+ K2CrO4 → 🟡 Kuning")
            visualisasi_tabung(warna_larutan="yellow")
        with c3:
            st.markdown("**Merkuri (Hg2^2+)**")
            st.write("+ NH4OH → ⚫ Hitam")
            visualisasi_tabung(warna_larutan="black")

# --- HALAMAN: GOLONGAN III ---
elif menu == "Golongan III (NH4OH)":
    st.header("🧪 Pemisahan Golongan III")
    st.write("Supernatan + **NH4OH**")
    
    if st.button("Jalankan Reaksi"):
        st.info("Terbentuk endapan Fe(OH)3 dan Al(OH)3 [3].")
        animasi_sentrifugasi()
        
        st.subheader("Hasil Identifikasi:")
        k1, k2 = st.columns(2)
        with k1:
            st.error("**Besi (Fe3+)**")
            st.write("+ SCN- → 🔴 Merah Darah")
            visualisasi_tabung(warna_larutan="rgba(139, 0, 0, 0.9)")
        with k2:
            st.success("**Aluminium (Al3+)**")
            st.write("Al(OH)3 larut dalam NaOH dan mengendap kembali dengan HCl [3].")
            visualisasi_tabung(warna_larutan="rgba(255, 255, 255, 0.3)", ada_pellet=True, warna_pellet="white")

# --- HALAMAN: GOLONGAN IV ---
elif menu == "Golongan IV ((NH4)2CO3)":
    st.header("🧪 Pemisahan Golongan IV")
    st.write("Supernatan + **(NH4)2CO3**")
    
    if st.button("Jalankan Pengendapan"):
        st.info("Terbentuk endapan BaCO3, SrCO3, dan CaCO3 (Semua Putih) [3].")
        animasi_sentrifugasi()
        
        st.subheader("Uji Spesifik & Simulasi Uji Nyala:")
        j1, j2, j3 = st.columns(3)
        with j1:
            st.warning("**Barium (Ba2+)**")
            st.write("+ CrO4^2- → 🟡 Kuning")
            st.markdown("<div style='background: #adff2f; color: black; padding: 5px; text-align:center;'>🔥 Nyala Hijau Apel</div>", unsafe_allow_html=True)
            visualisasi_tabung(warna_larutan="yellow")
        with j2:
            st.error("**Stronsium (Sr2+)**")
            st.write("+ SO4^2- → ⚪ Putih")
            st.markdown("<div style='background: #ff0000; color: white; padding: 5px; text-align:center;'>🔥 Nyala Merah Tua</div>", unsafe_allow_html=True)
            visualisasi_tabung(warna_larutan="white")
        with j3:
            st.error("**Kalsium (Ca2+)**")
            st.write("+ C2O4^2- → ⚪ Putih")
            st.markdown("<div style='background: #ff4500; color: white; padding: 5px; text-align:center;'>🔥 Nyala Merah Bata</div>", unsafe_allow_html=True)
            visualisasi_tabung(warna_larutan="white")

st.sidebar.markdown("---")
st.sidebar.info("Gunakan aplikasi ini untuk memahami urutan pemisahan kation secara kualitatif.")
