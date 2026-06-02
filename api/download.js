export default async function handler(req, res) {
  const { url } = req.query;
  
  if (!url || !url.includes("twitch.tv")) {
    return res.status(400).json({ error: "Ungültige Twitch-URL" });
  }

  // Wir simulieren hier den 'DownloadManager' durch eine API-Weiterleitung
  // Dies entlastet deinen Server komplett, da der Download nicht bei dir stattfindet.
  const downloadApi = "https://loader.to/api/button/?url=" + encodeURIComponent(url);

  res.status(200).json({
    status: "success",
    downloadUrl: downloadApi,
    message: "Download wird vorbereitet..."
  });
}
