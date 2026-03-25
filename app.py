import streamlit as st
import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
import qrcode
import io

st.title("✨ SMART CALCULATOR 2.0 👑✨")

# -------------------------
# ARITHMETIC & SCIENTIFIC FUNCTIONS
# -------------------------

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    try: return a / b
    except ZeroDivisionError: return "Error: Cannot divide by zero!"

def modulus(a, b): return a % b
def power(a, b): return a ** b
def square(x): return x ** 2
def square_root(x): return math.sqrt(x)

def logarithm(x, base=10): return math.log(x, base)
def natural_log(x): return math.log(x)

def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))
def tangent(x): return math.tan(math.radians(x))
def exponential(x): return math.exp(x)
def factorial(x): return math.factorial(int(x))

# -------------------------
# STATISTICS FUNCTIONS
# -------------------------

def calculate_statistics(data):
    stats = {}
    stats["Mean"] = statistics.mean(data)
    stats["Median"] = statistics.median(data)

    try:
        stats["Mode"] = statistics.mode(data)
    except:
        stats["Mode"] = "No unique mode"

    stats["Variance"] = statistics.variance(data)
    stats["Std Dev"] = statistics.stdev(data)
    stats["Minimum"] = min(data)
    stats["Maximum"] = max(data)
    stats["Range"] = max(data) - min(data)
    stats["Sum"] = sum(data)
    stats["Count"] = len(data)

    stats["Q1"] = np.percentile(data, 25)
    stats["Q2"] = np.percentile(data, 50)
    stats["Q3"] = np.percentile(data, 75)
    stats["IQR"] = stats["Q3"] - stats["Q1"]

    return stats

# -------------------------
# GRAPH FUNCTION
# -------------------------

def plot_graph(data, graph_type):
    plt.figure()

    if graph_type == "line":
        plt.plot(data, marker='o')
        plt.title("Line Graph")

    elif graph_type == "bar":
        plt.bar(range(len(data)), data)
        plt.title("Bar Graph")

    elif graph_type == "pie":
        plt.pie(data, labels=[f"Val {i+1}" for i in range(len(data))], autopct='%1.1f%%')
        plt.title("Pie Chart")

    plt.grid(True)
    st.pyplot(plt)

# -------------------------
# SIDEBAR MENU
# -------------------------

menu = st.sidebar.selectbox("Choose Feature", [
    "About" , "Calculator", "Statistics + Graph", "QR Code Generator"
])

# -------------------------
# CALCULATOR SECTION
# -------------------------

if menu == "Calculator":
    st.header("🧮 Arithmetic & Scientific Calculator")

    operation = st.selectbox("Choose Operation", [
        "Add", "Subtract", "Multiply", "Divide", "Modulus", "Power",
        "Square", "Square Root", "Log", "Natural Log",
        "Sine", "Cosine", "Tangent", "Exponential", "Factorial"
    ])

    if operation in ["Add", "Subtract", "Multiply", "Divide", "Modulus", "Power"]:
        a = st.number_input("Enter first number")
        b = st.number_input("Enter second number")

    else:
        x = st.number_input("Enter the number")

    if st.button("Calculate"):
        if operation == "Add": st.success(add(a, b))
        elif operation == "Subtract": st.success(subtract(a, b))
        elif operation == "Multiply": st.success(multiply(a, b))
        elif operation == "Divide": st.success(divide(a, b))
        elif operation == "Modulus": st.success(modulus(a, b))
        elif operation == "Power": st.success(power(a, b))
        elif operation == "Square": st.success(square(x))
        elif operation == "Square Root": st.success(square_root(x))
        elif operation == "Log": st.success(logarithm(x))
        elif operation == "Natural Log": st.success(natural_log(x))
        elif operation == "Sine": st.success(sine(x))
        elif operation == "Cosine": st.success(cosine(x))
        elif operation == "Tangent": st.success(tangent(x))
        elif operation == "Exponential": st.success(exponential(x))
        elif operation == "Factorial": st.success(factorial(x))

# -------------------------
# STATISTICS + GRAPH SECTION
# -------------------------

elif menu == "Statistics + Graph":
    st.header("📊 Advanced Statistics + Graph")

    data_input = st.text_input("Enter numbers separated by space")

    graph_type = st.selectbox("Choose Graph Type", ["line", "bar", "pie"])

    if st.button("Analyze"):
        try:
            data = list(map(float, data_input.split()))

            stats = calculate_statistics(data)

            st.subheader("📊 Statistics Result")
            for key, value in stats.items():
                st.write(f"{key}: {value}")

            st.subheader("📈 Graph")
            plot_graph(data, graph_type)

        except:
            st.error("Invalid input! Please enter valid numbers.")
#----------------------
#ABOUT
#---------------------
elif menu == "About":
    st.header("About This App 📚")
    st.write("""
    **Smart Calculator 2.0** is an all-in-one tool for both basic arithmetic and advanced statistical analysis. 
    It allows you to perform a wide range of calculations, from simple addition to complex scientific functions, as well as analyze datasets and visualize them with different graph types.
    
    Developed with Streamlit, this app is designed to be user-friendly and accessible for everyone, whether you're a student, professional, or just someone who loves numbers!
    
    **Features:**
    - Basic arithmetic operations (add, subtract, multiply, divide)
    - Scientific functions (trigonometry, logarithms, factorials)
    - Comprehensive statistics (mean, median, mode, variance, etc.)
    - Graphical visualization (line, bar, pie charts)
    
    Feel free to explore and make the most out of this smart calculator! 🚀
    """)

elif menu =="QR Code Generator":
    st.header("📱 QR Code Generator")
    url = "https://Smart-Calculator-2-0.streamlit.app"
    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    st.image(byte_im, caption="Point your phone camera here", width=300)


    
