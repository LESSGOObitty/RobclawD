import subprocess, sys

WIN_IP = "192.168.1.150"
WIN_USER = "RobDoe"

def exec_remote_ps(cmd):
    ssh_cmd = f"ssh {WIN_USER}@{WIN_IP} powershell.exe -Command \"{cmd}\""
    print(f"[+] Executing on Windows: {cmd}")
    res = subprocess.run(ssh_cmd, shell=True, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(f"[!] Error: {res.stderr}")

if __name__ == "__main__":
    ps_command = sys.argv[1] if len(sys.argv) > 1 else "Get-Process | Select-Object -First 5"
    exec_remote_ps(ps_command)
