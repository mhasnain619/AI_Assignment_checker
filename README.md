Code Analyzer
A Streamlit-based application to analyze Python (.py) and Jupyter Notebook (.ipynb) files using CodeBERT and Pylint.
Project Structure

app.py: Main Streamlit application.
models/codebert.py: CodeBERT model loading and analysis logic.
utils/code_utils.py: Pylint and Jupyter Notebook extraction utilities.
static/uploads/: Folder for uploaded files.
requirements.txt: Project dependencies.

Setup Instructions

Clone or Set Up the Project:

Create a project folder named code_analyzer.
Place the files in the structure described above.


Install Dependencies:

Ensure Python 3.8+ is installed.
Run:pip install -r requirements.txt




Run the Application:

Navigate to the code_analyzer directory.
Run:streamlit run app.py


Open the provided URL (usually http://localhost:8501) in your browser.


Usage:

Upload a .py or .ipynb file via the Streamlit UI.
View the analysis report with CodeBERT and Pylint feedback.



Notes

Ensure the static/uploads folder is created automatically or manually before running.
If using a GPU, CodeBERT will utilize CUDA if available.
Check logs in the terminal for debugging information.

Troubleshooting

Module Not Found: Verify all dependencies are installed (pip install -r requirements.txt).
File Upload Issues: Ensure files are valid .py or .ipynb.
CodeBERT Errors: Check internet connection for model downloading or GPU compatibility.
