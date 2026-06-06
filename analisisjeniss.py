import streamlit as st
import time

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LabKim — Analisis Kualitatif Kation",
    page_icon="⚗️",
    layout="wide",  # Tetap wide agar layouting kolom fleksibel
    initial_sidebar_state="collapsed",
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
css_code = """
<style>
@import url('https://googleapis.com');
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Space Mono', monospace;
    background-color: #0a1628;
    color: #e2e8f0;
}
[data-testid="stHeader"] {
    background: transparent;
}
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}
/* Memastikan seluruh teks di container tengah ikut center-aligned jika dibutuhkan */
.center-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
}
.lab-card {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
    text-align: left; /* Teks deskripsi tetap nyaman dibaca rata kiri */
}
.rxn-card {
    background: #1a2235;
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    transition: border-color .25s;
}
.rxn-card:hover {
    border-color: #7c3aed;
}
.equation-box {
    background: #0a0e1a;
    border: 1px solid #1e3a5f;
    border-radius: 8px;
    padding: 10px 14px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #c4b5fd;
}
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #00d4ff;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 4px;
    text-align: center; /* Set label ke tengah */
}
.hero-title {
    font-family: 'Syncopate', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #fff 0%, #00d4ff 50%, #7c3aed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
    margin-bottom: 6px;
    text-align: center; /* Judul di tengah */
}
.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #64748b;
    margin-bottom: 20px;
    text-align: center; /* Sub-judul di tengah */
}
.obs-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 12px;
    background: #0a0e1a;
    border: 1px solid #1e3a5f;
    border-radius: 8px;
    font-size: 12px;
    margin: 4px;
}
.log-box {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 14px 16px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    max-height: 220px;
    overflow-y: auto;
    color: #64748b;
    line-height: 1.9;
    text-align: left; /* Log tetap rata kiri agar mudah dibaca */
}
.log-react { color: #a78bfa; }
.log-result { color: #10b981; font-weight: 700; }
.log-time { color: #00d4ff; }
.tube-wrap {
    display: flex;
    gap: 18px;
    justify-content: center; /* Tabung otomatis di tengah */
    flex-wrap: wrap;
    margin: 16px 0;
}
.tube-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
}
.tube-lbl {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: #64748b;
    text-align: center;
    max-width: 80px;
}
.tube-svg { filter: drop-shadow(0 6px rgba(0,212,255,0.2)); }
.progress-bar-bg {
    height: 4px;
    background: #1e3a5f;
    border-radius: 20px;
    margin-bottom: 20px;
    overflow: hidden;
}
.progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #7c3aed, #00d4ff);
    border-radius: 2px;
}
.ref-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #94a3b8;
    margin-top: 15px;
}
.ref-table th {
    padding: 8px 10px;
    text-align: left;
    color: #64748b;
    border-bottom: 1px solid #1e3a5f;
}
.ref-table td {
    padding: 8px 10px;
    border-bottom: 1px solid rgba(30, 58, 95, 0.5);
}
.badge-white { background: rgba(255,255,255,0.1); color: #fff; border: 1px solid #334155; border-radius: 20px; padding: 3px 10px; }
.badge-yellow { background: rgba(245,158,11,0.15); color: #f59e0b; border-radius: 20px; padding: 3px 10px; }
.badge-red { background: rgba(239,68,68,0.15); color: #ef4444; border-radius: 20px; padding: 3px 10px; }

/* CSS Pembakar Bunsen Uji Nyala */
.bunsen-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background: #090f1d;
    border-radius: 12px;
    border: 1px solid #1e3a5f;
    max-width: 320px;
    margin: 0 auto; /* Bunsen otomatis di tengah container */
}
.flame {
    width: 35px;
    height: 90px;
    background: linear-gradient(to bottom, transparent, #00d4ff);
    border-radius: 50% 50% 20% 20% / 70% 70% 30% 30%;
    animation: flicker 0.15s infinite alternate;
    filter: blur(1px) drop-shadow(0px -5px 15px currentColor);
}
@keyframes flicker {
    0% { transform: scaleX(0.95) scaleY(0.95); }
    100% { transform: scaleX(1.05) scaleY(1.05); }
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# ─── DATA SIMULASI UTAMA ──────────────────────────────────────────────────────
sim_data_list = [
    {
        "id": "g0",
        "name": "Persiapan Sampel Awal",
        "reagent": "Campuran Kation",
        "base_pellet": 0,
        "desc": "Larutan awal mengandung campuran kation golongan I, III, dan IV sebelum separasi berurutan dilakukan.",
        "tubes": [{"label": "Sampel", "color": "#334155", "liquid_pct": 60}],
        "obs": [{"color": "#64748b", "text": "Larutan awal keruh homogen"}],
        "log": [("msg", "Sampel baru dimuat ke sistem."), ("msg", "Kation terdeteksi: Ag+, Pb2+, Hg22+, Fe3+, Al3+, Ba2+, Ca2+")]
    },
    {
        "id": "g1",
        "name": "Langkah 1 — Pengendapan Golongan I",
        "reagent": "HCl 6M",
        "base_pellet": 16,
        "desc": "Penambahan klorida encer memaksa kation Golongan I mengendap sebagai padatan garam klorida putih.",
        "tubes": [
            {"label": "Supernatan", "color": "#1e40af", "liquid_pct": 50},
            {"label": "Pellet G-I", "color": "#e2e8f0", "liquid_pct": 20}
        ],
        "obs": [{"color": "#e2e8f0", "text": "Endapan putih klorida terbentuk (AgCl, PbCl₂, Hg₂Cl₂)"}],
        "log": [
            ("react", "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓ [Ksp = 1.8×10⁻¹⁰]"),
            ("react", "Pb²⁺(aq) + 2Cl⁻(aq) → PbCl₂(s)↓ [Ksp = 1.6×10⁻⁵]"),
            ("result", "Sentrifugasi memisahkan pelet klorida dari filtrat kation atas.")
        ]
    },
    {
        "id": "g3",
        "name": "Langkah 2 — Pengendapan Golongan III",
        "reagent": "NH₄OH 6M",
        "base_pellet": 22,
        "desc": "Cairan sisa filtrat Langkah 1 diakumulasikan lalu direaksikan dengan amonia untuk mengikat gugus hidroksida.",
        "tubes": [
            {"label": "Supernatan", "color": "#0284c7", "liquid_pct": 45},
            {"label": "Pellet G-III", "color": "#b45309", "liquid_pct": 15}
        ],
        "obs": [{"color": "#b45309", "text": "Endapan cokelat kemerahan Fe(OH)₃ & putih gelatin Al(OH)₃"}],
        "log": [
            ("react", "Fe³⁺(aq) + 3OH⁻(aq) → Fe(OH)₃(s)↓ [Ksp = 4×10⁻³⁸]"),
            ("result", "Filtrat jernih dipisahkan kembali menuju cawan pengujian logam alkali tanah.")
        ]
    },
    {
        "id": "g4",
        "name": "Langkah 3 — Pengendapan Golongan IV",
        "reagent": "(NH₄)₂CO₃",
        "base_pellet": 14,
        "desc": "Karbonasi sisa larutan mengisolasi ion kalsium dan barium menjadi endapan karbonat.",
        "tubes": [
            {"label": "Supernatan", "color": "#0ea5e9", "liquid_pct": 40},
            {"label": "Pellet G-IV", "color": "#ffffff", "liquid_pct": 10}
        ],
        "obs": [{"color": "#ffffff", "text": "Endapan karbonat putih masif (BaCO₃ & CaCO₃)"}],
        "log": [
            ("react", "Ba²⁺(aq) + CO₃²⁻(aq) → BaCO₃(s)↓"),
            ("react", "Ca²⁺(aq) + CO₃²⁻(aq) → CaCO₃(s)↓"),
            ("result", "Pemisahan fisis basah selesai, pelet siap dilakukan destruksi kawat nikrom.")
        ]
    }
]

# ─── RENDERING TABUNG DYNAMIC PELLET ──────────────────────────────────────────
def render_tube_svg(label, liquid_color, liquid_pct, pellet_pct):
    liquid_height = (liquid_pct / 100) * 80
    pellet_height = (pellet_pct / 100) * 80
    
    liquid_y = 90 - liquid_height - pellet_height
    pellet_y = 90 - pellet_height
    
    return f"""
    <div class="tube-col">
        <svg class="tube-svg" width="60" height="130" viewBox="0 0 60 130">
            {f'<rect x="16" y="{liquid_y}" width="28" height="{liquid_height}" fill="{liquid_color}" opacity="0.75"/>' if liquid_pct > 0 else ''}
            {f'<path d="M 16 {pellet_y} L 44 {pellet_y} L 44 85 C 44 95, 16 95, 16 85 Z" fill="{liquid_color}" filter="brightness(0.5) contrast(1.5)"/>' if pellet_pct > 0 else ''}
            <path d="M 16 15 L 16 85 C 16 100, 44 100, 44 85 L 44 15" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
            <ellipse cx="30" cy="15" rx="16" ry="4" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
        </svg>
        <div class="tube-lbl">{label}</div>
    </div>
    """

# ─── HEADER UTAMA ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Laboratorium Virtual Interaktif v2.0</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">ANALISIS KATION & UJI NYALA</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Simulasi Sentrifugasi Dinamis & Eksitasi Spektroskopi Visual</div>', unsafe_allow_html=True)

# Pembuatan Struktur Menu Tab
tab_sim, tab_flame = st.tabs(["🧪 SENTRIFUGASI DINAMIS", "🔥 UJI NYALA (GOLONGAN IV)"])

# 📌 TAB 1: SENTRIFUGASI UTAMA (Dibuat Berada di Tengah)
with tab_sim:
    # Menggunakan trik 3 kolom [kolom_kosong, isi_konten, kolom_kosong] agar posisi konten di tengah
    col_left, col_center, col_right = st.columns([0.5, 2, 0.5])
    
    with col_center:
        st.markdown('<div class="section-label">PILIH TAHAPAN UTAMA</div>', unsafe_allow_html=True)
        step_names = [d["name"] for d in sim_data_list]
        selected_step = st.radio("Pilih Tahap:", step_names, label_visibility="collapsed")
        
        step_data = next(d for d in sim_data_list if d["name"] == selected_step)
        st.markdown(f'<p style="font-size:13px; text-align:center;">{step_data["desc"]}</p>', unsafe_allow_html=True)
        
        # Kontrol Slider Sentrifugasi
        st.markdown('<div class="section-label" style="margin-top:15px;">KONFIGURASI SENTRIFUGAL</div>', unsafe_allow_html=True)
        input_rpm = st.slider("Kecepatan Putaran (RPM):", min_value=0, max_value=6000, value=3000, step=500)
        input_time = st.slider("Durasi Waktu (Detik):", min_value=0, max_value=180, value=90, step=30)
        
        # Kalkulasi Efisiensi Pelet
        if input_rpm == 0 or input_time == 0:
            calc_pellet_pct = 0
            compactness_msg = "Reagen tercampur, koloid partikel masih melayang bebas di dalam fasa air."
        else:
            efficiency = min((input_rpm / 4000) * (input_time / 120), 1.2)
            calc_pellet_pct = int(step_data["base_pellet"] * efficiency)
            if efficiency < 0.6:
                compactness_msg = "⚠️ Pelet longgar & keruh: Gaya sentrifugal tidak mencukupi."
            elif efficiency <= 1.0:
                compactness_msg = "✅ Pelet terbentuk normal dan terkompaksi jernih."
            else:
                compactness_msg = "⚡ Pelet super-kompak terbentuk akibat G-Force tinggi."
                
        run_centrifuge = st.button("MULAI SENTRIFUGASI ⚡", use_container_width=True, disabled=(input_rpm == 0))
        if run_centrifuge:
            progress_bar = st.empty()
            for i in range(1, 101):
                progress_bar.markdown(f'<div class="progress-bar-bg"><div class="progress-bar-fill" style="width: {i}%"></div></div>', unsafe_allow_html=True)
                time.sleep(0.005)
            progress_bar.empty()
            st.success(compactness_msg)
            
        st.write("---")
        
        # Tampilan Hasil Profil Pemisahan (Tabung SVG)
        st.markdown('<div class="section-label">PROFIL PEMISAHAN FISIS</div>', unsafe_allow_html=True)
        tubes_html = ""
        for t in step_data["tubes"]:
            p_pct = calc_pellet_pct if "Pellet" in t["label"] else 0
            tubes_html += render_tube_svg(t["label"], t["color"], t["liquid_pct"], p_pct)
            
        st.markdown(f'<div class="tube-wrap">{tubes_html}</div>', unsafe_allow_html=True)
        
        # Informasi Observasi Fisik
        obs_html = '<div style="text-align: center; margin-bottom: 15px;">'
        for obs in step_data["obs"]:
            obs_html += f'<span class="obs-pill" style="border-color:{obs["color"]}"><span style="color:{obs["color"]};">●</span> {obs["text"]} (Tinggi Pelet: {calc_pellet_pct}%)</span>'
        obs_html += '</div>'
        st.markdown(obs_html, unsafe_allow_html=True)
        
        # Log Box Buku Catatan Laboratorium
        st.markdown('<div class="section-label">LOG REAKSI</div>', unsafe_allow_html=True)
        log_html = '<div class="log-box">'
        for ltype, msg in step_data["log"]:
            tag = '<span class="log-react">Rxn:</span>' if ltype == "react" else '<span>Info:</span>'
            log_html += f'<div><span class="log-time">[{time.strftime("%H:%M:%S")}]</span> {tag} {msg}</div>'
        log_html += '</div>'
        st.markdown(log_html, unsafe_allow_html=True)

# 📌 TAB 2: INTERAKTIF UJI NYALA (Dibuat Berada di Tengah)
with tab_flame:
    col_fl_left, col_fl_center, col_fl_right = st.columns([0.5, 2, 0.5])
    
    with col_fl_center:
        st.markdown('<div class="section-label">UJI NYALA (FLAME TEST) LOGAM ALKALI TANAH</div>', unsafe_allow_html=True)
        st.write("<p style='text-align: center;'>Identifikasi kation Golongan IV dilakukan dengan melarutkan sebagian pelet karbonat dalam sedikit HCl pekat, mencelupkan kawat nikrom, dan membakarnya langsung pada zona panas Bunsen.</p>", unsafe_allow_html=True)
        
        kation_selected = st.selectbox(
            "Pilih Kation Golongan IV untuk Diteliti:",
            ["Belum Memilih Kation", "Barium (Ba²⁺)", "Kalsium (Ca²⁺)", "Stronsium (Sr²⁺)"]
        )
        
        if kation_selected == "Barium (Ba²⁺)":
            flame_color = "#98fb98"  
            flame_style = "color: #98fb98;"
            desc_flame = "Kation **Ba²⁺** memancarkan radiasi emisi foton dengan panjang gelombang dominan di spektrum hijau, memberikan tampilan visual **Hijau Apel** yang khas."
        elif kation_selected == "Kalsium (Ca²⁺)":
            flame_color = "#ff4500"  
            flame_style = "color: #ff4500;"
            desc_flame = "Kation **Ca²⁺** menghasilkan emisi termal dengan pendaran warna **Merah Bata (Jingga Kemerahan Tua)** saat elektron kembali ke kondisi ground state."
        elif kation_selected == "Stronsium (Sr²⁺)":
            flame_color = "#e60026"  
            flame_style = "color: #e60026;"
            desc_flame = "Kation **Sr²⁺** melepaskan energi eksitasi eksklusif pada rentang panjang gelombang merah pekat, menghasilkan warna **Merah Karmin** yang tajam."
        else:
            flame_color = "#00d4ff"  
            flame_style = "color: #00d4ff;"
            desc_flame = "Silakan pilih salah satu kation di atas untuk memulai simulasi pembakaran sampel kawat nikrom pada nyala api oksidasi Bunsen."
            
        st.markdown(f'<div class="lab-card" style="margin-top:15px;">{desc_flame}</div>', unsafe_allow_html=True)
        
        # Tampilan Animasi Interaktif Bunsen di Tengah
        st.markdown(f"""
        <div class="bunsen-container">
            <div style="font-family:'Space Mono'; font-size:10px; color:#64748b; margin-bottom:15px; text-transform:uppercase;">Zona Oksidasi Bunsen</div>
            <div class="flame" style="{flame_style}"></div>
            <div style="width:25px; height:60px; background:#475569; margin-top:5px; border-radius:3px 3px 0 0;"></div>
            <div style="width:50px; height:10px; background:#334155; border-radius:2px;"></div>
            <div style="font-size:11px; margin-top:12px; font-weight:bold; color:{flame_color}; font-family:'Space Mono';">
                Spektrum Warna: {kation_selected}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─── TABEL DATA REFERENSI TEKNIS ──────────────────────────────────────────────
st.markdown('<div class="section-label" style="margin-top:30px;">KONSTANTA KELARUTAN & KARAKTERISTIK GOLONGAN IV</div>', unsafe_allow_html=True)
st.markdown("""
<table class="ref-table">
    <thead>
        <tr>
            <th>Kation</th>
            <th>Bentuk Reaksi Karbonat</th>
            <th>Warna Nyala Emisi</th>
            <th>Panjang Gelombang Dominan</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Barium (Ba²⁺)</td>
            <td>Ba²⁺ + CO₃²⁻ → BaCO₃↓ (Putih)</td>
            <td style="color:#98fb98; font-weight:bold;">Hijau Apel</td>
            <td>~553 nm</td>
        </tr>
        <tr>
            <td>Kalsium (Ca²⁺)</td>
            <td>Ca²⁺ + CO₃²⁻ → CaCO₃↓ (Putih)</td>
            <td style="color:#ff4500; font-weight:bold;">Merah Bata</td>
            <td>~622 nm</td>
        </tr>
        <tr>
            <td>Stronsium (Sr²⁺)</td>
            <td>Stronsium (Sr²⁺) + CO₃²⁻ → SrCO₃↓ (Putih)</td>
            <td style="color:#e60026; font-weight:bold;">Merah Karmin</td>
            <td>~650 nm</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)
