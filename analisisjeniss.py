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
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Space Mono', monospace;
    background-color: #0a1628;
    color: #e2e8f0;
}
[data-testid="stHeader"] { background: transparent; }
.main .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
/* ... (CSS lain tetap sama) ... */
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
    # ... (data g1, g3, g4 tetap sama) ...
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

# 📌 TAB 1: SENTRIFUGASI UTAMA
with tab_sim:
    col_ctrl, col_view = st.columns([1, 1.2])
    with col_ctrl:
        st.markdown('<div class="section-label">PILIH TAHAPAN UTAMA</div>', unsafe_allow_html=True)
        step_names = [d["name"] for d in sim_data_list]
        selected_step = st.radio("Pilih Tahap:", step_names, label_visibility="collapsed")

        step_data = next(d for d in sim_data_list if d["name"] == selected_step)
        st.markdown(f'<p style="font-size:13px;">{step_data["desc"]}</p>', unsafe_allow_html=True)

        input_rpm = st.slider("Kecepatan Putaran (RPM):", min_value=0, max_value=6000, value=3000, step=500)
        input_time = st.slider("Durasi Waktu (Detik):", min_value=0, max_value=180, value=90, step=30)

        if input_rpm == 0 or input_time == 0:
            calc_pellet_pct = 0
            compactness_msg = "Reagen tercampur, koloid partikel masih melayang bebas di dalam fasa air."
        else:
            efficiency = min((input_rpm / 4000) * (input_time / 120), 1.2)
            calc_pellet_pct = int(step_data["base_pellet"] * efficiency)
            if efficiency < 0.6:
                compactness_msg = "⚠️ Pelet longgar & keruh."
            elif efficiency <= 1.0:
                compactness_msg = "✅ Pelet terbentuk normal."
            else:
                compactness_msg = "⚡ Pelet super-kompak terbentuk."

        run_centrifuge = st.button("MULAI SENTRIFUGASI ⚡", use_container_width=True, disabled=(input_rpm == 0))
        if run_centrifuge:
            progress_bar = st.empty()
            for i in range(1, 101):
                progress_bar.markdown(f'<div class="progress-bar-bg"><div class="progress-bar-fill" style="width: {i}%"></div></div>', unsafe_allow_html=True)
                time.sleep(0.005)
            progress_bar.empty()
            st.success(compactness_msg)

    with col_view:
        st.markdown('<div class="section-label">PROFIL PEMISAHAN FISIS</div>', unsafe_allow_html=True)
        tubes_html = ""
        for t in step_data["tubes"]:
            p_pct = calc_pellet_pct if "Pellet" in t["label"] else 0
            tubes_html += render_tube_svg(t["label"], t["color"], t["liquid_pct"], p_pct)
        st.markdown(f'<div class="tube-wrap">{tubes_html}</div>', unsafe_allow_html=True)

        for obs in step_data["obs"]:
            st.markdown(f'<span class="obs-pill" style="border-color:{obs["color"]}"><span style="color:{obs["color"]};">●</span> {obs["text"]} (Tinggi Pelet: {calc_pellet_pct}%)</span>', unsafe_allow_html=True)

        st.markdown('<div class="section-label" style="margin-top:15px;">LOG REAKSI</div>', unsafe_allow_html=True)
        log_html = '<div class="log-box">'
        for ltype, msg in step_data["log"]:
            tag = '<span class="log-react">Rxn:</span>' if ltype == "react" else '<span>Info:</span>'
            log_html += f'<div><span class="log-time">[{time.strftime("%H:%M:%S")}]</span> {tag} {msg}</div>'
        log_html += '</div>'
        st.markdown(log_html, unsafe_allow_html=True)

# 📌 TAB 2: UJI NYALA
with tab_flame:
    st.markdown('<div class="section-label">UJI NYALA (FLAME TEST) LOGAM ALKALI TANAH</div>', unsafe_allow_html=True)
    st.write("Identifikasi kation Golongan IV dilakukan dengan melarutkan sebagian pelet karbonat dalam sedikit HCl pekat, mencelupkan kawat nikrom, dan membakarnya langsung pada zona panas Bunsen.")

    col_fl_ctrl, col_fl_view = st.columns(2)

    with col_fl_ctrl:
        kation_selected = st.selectbox(
            "Pilih Kation Golongan IV untuk Diteliti:",
            ["Belum Memilih Kation", "Barium (Ba²⁺)", "Kalsium (Ca²⁺)", "Stronsium (Sr²⁺)"]
        )

        if kation_selected == "Barium (Ba²⁺)":
            flame_color = "#98fb98"
            flame_style = "color: #98fb98;"
            desc_flame = "Kation **Ba²⁺** memancarkan radiasi dengan panjang gelombang dominan hijau, menghasilkan warna **Hijau Apel**."
        elif kation_selected == "Kalsium (Ca²⁺)":
            flame_color = "#ff4500"
            flame_style = "color: #ff4500;"
            desc_flame = "Kation **Ca²⁺** menghasilkan warna **Merah Bata (Jingga Kemerahan Tua)**."
        elif kation_selected == "Stronsium (Sr²⁺)":
            flame_color = "#e60026"
            flame_style = "color: #e60026;"
            desc_flame = "Kation **Sr²⁺** menghasilkan warna **Merah Karmin** yang tajam."
        else:
            flame_color = "#00d4ff"
            flame_style = "color: #00d4ff;"
            desc_flame = "Silakan pilih salah satu kation di atas untuk memulai simulasi."

        st.markdown(f'<div class="lab-card" style="margin-top:15px;">{desc_flame}</div>', unsafe_allow_html=True)

    with col_fl_view:
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
            <td>Sr²⁺ + CO₃²⁻ → SrCO₃↓ (Putih)</td>
            <td style="color:#e60026; font-weight:bold;">Merah Karmin</td>
            <td>~650 nm</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

    
