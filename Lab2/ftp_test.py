import ftplib
import os

# FTP server details
HOSTNAME = "ftp.dlptest.com"    # Example server;
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

# File names
upload_filename = "upload_test.txt"
download_filename = "downloaded.txt"

def create_test_file():
    # Create a simple text file to upload
    with open(upload_filename, "w") as f:
        f.write("This is a test file for FTP upload and download.\n")
    print(f"{upload_filename} created.")

def connect_ftp():
    try:
        ftp = ftplib.FTP(HOSTNAME)
        ftp.login(USERNAME, PASSWORD)
        ftp.set_pasv(True) 
        print("Connected and logged in.")
        return ftp
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

def upload_file(ftp):
    try:
        with open(upload_filename, "rb") as file:
            ftp.storbinary(f"STOR {upload_filename}", file)
        print(f"{upload_filename} uploaded successfully.")
    except Exception as e:
        print(f"Upload failed: {e}")

def download_file(ftp):
    try:
        with open(download_filename, "wb") as file:
            ftp.retrbinary(f"RETR {upload_filename}", file.write)
        print(f"{download_filename} downloaded successfully.")
    except Exception as e:
        print(f"Download failed: {e}")

def verify_files():
    try:
        with open(upload_filename, "r") as f1, open(download_filename, "r") as f2:
            content1 = f1.read()
            content2 = f2.read()
            if content1 == content2:
                print("Verification successful: Files match.")
            else:
                print("Verification failed: Files do not match.")
    except Exception as e:
        print(f"Error during verification: {e}")

def list_files(ftp):
    print("Listing files on server:")
    try:
        ftp.dir()
    except Exception as e:
        print(f"Could not list files: {e}")

def main():
    create_test_file()

    ftp = connect_ftp()
    if ftp:
        upload_file(ftp)
        list_files(ftp)
        download_file(ftp)
        verify_files()
        ftp.quit()
        print("FTP connection closed.")


if __name__ == "__main__":
    main()
