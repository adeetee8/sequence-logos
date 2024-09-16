import streamlit as st
from weblogo import LogoOptions, LogoData, logomaker

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
        # Create the sequence logo if sequences are provided
        data = LogoData.from_seqs(sequences)
        logo = logomaker.Logo(data)

        # Display the sequence logo
        st.pyplot(logo.fig)  # Display the logo in the web interface
    else:
        st.error("No valid sequences found. Please enter valid sequences.")
else:
    st.info("Please enter sequences to generate a logo.")
