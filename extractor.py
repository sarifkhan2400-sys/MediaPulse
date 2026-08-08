import yt_dlp

def get_video_info(video_url):
    """
    ইউটিউব লিংক থেকে ভিডিওর শিরোনাম, ডিরেক্ট স্ট্রিম লিংক এবং ফরম্যাটগুলো বের করে দেয়।
    """
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ভিডিওর মেটাডেটা ফেচ করা
            info_dict = ydl.extract_info(video_url, download=False)
            
            video_data = {
                'title': info_dict.get('title', null='Unknown'),
                'duration': info_dict.get('duration', 0),
                'uploader': info_dict.get('uploader', 'Unknown'),
                'direct_url': info_dict.get('url', ''),
                'formats': []
            }
            
            # বিভিন্ন রেজুলেশনের ফরম্যাটগুলো গুছিয়ে নেওয়া
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

# কোড টেস্ট করার জন্য (আপনার ভিডিও লিংক এখানে বসাবেন)
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=EXAMPLE_ID"
    result = get_video_info(url)
    print(result)
