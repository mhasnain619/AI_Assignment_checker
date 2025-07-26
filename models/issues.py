import ast
import re
import keyword


def check_common_issues(code):
    """Check for common Python coding issues."""
    issues = []
    
    # Check for missing imports
    if "pd." in code and "import pandas" not in code:
        issues.append("Error: 'pd' used but 'pandas' not imported.")
    if "np." in code and "import numpy" not in code:
        issues.append("Error: 'np' used but 'numpy' not imported.")
    
    # Check for undefined variables using AST
    try:
        tree = ast.parse(code)
        assigned_vars = set()
        used_vars = set()
        
        # Collect assigned variables
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    assigned_vars.add(node.id)
                elif isinstance(node.ctx, ast.Load):
                    used_vars.add(node.id)
        
        # Exclude built-ins, keywords, and common module names
        excluded = set(keyword.kwlist + dir(__builtins__) + ['numpy', 'pandas', 'sklearn', 'torch', 'tensorflow'])
        undefined_vars = [var for var in used_vars if var not in assigned_vars and var not in excluded]
        if undefined_vars:
            issues.append(f"Warning: Undefined variables detected: {', '.join(undefined_vars)}.")
    except SyntaxError as e:
        issues.append(f"Warning: Syntax error in code: {str(e)}. Unable to check for undefined variables.")
    
    # Check for bare except clauses
    if "except:" in code and not re.search(r'except\s+\w+:', code):
        issues.append("Warning: Bare 'except:' clause detected. Specify exception type for better error handling.")
    
    # Check for overly long lines
    lines = code.split('\n')
    long_lines = [i + 1 for i, line in enumerate(lines) if len(line.strip()) > 120]
    if long_lines:
        issues.append(f"Warning: Lines {', '.join(map(str, long_lines))} exceed 120 characters. Consider reformatting.")
    
    return issues


def check_ml_issues(code):
    """Check for machine learning-specific issues."""
    issues = []
    
    # Check for unscaled data in ML models
    if "LogisticRegression" in code and "StandardScaler" not in code:
        issues.append("Warning: LogisticRegression used without data scaling. Consider using StandardScaler for better performance.")
    
    # Check for missing train-test split
    if any(model in code for model in ["LogisticRegression", "RandomForest", "SVC"]) and "train_test_split" not in code:
        issues.append("Warning: No train-test split detected. Use sklearn.model_selection.train_test_split to evaluate model performance.")
    
    # Check for lack of cross-validation
    if any(model in code for model in ["LogisticRegression", "RandomForest", "SVC"]) and "cross_val_score" not in code and "GridSearchCV" not in code:
        issues.append("Warning: No cross-validation detected. Consider using cross_val_score or GridSearchCV for robust model evaluation.")
    
    # Check for direct use of model.predict without validation
    if ".predict(" in code and "train_test_split" not in code:
        issues.append("Warning: Model prediction used without train-test split. Validate model on separate test data to avoid overfitting.")
    
    return issues