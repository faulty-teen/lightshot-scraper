# 🌐 liteshot Scraper

![Liteshot Scraper Banner](imgs/Banner.png)

# ❔ Info
This is a [prnt.sc](https://prnt.sc/) scraper that generates random URLs, checks if the image is not a [Crypto Scam](#️-crypto-scam), and if it's safe, sends it to a Discord webhook. Threading is used to increase the speed of image verification. 🚀

## 🔧 How to Use

1. Make sure you have **Python 3** installed.  
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
3. [Connect to your Discord webhook](#️-connect-to-discord)
4. Run the scraper with:
    ```bash
    python3 main.py
    ```
## 🕹️ Connect to Discord
Once an image is verified, it sends the result to a Discord webhook on your server. If you're not sure how to set it up, you can check this guide here.

1. Copy your webhook URL from Discord. [How to make a discord webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
2. Paste it in the config file:
    ```python
    WEBHOOK_URL = 'WEBHOOK URL'
    SAVE_IMAGES = True
    THREADS = 2000
    ```
3. Change settings. Check [System Requirements](#-system-requirements) for thread amount and save setting.

## ⚠️ Crypto Scam
**prnt.sc** is known for hosting images with fake crypto wallet credentials designed to scam users. These images appear across the site and follow a similar pattern.

## 🧐 How to Identify a Scam Image?
When an image is found on prnt.sc, it is converted to base64 and compared against known scam images stored in data.json. If a match is found, the image is flagged as a scam and will not be sent.

Note: Sometimes false positives can occur.

## 💡 Contribute
Your [contributions](https://github.com/faulty-teen/liteshot-scraper/pulls) to the project are always welcome! If you find any bugs or have suggestions, feel free to open an [issue](https://github.com/faulty-teen/liteshot-scraper/issues). 💬

## 💻 System Requirements
Please read the [System Requirements](/system_requirements.md) to see what the recommended number of threads you should run on your system.

## 🛑 Worries about being blocked from prnt.sc?
No need to worry. This tool uses free proxies that refresh often to ensure that you won't get booted off.
