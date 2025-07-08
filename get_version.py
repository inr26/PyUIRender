import os
import subprocess
import re

def get_version():
    try:
        # Get the directory of this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Get version from git describe
        result = subprocess.run(
            ['git', 'describe', '--tags', '--dirty', '--always'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
            cwd=base_dir
        )
        version = result.stdout.strip()
        
        # Clean up version string
        version = re.sub(r'^v', '', version)  # Remove leading 'v'
        version = re.sub(r'-(\d+)-g([0-9a-f]+)', r'.dev\1+\2', version)  # Format dev versions
        version = re.sub(r'-dirty$', '.dirty', version)  # Format dirty flag
        return version
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "1.0.0.dev"  # Fallback version

if __name__ == "__main__":
    print(get_version())