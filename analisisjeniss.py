import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kation Explorer Pro", layout="wide")

# --- GAYA VISUAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #e3f2fd; }
    .main-header {
        background: #1565c0;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 10px solid #1565c0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .tube-container { display: flex; justify-content: center; padding: 20px; }
    .tube {
        width: 65px; height: 180px;
        border: 3px solid #444;
        border-radius: 0 0 35px 35px;
        position: relative;
        background: rgba(255,255,255,0.4);
        overflow: hidden;
    }
    .liquid { position: absolute; bottom: 0; width: 100%; transition: all 1s ease; }
    .pellet { position: absolute; bottom: 0; width: 100%; border-radius: 0 0 30px 30px; transition: all 1s ease; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA (Berdasarkan Sumber) ---
DATA_KATION = {
    "Ag+": {"reagen": "HCl & NH4OH", "hasil": "Endapan Putih larut dalam NH4OH", "warna": "white"},
    "Pb2+": {"reagen": "K2CrO4", "hasil": "Endapan Kuning", "warna": "#ffeb3b"},
    "Hg2^2+": {"reagen": "NH4OH", "hasil": "Endapan Hitam", "warna": "#212121"},
    "Fe3+": {"reagen": "SCN-", "hasil": "Larutan Merah Darah", "warna": "#b71c1c"},
    "Ba2+": {"reagen": "CrO4^2-", "hasil": "Endapan Kuning", "warna": "#fdd835"},
    "Sr2+": {"reagen": "SO4^2-", "hasil": "Endapan Putih", "warna": "white"},
    "Ca2+": {"reagen": "C2O4^2-", "hasil": "Endapan Putih", "warna": "white"}
}

# --- KOMPONEN ---
def render_tube(warna_cair, tinggi_cair=75, warna_pellet=None, tinggi_pellet=0):
    pellet_html = f'<div class="pellet" style="height:{tinggi_pellet}px; background:{warna_pellet};"></div>' if warna_pellet else ""
    st.markdown(f"""
        <div class="tube-container">
            <div class="tube">
                <div class="liquid" style="height:{tinggi_cair}%; background:{warna_cair}; opacity:0.8;"></div>
                {pellet_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

def animasi_sentrifugasi():
    with st.spinner("🌀 Proses Sentrifugasi (3000 rpm)..."):
        p = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            p.progress(i + 1)
    st.success("✅ Pemisahan Selesai! Supernatan dan Pellet terpisah.")

# --- UI ---
st.markdown('<div class="main-header"><h1>🧪 Tool Analisis Kation Interaktif</h1></div>', unsafe_allow_html=True)

# Perbaikan: st.columns memerlukan angka (2)
mode = st.radio("Pilih Mode Eksplorasi:", ["🔍 Berdasarkan Kation", "🧪 Berdasarkan Pereaksi"], horizontal=True)
col_input, col_visual = st.columns(2)

if mode == "🔍 Berdasarkan Kation":
    with col_input:
        kation = st.selectbox("Pilih Kation:", list(DATA_KATION.keys()))
        info = DATA_KATION[kation]
        st.markdown(f"""<div class="card"><h3>Kation: {kation}</h3><p><b>Pereaksi:</b> {info['reagen']}</p><p><b>Hasil:</b> {info['hasil']}</p></div>""", unsafe_allow_html=True)
        btn = st.button("Jalankan Uji")
    
    with col_visual:
        if btn:
            render_tube(info['warna'], tinggi_cair=80)
            animasi_sentrifugasi()
            # Visualisasi Pellet & Supernatan (Sumber [1])
            render_tube("rgba(200,230,255,0.4)", tinggi_cair=60, warna_pellet=info['warna'], tinggi_pellet=40)

else:
    with col_input:
        reagen = st.selectbox("Pilih Pereaksi:", ["HCl", "NH4OH", "K2CrO4", "SCN-", "(NH4)2CO3"])
        st.info(f"Pereaksi {reagen} digunakan untuk memisahkan golongan kation tertentu.")
        btn_reagen = st.button("Lihat Reaksi")

    with col_visual:
        if btn_reagen:
            # Contoh reaksi spesifik berdasarkan sumber [1, 2]
            if reagen == "HCl":
                st.write("Membentuk endapan putih (AgCl, PbCl2, Hg2Cl2)")
                render_tube("white", warna_pellet="white", tinggi_pellet=30)
            elif reagen == "SCN-":
                st.write("Membentuk warna Merah Darah (Fe3+)")
                render_tube("#b71c1c")
            elif reagen == "K2CrO4":
                st.write("Membentuk endapan kuning (Pb2+ atau Ba2+)")
                render_tube("yellow", warna_pellet="yellow", tinggi_pellet=30)

st.sidebar.warning("⚠️ Pastikan tabung seimbang saat sentrifugasi! (Sumber [3])")
