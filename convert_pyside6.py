import os
import sys
import subprocess
import shutil  # This import was missing
from pathlib import Path

def convert_ui_to_py(input_path, output_dir=None):
    """
    Convert a Qt Designer .ui file to a PySide6 .py file
    
    Args:
        input_path (str): Path to the input .ui file
        output_dir (str): Directory to save the output .py file (optional)
    
    Returns:
        str: Path to the generated .py file
    
    Raises:
        FileNotFoundError: If input file doesn't exist or pyside6-uic is not found
        ValueError: If input file doesn't have .ui extension
        RuntimeError: If conversion fails
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
    
    # Find pyside6-uic executable
    uic_executable = find_pyside6_uic()
    if not uic_executable:
        raise FileNotFoundError(
            "pyside6-uic executable not found. Make sure PySide6 is properly installed."
        )
    
    # Run conversion
    try:
        result = subprocess.run(
            [uic_executable, input_path, "-o", output_path],
            capture_output=True,
            text=True,
            check=True
        )
        return output_path
    except subprocess.CalledProcessError as e:
        # Clean up partially written file on error
        if os.path.exists(output_path):
            os.remove(output_path)
        error_msg = f"Conversion failed with error {e.returncode}:\n{e.stderr}"
        raise RuntimeError(error_msg) from e

def find_pyside6_uic():
    """Locate the pyside6-uic executable"""
    # First try: Check if it's in PATH
    if sys.platform == "win32":
        uic_name = "pyside6-uic.exe"
    else:
        uic_name = "pyside6-uic"
    
    # Check in PATH
    uic_path = shutil.which(uic_name)
    if uic_path:
        return uic_path
    
    # Second try: Check common installation locations
    python_dir = Path(sys.executable).parent
    possible_paths = [
        python_dir / uic_name,
        python_dir / "Scripts" / uic_name,  # Windows
        python_dir / "bin" / uic_name,      # Linux/macOS
    ]
    
    for path in possible_paths:
        if path.exists():
            return str(path)
    
    return None

# If you want to test the script independently
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_pyside6.py <input.ui> [output_dir]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        output_file = convert_ui_to_py(input_file, output_dir)
        print(f"Successfully converted: {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)