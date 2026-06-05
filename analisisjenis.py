import streamlit as st

st.set_page_config(page_title="Analisis Kation", layout="wide")

# ================= HEADER =================
st.title("🔬 Analisis Kation Klasik")
st.caption("Simulasi Pemisahan + Sentrifugasi Interaktif")

st.divider()

# ================= SIDEBAR =================
menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Beranda", "📊 Flowchart", "🧪 Simulasi", "📘 Reaksi", "🎓 Latihan"]
)

# ================= BERANDA =================
if menu == "🏠 Beranda":
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📘 Deskripsi")
        st.write("""
        Aplikasi ini membantu memahami:
        - Pemisahan kation
        - Reaksi kimia
        - Teknik sentrifugasi
        """)

    with col2:
        st.subheader("⚙️ Metode")
        st.write("""
        ✔ Pengendapan bertahap  
        ✔ Sentrifugasi  
        ✔ Identifikasi ion  
        """)

# ================= FLOWCHART =================
elif menu == "📊 Flowchart":
    st.subheader("📊 Alur Pemisahan")

    st.markdown("""
    ```
    Larutan Sampel
        ↓ + HCl
    Endapan (AgCl, PbCl2)
        ↓ Sentrifugasi
    Supernatan
        ↓ + H2S
    Endapan (CuS, CdS)
        ↓ Sentrifugasi
    Supernatan
        ↓ + NH4OH
    Endapan (Fe(OH)3, Al(OH)3)
        ↓ Sentrifugasi
    Supernatan
        ↓ + (NH4)2CO3
    Endapan (CaCO3, BaCO3)
    ```
    """)

# ================= SIMULASI =================
elif menu == "🧪 Simulasi":
    st.subheader("🌀 Simulasi Sentrifugasi")

    tahap = st.selectbox(
        "Pilih Pereaksi",
        ["HCl", "H2S", "NH4OH", "(NH4)2CO3"]
    )

    kecepatan = st.slider("Kecepatan Sentrifus (rpm)", 1000, 10000, 3000)

    if st.button("🔬 Jalankan"):
        st.success(f"Sentrifugasi pada {kecepatan} rpm berhasil!")

        if tahap == "HCl":
            st.info("Endapan terbentuk")
            st.write("🔽 Pellet: AgCl, PbCl2")
            st.write("🔼 Supernatan: ion lain")

        elif tahap == "H2S":
            st.write("🔽 Pellet: CuS, CdS")
            st.write("🔼 Supernatan: ion sisa")

        elif tahap == "NH4OH":
            st.write("🔽 Pellet: Fe(OH)3, Al(OH)3")
            st.write("🔼 Supernatan: ion alkali")

        elif tahap == "(NH4)2CO3":
            st.write("🔽 Pellet: CaCO3, BaCO3")
            st.write("🔼 Supernatan: larutan akhir")

# ================= REAKSI =================
elif menu == "📘 Reaksi":
    st.subheader("⚗️ Reaksi Kimia")

    st.markdown("""
    **1. Dengan HCl**
    - Ag⁺ + Cl⁻ → AgCl(s)
    - Pb²⁺ + 2Cl⁻ → PbCl₂(s)

    **2. Dengan H₂S**
    - Cu²⁺ + S²⁻ → CuS(s)

    **3. Dengan NH₄OH**
    - Fe³⁺ + OH⁻ → Fe(OH)₃(s)

    **4. Dengan (NH₄)₂CO₃**
    - Ca²⁺ + CO₃²⁻ → CaCO₃(s)
    """)

# ================= LATIHAN =================
elif menu == "🎓 Latihan":
    st.subheader("🧠 Latihan Soal")

    soal = st.radio(
        "Ion mana yang mengendap dengan HCl?",
        ["Na⁺", "Ag⁺", "K⁺"]
    )

    if st.button("Cek Jawaban"):
        if soal == "Ag⁺":
            st.success("Benar! 🎉")
        else:
            st.error("Salah, coba lagi!")

st.divider()
st.caption("💡 Dibuat untuk praktikum kimia analis")
