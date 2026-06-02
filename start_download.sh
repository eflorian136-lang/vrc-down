#!/bin/bash
read -p "Gib die Twitch VOD URL ein: " vod_url
gh workflow run download.yml -f url="$vod_url"
echo "Download-Workflow für $vod_url wurde gestartet."
