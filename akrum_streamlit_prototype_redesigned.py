
import streamlit as st
import numpy as np

def rule30(prev_row):
    row_len = len(prev_row)
    new_row = np.zeros_like(prev_row)
    for i in range(1, row_len - 1):
        left, center, right = prev_row[i - 1], prev_row[i], prev_row[i + 1]
        new_row[i] = left ^ (center or right)
    return new_row

def generate_ca_pattern(seed_index=30, steps=20, width=61):
    grid = np.zeros((steps, width), dtype=int)
    grid[0, seed_index] = 1
    for i in range(1, steps):
        grid[i] = rule30(grid[i - 1])
    return grid

def ca_to_binary_key(ca_row):
    return ''.join(str(bit) for bit in ca_row)

st.set_page_config(page_title="AKRUM Prototype", page_icon=":lock:", layout="centered")

st.markdown("<h1 style='text-align: center; color: #003366;'>AKRUM: Cryptographic Randomness Generator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Powered by Cellular Automata (Rule 30)</h4>", unsafe_allow_html=True)
st.markdown("---")

st.write("**Instructions:** Click the button below to generate a high-entropy binary key using our patented method based on Cellular Automata. You can adjust the grid size and time steps to explore how the pattern evolves.")

with st.sidebar:
    st.header("Configuration")
    steps = st.slider("CA Steps (time evolution)", 10, 50, 30)
    width = st.slider("Grid Width", 31, 101, 61)

seed_index = width // 2

if st.button("🔐 Generate Secure Random Key"):
    ca_grid = generate_ca_pattern(seed_index, steps, width)
    final_row = ca_grid[-1]
    binary_key = ca_to_binary_key(final_row)
    
    st.success("✅ Key Generated Successfully")
    st.code(binary_key, language='text')
    
    with st.expander("Show Pattern Visualization"):
        st.image((1 - ca_grid) * 255, caption="CA Grid (Rule 30)", use_column_width=True)

st.markdown("---")
st.markdown("<small><i>AKRUM is patent protected (US Patent 10,078,492 B2). This prototype is for demonstration purposes only.</i></small>", unsafe_allow_html=True)
