import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
    
def cari_akar(a, b, c):
    D = hitung_diskriminan(a, b, c)
    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        return f"Akar real: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2*a)
        return f"Akar kembar: x = {x}"
    else:
        real_part = -b / (2*a)
        imag_part = np.sqrt(-D) / (2*a)
        return f"Akar kompleks: x1 = {real_part} + {imag_part}i, x2 = {real_part} - {imag_part}i"

# Menghitung titik puncak
if a != 0:
    x_p = -b / (2 * a)
    y_p = -D / (4 * a)

# UI di Streamlit
st.title("📐 Kalkulator Fungsi Kuadrat")
st.markdown("#### Masukkan nilai a, b, dan c dari persamaan kuadrat:")
st.markdown("#### $ax^2 + bx + c = 0$")

a = st.number_input("Masukkan nilai a", value=1.0, format="%.2f")
b = st.number_input("Masukkan nilai b", value=0.0, format="%.2f")
c = st.number_input("Masukkan nilai c", value=0.0, format="%.2f")

if st.button("🔍 Hitung"):
    D = hitung_diskriminan(a, b, c)
    definit = cek_definit(D, a)  
    akar = cari_akar(a, b, c)
    
    st.subheader("📊 Hasil Perhitungan")
    st.write(f"📌 **Diskriminan:** {D}")
    st.write(f"📌 **Definit:** {definit}")  
    st.write(f"📌 **Akar:** {akar}")
    st.markdown("### Titik Puncak (Nilai Optimum):")
    st.markdown(f"$ x_p = \\frac{{-({b})}}{{2({a})}} = {x_p:.2f} $")
    st.markdown(f"$ y_p = \\frac{{-({D})}}{{4({a})}} = {y_p:.2f} $")

    # Menampilkan grafik fungsi kuadrat
    x = np.linspace(-10, 10, 100)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"{a}x² + {b}x + {c}")
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid()
    ax.legend()

    st.pyplot(fig)
  
