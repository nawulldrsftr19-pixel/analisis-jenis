import streamlit as st
import time

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LabKim — Analisis Kualitatif Kation",
    page_icon="⚗️",
    layout="wide",
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
.lab-card {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #00d4ff;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 4px;
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
}
.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #64748b;
    margin-bottom: 20px;
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
    margin: 4px 4px 4px 0;
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
}
.log-react { color: #a78bfa; }
.log-result { color: #10b981; font-weight: 700; }
.log-time { color: #00d4ff; }
.tube-wrap {
    display: flex;
    gap: 18px;
    justify-content: center;
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
[data-testid="stTabs"] button {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 1px;
    color: #64748b !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #00d4ff !important;
    border-bottom-color: #00d4ff !important;
}
/* CSS Pembakar Bunsen Uji Nyala */
.bunsen-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background: #090f1d;
    border-radius: 12px;
    border: 1px solid #1e3a5f;
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
        "desc": "Larutan awal mengandung kation golongan I, III, dan IV sebelum separasi.",
        "tubes": [{"label": "Sampel", "color": "#334155", "liquid_pct": 60}],
        "obs": [{"color": "#64748b", "text": "Larutan awal keruh homogen"}],
        "log": [("msg", "Sampel siap dianalisis."), ("msg", "Kation: Ag+, Pb2+, Fe3+, Ba2+, Ca2+")]
    },
    {
        "id": "g1",
        "name": "Langkah 1 — Golongan I",
        "reagent": "HCl 6M",
        "base_pellet": 16,
        "desc": "Penambahan HCl mengendapkan kation klorida tidak larut (Golongan I).",
        "tubes": [
            {"label": "Supernatan", "color": "#1e40af", "liquid_pct": 50},
            {"label": "Pellet G-I", "color": "#e2e8f0", "liquid_pct": 20}
        ],
        "obs": [{"color": "#e2e8f0", "text": "Endapan putih klorida terbentuk"}],
        "log": [
            ("react", "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓"),
            ("react", "Pb²⁺(aq) + 2Cl⁻(aq) → PbCl₂(s)↓"),
            ("result", "Sentrifugasi memisahkan Golongan I dari filtrat sisa.")
        ]
    },
    {
        "id": "g3",
        "name": "Langkah 2 — Golongan III",
        "reagent": "NH₄OH 6M",
        "base_pellet": 22,
        "desc": "Supernatan ditambah buffer basa amonia mengendapkan hidroksida (Golongan III).",
        "tubes": [
            {"label": "Supernatan", "color": "#0284c7", "liquid_pct": 45},
            {"label": "Pellet G-III", "color": "#b45309", "liquid_pct": 15}
        ],
        "obs": [{"color": "#b45309", "text": "Endapan cokelat kemerahan Fe(OH)₃"}],
        "log": [
            ("react", "Fe³⁺(aq) + 3OH⁻(aq) → Fe(OH)₃(s)↓"),
            ("result", "Filtrat dipisahkan untuk pengujian logam alkali tanah.")
        ]
    },
    {
        "id": "g4",
        "name": "Langkah 3 — Golongan IV",
        "reagent": "(NH₄)₂CO₃",
        "base_pellet": 14,
        "desc": "Karbonasi supernatan terakhir mengisolasi endapan kalsium dan barium.",
        "tubes": [
            {"label": "Supernatan", "color": "#0ea5e9", "liquid_pct": 40},
            {"label": "Pellet G-IV", "color": "#ffffff", "liquid_pct": 10}
        ],
        "obs": [{"color": "#ffffff", "text": "Endapan karbonat putih masif"}],
        "log": [
            ("react", "Ba²⁺(aq) + CO₃²⁻(aq) → BaCO₃(s)↓"),
            ("react", "Ca²⁺(aq) + CO₃²⁻(aq) → CaCO₃(s)↓"),
            ("result", "Pellet putih siap dilarutkan kembali untuk uji nyala.")
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

# ─── HEADER ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Laboratorium Virtual Interaktif v2.0</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">ANALISIS KATION & UJI NYALA</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Simulasi Sentrifugasi Dinamis & Eksitasi Spektroskopi Visual</div>', unsafe_allow_html=True)

tab_sim, tab_flame = st.tabs(["🧪 SENTRIFUGASI DINAMIS", "🔥 UJI NYALA (GOLONGAN IV)"])

# 📌 TAB 1: SENTRIFUGASI DENGAN RPM DAN DURASI MEMENGARUHI ENDAPAN
with tab_sim:
    col_ctrl, col_view = st.columns([1, 1.2])
    
    with col_ctrl:
        st.markdown('<div class="section-label">PILIH TAHAPAN UTAMA</div>', unsafe_allow_html=True)
        step_names = [d["name"] for d in sim_data_list]
        selected_step = st.radio("Pilih Tahap:", step_names, label_visibility="collapsed")
        step_data = next(d for d in sim_data_list if d["name"] == selected_step)
        
        st.markdown(f'<p style="font-size:13px;">{step_data["desc"]}</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-label" style="margin-top:10px;">KONFIGURASI SENTRIFUGAL</div>', unsafe_allow_html=True)
        input_rpm = st.slider("Kecepatan Putaran (RPM):", min_value=0, max_value=6000, value=3000, step=500)
        input_time = st.slider("Durasi Waktu (Detik):", min_value=0, max_value=180, value=90, step=30)
        
        # Matematika Kompaksi Endapan: Efisiensi pengandapan dihitung dari RPM dan waktu
        if input_rpm == 0 or input_time == 0:
            calc_pellet_pct = 0
            compactness_msg = "Reagen dicampur, partikel masih melayang (belum mengendap)."
        else:
