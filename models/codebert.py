from transformers import AutoTokenizer, AutoModel
import torch
import re
from .issues import check_common_issues, check_ml_issues
from scripts.logger import get_logger

logger = get_logger(__name__)

def load_codebert():
    try:
        tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
        model = AutoModel.from_pretrained("microsoft/codebert-base")
        if torch.cuda.is_available():
            model.to('cuda')
        logger.info("CodeBERT loaded successfully.")
        return tokenizer, model
    except Exception as e:
        logger.error(f"Error loading CodeBERT: {e}")
        return None, None

def strip_comments(code):
    """Remove single-line and multi-line comments from code."""
    # Remove single-line comments
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
    # Remove multi-line comments (docstrings or triple-quoted strings)
    code = re.sub(r'"""[\s\S]*?"""|''[\s\S]*?''', '', code)
    return code

def analyze_with_codebert(code):
    tokenizer, model = load_codebert()
    if tokenizer is None or model is None:
        return "CodeBERT not loaded."
    
    try:
        # Strip comments to avoid processing comment text
        clean_code = strip_comments(code)
        
        # Tokenize and analyze code with CodeBERT
        inputs = tokenizer(code, return_tensors="pt", truncation=True, max_length=512, padding=True)
        if torch.cuda.is_available():
            inputs = {k: v.to('cuda') for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
        
        # Basic feedback based on code length and complexity
        feedback = [f"Code analyzed with CodeBERT. Length: {len(code)} characters."]
        if len(code) > 1000:
            feedback.append("Warning: Code is lengthy (>1000 characters), consider refactoring for readability.")
        
        # Heuristic checks for common issues
        feedback.extend(check_common_issues(clean_code))
        
        # Machine learning-specific checks if relevant
        if any(lib in code for lib in ["sklearn", "tensorflow", "torch"]):
            feedback.extend(check_ml_issues(code))
        
        # Combine feedback
        if len(feedback) == 1:
            feedback.append("No critical issues detected by heuristic checks.")
        return "\n".join(feedback)
    except Exception as e:
        logger.error(f"Error analyzing code with CodeBERT: {e}")
        return f"Error analyzing code: {str(e)}"

