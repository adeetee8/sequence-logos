import streamlit as st
import logomaker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Sequence Logo Generator")

# User input: multiline text area for sequences
user_input = st.text_area(
    "Enter sequences (one per line):",
    help="Each sequence should be on a new line."
)

# Process user input into list of sequences
if user_input:
    sequences = user_input.splitlines()  # Split by line to get sequences
    sequences = [seq.strip() for seq in sequences if seq.strip()]  # Clean and ignore empty lines

    if sequences:
        # Create a pandas DataFrame with the count matrix
        counts_mat = np.zeros((len(sequences[0]), 4))  # Assuming A, C, G, T sequences
        
        for seq in sequences:
            for idx, nt in enumerate(seq):
                if nt == 'A':
                    counts_mat[idx, 0] += 1
                elif nt == 'C':
                    counts_mat[idx, 1] += 1
                elif nt == 'G':
                    counts_mat[idx, 2] += 1
                elif nt == 'T':
                    counts_mat[idx, 3] += 1

        # Create a pandas DataFrame for logomaker
        df = pd.DataFrame(counts_mat, columns=['A', 'C', 'G', 'T'])
        
        # Generate and display the sequence logo
        fig, ax = plt.subplots()
        logomaker.Logo(df, ax=ax)
        ax.set_xlabel("Position")
        ax.set_ylabel("Frequency")

        st.pyplot(fig)  # Display the logo in the web interface
    else:
        st.error("No valid sequences found. Please enter valid sequences.")
else:
    st.info("Please enter sequences to generate a logo.")
