# Instagram Mass Unlike Script 🔁

A Python script that safely unlikes Instagram posts in bulk while respecting Instagram's rate limits to avoid account restrictions.

## Features ✨

- Bulk unlike Instagram posts automatically
- Smart rate limiting to prevent account restrictions
- Respects Instagram's hourly and daily limits
- Clean, emoji-based progress indicators
- Error handling and automatic retries
- Safe login and logout procedures
- Multiple methods to find liked posts

## Prerequisites 📋

Before running the script, make sure you have:

1. Python 3.7 or higher installed
2. pip (Python package manager)
3. Your Instagram username and password

## Installation 🚀

1. Clone this repository:
```bash
git clone https://github.com/DevRajVerma/Unlike-Insta-Liked-Reels.git
```

```bash
cd Unlike-Insta-Liked-Reels
```

2. Install the required package:
```bash
pip install instagrapi
```

## Usage 💻

1. Open `unlike_instagram.py` in a text editor
2. Replace the placeholder credentials with your Instagram login details:
```python
username = "your_username"  # Enter your Instagram username
password = "your_password"  # Enter your Instagram password
```

3. Run the script:
```bash
python unlike_instagram.py
```

## How It Works 🔍

The script:
1. Logs into your Instagram account using official API endpoints
2. Finds posts you've liked using multiple methods
3. Unlikes posts one by one with safe delays between actions
4. Shows progress with clean, emoji-based output
5. Automatically handles rate limits:
   - Max 50 unlikes per hour
   - Max 200 unlikes per day

## Safety Features 🛡️

- Random delays between actions
- Respects Instagram's rate limits
- Secure login handling
- Error handling and automatic retries
- Safe session management
- Automatic logout after completion

## Output Example 📝

```
🔄 Logging in to Instagram...
✅ Login successful!
🔍 Searching for your liked posts...
📝 Found 25 liked posts
✅ Unliked post 1/25 | This hour: 1/50 | Today: 1/200
...
✨ Completed unliking process!
👋 Logged out of Instagram
```

## Rate Limits ⚠️

To maintain account safety, the script enforces:
- Maximum 50 unlikes per hour
- Maximum 200 unlikes per day
- Random delays between actions (5-10 seconds)

## Important Notes 📌

1. Keep your credentials secure and never share them
2. Run the script with reliable internet connection
3. Don't modify the delay settings unless you know what you're doing
4. Consider using an Instagram account with 2FA disabled
5. The script may take several hours to complete due to rate limiting

## Troubleshooting 🔧

If you encounter issues:
1. Check your internet connection
2. Verify your login credentials
3. Ensure you're using the latest version of the script
4. Check if your account has any temporary restrictions
5. Make sure you have the latest version of Python and instagrapi

## Contributing 🤝

Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Share your experience

## Personal Note from the author

This is currently fetching 21 liked posts once you run this script, to remove all the liked videos from your account, you have to run this script multiple times

You don't have to care about privacy as this is open-source code, you can review this code line by line and check yourself if you don't trust me

## Disclaimer ⚖️

This script is for educational purposes only. Use it responsibly and at your own risk. The author is not responsible for any account restrictions or other issues that may arise from using this script.

## License 📄

MIT License - feel free to use and modify the script as needed.