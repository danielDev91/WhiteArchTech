import customtkinter as ctk
from tkinter import filedialog
import requests
import os
import time
import PIL
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Your VirusTotal API key
API_KEY = "bef642f35acead3bb6e6d7cc97e0baa7eead6d13400c7c61b4b874e06ac02dc8"

def scan_file(file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': API_KEY}
    files = {'file': (os.path.basename(file_path), open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)
    response_json = response.json()
    if response.status_code != 200 or 'resource' not in response_json:
        print("Error in scan response:", response_json)
        return None
    return response_json

def get_report(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': API_KEY, 'resource': resource}
    response = requests.get(url, params=params)
    return response.json()

def open_scan_page():
    scan_app = ctk.CTk()
    scan_app.geometry("1280x720")
    scan_app.title("Virus Scan via API VirusTotal")

    scan_app.grid_rowconfigure(0, weight=1)
    scan_app.grid_rowconfigure(1, weight=1)
    scan_app.grid_rowconfigure(2, weight=1)
    scan_app.grid_rowconfigure(3, weight=1)

    scan_app.grid_columnconfigure(0, weight=1)
    scan_app.grid_columnconfigure(1, weight=1)
    scan_app.grid_columnconfigure(2, weight=1)

    # Load image
    
    file_label = ctk.CTkLabel(scan_app, text="Choose a file to scan", font=("Helvetica", 18, "bold"))
    file_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="n")

    file_path_label = ctk.CTkLabel(scan_app, text="")
    file_path_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="n")

    def choose_file():
        file_path = filedialog.askopenfilename()
        file_path_label.configure(text=f"Selected File: {file_path}")
        scan_result = scan_file(file_path)
        if not scan_result:
            result_label.configure(text="Failed to scan file.")
            print("Failed to scan file.")
            return

        resource = scan_result.get('resource')
        if not resource:
            result_label.configure(text="Failed to retrieve resource key.")
            print("Failed to retrieve resource key.")
            return
        
        # Wait for the report and check until it's available
        scan_status = "Scan Result: No report available"
        for _ in range(12):  # Try for up to 3 minutes (12*15s)
            report = get_report(resource)
            print("Report:", report)  # Log the report
            
            if report['response_code'] == 1:
                positives = report['positives']
                total = report['total']
                scan_status = f"Detected as malicious by {positives}/{total} antivirus engines" if positives > 0 else "No threats detected"
                break
            time.sleep(15)
        
        result_label.configure(text=scan_status)
        print(scan_status)  # Log the final scan status
        return file_path

    file_button = ctk.CTkButton(scan_app, text="Choose File", command=choose_file, width=200, height=50)
    file_button.grid(row=2, column=1, padx=10, pady=10, sticky='n')

    result_label = ctk.CTkLabel(scan_app, text="", font=("Helvetica", 14))
    result_label.grid(row=3, column=0,  columnspan=3, padx=10, pady=10, sticky="nsew")

    scan_app.mainloop()

if __name__ == "__main__":
    open_scan_page()
