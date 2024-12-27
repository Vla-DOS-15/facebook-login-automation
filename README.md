# Facebook Login Automation

A Python script that automates the login process for Facebook, downloads the profile picture, and stores it in a specified directory. This tool is intended for educational and personal use only.

## Features

- **Automated Login:** Logs into Facebook using provided credentials.
- **Profile Picture Download:** Retrieves the profile picture and saves it with a unique filename.
- **Logging:** Logs actions and errors in an `out.log` file.

## Requirements

- Python 3.8 or higher
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- Required Python packages (see below)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vla-DOS-15/facebook-login-automation.git
   cd facebook-login-automation
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and install the correct version of ChromeDriver:
   - [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

4. Add the ChromeDriver executable to your system's PATH.

## Usage

1. Update the script with your Facebook credentials:
   ```python
   email = "replace_with_your_email_or_phone"
   password = "replace_with_your_password"
   ```

2. Run the script:
   ```bash
   python facebook_login_automation.py
   ```

3. The downloaded profile picture will be saved in the `data/logins_img` directory with a unique name.

## Example Output

- **Log File (`out.log`):**
  ```
  2024-12-26 10:00:00 - The login site is open
  2024-12-26 10:00:05 - Login data entered
  2024-12-26 10:00:07 - The login button is clicked
  2024-12-26 10:00:15 - Profile picture URL: https://...
  2024-12-26 10:00:20 - Profile picture saved at: data/logins_img/profile_picture_1672077620.jpg
  ```

- **Saved Profile Picture:**
  The profile picture will be stored in the `data/logins_img` folder with a filename like `profile_picture_<timestamp>.jpg`.

## Project Structure

```
.
??? facebook_login_automation.py  # Main script
??? data/
?   ??? logins_img/               # Directory for saving profile pictures
??? out.log                       # Log file
??? README.md                     # Project documentation
```

## Dependencies

The following Python libraries are used:

- `selenium` - For browser automation
- `requests` - For downloading the profile picture

To install all dependencies, use:
```bash
pip install selenium requests
```