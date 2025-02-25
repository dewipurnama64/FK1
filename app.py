import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import sympy as sp

# Fungsi Matematika
def hitung_diskriminan(a, b, c):
    return b**2 - 4*a*c

def cek_definit(D, a):
    if D < 0:
        return "Definit positif" if a > 0 else "Definit negatif"
    return "Bukan definit positif maupun definit negatif"

def cari_akar(a, b, c):
    D = hitung_diskriminan(a, b, c)
    if D > 0:
        x1 = f"(-{b} + √{D}) / (2 * {a})"
        x2 = f"(-{b} - √{D}) / (2 * {a})"
        return f"Akar real: x₁ = {x1}, x₂ = {x2}"
    elif D == 0:
        x = Fraction(-b, 2*a)
        return f"Akar kembar: x = {x}"
    else:
        real_part = Fraction(-b, 2*a)
        imag_part = f"√{-D} / (2 * {a})"
        return f"Akar kompleks: x₁ = {real_part} + {imag_part} i, x₂ = {real_part} - {imag_part} i"
        
# UI di Streamlit
st.title("📐 Kalkulator Fungsi Kuadrat")
st.markdown("#### Masukkan nilai a, b, dan c dari persamaan kuadrat:")
st.latex(r"f(x) = ax^2 + bx + c")

a = st.number_input("Masukkan nilai a", value=1.0, format="%.2f")
b = st.number_input("Masukkan nilai b", value=0.0, format="%.2f")
c = st.number_input("Masukkan nilai c", value=0.0, format="%.2f")

if st.button("🔍 Hitung"):
    D = hitung_diskriminan(a, b, c)
    definit = cek_definit(D, a)
    akar = cari_akar(a, b, c)
    
    st.subheader("📊 Hasil Perhitungan")
    
    # Menampilkan persamaan kuadrat lengkap
    st.markdown("### 📌 Persamaan Kuadrat:")
    st.latex(f"f(x) = {a}x^2 + {b}x + {c}")
    
    # Diskriminan dan definit
    st.write(f"📌 **Diskriminan:** {D}")
    st.write(f"📌 **Definit:** {definit}")
    st.write(f"📌 **Akar:** {akar}")

    # Titik puncak (nilai optimum)
    if a != 0:
        x_p = -b / (2 * a)
        y_p = -D / (4 * a)

        st.markdown("### Titik Puncak (Nilai Optimum):")
        st.latex(r"x_p = \frac{-b}{2a} = " + f"\\frac{{-({b})}}{{2({a})}} = {x_p:.2f}")
        st.latex(r"y_p = \frac{-D}{4a} = " + f"\\frac{{-({D})}}{{4({a})}} = {y_p:.2f}")

        # Perbaikan skala grafik
        x_min = x_p - 5
        x_max = x_p + 5
        x = np.linspace(x_min, x_max, 400)
        y = a*x**2 + b*x + c

        y_min, y_max = min(y), max(y)
        margin = (y_max - y_min) * 0.1
        y_min -= margin
        y_max += margin

        # Plot grafik
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"${a}x^2 + {b}x + {c}$", color="blue")
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        
        # Menandai titik puncak
        ax.scatter(x_p, y_p, color='red', zorder=3, label=f"Titik Puncak ({x_p:.2f}, {y_p:.2f})")

        # Menyesuaikan skala
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        ax.grid()
        ax.legend()

        st.pyplot(fig)
