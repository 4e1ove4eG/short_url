import subprocess
ya = subprocess.run(['whois', 'aaf.im'],stdout = subprocess.PIPE )
output = str(ya.stdout)
if output.find('Expiry Date') == -1 and output.find('Creation Date') == -1:
    print(ya.stdout)
print(str(ya.stdout).find('Expiry Date'))