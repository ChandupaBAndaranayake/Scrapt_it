# TorrentGalaxy Discord Bot

This Discord bot checks TorrentGalaxy for the latest uploads and posts them to a specified Discord channel every hour.

## Features

- Scrapes the latest uploads from TorrentGalaxy.
- Posts the latest uploads to a specified Discord channel.
- Runs every hour to ensure the latest uploads are always up-to-date.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/torrentgalaxy-discord-bot.git
    cd torrentgalaxy-discord-bot
    ```

2. Install the required dependencies:
    ```sh
    pip install requests beautifulsoup4 discord.py
    ```

## Configuration

1. Open the `bot.py` file in a text editor.

2. Replace `'Token of the discord'` with your Discord bot token:
    ```python
    TOKEN = 'your-discord-bot-token'
    ```

3. Replace `CHANNEL_ID` with the ID of the Discord channel where you want to send the notifications:
    ```python
    CHANNEL_ID = your-channel-id
    ```

## Usage

1. Run the bot:
    ```sh
    python bot.py
    ```

2. The bot will start and post the latest uploads to the specified Discord channel every hour.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- [Discord.py](https://discordpy.readthedocs.io/en/stable/) for creating the Discord bot.
- [TorrentGalaxy](https://torrentgalaxy.to/) for providing the torrent data.

## Contact

If you have any questions, feel free to contact me at [your-email@example.com](mailto:your-email@example.com).
