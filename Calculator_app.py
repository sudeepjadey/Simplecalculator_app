import streamlit as st
import math

st.set_page_config(page_title="Advanced Real-Time Calculator", layout="centered")
st.title("Advanced Real-Time Calculator")

# Initialize history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Input fields
num1 = st.number_input("Enter the first number", key="num1")
operation = st.selectbox("Choose operation", [
    "Addition", "Subtraction", "Multiplication", "Division",
    "Power", "Square Root", "Sine", "Cosine", "Tangent", "Log"
])

# For operations that require two inputs
if operation not in ["Square Root", "Sine", "Cosine", "Tangent", "Log"]:
    num2 = st.number_input("Enter the second number", key="num2")
else:
    num2 = None

# Compute result
result = None
error = None

try:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Power":
        result = math.pow(num1, num2)
    elif operation == "Square Root":
        result = math.sqrt(num1) if num1 >= 0 else "Error: Negative root"
    elif operation == "Sine":
        result = math.sin(math.radians(num1))
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
    elif operation == "Log":
        result = math.log10(num1) if num1 > 0 else "Error: Log of non-positive number"
except Exception as e:
    error = f"Error: {e}"

# Display result
st.subheader("Result:")
if error:
    st.error(error)
else:
    st.success(result)
    # Save to history
    st.session_state.history.append(f"{operation}: {num1} {'and ' + str(num2) if num2 is not None else ''} = {result}")

# Show history
with st.expander("Calculator History"):
    if st.session_state.history:
        for entry in st.session_state.history[::-1]:
            st.write(entry)
    else:
        st.write("No history yet.")
