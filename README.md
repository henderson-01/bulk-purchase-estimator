# 🏗️ Python Bulk Purchase Estimator

A smart, interactive (Command Line Interface) tool designed to calculate the total cost of bulk materials. Built with ensures accuracy for trade, construction, or retail estimates.

---

## ✨ Key Features

* **Dynamic Contextual Prompts:** The code remembers your item name (e.g., *cls timber 2.4m*) and injects it into every follow-up question so you never lose track of your input.
* **Robust Input Validation:** Uses `try-except` blocks to catch non-numeric entries, preventing the program from crashing if a user mistypes.
* **Financial Precision:** Automatically formats totals to exactly 2 decimal places (£0.00) for professional-grade quotes.
* **Error Recovery:** If an invalid number is entered, the script gently asks the question again rather than closing.

---

## 🚀 How to Run the Program

### 🪟 Windows Terminal (CMD or PowerShell)
1.  **Open your terminal** and navigate to your project folder:
    ```powershell
    cd C:\Users\YourName\Documents\your-project-folder
    ```
2.  **Run the script:**
    ```powershell
    python estimator.py
    ```
    *(Note: If `python` isn't recognized, try the command `py estimator.py`)*

---

### 🐧 Ubuntu / Linux Desktop (Step-by-Step)
Ubuntu require a **Virtual Environment (.venv)** to run Python code safely without interfering with system files.

1.  **Open your Terminal** (`Ctrl+Alt+T`).
2.  **Navigate to the folder** containing your `estimator.py` file:
    ```bash
    cd ~/Documents/your-project-folder
    ```
    *💡 Pro Tip: You can also open your file manager, right-click inside your project folder, and select **"Open in Terminal"** to jump straight to this step.*

3.  **Create a Virtual Environment:**
    This creates a protected "bubble" for your code to run in:
    ```bash
    python3 -m venv venv
    ```
4.  **Activate the Environment:**
    You must do this every time you open a new terminal to run the script:
    ```bash
    source venv/bin/activate
    ```
    *You will now see `(.venv)` appear at the start of your command line prompt.*

5.  **Run your script:**
    ```bash
    python3 estimator.py
    ```
6.  **Exit the Environment:**
    Once you are finished, simply type:
    ```bash
    deactivate
    ```

---

## 📋 Example Walkthrough

```text
What would you like to buy?: cls timber 2.4m

How much is one single cls timber 2.4m going to cost £: 3.75

Amount, how many cls timber 2.4m do you want to buy?: 54

If you buy 54 x cls timber 2.4m
Your total is £202.50

```

---

## 🛠️ Technical Concepts Used

* **Exception Management:** Handling `ValueError` during data conversion.
* **Control Flow:** Using `while True` loops for persistent error recovery.
* **String Interpolation:** Clean output using Python f-strings.
* **Environment Isolation:** Best-practice usage of `.venv` on Linux systems.

___
## ⚠️ Disclaimer 

This is provided "as-is" without any warranty of any kind. I am not responsible for any issues, data loss, or other problems that may arise from using this project. (code-related or otherwise) **Use it at your own risk**.