import streamlit as st
import time

# --- KONFIGURASI & TEMA ---
st.set_page_config(page_title="Kation Explorer Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #e3f2fd; }
    .main-header {
        background: #0d47a1;
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #1976d2;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    /* Animasi Tabung Reaksi */
    .tube-container { display: flex; justify-content: center; padding: 20px; }
    .tube {
        width: 60px; height: 180px;
        border: 3px solid #555;
        border-radius: 0 0 30px 30px;
        position: relative;
        background: rgba(255,255,255,0.3);
        overflow: hidden;
    }
    .liquid {
        position: absolute; bottom: 0; width: 100%;
        transition: all 1s ease;
    }
    .pellet {
        position: absolute; bottom: 0; width: 100%;
        border-radius: 0 0 25px 25px;
        transition: all 1s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA REAKSI (Berdasarkan Sumber) ---
DATA_KATION = {
    "Ag+": {"reagen": "HCl", "hasil": "Endapan Putih AgCl", "warna": "white", "ket": "Larut dalam NH4OH [1]"},
    "Pb2+": {"reagen": "K2CrO4", "hasil": "Endapan Kuning", "warna": "#ffeb3b", "ket": "Membentuk PbCl2 putih dengan HCl [1]"},
    "Hg2^2+": {"reagen": "NH4OH", "hasil": "Endapan Hitam", "warna": "#212121", "ket": "Awalnya Hg2Cl2 putih [1]"},
    "Fe3+": {"reagen": "SCN-", "hasil": "Larutan Merah Darah", "warna": "#b71c1c", "ket": "Membentuk Fe(OH)3 coklat dengan NH4OH [2]"},
    "Al3+": {"reagen": "NaOH/HCl", "hasil": "Endapan Putih Gelatin", "warna": "#f5f5f5", "ket": "Larut dalam NaOH berlebih [2]"},
    "Ba2+": {"reagen": "CrO4^2-", "hasil": "Endapan Kuning", "warna": "#fdd835", "ket": "Grup IV [2]"},
    "Sr2+": {"reagen": "SO4^2-", "hasil": "Endapan Putih", "warna": "white", "ket": "Grup IV [2]"},
    "Ca2+": {"reagen": "C2O4^2-", "hasil": "Endapan Putih", "warna": "white", "ket": "Grup IV [2]"}
}

# --- KOMPONEN VISUAL ---
def render_tube(warna_cair, tinggi_cair=70, warna_pellet=None, tinggi_pellet=0):
    pellet_html = f'<div class="pellet" style="height:{tinggi_pellet}px; background:{warna_pellet};"></div>' if warna_pellet else ""
    st.markdown(f"""
        <div class="tube-container">
            <div class="tube">
                <div class="liquid" style="height:{tinggi_cair}%; background:{warna_cair}; opacity:0.8;"></div>
                {pellet_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

def simulasi_sentrifugasi():
    with st.spinner("🌀 Memutar pada 3000 rpm..."):
        p = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            p.progress(i + 1)
    st.success("✅ Sentrifugasi Selesai! Pellet dan Supernatan terpisah [1].")

# --- UI UTAMA ---
st.markdown('<div class="main-header"><h1>🧪 Tool Analisis Kation Interaktif</h1></div>', unsafe_allow_html=True)

mode = st.radio("Pilih Mode Eksplorasi:", ["🔍 Berdasarkan Kation", "🧪 Berdasarkan Pereaksi"], horizontal=True)

col_input, col_visual = st.columns([1])

if mode == "🔍 Berdasarkan Kation":
    with col_input:
        kation = st.selectbox("Pilih Kation yang ingin diuji:", list(DATA_KATION.keys()))
        info = DATA_KATION[kation]
        st.markdown(f"""
            <div class="card">
                <h3>Kation: {kation}</h3>
                <p><b>Pereaksi Utama:</b> {info['reagen']}</p>
                <p><b>Hasil Reaksi:</b> {info['hasil']}</p>
                <p><i>Catatan: {info['ket']}</i></p>
            </div>
        """, unsafe_allow_html=True)
        btn = st.button(f"Uji {kation}")

    with col_visual:
        if btn:
            st.write("### Proses Laboratorium")
            st.write("1. Mencampur Larutan...")
            render_tube(info['warna'], tinggi_cair=80)
            simulasi_sentrifugasi()
            st.write("2. Hasil Akhir (Supernatan jernih di atas, Pellet di bawah) [1, 2]:")
            render_tube("rgba(200,230,255,0.3)", tinggi_cair=60, warna_pellet=info['warna'], tinggi_pellet=40)

else:
    with col_input:
        reagen = st.selectbox("Pilih Pereaksi (Reagent):", 
                             ["HCl", "NH4OH", "K2CrO4", "SCN-", "(NH4)2CO3"])
        
        # Logika filter berdasarkan pereaksi dari sumber
        targets = []
        if reagen == "HCl": targets = ["Ag+", "Pb2+", "Hg2^2+"]
        elif reagen == "NH4OH": targets = ["Fe3+", "Al3+", "Hg2^2+"]
        elif reagen == "K2CrO4": targets = ["Pb2+", "Ba2+"]
        elif reagen == "SCN-": targets = ["Fe3+"]
        elif reagen == "(NH4)2CO3": targets = ["Ba2+", "Sr2+", "Ca2+"]

        st.markdown(f"""
            <div class="card" style="border-left-color: #4caf50;">
                <h3>Pereaksi: {reagen}</h3>
                <p>Digunakan untuk mengidentifikasi kation: <b>{', '.join(targets)}</b></p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_visual:
        if targets:
            st.info(f"Pereaksi {reagen} akan menghasilkan perubahan visual pada kation tersebut [1, 2].")
            render_tube("#bbdefb", tinggi_cair=50)
            st.caption("Ilustrasi tabung siap reaksi")


