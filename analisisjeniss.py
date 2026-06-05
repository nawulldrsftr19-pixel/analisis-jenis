import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="Simulasi Analisis Kation", layout="wide")

# Gaya CSS Custom untuk tampilan menarik
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        border-left: 5px solid #007bff;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 Aplikasi Laboratorium Virtual: Analisis Kation")
st.write("Metode Sentrifugasi - Berdasarkan Dokumen Analisis Kualitatif")

# Sidebar untuk Navigasi
st.sidebar.header("Pilih Tahapan Analisis")
tahapan = st.sidebar.radio("Tahapan:", ["Prinsip & Persiapan", "Golongan I", "Golongan III", "Golongan IV"])

# Fungsi Simulasi Sentrifugasi
def simulasi_sentrifugasi():
    with st.spinner('Proses Sentrifugasi sedang berlangsung (3000 rpm)...'):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            progress_bar.progress(percent_complete + 1)
    st.success("✅ Sentrifugasi Selesai! Pellet dan Supernatan telah terpisah.")
    st.info("💡 Tips: Ambil supernatan dengan hati-hati dan jangan mengganggu pellet [1].")

# --- Halaman 1: Prinsip ---
if tahapan == "Prinsip & Persiapan":
    st.header("🔍 Prinsip Dasar Sentrifugasi")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        Sentrifugasi digunakan untuk memisahkan endapan (**pellet**) dan larutan (**supernatan**) dengan gaya putar [2].
        - **Pellet**: Berada di bagian bawah tabung.
        - **Supernatan**: Berada di bagian atas.
        """)
    with col2:
        st.warning("⚠️ Pastikan tabung seimbang saat sentrifugasi [1].")
    
    if st.button("Lihat Animasi Pemisahan"):
        st.write("🔵 Larutan Keruh → 🔄 Sentrifugasi → ⚪ Pellet (Bawah) + 💧 Supernatan (Atas)")
        simulasi_sentrifugasi()

# --- Halaman 2: Golongan I ---
elif tahapan == "Golongan I":
    st.header("🧪 Identifikasi Golongan I (Ag⁺, Pb²⁺, Hg₂²⁺)")
    st.write("Langkah: Tambahkan **HCl encer** ke sampel [2].")
    
    if st.button("Tambahkan HCl & Sentrifugasi"):
        simulasi_sentrifugasi()
        st.subheader("Hasil Reaksi:")
        st.code("AgCl (Putih), PbCl2 (Putih), Hg2Cl2 (Putih)")
        
        st.markdown("### Uji Identifikasi Lanjutan")
        kol1, kol2, kol3 = st.columns(3)
        with kol1:
            st.info("**Ag⁺**")
            st.write("AgCl + NH₄OH → Larut")
            st.write("+ HNO₃ → Endapan Kembali [2]")
        with kol2:
            st.info("**Pb²⁺**")
            st.write("Pb²⁺ + K₂CrO₄ → 🟡 Endapan Kuning [2]")
            # Informasi luar sumber untuk uji nyala
            st.markdown("*Uji Nyala: Putih Kebiruan (Info Tambahan)*")
        with kol3:
            st.info("**Hg₂²⁺**")
            st.write("Hg₂Cl₂ + NH₄OH → ⚫ Endapan Hitam [2]")

# --- Halaman 3: Golongan III ---
elif tahapan == "Golongan III":
    st.header("🧪 Identifikasi Golongan III (Fe³⁺, Al³⁺)")
    st.write("Langkah: Tambahkan **NH₄OH** ke supernatan [3].")
    
    if st.button("Tambahkan NH₄OH & Sentrifugasi"):
        simulasi_sentrifugasi()
        st.subheader("Hasil Reaksi:")
        st.code("Fe(OH)3 (Coklat Kemerahan), Al(OH)3 (Putih Gelatin)")
        
        st.markdown("### Uji Identifikasi Lanjutan")
        k1, k2 = st.columns(2)
        with k1:
            st.error("**Fe³⁺**")
            st.write("Fe³⁺ + SCN⁻ → 🔴 Merah Darah [3]")
        with k2:
            st.success("**Al³⁺**")
            st.write("Al(OH)₃ larut dalam NaOH dan mengendap kembali dengan HCl [3]")

# --- Halaman 4: Golongan IV ---
elif tahapan == "Golongan IV":
    st.header("🧪 Identifikasi Golongan IV (Ba²⁺, Sr²⁺, Ca²⁺)")
    st.write("Langkah: Tambahkan **(NH₄)₂CO₃** ke supernatan [3].")
    
    if st.button("Tambahkan (NH₄)₂CO₃ & Sentrifugasi"):
        simulasi_sentrifugasi()
        st.subheader("Hasil Reaksi:")
        st.code("BaCO3, SrCO3, CaCO3 (Semua Putih)")
        
        st.markdown("### 🔦 Uji Identifikasi & Uji Nyala")
        st.write("Berikut adalah hasil uji spesifik dan warna nyala (Simulasi):")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("Barium (Ba²⁺)")
            st.write("Ba²⁺ + CrO₄²⁻ → 🟡 Kuning [3]")
            st.markdown("<div style='background-color: #adff2f; padding:10px; border-radius:5px; text-align:center;'>🔥 Hijau Apel</div>", unsafe_allow_html=True)
        with c2:
            st.subheader("Stronsium (Sr²⁺)")
            st.write("Sr²⁺ + SO₄²⁻ → ⚪ Putih [3]")
            st.markdown("<div style='background-color: #ff0000; color:white; padding:10px; border-radius:5px; text-align:center;'>🔥 Merah Tua</div>", unsafe_allow_html=True)
        with c3:
            st.subheader("Kalsium (Ca²⁺)")
            st.write("Ca²⁺ + C₂O₄²⁻ → ⚪ Putih [3]")
            st.markdown("<div style='background-color: #ff4500; color:white; padding:10px; border-radius:5px; text-align:center;'>🔥 Merah Bata</div>", unsafe_allow_html=True)
