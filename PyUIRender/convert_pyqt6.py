import os
import sys
from PyQt6 import uic

def convert_ui_to_py(input_path, output_dir=None):
    """
    Convert a Qt Designer .ui file to a PyQt6 .py file
    
    """
    # Validate input file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if not input_path.lower().endswith('.ui'):
        raise ValueError("Input file must have a .ui extension")
    
    # Get base filename without extension
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    # Determine output path
    if output_dir:
        # Create output directory if needed
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{base_name}.py")
    else:
        # Use same directory as input file
        output_dir = os.path.dirname(input_path)
        output_path = os.path.join(output_dir, f"{base_name}.py")
    
    # Perform conversion
    try:
        with open(output_path, 'w', encoding='utf-8') as py_file:
            uic.compileUi(input_path, py_file)
        return output_path
    except Exception as e:
        # Clean up partially written file on error
        if os.path.exists(output_path):
            os.remove(output_path)
        raise RuntimeError(f"Conversion failed: {str(e)}") from e

# If you want to test the script independently
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_pyqt6.py <input.ui> [output_dir]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        output_file = convert_ui_to_py(input_file, output_dir)
        print(f"Successfully converted: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)