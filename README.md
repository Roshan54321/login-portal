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
3. **Install the requirements**
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

## Shell Script

### Usage Instructions

1. **Navigate to Directory**: Change into the `bash-shell` directory.
2. **Grant Execution Permissions**: Make the `login.sh` script executable.

    ```bash
    chmod +x login.sh
    ```

3. **Move Script to System Binaries**: Move the script to `/usr/local/bin/` for system-wide access.

    ```bash
    sudo mv login.sh /usr/local/bin/
    ```

4. **Create systemd Service**

   Open the systemd service file for editing.

    ```bash
    sudo nano /etc/systemd/system/login.service
    ```

    Copy and paste the following:

    ```ini
    [Unit]
    Description=Network Login Script

    [Service]
    ExecStart=/usr/local/bin/login.sh

    [Install]
    WantedBy=default.target
    ```

5. **Create systemd Timer Unit**

    Open the systemd timer file for editing.

    ```bash
    sudo nano /etc/systemd/system/network-login.timer
    ```

    Copy and paste the following:

    ```ini
    [Unit]
    Description=Run Network Login Script After Network is Up

    [Timer]
    OnBootSec=1min
    OnUnitActiveSec=1min

    [Install]
    WantedBy=timers.target
    ```

6. **Reload systemd Configuration**

    ```bash
    sudo systemctl daemon-reload
    ```

7. **Enable Timer**

    ```bash
    sudo systemctl enable network-login.timer
    ```


### Direct Invocation via Symbolic Link

1. **Create Symbolic Link**

    ```bash
    sudo ln -s /usr/local/bin/login.sh /usr/local/bin/login
    ```

2. **Run the Script**

    Execute the script by typing `login` in the terminal.

    ```bash
    login
    ```






