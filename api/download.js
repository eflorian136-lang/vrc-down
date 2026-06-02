export default async function handler(req, res) {
  const { url } = req.query;
  // Hier simulieren wir die Logik, die normalerweise dein Python-Downloader macht
  // Wir geben dem Frontend die Info, wo die Datei liegt
  res.status(200).json({
    downloadLink: "https://loader.to/api/button/?url=" + encodeURIComponent(url)
  });
}
