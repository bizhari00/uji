
import streamlit as st
import plotly.express as px
from PIL import Image
import time

# ==============================================================================
# 1. KONFIGURASI HALAMAN UTAMA (Wajib Paling Atas)
# ==============================================================================
st.set_page_config(
    page_title="CLD - Mode Live",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Pengaturan padding halaman utama agar aman di Forio 80%
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2.0rem !important; 
        padding-bottom: 1.5rem !important;
        padding-left: 2.0rem !important;
        padding-right: 2.0rem !important;
        max-width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# 2. STRATEGI TURUNKAN LAYOUT 
# ==============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)

# ==============================================================================
# 3. NAVIGASI & JUDUL SEBARIS (Balanced Design Button & Title)
# ==============================================================================
st.markdown(
    """
    <style>
    /* 1. Mengatur Ukuran & Corak Kotak Tombol Navigasi */
    .stLinkButton > a {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important; /* Gradasi biru premium */
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important; 
        padding: 8px 20px !important; 
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
        transition: all 0.3s ease-in-out !important;
        text-decoration: none !important;
        
        /* KUNCI KESEIMBANGAN: Lebar otomatis dan tidak melar penuh */
        display: inline-flex !important;
        width: auto !important;
        max-width: 320px !important; 
    }

    /* 2. Menyesuaikan Ukuran Font di Dalam Tombol */
    .stLinkButton > a p {
        font-size: 16px !important; 
        font-weight: bold !important;
        color: #FFFFFF !important;
        letter-spacing: 0.5px !important;
    }

    /* 3. Efek Hover Interaktif */
    .stLinkButton > a:hover {
        background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%) !important;
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4) !important;
        transform: translateY(-1px) !important;
    }

    /* 4. Mengatur Teks Judul Diagram Agar Selaras Sebaris */
    .custom-title {
        font-size: 20px !important; 
        font-weight: 500 !important;
        color: #1E293B;
        margin-top: 8px; 
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Pembagian kolom rasio agar seimbang dan sejajar lurus secara vertikal
col_btn, col_title = st.columns([1.2, 2.8])

with col_btn:
    st.link_button("🏠 ke Menu Utama", "https://forio.com/app/univ_sumaterautara/research-ptpn", use_container_width=False)

with col_title:
    st.markdown('<p class="custom-title">Model Analisis Ketahanan Energi & Pangan (Live Animasi)</p>', unsafe_allow_html=True)

st.divider()

# ==============================================================================
# 4. MEMUAT BACKGROUND IMAGE CLD
# ==============================================================================
try:
    img = Image.open("cldnew.png")
except FileNotFoundError:
    st.error("File 'cldnew.png' tidak ditemukan. Pastikan file gambar ada di root repository GitHub Anda.")
    st.stop()

# ==============================================================================
# 5. DATA KOORDINAT XY MURNI (Sesuai Permintaan Alur Baru)
#    Format tank_area: [X_Mulai, Y_Mulai, X_Akhir, Y_Akhir]
# ==============================================================================
process_phases = [
    # --- FASE 1: GERAKAN ANIMASI 2 KOTAK BARENGAN ---
    [
        {
            'label': 'Kapasitas Kilang',
            'shape_type': 'rect',
            'tank_area': [240, 120, 310, 180]  # Silakan kalibrasi koordinat pasnya
        },
        {
            'label': 'Lahan Sawit Produktif TM',
            'shape_type': 'rect',
            'tank_area': [80, 640, 160, 720]   # Silakan kalibrasi koordinat pasnya
        }
    ],
    
    # --- FASE 2: KEMUDIAN 2 KOTAK BARU TERBENTUK BARENGAN ---
    [
        {
            'label': 'Produksi BBM',
            'shape_type': 'rect',
            'tank_area': [370, 110, 440, 170]  # Silakan kalibrasi koordinat pasnya
        },
        {
            'label': 'Pabrik Kelapa Sawit PKS',
            'shape_type': 'rect',
            'tank_area': [240, 760, 310, 830]  # Silakan kalibrasi koordinat pasnya
        }
    ],
    
    # --- FASE 3: KEMUDIAN 3 KOTAK BARU TERBENTUK BARENGAN ---
    [
        {
            'label': 'Palm Kernel',
            'shape_type': 'rect',
            'tank_area': [250, 610, 320, 670]  # Silakan kalibrasi koordinat pasnya
        },
        {
            'label': 'Hasil CPO',
            'shape_type': 'rect',
            'tank_area': [490, 750, 560, 810]  # Silakan kalibrasi koordinat pasnya
        },
        {
            'label': 'Kebutuhan BBM',
            'shape_type': 'rect',
            'tank_area': [490, 170, 560, 230]  # Silakan kalibrasi koordinat pasnya
        }
    ]
]

# ==============================================================================
# 6. LOOPING RENDERING (MODE NORMAL - GRID OFF)
# ==============================================================================
placeholder = st.empty()
render_count = 0

while True:
    for phase in process_phases:
        fig = px.imshow(img)
        
        # --- MODE NORMAL: Menonaktifkan Grid dan Sumbu Koordinat ---
        fig.update_xaxes(visible=False, showgrid=False)
        fig.update_yaxes(visible=False, showgrid=False)
        
        for component in phase:
            area = component['tank_area']
            shape = component.get('shape_type', 'rect')
            
            # 1. Menggambar Bentuk Berdasarkan Tipe Dinamik (Kotak/Lingkaran)
            # Menggunakan warna merah (Red) agar lebih kontras di diagram
            fig.add_shape(
                type=shape, 
                x0=area[0], y0=area[1], x1=area[2], y1=area[3],
                fillcolor="rgba(255, 0, 0, 0.4)",
                line=dict(color="Red", width=3),
            )
            
            # 2. Perhitungan Otomatis Koordinat Label di Bawah Kotak Indikator
            text_x = (area[0] + area[2]) / 2  # Titik tengah horizontal kotak
            text_y = area[3] + 25             # Menaruh teks 25 piksel di bawah batas bawah kotak
            
            # 3. Menggambar Teks Label Hasil Kalkulasi Dinamis
            fig.add_scatter(
                x=[text_x], y=[text_y], 
                mode="text",
                text=[component['label']], 
                textposition="bottom center",
                textfont=dict(size=12, color="DarkRed", family="Arial Black")
            )
        
        fig.update_layout(
            margin=dict(l=0, r=0, t=15, b=0), 
            height=600,
            autosize=True,
            showlegend=False
        )
        
        with placeholder.container():
            st.plotly_chart(
                fig, 
                use_container_width=True, 
                config={
                    'displayModeBar': False, 
                    'responsive': True
                }, 
                key=f"cld_live_mode_{render_count}"
            )
        
        render_count += 1
        time.sleep(3.0)  # Durasi transisi antar fase (3 detik)
