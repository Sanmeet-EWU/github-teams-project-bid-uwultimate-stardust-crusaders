import ftplib


class FTP:
    def login_to_ftp(host):
        try:
        # Create an FTP object and connect to the FTP server
        with ftplib.FTP(host) as ftp:
            # Attempt to login with default anonymous credentials
            ftp.login()  # login() defaults to anonymous login
            print("Login successful!")
            return True
        except ftplib.all_errors as e:
        # Handle different FTP exceptions
        print(f"Failed to connect or login: {e}")
        return False

# Example usage:
host = 'ftp.example.com'  # Replace with the FTP server's address
result = login_to_ftp(host)
print(result)