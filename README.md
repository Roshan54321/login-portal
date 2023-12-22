# Campus Portal Login Automation

This project facilitates the automation of the campus (Pulchowk Campus) portal login process using batch and Python scripts.

## Batch File

### Usage Instructions

1. **Locate Directory**: Navigate to the `batch-file` directory.
2. **Enter Credentials**: Change the username and password in the `login.bat` file using some text editors.
3. **Run the Script**: Execute the `login.bat` file.

   ```bash
   login.bat
   ```

## Python Script

### Usage Instructions

1. **Directory Navigation**: Access the python-script directory.
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv env && source env/bin/activate
   ```
3. **CInstall the requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Edit Configuration**: Edit chrome driver path.
   ```python
    # Modify the following line with your OS-specific Chrome driver path
    chrome_driver_path = '/usr/bin/chromedriver'
   ```
5. **Enter Credentials**: Change the username and password in the `internet.py` file using some text editors.
6. **Run the Script**: Execute the `python login.py` file.

   ```bash
   python login.py
   ```

### Converting to Executable

1. **Convert to Executable**
   ```bash
   pyinstaller --onefile login.py
   ```