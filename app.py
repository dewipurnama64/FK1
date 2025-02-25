import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
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
    sqrt_D = sp.sqrt(D)

    if D > 0:
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
    elif D == 0:
        x1 = x2 = -b / (2*a)
    else:
        real_part = -b / (2*a)
        imag_part = sp.sqrt(-D) / (2*a)
        return f"{real_part:.2f} + {imag_part:.2f}i", f"{real_part:.2f} - {imag_part:.2f}i"

    return x1, x2

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
    akar1, akar2 = cari_akar(a, b, c)

    st.subheader("📊 Hasil Perhitungan")

    # Menampilkan persamaan kuadrat lengkap
    st.markdown("### 📌 Persamaan Kuadrat:")
    st.latex(f"f(x) = {a}x^2 + {b}x + {c}")

    # Diskriminan dan definit
    st.write(f"📌 **Diskriminan:** {D}")
    st.write(f"📌 **Definit:** {definit}")

    # Menampilkan cara pengerjaan akar
    st.markdown("### 📌 Cara Menghitung Akar-Akar:")
    st.latex(r"x_{1,2} = \frac{-b \pm \sqrt{D}}{2a}")
    st.latex(fr"x_{{1,2}} = \frac{{-({b}) \pm \sqrt{{{D}}}}}{{2({a})}}")
    
    if D >= 0:
        x1, x2 = akar1, akar2
        st.latex(fr"x_1 = \frac{{-({b}) + \sqrt{{{D}}}}}{{2({a})}} = {x1:.2f}")
        st.latex(fr"x_2 = \frac{{-({b}) - \sqrt{{{D}}}}}{{2({a})}} = {x2:.2f}")
        st.write(f"**Akar-akar persamaan:** x₁ = {x1:.2f}, x₂ = {x2:.2f}")
    else:
        st.write(f"**Akar-akar kompleks:** x₁ = {akar1}, x₂ = {akar2}")

    # Titik puncak (nilai optimum)
    if a != 0:
        x_p = -b / (2 * a)
        y_p = -D / (4 * a)

        st.markdown("### Titik Puncak (Nilai Optimum):")
        st.latex(r"x_p = \frac{-b}{2a} = " + f"\\frac{{-({b})}}{{2({a})}} = {x_p:.2f}")
        st.latex(r"y_p = \frac{-D}{4a} = " + f"\\frac{{-({D})}}{{4({a})}} = {y_p:.2f}")

        # Perbaikan skala grafik agar lebih sesuai
        x_min = x_p - 5
        x_max = x_p + 5
        x = np.linspace(x_min, x_max, 400)
        y = a*x**2 + b*x + c

        y_min, y_max = min(y), max(y)
        margin = (y_max - y_min) * 0.2
        y_min -= margin
        y_max += margin

        # Plot grafik
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"${a}x^2 + {b}x + {c}$", color="blue")
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        
        # Menandai titik puncak
        ax.scatter(float(x_p), float(y_p), color='red', zorder=3, label=f"Titik Puncak ({x_p:.2f}, {y_p:.2f})")

        # Menyesuaikan skala
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        ax.grid()
        ax.legend()

        st.pyplot(fig)
