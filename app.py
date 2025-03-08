import streamlit as st

# Set the title of the app
st.title("Word and Character Counter")

# Create a larger text area with a fixed height (in pixels) so that a scrollbar appears for overflow
paragraph = st.text_area("Enter your paragraph below:", height=300)

# Add a button that triggers the counting process
if st.button("Count"):
    # Split the paragraph into words based on whitespace and count them
    words = paragraph.split()
    word_count = len(words)
    
    # Count the characters in the paragraph (including spaces and punctuation)
    char_count = len(paragraph)

    # Display the counts
    st.write("### Results:")
    st.write(f"**Word Count:** {word_count}")
    st.write(f"**Character Count:** {char_count}")
