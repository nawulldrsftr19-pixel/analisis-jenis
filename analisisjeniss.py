import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sentrifugasi Lab Pro", layout="wide")

# --- CUSTOM CSS (Tema Biru & Animasi Tabung) ---
st.markdown("""
    <style>
    /* Tema Utama Biru */
    .stApp {
        background: linear-gradient(to right, #e3f2fd, #bbdefb);
    }
    .main-title {
        color: #0d47a1;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 20px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Desain Tabung Reaksi Realistis */
    .glass-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .tube {
        width: 70px;
        height: 200px;
        border: 3px solid rgba(255, 255, 255, 0.6);
        border-bottom-left-radius: 35px;
        border-bottom-right-radius: 35px;
        position: relative;
        background: rgba(255, 255, 255, 0.2);
        box-shadow: inset 0 0 15px rgba(255,255,255,0.5), 5px 5px 15px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    .supernatant {
        position: absolute;
        bottom: 0;
        width: 100%;
        transition: all 2s ease-in-out;
    }
    .pellet {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 0px;
        transition: all 2s ease-in-out;
        border-bottom-left-radius: 30px;
        border-bottom-right-radius: 30px;
    }
    
    /* Efek Berkilau Gelas */
    .tube::after {
        content: "";
        position: absolute;
        top: 10px;
        left: 10px;
        width: 10px;
        height: 150px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI KOMPONEN ---
def tampilkan_tabung(warna_cair, tinggi_cair, warna_endapan="#fff", tinggi_endapan=0, cloudy=False):
    opacity = "0.6" if cloudy else "0.9"
    st.markdown(f"""
        <div class="glass-container">
            <div class="tube">
                <div class="supernatant" style="height: {tinggi_cair}%; background-color: {warna_cair}; opacity: {opacity};"></div>
                <div class="pellet" style="height: {tinggi_endapan}px; background-color: {warna_endapan};"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def proses_sentrifugasi(warna_awal, warna_akhir, warna_pellet):
    placeholder = st.empty()
    with placeholder.container():
        st.write("🔄 **Sentrifugasi 3000 rpm Sedang Berlangsung...**")
        tampilkan_tabung(warna_awal, 80, cloudy=True)
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
    
    placeholder.empty()
    st.success("✅ Pemisahan Selesai! Supernatan (atas) dan Pellet (bawah) telah terpisah.")
    tampilkan_tabung(warna_akhir, 70, warna_endapan=warna_pellet, tinggi_endapan=30)

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Virtual Lab: Analisis Kation Pro</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔹 Golongan I", "🔹 Golongan III", "🔹 Golongan IV"])

# --- GOLONGAN I ---
with tab1:
    st.subheader("Pemisahan Ag+, Pb2+, Hg2^2+")
    st.info("Prinsip: Penambahan HCl membentuk endapan klorida putih [1].")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Tambahkan HCl & Putar"):
            proses_sentrifugasi("rgba(255,255,255,0.8)", "rgba(200,230,255,0.4)", "#ffffff")
    with col2:
        st.write("**Hasil Identifikasi:**")
        reaksi = st.selectbox("Pilih Uji Spesifik:", ["-", "Uji Timbal (K2CrO4)", "Uji Merkuri (NH4OH)"])
        if reaksi == "Uji Timbal (K2CrO4)":
            st.warning("Hasil: Pb2+ + K2CrO4 → 🟡 Endapan Kuning [1]")
            tampilkan_tabung("yellow", 80, warna_endapan="#ffd700", tinggi_endapan=40)
        elif reaksi == "Uji Merkuri (NH4OH)":
            st.error("Hasil: Hg2Cl2 + NH4OH → ⚫ Endapan Hitam [1]")
            tampilkan_tabung("#333", 80, warna_endapan="#000", tinggi_endapan=40)

# --- GOLONGAN III ---
with tab2:
    st.subheader("Pemisahan Fe3+ & Al3+")
    st.info("Prinsip: Penambahan NH4OH membentuk endapan hidroksida [2].")
    
    if st.button("Tambahkan NH4OH"):
        proses_sentrifugasi("rgba(165, 42, 42, 0.6)", "rgba(255,255,255,0.2)", "#8B4513")
        st.write("**Analisis Lanjutan:**")
        st.markdown("- **Fe3+ + SCN-**: Larutan berubah menjadi 🔴 **Merah Darah** [2].")
        tampilkan_tabung("rgba(139, 0, 0, 0.9)", 85)

# --- GOLONGAN IV ---
with tab3:
    st.subheader("Pemisahan Ba2+, Sr2+, Ca2+")
    st.info("Prinsip: Penambahan (NH4)2CO3 menghasilkan endapan putih [2].")
    
    if st.button("Jalankan Uji Golongan IV"):
        proses_sentrifugasi("rgba(255,255,255,0.7)", "rgba(240,248,255,0.5)", "#ffffff")
        
    st.divider()
    st.write("**🔥 Simulasi Uji Nyala & Reaksi Warna:**")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("Barium (Ba2+)")
        st.write("🟡 Endapan Kuning (Kromat) [2]")
        st.markdown("<div style='background: #adff2f; height: 20px; border-radius: 5px;'></div>", unsafe_allow_html=True)
    with c2:
        st.write("Stronsium (Sr2+)")
        st.write("⚪ Endapan Putih (Sulfat) [2]")
        st.markdown("<div style='background: #ff0000; height: 20px; border-radius: 5px;'></div>", unsafe_allow_html=True)
    with c3:
        st.write("Kalsium (Ca2+)")
        st.write("⚪ Endapan Putih (Oksalat) [2]")
        st.markdown("<div style='background: #ff4500; height: 20px; border-radius: 5px;'></div>", unsafe_allow_html=True)

# --- FOOTER ---
st.sidebar.markdown("""
### 📘 Panduan Teknis
1. **Keseimbangan**: Pastikan tabung seimbang sebelum memutar [3].
2. **Kecepatan**: Aplikasi ini mensimulasikan putaran **3000 rpm** [1].
3. **Pemisahan**: Ambil supernatan perlahan tanpa mengganggu pellet di dasar tabung [3].
""")
Keunggulan Pembaruan Ini:
Visualisasi Tabung Lebih Nyata: Menggunakan CSS box-shadow dan linear-gradient untuk menciptakan efek tabung kaca tiga dimensi yang transparan.
Perbedaan Larutan & Endapan:
Supernatan: Direpresentasikan sebagai lapisan atas yang jernih (rgba transparan).
Pellet: Direpresentasikan sebagai lapisan padat di bagian paling bawah tabung dengan warna yang sesuai dengan reaksi kimia (misalnya hitam untuk merkuri atau kuning untuk timbal).
Animasi Transisi: Saat tombol ditekan, aplikasi akan menunjukkan kondisi "Cloudy" (keruh/bercampur) terlebih dahulu sebelum perlahan-lahan berubah menjadi jernih dengan endapan di bawah setelah proses sentrifugasi selesai.
Tema Biru yang Menarik: Menggunakan palet warna biru muda hingga biru tua untuk memberikan kesan profesional laboratorium modern.
Interaktivitas: Menggunakan tabs dan selectbox agar pengguna bisa fokus pada satu golongan kation pada satu waktu, sesuai dengan prosedur bertahap dalam sumber.
Anda dapat menjalankan kode ini dengan perintah streamlit run nama_file.py untuk melihat animasinya secara langsung.
