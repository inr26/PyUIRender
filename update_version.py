import sys
import re

def update_version(major=None, minor=None, patch=None, dev=None):
    version_file = "PyUIRender/version.py"
    
    # Read current version
    with open(version_file, "r") as f:
        content = f.read()
    
    # Update components
    if major is not None:
        content = re.sub(r"MAJOR = \d+", f"MAJOR = {major}", content)
    if minor is not None:
        content = re.sub(r"MINOR = \d+", f"MINOR = {minor}", content)
    if patch is not None:
        content = re.sub(r"PATCH = \d+", f"PATCH = {patch}", content)
    if dev is not None:
        content = re.sub(r"DEV = (True|False)", f"DEV = {dev}", content)
    
    # Write updated version
    with open(version_file, "w") as f:
        f.write(content)
    
    print(f"Version updated: {get_current_version()}")

def get_current_version():
    from PyUIRender.version import __version__
    return __version__

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Parse command line arguments
        args = {}
        for arg in sys.argv[1:]:
            if "=" in arg:
                key, value = arg.split("=")
                if key in ["major", "minor", "patch"]:
                    args[key] = int(value)
                elif key == "dev":
                    args["dev"] = value.lower() == "true"
        update_version(**args)
    else:
        print(f"Current version: {get_current_version()}")