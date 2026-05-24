
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
    .stLinkButton > a {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important; 
        padding: 8px 20px !important; 
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
        transition: all 0.3s ease-in-out !important;
        text-decoration: none !important;
        display: inline-flex !important;
        width: auto !important;
        max-width: 320px !important; 
    }
    .stLinkButton > a p {
        font-size: 16px !important; 
        font-weight: bold !important;
        color: #FFFFFF !important;
        letter-spacing: 0.5px !important;
    }
    .stLinkButton > a:hover {
        background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%) !important;
        box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4) !important;
        transform: translateY(-1px) !important;
    }
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

col_btn, col_title = st.columns([1.2, 2.8])
with col_btn:
    st.link_button("🏠 ke Menu Utama", "https://forio.com/app/univ_sumaterautara/research-ptpn", use_container_width=False)
with col_title:
    st.markdown('<p class="custom-title">Model Analisis Ketahanan Energi & Pangan (Live Animasi Akumulatif Lengkap)</p>', unsafe_allow_html=True)

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
# 5. DATA KOORDINAT KOTAK INDIVIDUAL
# ==============================================================================
# KELOMPOK 1 (Fase 1)
box_kapasitas_kilang = {'label': 'Kapasitas Kilang', 'shape_type': 'rect', 'tank_area': [363, 137, 466, 208]}
box_lahan_sawit_tm   = {'label': 'Lahan Sawit Produktif TM', 'shape_type': 'rect', 'tank_area': [121, 433, 231, 511]}

# KELOMPOK 2 (Fase 2)
box_produksi_bbm     = {'label': 'Produksi BBM', 'shape_type': 'rect', 'tank_area': [631, 84, 723, 143]}
box_pks              = {'label': 'Pabrik Kelapa Sawit PKS', 'shape_type': 'rect', 'tank_area': [396, 548, 518, 625]}

# KELOMPOK 3 (Fase 3)
box_palm_kernel      = {'label': 'Palm Kernel', 'shape_type': 'rect', 'tank_area': [357, 412, 468, 454]}
box_hasil_cpo        = {'label': 'Hasil CPO', 'shape_type': 'rect', 'tank_area': [664, 515, 760, 560]}
box_kebutuhan_bbm    = {'label': 'Kebutuhan BBM', 'shape_type': 'rect', 'tank_area': [833, 110, 942, 175]}

# KELOMPOK 4 (Fase 4)
box_refinery_cpo     = {'label': 'Ketersediaan BioSolar Nasional', 'shape_type': 'rect', 'tank_area': [1091, 126, 1209, 197]}
box_rbdpo            = {'label': 'Refinery CPO', 'shape_type': 'rect', 'tank_area': [837, 567, 930, 626]}

# KELOMPOK 5 (Fase 5)
box_olein            = {'label': 'RBDPO', 'shape_type': 'rect', 'tank_area': [1047, 555, 1137, 601]}
box_biosolar         = {'label': 'Produk Samping PFAD', 'shape_type': 'rect', 'tank_area': [870, 409, 1002, 464]}

# KELOMPOK 6 (Fase 6)
box_prod_biodiesel   = {'label': 'Produksi Biodiesel', 'shape_type': 'rect', 'tank_area': [1124, 390, 1208, 451]}
box_gap_energi       = {'label': 'Olein (Minyak Goreng)', 'shape_type': 'rect', 'tank_area': [1264, 493, 1396, 553]}

# KELOMPOK 7 (Fase 7)
box_avail_migor      = {'label': 'Ketersediaan BioSolar Nasional', 'shape_type': 'rect', 'tank_area': [1228, 251, 1396, 310]}
box_gap_pangan       = {'label': 'Ketersediaan Minyak Goreng Nasional ', 'shape_type': 'rect', 'tank_area': [1485, 492, 1610, 579]}

# KELOMPOK 8 (Fase 8 - Kotak Indikator GAP Deteksi Otomatis Menjadi Belah Ketupat)
box_impor_bbm        = {'label': 'GAP Ketahanan Energi?', 'shape_type': 'rect', 'tank_area': [1399,81,1502,183]}
box_impor_crude      = {'label': 'GAP Ketahanan Pangan?', 'shape_type': 'rect', 'tank_area': [1582,323,1677,417]}

# ==============================================================================
# 5B. STRUKTUR FASE ANIMASI AKUMULATIF (Kotak Sebelumnya Tetap Bertahan)
# ==============================================================================
process_phases = [
    # FASE 1: Muncul 2 Kotak Awal
    [box_kapasitas_kilang, box_lahan_sawit_tm],
    
    # FASE 2: + 2 Kotak Baru
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks],
    
    # FASE 3: + 3 Kotak Baru
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks, 
     box_palm_kernel, box_hasil_cpo, box_kebutuhan_bbm],
    
    # FASE 4: + 2 Kotak Lagi
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks, 
     box_palm_kernel, box_hasil_cpo, box_kebutuhan_bbm, 
     box_refinery_cpo, box_rbdpo],
     
    # FASE 5: + 2 Kotak Lagi
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks, 
     box_palm_kernel, box_hasil_cpo, box_kebutuhan_bbm, 
     box_refinery_cpo, box_rbdpo, 
     box_olein, box_biosolar],

    # FASE 6: + 2 Kotak Lagi
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks, 
     box_palm_kernel, box_hasil_cpo, box_kebutuhan_bbm, 
     box_refinery_cpo, box_rbdpo, 
     box_olein, box_biosolar,
     box_prod_biodiesel, box_gap_energi],

    # FASE 7: + 2 Kotak Lagi
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks, 
     box_palm_kernel, box_hasil_cpo, box_kebutuhan_bbm, 
     box_refinery_cpo, box_rbdpo, 
     box_olein, box_biosolar,
     box_prod_biodiesel, box_gap_energi,
     box_avail_migor, box_gap_pangan],

    # FASE 8: + 2 Kotak Akhir (GAP Ketahanan Energi & GAP Ketahanan Pangan)
    [box_kapasitas_kilang, box_lahan_sawit_tm, box_produksi_bbm, box_pks, 
     box_palm_kernel, box_hasil_cpo, box_kebutuhan_bbm, 
     box_refinery_cpo, box_rbdpo, 
     box_olein, box_biosolar,
     box_prod_biodiesel, box_gap_energi,
     box_avail_migor, box_gap_pangan,
     box_impor_bbm, box_impor_crude]
]

# ==============================================================================
# 6. LOOPING RENDERING (DENGAN GEOMETRI BELAH KETUPAT)
# ==============================================================================
placeholder = st.empty()
render_count = 0

while True:
    for phase in process_phases:
        fig = px.imshow(img)
        
        # Menonaktifkan Grid dan Sumbu Koordinat
        fig.update_xaxes(visible=False, showgrid=False)
        fig.update_yaxes(visible=False, showgrid=False)
        
        for component in phase:
            area = component['tank_area']
            
            # CEK OTOMATIS: Jika label memiliki kata "GAP", render menjadi bentuk Belah Ketupat
            if "GAP" in component['label']:
                x_mid = (area[0] + area[2]) / 2
                y_mid = (area[1] + area[3]) / 2
                
                fig.add_shape(
                    type="path",
                    # Alur Garis: Atas -> Kanan -> Bawah -> Kiri -> Selesai (Z)
                    path=f"M {x_mid},{area[1]} L {area[2]},{y_mid} L {x_mid},{area[3]} L {area[0]},{y_mid} Z",
                    fillcolor="rgba(255, 0, 0, 0.35)",
                    line=dict(color="Red", width=3),
                )
            else:
                # Bentuk Kotak Standar untuk komponen non-GAP
                shape = component.get('shape_type', 'rect')
                fig.add_shape(
                    type=shape, 
                    x0=area[0], y0=area[1], x1=area[2], y1=area[3],
                    fillcolor="rgba(255, 0, 0, 0.35)",
                    line=dict(color="Red", width=3),
                )
            
            # 2. Koordinat Label Teks Dinamis
            text_x = (area[0] + area[2]) / 2
            text_y = area[3] + 25             
            
            # 3. Render Teks Label di Bawah Elemen Penanda
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
                key=f"cld_accumulated_mode_{render_count}"
            )
        
        render_count += 1
        time.sleep(3.5)  # Jeda waktu transisi animasi antar fase
