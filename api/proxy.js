import { execSync } from 'child_process';
import path from 'path';

export default async function handler(req, res) {
    const { url } = req.query;
    try {
        // Vercel kopiert Dateien nach /var/task/bin/yt-dlp
        // Wir verwenden path.join, um den absoluten Pfad zur Laufzeit zu bilden
        const binPath = path.join(process.cwd(), 'bin', 'yt-dlp');
        
        const output = execSync(`"${binPath}" -j "${url}"`).toString();
        res.status(200).json(JSON.parse(output));
    } catch (e) {
        res.status(500).json({ error: "Fehler: " + e.message });
    }
}
