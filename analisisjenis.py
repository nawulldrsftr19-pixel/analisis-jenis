"""
LabKim Interactive — Analisis Kualitatif Kation (Metode Sentrifugasi)
Streamlit App
"""

import streamlit as st
import time

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LabKim — Analisis Kualitatif Kation",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -- CUSTOM CSS --
st.markdown("""
<style>
@import url('https://googleapis.com');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Syncopate', sans-serif;
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

/* cards */
.lab-card {
    background: #111827;
    border: 1px solid #1e3a5f;
}
</style>
""", unsafe_allow_html=True) # <-- PASTIKAN ADA PENUTUP INI RATA KIRI
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.rxn-card {
    background: #1a2235;
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    transition: border-color .2s;
}
.rxn-card:hover { border-color: #7c3aed; }
.equation-box {
    background: #0a0e1a;
    border: 1px solid #1e3a5f;
    border-radius: 8px;
    padding: 10px 14px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    margin: 6px 0;
    color: #c4b5fd;
}
.equation-title-sm {
    font-size: 10px;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 2px;
    font-family: 'Space Mono', monospace;
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
.tag {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 10px;
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 1px;
    background: rgba(0,212,255,0.08);
    color: #00d4ff;
    border: 1px solid rgba(0,212,255,0.2);
    margin-right: 6px;
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
.log-warn { color: #f59e0b; }
.log-time { color: #00d4ff; }

/* tube */
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
.tube-svg { filter: drop-shadow(0 0 6px rgba(0,212,255,0.2)); }

/* flow */
.flow-box {
    background: #1a2235;
    border: 2px solid #1e3a5f;
    border-radius: 10px;
    padding: 14px 20px;
    text-align: center;
    margin: 4px auto;
}
.flow-start { border-color: #7c3aed; }
.flow-reagent { border-color: #f59e0b; }
.flow-pellet { border-color: #f59e0b; }
.flow-super { border-color: #00d4ff; }
.flow-done { border-color: #10b981; }
.flow-arrow {
    text-align: center;
    color: #00d4ff;
    font-size: 18px;
    line-height: 1;
    margin: 2px 0;
}
.flow-title { font-weight: 700; font-size: 14px; color: #e2e8f0; }
.flow-sub { font-family: 'Space Mono', monospace; font-size: 10px; color: #64748b; margin-top: 2px; }
.flow-gtype { font-family: 'Space Mono', monospace; font-size: 9px; text-transform: uppercase; letter-spacing: 2px; }

/* quiz */
.quiz-opt-btn {
    width: 100%;
    padding: 12px 16px;
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 8px;
    color: #e2e8f0;
    font-size: 13px;
    text-align: left;
    cursor: pointer;
    margin-bottom: 8px;
    transition: all .2s;
}
.progress-bar-bg {
    height: 4px;
    background: #1e3a5f;
    border-radius: 2px;
    margin-bottom: 20px;
    overflow: hidden;
}
.progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, #7c3aed, #00d4ff);
    border-radius: 2px;
    transition: width .4s;
}

/* ref table */
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
    border-bottom: 1px solid rgba(30,58,95,0.4);
    color: #e2e8f0;
}
.info-box {
    background: rgba(0,212,255,0.05);
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: 8px;
    padding: 12px 16px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.7;
    margin-bottom: 16px;
}
.badge-white  { background:rgba(255,255,255,0.1); color:#fff; border:1px solid #334155; border-radius:20px; padding:3px 10px; font-size:10px; font-family:'Space Mono',monospace; }
.badge-yellow { background:rgba(245,158,11,0.15); color:#f59e0b; border-radius:20px; padding:3px 10px; font-size:10px; font-family:'Space Mono',monospace; }
.badge-black  { background:rgba(0,0,0,0.4); color:#94a3b8; border:1px solid #333; border-radius:20px; padding:3px 10px; font-size:10px; font-family:'Space Mono',monospace; }
.badge-red    { background:rgba(239,68,68,0.15); color:#f87171; border-radius:20px; padding:3px 10px; font-size:10px; font-family:'Space Mono',monospace; }

[data-testid="stTabs"] button { font-family:'Space Mono',monospace; font-size:11px; letter-spacing:1px; color:#64748b !important; }
[data-testid="stTabs"] button[aria-selected="true"] { color:#00d4ff !important; border-bottom-color:#00d4ff !important; }
[data-testid="stTabs"] { border-bottom: 1px solid #1e3a5f; }

/* spinner override */
[data-testid="stSpinner"] { color: #00d4ff; }

/* expander */
[data-testid="stExpander"] {
    background: #111827;
    border: 1px solid #1e3a5f !important;
    border-radius: 10px !important;
}

/* button overrides */
.stButton>button {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    border: 1px solid #00d4ff;
    background: rgba(0,212,255,0.08);
    color: #00d4ff;
    border-radius: 8px;
    transition: all .2s;
}
.stButton>button:hover {
    background: rgba(0,212,255,0.18) !important;
    border-color: #00d4ff !important;
    color: #00d4ff !important;
}
.stButton>button:disabled {
    border-color: #1e3a5f !important;
    color: #64748b !important;
    background: transparent !important;
    cursor: not-allowed !important;
}

div[data-testid="stMarkdownContainer"] p { color: #94a3b8; }
</style>
""", unsafe_allow_html=True)


# ─── DATA ──────────────────────────────────────────────────────────────────────

STEPS = [
    {
        "id": "prep",
        "name": "Persiapan Sampel",
        "reagent": "Sampel awal",
        "desc": "Larutkan sampel dalam akuades. Pastikan semua kation terlarut sempurna. Volume: ±5 mL.",
        "rpm": 0,
        "duration": 0,
        "tubes": [
            {"label": "Sampel", "color": "#334155", "liquid_pct": 60, "pellet_pct": 0},
        ],
        "obs": [
            {"color": "#64748b", "text": "Larutan jernih / sedikit keruh"},
        ],
        "log": [
            ("msg",    "Sampel dimuat ke tabung sentrifugasi."),
            ("msg",    "Kation potensial: Ag⁺, Pb²⁺, Hg₂²⁺, Fe³⁺, Al³⁺, Ba²⁺, Sr²⁺, Ca²⁺"),
        ],
    },
    {
        "id": "g1",
        "name": "Langkah 1 — Golongan I",
        "reagent": "HCl encer (2M)",
        "desc": "Tambahkan HCl encer 2M tetes demi tetes ke sampel. Kation Golongan I mengendap sebagai klorida tak larut. Kocok lembut lalu sentrifugasi.",
        "rpm": 3000,
        "duration": 3,   # seconds in sim (represents 90 s real)
        "tubes": [
            {"label": "Supernatan", "color": "#1e40af", "liquid_pct": 50, "pellet_pct": 0},
            {"label": "Pellet G-I",  "color": "#93c5fd", "liquid_pct": 25, "pellet_pct": 14},
        ],
        "obs": [
            {"color": "#e2e8f0", "text": "Endapan putih: AgCl"},
            {"color": "#e2e8f0", "text": "Endapan putih: PbCl₂"},
            {"color": "#cbd5e1", "text": "Endapan putih: Hg₂Cl₂"},
        ],
        "log": [
            ("react",  "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓   [Ksp = 1.8×10⁻¹⁰]"),
            ("react",  "Pb²⁺(aq) + 2Cl⁻(aq) → PbCl₂(s)↓  [Ksp = 1.6×10⁻⁵]"),
            ("react",  "Hg₂²⁺(aq) + 2Cl⁻(aq) → Hg₂Cl₂(s)↓  [Ksp = 1.4×10⁻¹⁸]"),
            ("result", "Endapan putih terbentuk → Sentrifugasi 3000 rpm / 90 det"),
            ("msg",    "Pisahkan supernatan → lanjut ke Langkah 2"),
        ],
    },
    {
        "id": "g1id",
        "name": "Identifikasi Golongan I",
        "reagent": "NH₄OH / K₂CrO₄",
        "desc": "Uji pellet Golongan I: AgCl larut dalam NH₄OH. Pb²⁺ + K₂CrO₄ → kuning. Hg₂Cl₂ + NH₄OH → hitam.",
        "rpm": 0,
        "duration": 0,
        "tubes": [
            {"label": "AgCl+NH₄OH",   "color": "#6366f1", "liquid_pct": 50, "pellet_pct": 0},
            {"label": "Pb+CrO₄",      "color": "#ca8a04", "liquid_pct": 50, "pellet_pct": 12},
            {"label": "Hg₂Cl₂+NH₃",  "color": "#1c1917", "liquid_pct": 50, "pellet_pct": 18},
        ],
        "obs": [
            {"color": "#818cf8", "text": "AgCl larut dalam NH₄OH → Ag⁺ terkonfirmasi"},
            {"color": "#facc15", "text": "PbCrO₄ kuning → Pb²⁺ terkonfirmasi"},
            {"color": "#374151", "text": "Hg(NH₂)Cl hitam → Hg₂²⁺ terkonfirmasi"},
        ],
        "log": [
            ("react",  "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻  (larut)"),
            ("react",  "[Ag(NH₃)₂]⁺ + HNO₃ → AgCl↓ (endapan kembali)"),
            ("react",  "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓  (kuning)"),
            ("react",  "Hg₂Cl₂ + 2NH₃ → HgNH₂Cl(s)↓ + Hg(l) + NH₄⁺ + Cl⁻  (hitam)"),
            ("result", "✓ Identifikasi Golongan I selesai"),
        ],
    },
    {
        "id": "g3",
        "name": "Langkah 2 — Golongan III",
        "reagent": "NH₄OH (6M)",
        "desc": "Ambil supernatan Langkah 1, tambahkan NH₄OH 6M. Kation Golongan III mengendap sebagai hidroksida. Sentrifugasi kembali.",
        "rpm": 3000,
        "duration": 3,
        "tubes": [
            {"label": "Supernatan",      "color": "#065f46", "liquid_pct": 50, "pellet_pct": 0},
            {"label": "Fe(OH)₃/Al(OH)₃","color": "#92400e", "liquid_pct": 25, "pellet_pct": 16},
        ],
        "obs": [
            {"color": "#b45309", "text": "Endapan cokelat: Fe(OH)₃"},
            {"color": "#e2e8f0", "text": "Endapan putih gel: Al(OH)₃"},
        ],
        "log": [
            ("react",  "Fe³⁺(aq) + 3OH⁻(aq) → Fe(OH)₃(s)↓  (cokelat-merah)"),
            ("react",  "Al³⁺(aq) + 3OH⁻(aq) → Al(OH)₃(s)↓  (putih gel)"),
            ("result", "Endapan cokelat/putih terbentuk → Sentrifugasi 3000 rpm / 90 det"),
            ("msg",    "Pisahkan supernatan → lanjut ke Langkah 3"),
        ],
    },
    {
        "id": "g3id",
        "name": "Identifikasi Golongan III",
        "reagent": "KSCN / NaOH",
        "desc": "Fe³⁺: + SCN⁻ → merah darah. Al³⁺: larut dalam NaOH berlebih, endap kembali dengan HCl.",
        "rpm": 0,
        "duration": 0,
        "tubes": [
            {"label": "Fe+SCN⁻",  "color": "#dc2626", "liquid_pct": 55, "pellet_pct": 0},
            {"label": "Al+NaOH",  "color": "#1d4ed8", "liquid_pct": 55, "pellet_pct": 0},
        ],
        "obs": [
            {"color": "#ef4444", "text": "FeSCN²⁺ merah darah → Fe³⁺ terkonfirmasi"},
            {"color": "#3b82f6", "text": "Al(OH)₄⁻ larut basa → Al³⁺ terkonfirmasi"},
        ],
        "log": [
            ("react",  "Fe³⁺ + 3SCN⁻ → Fe(SCN)₃  (merah darah pekat)"),
            ("react",  "Al(OH)₃ + NaOH → NaAlO₂ + 2H₂O  (larut dalam basa)"),
            ("react",  "NaAlO₂ + HCl + H₂O → Al(OH)₃↓ + NaCl  (endap kembali)"),
            ("result", "✓ Identifikasi Golongan III selesai"),
        ],
    },
    {
        "id": "g4",
        "name": "Langkah 3 — Golongan IV",
        "reagent": "(NH₄)₂CO₃",
        "desc": "Ambil supernatan Langkah 2, tambahkan (NH₄)₂CO₃. Kation tanah alkali mengendap sebagai karbonat. Sentrifugasi.",
        "rpm": 3000,
        "duration": 3,
        "tubes": [
            {"label": "Supernatan",            "color": "#1e3a5f", "liquid_pct": 50, "pellet_pct": 0},
            {"label": "BaCO₃/SrCO₃/CaCO₃",   "color": "#f0fdf4", "liquid_pct": 20, "pellet_pct": 14},
        ],
        "obs": [
            {"color": "#e2e8f0", "text": "Endapan putih: BaCO₃"},
            {"color": "#e2e8f0", "text": "Endapan putih: SrCO₃"},
            {"color": "#e2e8f0", "text": "Endapan putih: CaCO₃"},
        ],
        "log": [
            ("react",  "Ba²⁺ + CO₃²⁻ → BaCO₃(s)↓  [Ksp = 2.6×10⁻⁹]"),
            ("react",  "Sr²⁺ + CO₃²⁻ → SrCO₃(s)↓  [Ksp = 5.6×10⁻¹⁰]"),
            ("react",  "Ca²⁺ + CO₃²⁻ → CaCO₃(s)↓  [Ksp = 3.4×10⁻⁹]"),
            ("result", "Endapan putih terbentuk → Sentrifugasi 3000 rpm / 90 det"),
        ],
    },
    {
        "id": "g4id",
        "name": "Identifikasi Golongan IV",
        "reagent": "K₂CrO₄ / H₂SO₄ / C₂O₄²⁻",
        "desc": "Ba²⁺ + CrO₄²⁻ → kuning. Sr²⁺ + SO₄²⁻ → putih. Ca²⁺ + C₂O₄²⁻ → putih.",
        "rpm": 0,
        "duration": 0,
        "tubes": [
            {"label": "Ba+CrO₄",  "color": "#ca8a04", "liquid_pct": 55, "pellet_pct": 12},
            {"label": "Sr+SO₄",   "color": "#e2e8f0", "liquid_pct": 55, "pellet_pct": 14},
            {"label": "Ca+C₂O₄",  "color": "#f0fdf4", "liquid_pct": 55, "pellet_pct": 12},
        ],
        "obs": [
            {"color": "#fbbf24", "text": "BaCrO₄ kuning → Ba²⁺ terkonfirmasi"},
            {"color": "#cbd5e1", "text": "SrSO₄ putih → Sr²⁺ terkonfirmasi"},
            {"color": "#e2e8f0", "text": "CaC₂O₄ putih → Ca²⁺ terkonfirmasi"},
        ],
        "log": [
            ("react",  "Ba²⁺ + K₂CrO₄ → BaCrO₄↓ + 2K⁺  (kuning)"),
            ("react",  "Sr²⁺ + H₂SO₄ → SrSO₄↓ + 2H⁺  (putih)"),
            ("react",  "Ca²⁺ + (NH₄)₂C₂O₄ → CaC₂O₄↓ + 2NH₄⁺  (putih)"),
            ("result", "✓ Identifikasi Golongan IV selesai"),
            ("result", "▶️ Analisis selesai! Semua golongan teridentifikasi."),
        ],
    },
]

REACTIONS = [
    {
        "group": "Golongan I", "color": "#6366f1",
        "ion": "Ag⁺", "desc": "Perak — Endapan klorida putih, sangat tidak larut",
        "badge_cls": "badge-white", "badge_text": "AgCl — Putih",
        "equations": [
            ("Pengendapan dengan HCl",      "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓"),
            ("Netto ionik",                 "Ag⁺ + Cl⁻ → AgCl↓"),
            ("Konfirmasi: larut NH₄OH",      "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻"),
            ("Re-presipitasi dengan HNO₃",   "[Ag(NH₃)₂]⁺ + Cl⁻ + 2H⁺ → AgCl↓ + 2NH₄⁺"),
        ],
    },
    {
        "group": "Golongan I", "color": "#f59e0b",
        "ion": "Pb²⁺", "desc": "Timbal — Klorida larut sedikit dalam air dingin",
        "badge_cls": "badge-yellow", "badge_text": "PbCrO₄ — Kuning",
        "equations": [
            ("Pengendapan dengan HCl",  "Pb²⁺(aq) + 2Cl⁻(aq) → PbCl₂(s)↓"),
            ("Netto ionik",              "Pb²⁺ + 2Cl⁻ → PbCl₂↓"),
            ("Konfirmasi: K₂CrO₄",      "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓  (kuning)"),
        ],
    },
    {
        "group": "Golongan I", "color": "#94a3b8",
        "ion": "Hg₂²⁺", "desc": "Merkuri(I) — Reaksi unik dengan amonia menghasilkan warna hitam",
        "badge_cls": "badge-black", "badge_text": "Hg + HgNH₂Cl — Hitam",
        "equations": [
            ("Pengendapan dengan HCl",       "Hg₂²⁺(aq) + 2Cl⁻(aq) → Hg₂Cl₂(s)↓"),
            ("Konfirmasi dengan NH₃",         "Hg₂Cl₂ + 2NH₃ → HgNH₂Cl↓ + Hg(l) + NH₄⁺ + Cl⁻"),
            ("Produk (disproportionasi)",      "Hg₂²⁺ → Hg⁰ + Hg²⁺  (oksidasi-reduksi)"),
        ],
    },
    {
        "group": "Golongan III", "color": "#b45309",
        "ion": "Fe³⁺", "desc": "Besi(III) — Hidroksida cokelat merah, uji SCN⁻ sangat sensitif",
        "badge_cls": "badge-red", "badge_text": "Fe(SCN)₃ — Merah darah",
        "equations": [
            ("Pengendapan dengan NH₄OH",  "Fe³⁺(aq) + 3OH⁻(aq) → Fe(OH)₃(s)↓"),
            ("Persamaan molekuler",        "FeCl₃ + 3NH₄OH → Fe(OH)₃↓ + 3NH₄Cl"),
            ("Konfirmasi dengan SCN⁻",     "Fe³⁺ + 3SCN⁻ → Fe(SCN)₃  (merah darah)"),
        ],
    },
    {
        "group": "Golongan III", "color": "#64748b",
        "ion": "Al³⁺", "desc": "Aluminium — Hidroksida amfoter: larut dalam asam maupun basa",
        "badge_cls": "badge-white", "badge_text": "Al(OH)₃ — Putih gel",
        "equations": [
            ("Pengendapan dengan NH₄OH",  "Al³⁺(aq) + 3OH⁻(aq) → Al(OH)₃(s)↓"),
            ("Larut dalam NaOH (basa)",    "Al(OH)₃ + OH⁻ → [Al(OH)₄]⁻  (tetrahidroksoaluminat)"),
            ("Re-presipitasi dengan HCl",  "[Al(OH)₄]⁻ + H⁺ → Al(OH)₃↓ + H₂O"),
        ],
    },
    {
        "group": "Golongan IV", "color": "#10b981",
        "ion": "Ba²⁺", "desc": "Barium — Karbonat putih; uji kromat paling spesifik",
        "badge_cls": "badge-yellow", "badge_text": "BaCrO₄ — Kuning",
        "equations": [
            ("Pengendapan dengan (NH₄)₂CO₃", "Ba²⁺(aq) + CO₃²⁻(aq) → BaCO₃(s)↓"),
            ("Persamaan molekuler",            "BaCl₂ + (NH₄)₂CO₃ → BaCO₃↓ + 2NH₄Cl"),
            ("Konfirmasi dengan K₂CrO₄",       "Ba²⁺ + CrO₄²⁻ → BaCrO₄↓  (kuning)"),
        ],
    },
    {
        "group": "Golongan IV", "color": "#06b6d4",
        "ion": "Sr²⁺", "desc": "Strontium — Karbonat putih; uji sulfat dalam asam asetat",
        "badge_cls": "badge-white", "badge_text": "SrSO₄ — Putih",
        "equations": [
            ("Pengendapan dengan (NH₄)₂CO₃", "Sr²⁺(aq) + CO₃²⁻(aq) → SrCO₃(s)↓"),
            ("Konfirmasi dengan H₂SO₄",        "Sr²⁺ + SO₄²⁻ → SrSO₄↓  (putih)"),
        ],
    },
    {
        "group": "Golongan IV", "color": "#8b5cf6",
        "ion": "Ca²⁺", "desc": "Kalsium — Karbonat putih; oksalat sangat spesifik",
        "badge_cls": "badge-white", "badge_text": "CaC₂O₄ — Putih",
        "equations": [
            ("Pengendapan dengan (NH₄)₂CO₃",     "Ca²⁺(aq) + CO₃²⁻(aq) → CaCO₃(s)↓"),
            ("Konfirmasi dengan (NH₄)₂C₂O₄",      "Ca²⁺ + C₂O₄²⁻ → CaC₂O₄↓  (putih)"),
            ("Tidak larut dalam asam asetat",       "CaC₂O₄ + CH₃COOH → tidak larut (membedakan dari Sr)"),
        ],
    },
]

QUIZ = [
    {
        "q":    "Reagen apa yang digunakan untuk mengendapkan kation Golongan I?",
        "hint": "Kation Golongan I membentuk garam klorida tidak larut",
        "opts": ["HCl encer", "H₂SO₄", "NH₄OH", "(NH₄)₂CO₃"],
        "ans":  0,
        "exp":  "HCl encer menghasilkan Cl⁻ yang mengendapkan Ag⁺, Pb²⁺, dan Hg₂²⁺ sebagai klorida tidak larut.",
    },
    {
        "q":    "Apa warna endapan ketika Hg₂Cl₂ ditambah NH₄OH berlebih?",
        "hint": "Terjadi reaksi disproportionasi Hg₂²⁺",
        "opts": ["Putih", "Kuning", "Merah", "Hitam"],
        "ans":  3,
        "exp":  "Hg₂Cl₂ + 2NH₃ → HgNH₂Cl↓ + Hg(l) + NH₄⁺ + Cl⁻. Merkuri logam (Hg⁰) menyebabkan warna hitam.",
    },
    {
        "q":    "Uji apa yang digunakan untuk mengkonfirmasi keberadaan Fe³⁺?",
        "hint": "Menghasilkan warna merah darah",
        "opts": ["K₂CrO₄", "KSCN", "(NH₄)₂C₂O₄", "H₂SO₄ encer"],
        "ans":  1,
        "exp":  "Fe³⁺ + 3SCN⁻ → Fe(SCN)₃. Ion tiosianat menghasilkan warna merah darah yang sangat khas untuk Fe³⁺.",
    },
    {
        "q":    "Al(OH)₃ bersifat amfoter. Apa artinya?",
        "hint": "Amfoter = dapat bereaksi dengan asam DAN basa",
        "opts": [
            "Hanya larut dalam asam kuat",
            "Tidak larut dalam reagen apapun",
            "Larut dalam asam kuat maupun basa kuat",
            "Membentuk endapan berwarna-warni",
        ],
        "ans":  2,
        "exp":  "Al(OH)₃ + OH⁻ → [Al(OH)₄]⁻ (larut basa). Al(OH)₃ + 3H⁺ → Al³⁺ + 3H₂O (larut asam).",
    },
    {
        "q":    "Kecepatan sentrifugasi yang digunakan dalam analisis ini adalah?",
        "hint": "Cukup kuat untuk memisahkan endapan halus",
        "opts": ["1000 rpm", "3000 rpm", "5000 rpm", "10000 rpm"],
        "ans":  1,
        "exp":  "3000 rpm selama 1-2 menit cukup untuk memisahkan endapan klorida/hidroksida/karbonat dari supernatan.",
    },
    {
        "q":    "Persamaan yang BENAR untuk pembentukan BaCrO₄?",
        "hint": "Produknya adalah endapan kuning",
        "opts": [
            "Ba²⁺ + SO₄²⁻ → BaSO₄↓",
            "Ba²⁺ + CrO₄²⁻ → BaCrO₄↓",
            "Ba²⁺ + 2Cl⁻ → BaCl₂↓",
            "Ba²⁺ + CO₃²⁻ → BaCO₃↓",
        ],
        "ans":  1,
        "exp":  "Ba²⁺ + CrO₄²⁻ → BaCrO₄↓ (kuning). Uji konfirmasi spesifik Ba²⁺ dalam suasana netral/asam lemah.",
    },
    {
        "q":    "Mengapa tabung sentrifugasi harus dipasang seimbang (simetris)?",
        "hint": "Berkaitan dengan keselamatan dan fungsi alat",
        "opts": [
            "Agar endapan lebih banyak",
            "Mencegah getaran berlebih dan kerusakan rotor",
            "Agar supernatan lebih jernih",
            "Untuk mempercepat reaksi kimia",
        ],
        "ans":  1,
        "exp":  "Tabung tidak seimbang menyebabkan vibrasi yang merusak rotor dan berbahaya bagi operator.",
    },
    {
        "q":    "Reaksi ionik netto pengendapan AgCl yang benar adalah?",
        "hint": "Hanya spesi yang bereaksi yang ditulis",
        "opts": [
            "AgNO₃ + HCl → AgCl + HNO₃",
            "Ag⁺ + Cl⁻ → AgCl↓",
            "AgNO₃ → Ag⁺ + NO₃⁻",
            "Ag + Cl → AgCl",
        ],
        "ans":  1,
        "exp":  "Persamaan ionik netto hanya menampilkan ion yang terlibat: Ag⁺(aq) + Cl⁻(aq) → AgCl(s)↓",
    },
]


# ─── HELPERS ───────────────────────────────────────────────────────────────────

def tube_svg(tubes: list) -> str:
    """Render test tubes as SVG-based HTML."""
    parts = ['<div class="tube-wrap">']
    for t in tubes:
        liq_h = int(t["liquid_pct"] * 0.7)   # px out of 90px tube body
        pell_h = int(t["pellet_pct"] * 0.7)
        liq_y  = 90 - liq_h
        pell_y = 90 - pell_h
        parts.append(f"""
        <div class="tube-col">
          <div class="tube-lbl">{t['label']}</div>
          <svg width="40" height="110" class="tube-svg" xmlns="http://www.w3.org/2000/svg">
            <rect x="4" y="0" width="32" height="10" rx="3"
                  fill="rgba(100,180,255,0.25)" stroke="rgba(100,180,255,0.4)" stroke-width="1"/>
            <path d="M6,10 L6,88 Q6,100 20,100 Q34,100 34,88 L34,10"
                  fill="rgba(10,14,26,0.85)"
                  stroke="rgba(100,180,255,0.35)" stroke-width="1.5"/>
            <clipPath id="clip-{t['label'].replace(' ','').replace('⁺','').replace('²','').replace('₂','').replace('⁻','')}">
              <path d="M7,10 L7,88 Q7,99 20,99 Q33,99 33,88 L33,10 Z"/>
            </clipPath>
            <rect x="7" y="{liq_y}" width="26" height="{liq_h}"
                  fill="{t['color']}" opacity="0.85"
                  clip-path="url(#clip-{t['label'].replace(' ','').replace('⁺','').replace('²','').replace('₂','').replace('⁻','')})"/>
            <rect x="7" y="{pell_y}" width="26" height="{pell_h}"
                  fill="{t['color']}" opacity="0.55"
                  clip-path="url(#clip-{t['label'].replace(' ','').replace('⁺','').replace('²','').replace('₂','').replace('⁻','')})"/>
          </svg>
        </div>
        """)
    parts.append("</div>")
    return "".join(parts)


def render_log(logs: list) -> str:
    rows = []
    for typ, txt in logs:
        cls = {"react": "log-react", "result": "log-result", "warn": "log-warn"}.get(typ, "")
        rows.append(f'<div><span class="log-time">[LOG]</span> <span class="{cls}">{txt}</span></div>')
    return f'<div class="log-box">{"".join(rows)}</div>'


def render_obs(obs: list) -> str:
    pills = "".join(
        f'<span class="obs-pill"><span style="display:inline-block;width:12px;height:12px;'
        f'border-radius:50%;background:{o["color"]};border:1px solid rgba(255,255,255,0.15);'
        f'flex-shrink:0"></span>{o["text"]}</span>'
        for o in obs
    )
    return f'<div style="margin-top:10px">{pills}</div>'


# ─── SESSION STATE ──────────────────────────────────────────────────────────────

def init_state():
    if "sim_step" not in st.session_state:
        st.session_state.sim_step = 0          # which step is active/displayed
    if "completed" not in st.session_state:
        st.session_state.completed = set()
    if "quiz_idx" not in st.session_state:
        st.session_state.quiz_idx = 0
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False
    if "quiz_choice" not in st.session_state:
        st.session_state.quiz_choice = None
    if "quiz_done" not in st.session_state:
        st.session_state.quiz_done = False

init_state()


# ─── HEADER ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="section-label">⬡ LabKim Interactive</div>
<div class="hero-title">Analisis Kualitatif Kation<br><span style="font-size:0.6em">Metode Sentrifugasi</span></div>
<div class="hero-sub">// Simulasi reaksi stoikiometri · pemisahan golongan · identifikasi visual</div>
<span class="tag">3000 rpm</span>
<span class="tag">1–2 menit</span>
<span class="tag">3 golongan</span>
<hr style="border-color:#1e3a5f;margin:18px 0 0">
""", unsafe_allow_html=True)


# ─── TABS ──────────────────────────────────────────────────────────────────────

tab_sim, tab_rxn, tab_flow, tab_quiz, tab_ref = st.tabs([
    "⚗  Simulator",
    "⚛  Reaksi",
    "⬡  Alur Analisis",
    "◈  Kuis",
    "◻  Referensi",
])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — SIMULATOR
# ══════════════════════════════════════════════════════════════════════════════
with tab_sim:
    st.markdown('<div class="section-label">// Panel Kontrol</div>', unsafe_allow_html=True)
    st.markdown("### Simulator Sentrifugasi")
    st.markdown(
        '<p style="font-family:\'Space Mono\',monospace;font-size:12px;color:#64748b;margin-bottom:16px">'
        "Jalankan setiap langkah secara berurutan. Perhatikan pembentukan endapan (pellet) dan "
        "pemisahan supernatan secara visual. Setiap reaksi disertai stoikiometri lengkap di log."
        "</p>",
        unsafe_allow_html=True,
    )

    col_vis, col_ctrl = st.columns([3, 2], gap="large")

    # ── Visualisation column ──────────────────────────────────────────────────
    with col_vis:
        current = STEPS[st.session_state.sim_step]

        # Centrifuge ring visual (CSS animation placeholder)
        spinning = False  # only true during run callback
        rpm_display = current["rpm"] if st.session_state.sim_step in st.session_state.completed else 0

st.markdown(f"""
<div style="background:#1a2235; border:1px solid #1e3a5f; border-radius:16px; padding:28px; text-align:center; min-height:380px;">
    <div style="margin-bottom:18px;">
        <svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://w3.org">
            <circle cx="60" cy="60" r="54" fill="#0a1628" stroke="#00d4ff" stroke-width="3" style="filter: drop-shadow(0 10px rgba(0,212,255,0.3));" />
            <line x1="60" y1="60" x2="110" y2="60" stroke="#00d4ff" stroke-width="3" stroke-linecap="round" opacity="0.7" />
            <line x1="60" y1="60" x2="10" y2="60" stroke="#00d4ff" stroke-width="3" stroke-linecap="round" opacity="0.7" />
            <line x1="60" y1="60" x2="60" y2="110" stroke="#00d4ff" stroke-width="3" stroke-linecap="round" opacity="0.7" />
            <line x1="60" y1="60" x2="60" y2="10" stroke="#00d4ff" stroke-width="3" stroke-linecap="round" opacity="0.7" />
            <line x1="60" y1="60" x2="10" y2="10" stroke="#00d4ff" stroke-width="3" stroke-linecap="round" opacity="0.7" />
            <line x1="60" y1="60" x2="95" y2="25" stroke="#00d4ff" stroke-width="3" stroke-linecap="round" opacity="0.7" />
            <circle cx="60" cy="60" r="8" fill="#00d4ff" opacity="0.6" />
        </svg>
    </div>
    
    <div style="display:flex; align-items:center; gap:12px; background:#0a1a3a; border:1px solid #1e3a5f; border-radius:10px; padding:10px 16px; margin-bottom:18px; justify-content:space-between;">
        <div>
            <div style="font-family:'Space Mono', monospace; font-size:9px; color:#64748b; text-transform:uppercase; letter-spacing:1px;">RPM</div>
            <div style="font-family:'Space Mono', monospace; font-size:22px; font-weight:700; color:#00d4ff;">{rpm_display}</div>
        </div>
    </div>
    
    <div style="flex:1; height:6px; background:#1e3a5f; border-radius:3px; overflow:hidden;">
        <div style="width:{rpm_display}%;"></div>
    </div>
</div>
""", unsafe_allow_html=True)
