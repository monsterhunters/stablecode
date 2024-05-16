import subprocess

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"stderr: {stderr.decode('utf-8')}")
        return False
    return True

# Download cloudflared
if not run_command("wget https://github.com/cloudflare/cloudflared/releases/download/2024.5.0/cloudflared-fips-linux-amd64.deb"):
    exit(1)

# Install cloudflared
if not run_command("dpkg -i cloudflared-fips-linux-amd64.deb"):
    exit(1)

# Install dependencies if needed
if not run_command("apt-get install -f"):
    exit(1)

# Move cloudflared to /usr/local/bin/wex
if not run_command("mv /usr/local/bin/cloudflared /usr/local/bin/wex"):
    exit(1)

print("Installation successful.")
