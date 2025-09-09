import ftplib
import os

def ftp_test():
    SERVER = "ftp.dlptest.com"
    USER = "dlpuser"
    PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"
    FILE = "test_ftp.txt"
    DOWNLOADED_FILE = "downloaded.txt"

    # Check if the file exists
    if not os.path.isfile(FILE):
        print(f"Error: {FILE} does not exist.")
        return

    try:
        ftp = ftplib.FTP(SERVER)
        ftp.login(USER, PASSWORD)
        ftp.set_pasv(True)
        print("Connected to FTP server.")

        # Upload existing file
        with open(FILE, "rb") as file:
            ftp.storbinary(f"STOR {FILE}", file)
        print(f"{FILE} uploaded successfully.")

        # List files on server
        print("Files present on server:")
        ftp.dir()

        # Download the file with a new name
        with open(DOWNLOADED_FILE, "wb") as file:
            ftp.retrbinary(f"RETR {FILE}", file.write)
        print(f"{DOWNLOADED_FILE} downloaded successfully.")

        # Verify file contents
        with open(FILE, "r") as f1, open(DOWNLOADED_FILE, "r") as f2:
            if f1.read() == f2.read():
                print("Verification passed: Files are identical.")
            else:
                print("Verification failed: Files differ.")

    except Exception as e:
        print(f"FTP operation failed: {e}")

    finally:
        ftp.quit()
        print("Disconnected from FTP.")

if __name__ == "__main__":
    ftp_test()
