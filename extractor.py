import yt_dlp

def get_video_info(video_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # ইউটিউব থেকে বোট ডিটেকশন এড়াতে কিছু অতিরিক্ত সেটিংস
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            # সংশোধিত অংশ: null='Unknown' এর বদলে সরাসরি ডিফল্ট ভ্যালু
            video_data = {
                'title': info_dict.get('title', 'Unknown'), 
                'duration': info_dict.get('duration', 0),
                'uploader': info_dict.get('uploader', 'Unknown'),
                'direct_url': info_dict.get('url', ''),
                'formats': []
            }
            
            # ফরম্যাট লিস্ট তৈরি
            for f in info_dict.get('formats', []):
                if f.get('url'):
                    video_data['formats'].append({
                        'resolution': f.get('format_note', 'N/A'),
                        'ext': f.get('ext', 'mp4'),
                        'url': f.get('url')
                    })
                    
            return video_data
            
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=EXAMPLE_ID"
    print(get_video_info(url))
