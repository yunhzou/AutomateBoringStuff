import os
import subprocess
import webbrowser
import platform

os_name = platform.system()

def open_application(app_name):
    if os_name == 'Windows':
        # Define paths
        username = os.getlogin()
        paths_dict = {
            'Notion': [
                r"C:\Users\Lenovo\AppData\Local\Programs\Notion\Notion.exe"
            ],
            'Slack': [
                r"C:\Users\Lenovo\AppData\Local\slack\slack.exe"
            ],
            'Visual Studio': [
                r"C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            ]
        }
        app_paths = paths_dict.get(app_name, [])
        for path in app_paths:
            if os.path.exists(path):
                subprocess.Popen([path])
                return
        print(f"{app_name} not found.")
    elif os_name == 'Darwin':
        # Mac OS
        subprocess.Popen(['open', '-a', app_name])
    elif os_name == 'Linux':
        # Linux
        try:
            subprocess.Popen([app_name.lower()])
        except FileNotFoundError:
            print(f"{app_name} not found.")

def open_chrome_with_urls(urls):
    if os_name == 'Windows':
        username = os.getlogin()
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        ]
        chrome_path = None
        for path in chrome_paths:
            if os.path.exists(path):
                chrome_path = path
                break
        if chrome_path:
            for url in urls:
                subprocess.Popen([chrome_path, url])
            return
    elif os_name == 'Darwin':
        # Mac OS
        for url in urls:
            subprocess.Popen(['open', '-a', 'Google Chrome', url])
        return
    elif os_name == 'Linux':
        try:
            # Try to open with google-chrome
            for url in urls:
                subprocess.Popen(['google-chrome', url])
            return
        except FileNotFoundError:
            pass
    # If all else fails, use default browser
    for url in urls:
        webbrowser.open(url)

# Open applications
open_application('Notion')
open_application('Slack')
open_application('Visual Studio')

# Open Chrome with URLs
urls = [
    "https://chatgpt.com/?model=o1-preview",
    "https://www.perplexity.ai/"
    "https://smith.langchain.com/o/3ae59214-285d-5cf3-b992-4ee5c96f2a9f/"
]
open_chrome_with_urls(urls)
