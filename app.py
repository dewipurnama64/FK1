import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Fungsi untuk format angka (bulat tanpa desimal, desimal dengan 2 angka di belakang koma)
def format_angka(x):
    if x == int(x):  
        return str(int(x))  # Jika bilangan bulat, tampilkan tanpa desimal
    return f"{x:.2f}"  # Jika desimal, tampilkan dengan 2 angka di belakang koma

# Fungsi untuk membentuk persamaan kuadrat dengan format yang benar
def format_persamaan(a, b, c):
    persamaan = f"f(x) = {format_angka(a)}x²"

    if b != 0:
        if b > 0:
            persamaan += f" + {format_angka(b)}x"
        else:
            persamaan += f" - {format_angka(abs(b))}x"

    if c != 0:
        if c > 0:
            persamaan += f" + {format_angka(c)}"
        else:
            persamaan += f" - {format_angka(abs(c))}"

    return persamaan

# Fungsi menghitung diskriminan
def hitung_diskriminan(a, b, c):
    return b**2 - 4*a*c

# Fungsi mengecek apakah definit positif atau negatif
def cek_definit(D, a):
    if D < 0:
        return "Definit positif" if a > 0 else "Definit negatif"
    return "Bukan definit positif maupun definit negatif"

# Fungsi mencari akar persamaan kuadrat
def cari_akar(a, b, c):
    D = hitung_diskriminan(a, b, c)
    
    if D > 0:  # Akar real berbeda
        akar1 = sp.N((-b + sp.sqrt(D)) / (2*a))  # Hitung dalam bentuk numerik
        akar2 = sp.N((-b - sp.sqrt(D)) / (2*a))
        return f"x₁ = {format_angka(akar1)}, x₂ = {format_angka(akar2)}"
    
    elif D == 0:  # Akar kembar
        akar = sp.N(-b / (2*a))
        return f"x = {format_angka(akar)} (Akar kembar)"
    
    else:  # Akar kompleks
        real_part = sp.N(-b / (2*a))
        imag_part = sp.N(sp.sqrt(-D) / (2*a))
        return f"x₁ = {format_angka(real_part)} + {format_angka(imag_part)}i, x₂ = {format_angka(real_part)} - {format_angka(imag_part)}i"

# Fungsi mencari titik puncak
def cari_titik_puncak(a, b, c):
    x_p = sp.N(-b / (2*a))
    y_p = sp.N(-hitung_diskriminan(a, b, c) / (4*a))
    return x_p, y_p

# UI di Streamlit
st.title("📐 Kalkulator Fungsi Kuadrat")

st.markdown("### Masukkan nilai a, b, dan c dari persamaan kuadrat:")
st.latex("ax^2 + bx + c = 0")

a = st.number_input("Masukkan nilai a", value=1.0, format="%.2f")
b = st.number_input("Masukkan nilai b", value=0.0, format="%.2f")
c = st.number_input("Masukkan nilai c", value=0.0, format="%.2f")

if st.button("🔍 Hitung"):
    if a == 0:
        st.error("Nilai a tidak boleh 0! Persamaan ini bukan fungsi kuadrat.")
    else:
        D = hitung_diskriminan(a, b, c)
        definit = cek_definit(D, a)
        akar = cari_akar(a, b, c)
        x_p, y_p = cari_titik_puncak(a, b, c)
        
        st.subheader("📊 Hasil Perhitungan")
        st.markdown(f"#### **Persamaan Kuadrat:**")
        st.latex(format_persamaan(a, b, c))  # Menampilkan persamaan kuadrat
        
        st.write(f"📌 **Diskriminan (D):** {D}")
        st.write(f"📌 **Definit:** {definit}")  
        st.write(f"📌 **Akar-akar persamaan:** {akar}")

        st.markdown("### Titik Puncak (Nilai Optimum):")
        st.latex(f"x_p = \\frac{{-({format_angka(b)})}}{{2({format_angka(a)})}} = {format_angka(x_p)}")
        st.latex(f"y_p = \\frac{{-({format_angka(D)})}}{{4({format_angka(a)})}} = {format_angka(y_p)}")

        # Menampilkan grafik fungsi kuadrat
        x_range = max(abs(int(x_p)) + 5, 10)  # Menyesuaikan range x agar grafik lebih proporsional
        x = np.linspace(-x_range, x_range, 400)
        y = a*x**2 + b*x + c

        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"{format_persamaan(a, b, c)}")
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.scatter([float(x_p)], [float(y_p)], color="red", zorder=5, label="Titik Puncak")
        ax.grid()
        ax.legend()

        st.pyplot(fig)
