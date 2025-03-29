import streamlit as st
import pandas as pd
import os

# file to store books
data_file = "books.csv"

# display existing data
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=["Title", "Author", "Genre", "Year"])

st.title("📚 Personal Library Manager")

# Sidebar for Add a new book
st.sidebar.header("Add a New Book")
title = st.sidebar.text_input("Book Title")
author = st.sidebar.text_input("Author")
genre = st.sidebar.text_input("Genre")
year = st.sidebar.number_input("Year", min_value=0, max_value=2100, step=1)

if st.sidebar.button("Add Book"):
    if title and author:
        new_book = pd.DataFrame({"Title": [title], "Author": [author], "Genre": [genre], "Year": [year]})
        df = pd.concat([df, new_book], ignore_index=True)
        df.to_csv(data_file, index=False)
        st.sidebar.success("Book added successfully!")
    else:
        st.sidebar.error("Please enter at least Title and Author")

# for display books
st.subheader("📖 Your Library")
if df.empty:
    st.info("No books added yet. Add some from the sidebar!")
else:
    st.dataframe(df)

    # for delete book
    st.subheader("🗑️ Remove a Book")
    book_to_delete = st.selectbox("Select a book to delete", df["Title"].tolist())
    if st.button("Delete Book"):
        df = df[df.Title != book_to_delete]
        df.to_csv(data_file, index=False)
        st.success(f'Book "{book_to_delete}" deleted successfully!')
        st.rerun()
