from pylint.lint import Run
from pylint.reporters.text import TextReporter
from io import StringIO

def pylint_check(file_path):
    try:
        output = StringIO()
        reporter = TextReporter(output)
        Run([file_path, '--disable=C0114,C0115,C0116,R0903,W0311,W0703,C0303,C0301', '--max-line-length=120'], reporter=reporter, exit=False)
        return output.getvalue()
    except Exception as e:
        return f"Pylint error: {str(e)}"

print(pylint_check("uploads/test.py"))