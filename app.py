import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction  # Untuk menampilkan pecahan

# Fungsi Matematika
def hitung_diskriminan(a, b, c):
    return b**2 - 4*a*c

def cek_definit(D, a):
    if D < 0:
        if a > 0:
            return "Definit positif"
        elif a < 0:
            return "Definit negatif"
    return "Bukan definit positif maupun definit negatif"

def format_pecahan(nilai):
    """Mengubah nilai menjadi pecahan jika memungkinkan"""
    pecahan = Fraction(nilai).limit_denominator()
    return str(pecahan) if pecahan.denominator != 1 else str(pecahan.numerator)

def cari_akar(a, b, c):
    D = hitung_diskriminan(a, b, c)
    
    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        return f"Akar real: x₁ = {format_pecahan(x1)}, x₂ = {format_pecahan(x2)}"
    
    elif D == 0:
        x = -b / (2*a)
        return f"Akar kembar: x = {format_pecahan(x)}"
    
    else:
        real_part = -b / (2*a)
        imag_part = np.sqrt(-D) / (2*a)
        return f"Akar kompleks: x₁ = {format_pecahan(real_part)} + √{format_pecahan(-D)}/{2*a}, x₂ = {format_pecahan(real_part)} - √{format_pecahan(-D)}/{2*a}"

# UI di Streamlit
st.title("📐 Kalkulator Fungsi Kuadrat")
st.markdown("#### Masukkan nilai a, b, dan c dari persamaan kuadrat:")
st.markdown("#### $ax^2 + bx + c = 0$")

# Input pengguna
a = st.number_input("Masukkan nilai a", value=1.0, format="%.2f")
b = st.number_input("Masukkan nilai b", value=0.0, format="%.2f")
c = st.number_input("Masukkan nilai c", value=0.0, format="%.2f")

# Tombol Hitung
if st.button("🔍 Hitung"):
    # Hitung nilai diskriminan
    D = hitung_diskriminan(a, b, c)
    definit = cek_definit(D, a)  
    akar = cari_akar(a, b, c)

    # Hitung titik puncak (nilai optimum)
    if a != 0:
        x_p = -b / (2 * a)
        y_p = -D / (4 * a)
    else:
        x_p, y_p = None, None  # Jika a = 0, tidak ada titik puncak

    # Menampilkan hasil
    st.subheader("📊 Hasil Perhitungan")
    st.write(f"📌 **Diskriminan:** {D}")
    st.write(f"📌 **Definit:** {definit}")  
    st.write(f"📌 **Akar:** {akar}")

    # Menampilkan langkah penyelesaian akar
    st.markdown("### 📜 Cara Pengerjaan Akar:")
    st.markdown(f"$ x_{{1,2}} = \\frac{{-({b}) \\pm \\sqrt{{{D}}}}}{{2({a})}} $")
    
    # Menampilkan titik puncak hanya jika a ≠ 0
    if a != 0:
        st.markdown("### 🎯 Titik Puncak (Nilai Optimum):")
        st.markdown(f"$ x_p = \\frac{{-({b})}}{{2({a})}} = {format_pecahan(x_p)} $")
        st.markdown(f"$ y_p = \\frac{{-({D})}}{{4({a})}} = {format_pecahan(y_p)} $")

    # Menampilkan grafik fungsi kuadrat hanya jika a ≠ 0
    if a != 0:
        # Menentukan rentang x sekitar titik puncak
        x_min = x_p - 10 if x_p is not None else -10
        x_max = x_p + 10 if x_p is not None else 10
        x = np.linspace(x_min, x_max, 400)
        y = a*x**2 + b*x + c

        # Menentukan rentang y agar grafik proporsional
        y_min, y_max = min(y), max(y)
        margin = (y_max - y_min) * 0.1  # Tambahkan sedikit margin
        y_min -= margin
        y_max += margin

        # Plot grafik
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"${a}x^2 + {b}x + {c}$", color="blue")
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)

        # Plot titik puncak
        ax.scatter(x_p, y_p, color='red', zorder=3, label="Titik Puncak")

        # Menyesuaikan skala
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        ax.grid()
        ax.legend()

        st.pyplot(fig)
    else:
        st.warning("Grafik tidak bisa ditampilkan karena bukan fungsi kuadrat (a = 0).")
