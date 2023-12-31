import pandas as pd
import spacy
import os 


nlp = spacy.load("en_core_web_sm")

def calculate_lexical_density(text):
    """
    Calculate lexical density as the percentage of functional words in the text.

    Parameters:
    - text: str, the input text for analysis

    Returns:
    - lexical_density: float, the calculated lexical density percentage

    Interpretation of results:
    A lower percentage of lexical density will mean a lower presence of functional words,
    a classic symptom of aphasic speech.
    """
    # Check if the text is a valid string, if not, return 0.0
    if isinstance(text, str):
        # Process the text using SpaCy
        doc = nlp(text)

        # Filter functional words based on part-of-speech (PoS) tagging
        functional_words = [token.text.lower() for token in doc if token.pos_ in {'ADP', 'AUX', 'CONJ', 'DET', 'PRON', 'SCONJ'}]

        # Calculate lexical density percentage
        total_words = len(doc)
        functional_words_count = len(functional_words)

        if total_words == 0:
            return 0.0

        lexical_density = (functional_words_count / total_words) * 100
        return lexical_density
    else:
        return 0.0

def process_csv_files(source_directory, destination_directory):
    """
    Process all CSV files in the specified source directory and its subdirectories,
    and save the processed files to the specified destination directory.

    This function reads each CSV file, calculates the lexical density for each text entry,
    and saves the result in a new CSV file in the destination directory, adding a column for lexical density.

    The new CSV files will maintain the same directory structure as the source.

    Parameters:
    - source_directory (str): The root directory containing the original CSV files.
    - destination_directory (str): The root directory where processed CSV files will be saved.

    Processed files will be stored in the destination directory with a structure mirroring that of the source.
    Each row in the processed files will contain the original columns, plus a 'lexical_density' column.
    """
    for subdir, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(subdir, file)
                df = pd.read_csv(file_path)

                # Apply the lexical density calculation to the 'text' column
                df['lexical_density'] = df['text'].apply(calculate_lexical_density)

                # Construct the new file path in the destination directory
                relative_path = os.path.relpath(subdir, source_directory)
                new_dir = os.path.join(destination_directory, relative_path)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                new_file_path = os.path.join(new_dir, f"processed_{file}")
                df.to_csv(new_file_path, index=False)

# Example usage
process_csv_files('New_clean_code\Data\Tagged_diagnosis_data_csv', 'New_clean_code\Data\Tagged_full_data')