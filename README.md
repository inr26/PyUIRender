PyUIRender - Qt UI to Python Converter

![Banner_s](https://github.com/user-attachments/assets/99f7d9c6-696d-44ee-8c05-e201b9819de3)




PyUIRender is a user-friendly graphical tool that converts Qt Designer .ui files into Python code for multiple frameworks. With its intuitive interface, you can batch-convert UI files to PyQt5, PyQt6, or PySide6 formats with just a few clicks.



**🚀 Why PyUIRender?**

PyUIRender is a powerful, user-friendly desktop application tailored for developers and designers who need to:

- Rapidly **convert** Qt Designer UI (`.ui`) files into **Python** code for  
  - PyQt5  
  - PyQt6  
  - PySide6  

- **Batch-process** dozens of UI files in one session  
- Track progress with a **visual progress bar**  
- Remember your preferred output folders for streamlined workflows  
- Quickly **copy** output paths to clipboard after conversion  
- Get clear **success** and **error** dialogs  

Whether you’re building internal tools, shipping client-facing GUIs, or automating your build pipeline, PyUIRender saves time and enforces consistency.


**⭐ Key Features**

🖼️ Multi-Format Conversion: Convert UI files to PyQt5, PyQt6, or PySide6 code

📁 Batch Processing: Convert multiple UI files simultaneously

📊 Progress Tracking: Visual progress bar shows conversion status

💾 Settings Memory: Remembers your last used output directory

📋 Output Management: Copy output path to clipboard with one click

🎨 Modern UI: Clean, responsive interface with dark/light mode support

✅ Error Handling: Clear error messages and success notifications


**🎯 Installation**

Prerequisites

Python 3.7 or higher
Avoid using version 3.13 or higher, as PySide6 is not yet supported.

PySide6

Installation Steps
Clone the repository:

git clone https://github.com/inr26/PyUIRender.git


Install required dependencies:

# For PySide6 conversions
bash
pip install PySide6
For additional framework support (optional):

bash
# For PyQt5 conversions
pip install PyQt5

# For PyQt6 conversions
pip install PyQt6
Usage
Launch the application:

bash
python main.py


**Using the interface:**

Click "Browse .ui Files" to select UI files for conversion

Choose an output directory with "Choose Destination Folder"

Select your target framework (PyQt5, PyQt6, or PySide6)

Click "Convert Now" to start the conversion process

After conversion:

Success dialog shows output directory with copy button

Error dialog provides details for any failed conversions

Progress bar tracks conversion status


**Screenshots**

Main Window	
![Screenshot 2025-07-08 222653](https://github.com/user-attachments/assets/37a95164-c079-44b9-95c5-276d9a70819d)

Success Dialog	
![image](https://github.com/user-attachments/assets/6faa2689-f15e-44e1-8af6-fae3595a4991)

Error Dialog
![image](https://github.com/user-attachments/assets/38e0ecee-9c96-49ec-81b8-aa080c3983a5)


**File Structure**

![image](https://github.com/user-attachments/assets/65b126a4-2f70-441b-b192-f136a628144f)


Requirements
The core application requires:

PySide6

For conversion capabilities:

PyQt5 (for PyQt5 conversions)

PyQt6 (for PyQt6 conversions)

PySide6 (for PySide6 conversions - already installed)

Troubleshooting
Common Issues
Conversion fails for PySide6:

Ensure pyside6-uic is in your system PATH

Verify PySide6 is properly installed

Icon not loading:

Check the icon exists at icon/ico.png

Verify file permissions

Missing dependencies:

Run pip install -r requirements.txt (if available)

Ensure all required packages are installed

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -am 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Create a new Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
If you encounter any issues or have questions, please open an issue on GitHub.
