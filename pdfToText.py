import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "result.pdf"
abs_file_path = os.path.join(script_dir, rel_path)
