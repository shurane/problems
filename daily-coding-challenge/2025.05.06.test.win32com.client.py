import win32com.client
import time

# need to `python -m pip install pywin32`
# also related: https://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html
# https://ss64.com/vb/sendkeys.html

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("Chrome")  # Try to focus Chrome

shell.SendKeys("^k")
shell.SendKeys("what's the weather?{ENTER}")


# for _ in range(8):
    # time.sleep(0.1)
    # shell.SendKeys("^t")

for i in range(8):
    time.sleep(0.2)
    shell.SendKeys(f"^{i}")
