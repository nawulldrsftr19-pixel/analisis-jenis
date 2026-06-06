import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Pro-Lab: Analisis Kualitatif", layout="wide")

# --- CSS KHUSUS (TEMA BIRU, ANIMASI API, & TABUNG BERGERAK) ---
st.markdown("""
    <style>
    .stApp { background-color: #e3f2fd; }
    .main-title { color: #0d47a1; text-align: center; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    
    /* Animasi Api untuk Uji Nyala */
    .flame-container { display: flex; justify-content: center; align-items: flex-end; height: 100px; margin: 10px; }
    .flame {
        width: 40px; height: 40px; border-radius: 50% 0 50% 50%;
        transform: rotate(-45deg);
        animation: flicker 0.5s infinite alternate;
    }
    @keyframes flicker {
        0% { transform: rotate(-45deg) scale(1); opacity: 0.8; }
        100% { transform: rotate(-45deg) scale(1.1); opacity: 1; }
    }
    
    /* Animasi Tabung Sentrifugasi Berputar */
    .centrifuge-spin {
        width: 80px; height: 80px; border: 5px dashed #1565c0;
        border-radius: 50%; animation: spin 1s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* Visualisasi Tabung Reaksi */
    .tube-container { display: flex; flex-direction: column; align-items: center; }
    .tube {
        width: 50px; height: 150px; border: 3px solid #444;
        border-radius: 0 0 25px 25px; position: relative;
        background: rgba(255,255,255,0.3); overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: height 1s; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 22px 22px; transition: height 1s; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI PEMBANTU ---
def render_flame(color):
    st.markdown(f"""
        <div class="flame-container">
            <div class="flame" style="background: {color}; box-shadow: 0 0 20px {color};"></div>
        </div>
    """, unsafe_allow_html=True)

def centrifuge_animation():
    placeholder = st.empty()
    for _ in range(3): # Animasi berputar 3 detik
        placeholder.markdown('<div class="centrifuge-spin"></div>', unsafe_allow_html=True)
        time.sleep(1)
    placeholder.empty()
    st.success("✅ Sentrifugasi Selesai (3000 rpm) [1].")

def show_tube(liq_color, pellet_color=None, pellet_height=0):
    p_html = f'<div class="pellet" style="height:{pellet_height}px; background:{pellet_color};"></div>' if pellet_color else ""
    st.markdown(f"""
        <div class="tube-container">
            <div class="tube">
                <div class="liquid" style="height:70%; background:{liq_color}; opacity:0.6;"></div>
                {p_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- UI UTAMA ---
st.markdown('<h1 class="main-title">🧪 Aplikasi Analisis Kation Pro-Virtual</h1>', unsafe_allow_html=True)

tab_bagan, tab_gol1, tab_gol3, tab_gol4 = st.tabs(["📊 Bagan Alir", "🔹 Golongan I", "🔹 Golongan III", "🔥 Golongan IV"])

# --- TAB 1: BAGAN ALIR (Source 4) ---
with tab_bagan:
    st.header("Bagan Pemisahan Kation (Berdasarkan Gambar)")
    # Pastikan file gambar "bc6fb4ca-a52a-4085-a0ec-982bb89d39e0.jpeg" ada di folder yang sama
    try:
        st.image("bc6fb4ca-a52a-4085-a0ec-982bb89d39e0.jpeg", caption="Bagan Alir Pemisahan Golongan I - V [3]", use_column_width=True)
    except:
        st.warning("⚠️ File gambar bagan tidak ditemukan. Silakan pastikan file 'bc6fb4ca-a52a-4085-a0ec-982bb89d39e0.jpeg' tersedia.")

# --- TAB 2: GOLONGAN I ---
with tab_gol1:
    st.subheader("Identifikasi Ag+, Pb2+, Hg2^2+")
    st.write("Pereaksi: HCl encer [1]")
    if st.button("Tambahkan HCl"):
        show_tube("white")
        centrifuge_animation()
        st.write("**Hasil:** Terbentuk Pellet Putih (AgCl, PbCl2, Hg2Cl2) [1]")
        show_tube("rgba(173,216,230,0.3)", "white", 30)

# --- TAB 3: GOLONGAN III ---
with tab_gol3:
    st.subheader("Identifikasi Fe3+ & Al3+")
    st.write("Pereaksi: NH4OH [2]")
    if st.button("Uji Besi (Fe3+)"):
        st.write("Menambahkan SCN- → 🔴 Larutan Merah Darah [2, 3]")
        show_tube("#b71c1c")

# --- TAB 4: GOLONGAN IV (DENGAN ANIMASI API) ---
with tab_gol4:
    st.subheader("Uji Nyala & Identifikasi Golongan IV")
    st.info("Berdasarkan Source 2: Ba2+, Sr2+, Ca2+ membentuk endapan karbonat putih.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Barium (Ba2+)**")
        st.caption("Hasil: 🟡 Endapan Kuning (CrO4^2-) [2]")
        render_flame("#adff2f") # Hijau Apel
        st.button("Nyala Ba", on_click=None, key="ba")
        
    with col2:
        st.markdown("**Stronsium (Sr2+)**")
        st.caption("Hasil: ⚪ Endapan Putih (SO4^2-) [2]")
        render_flame("#ff0000") # Merah Tua
        st.button("Nyala Sr", on_click=None, key="sr")
        
    with col3:
        st.markdown("**Kalsium (Ca2+)**")
        st.caption("Hasil: ⚪ Endapan Putih (C2O4^2-) [2]")
        render_flame("#ff4500") # Merah Bata
        st.button("Nyala Ca", on_click=None, key="ca")
