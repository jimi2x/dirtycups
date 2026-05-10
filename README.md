<h1> dirtycups.py </h1>
<p><strong>Dirty CUPS</strong> is a free Linux/Unix CVE scanner (Python3 script) to validate if a target is vulnerable to CVE-2024-47176. This is a socket only CUPS scanner based off of MalwareTech's cups_scanner.py: https://github.com/MalwareTech/CVE-2024-47176-Scanner/blob/master/cups_scanner.py</p>

## Original script
<strong>jimi2x</strong>

---
## Functions
* **Creates local socket listener for callback**
* **Triggers response from target**
* **Waits for incoming connection**

---
## Quick install notes:
```
Nothing to install, sockets FTW!
```
---
## Example Usage:
```
chmod 755 dirtycups.py
python3 dirtycups.py
```
---
## License
MIT License
