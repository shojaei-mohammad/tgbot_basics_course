# Deploying Your Telegram Bot as a Systemd Service

This guide will walk you through the process of deploying your Telegram bot as a systemd service on a Linux server.

## Prerequisites

- A Linux server with systemd (most modern distributions use systemd)
- SSH access to your server
- Your bot's Python script and any necessary files
- Python 3 installed on your server

## Step 1: Prepare Your Bot

1. Connect to your server via SSH:
   ```
   ssh username@your_server_ip
   ```

2. Create a directory for your bot:
   ```
   mkdir ~/mybot
   cd ~/mybot
   ```

3. Upload your bot files to this directory (you can use SCP, SFTP, or Git).

4. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Step 2: Create a Systemd Service File

1. Create a new service file:
   ```
   sudo nano /etc/systemd/system/mybot.service
   ```

2. Add the following content to the file:
   ```
   [Unit]
   Description=My Telegram Bot
   After=network.target

   [Service]
   User=your_username
   WorkingDirectory=/home/your_username/mybot
   ExecStart=/home/your_username/mybot/venv/bin/python /home/your_username/mybot/main.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Replace `your_username` with your actual username and adjust the paths if necessary.

3. Save and exit the editor (in nano, press Ctrl+X, then Y, then Enter).

## Step 3: Configure Environment Variables (Optional)

If your bot uses environment variables (e.g., for the API token):

1. Create an environment file:
   ```
   cd ~/mybot
   sudo nano /.env
   ```

2. Add your environment variables:
   ```
   BOT_TOKEN="your_bot_token_here"
   ```

3. Save and exit the editor.

## Step 4: Start and Enable the Service

1. Reload systemd to recognize the new service:
   ```
   sudo systemctl daemon-reload
   ```

2. Start the bot service:
   ```
   sudo systemctl start mybot
   ```

3. Enable the service to start on boot:
   ```
   sudo systemctl enable mybot
   ```

## Step 5: Verify the Bot is Running

1. Check the status of your bot:
   ```
   sudo systemctl status mybot
   ```

2. If everything is working, you should see "active (running)" in the output.

## Managing Your Bot

- To stop the bot: `sudo systemctl stop mybot`
- To restart the bot: `sudo systemctl restart mybot`
- To view logs: `sudo journalctl -u mybot -f`

## Updating Your Bot

1. Stop the service:
   ```
   sudo systemctl stop mybot
   ```

2. Update your bot files in the `/home/your_username/mybot` directory.

3. Restart the service:
   ```
   sudo systemctl start mybot
   ```

Congratulations! Your Telegram bot is now running as a systemd service and will automatically start on server reboots.