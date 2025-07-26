from pylint.lint import Run
from pylint.reporters.text import TextReporter
from nbformat import read
import os
from io import StringIO
from scripts.logger import get_logger
from charset_normalizer import detect

logger = get_logger(__name__)

def pylint_check(file_path):
    logger.debug(f"Checking file: {file_path}")
    try:
        # Preprocess file to ensure UTF-8
        with open(file_path, 'rb') as f:
            raw_content = f.read()
        detected = detect(raw_content)
        encoding = detected['encoding']
        if encoding not in ['utf-8', 'ascii']:
            # logger.warning(f"File {file_path} is not UTF-8 (detected {encoding}). Converting to UTF-8.")
            content = raw_content.decode(encoding, errors='replace').encode('utf-8').decode('utf-8')
            temp_file_path = file_path + '.utf8'
            with open(temp_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            file_path = temp_file_path
        
        output = StringIO()
        reporter = TextReporter(output)
        Run([file_path, '--disable=C0114,C0115,W0311,W0703,C0116,R0903,C0303,C0301', '--max-line-length=120'], reporter=reporter, exit=False)
        pylint_output = output.getvalue()
        
        # Clean up temporary file if created
        if file_path.endswith('.utf8'):
            try:
                os.unlink(file_path)
            except Exception as e:
                logger.warning(f"Failed to delete temporary file {file_path}: {e}")
                
        return pylint_output if pylint_output.strip() else "No critical issues found. Code looks good!"
    except Exception as e:
        logger.error(f"Pylint error: {e}")
        return f"Pylint error: {str(e)}"

def extract_code_from_ipynb(file_path):
    logger.debug(f"Extracting code from: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            notebook = read(file, as_version=4)
        code = ""
        for cell in notebook.cells:
            if cell.cell_type == 'code':
                source = ''.join(cell.source) if isinstance(cell.source, list) else cell.source
                # Sanitize code to remove non-text characters
                source = ''.join(c for c in source if ord(c) < 128 or c in '\n\t\r')
                code += source + '\n'
        if not code.strip():
            logger.warning("No code cells found in .ipynb file.")
            return None
        return code
    except UnicodeDecodeError as e:
        logger.error(f"Error decoding .ipynb file: {e}")
        return None
    except Exception as e:
        logger.error(f"Error extracting code from .ipynb: {e}")
        return None