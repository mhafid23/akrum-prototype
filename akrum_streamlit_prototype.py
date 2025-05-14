
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

st.title("AKRUM Prototype: Cryptographic Randomness Generator")
st.write("This prototype demonstrates how AKRUM generates randomness using Cellular Automata (Rule 30).")

steps = st.slider("Number of CA steps (time evolution)", min_value=10, max_value=50, value=30)
width = st.slider("Width of the CA grid", min_value=31, max_value=101, value=61)
seed_index = width // 2

if st.button("Generate Random Key"):
    ca_grid = generate_ca_pattern(seed_index, steps, width)
    final_row = ca_grid[-1]
    binary_key = ca_to_binary_key(final_row)
    st.code(binary_key, language='text')
    st.success("Random Key Generated Successfully!")
    st.write("Final Cellular Automata Pattern:")
    st.image((1 - ca_grid) * 255, caption="CA Grid (Rule 30)", use_column_width=True)
