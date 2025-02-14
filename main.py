import ftplib
import paramiko
import re

def read_ip_addresses(file_path):
    with open(file_path, 'r') as file:
        ip_addresses = file.read().splitlines()
    return ip_addresses

def upload_and_reboot(ip_address, directoryname, filename):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ip_address)
        ftp.login("root", "wago")

        # Change to the desired directory
        ftp.cwd(directoryname)

        # Upload the file
        with open(filename, "rb") as file:
            ftp.storbinary(f"STOR {filename}", file)

        # Close the FTP connection
        ftp.quit()
        print(f"{filename} uploaded successfully to {ip_address} via FTP")

        # SSH command
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip_address, username="root", password="wago")
            stdin, stdout, stderr = ssh.exec_command("reboot")
            print(stdout.read().decode())
        except Exception as e:
            print(f"SSH command failed for {ip_address}: {e}")
        finally:
            # Close the SSH connection
            ssh.close()
            print(f"SSH connection to {ip_address} closed")
    except Exception as e:
        print(f"Failed to upload and reboot {ip_address}: {e}")

def main():
    file_path = 'IPadres.txt'
    ip_addresses = read_ip_addresses(file_path)
    directoryname = "/home/codesys_root/PlcLogic/Application" #<-- BC100 := A:/plc/PlcLogic/Application 
    filename = "file.txt"
    print(f"Uploading {filename} to the following IP addresses: {ip_addresses}")
    
    for ip_address in ip_addresses:
        upload_and_reboot(ip_address, directoryname, filename)

if __name__ == "__main__":
    main()