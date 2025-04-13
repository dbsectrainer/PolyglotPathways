class VideoLoader {
    constructor() {
        this.videos = null;
        this.pendingLoads = [];
    }

    async init() {
        try {
            console.log('Initializing video loader...');
            // Load video configuration
            const response = await fetch('videos.json');
            if (!response.ok) {
                throw new Error('Failed to load video configuration');
            }
            const data = await response.json();
            console.log('Loaded videos.json:', data);
            this.videos = data;
            
            // Process any pending video loads
            while (this.pendingLoads.length > 0) {
                const {day, lang} = this.pendingLoads.shift();
                this.loadVideo(day, lang);
            }
        } catch (error) {
            console.error('Error initializing video loader:', error);
            this.showFallback();
        }
    }

    loadVideo(day, lang) {
        // If videos aren't loaded yet, queue this request
        if (!this.videos) {
            console.log('Videos not loaded yet, queueing request...');
            this.pendingLoads.push({day, lang});
            return;
        }

        const iframe = document.getElementById('youtube-video');
        const fallback = document.getElementById('video-fallback');
        const container = document.getElementById('video-player');
        
        const dayKey = `day${day}`;
        console.log('Looking for video with key:', dayKey, 'in videos:', this.videos);
        
        if (this.videos && this.videos[dayKey] && this.videos[dayKey][lang]) {
            const videoId = this.videos[dayKey][lang];
            const embedUrl = `https://www.youtube.com/embed/${videoId}`;
            console.log('Setting video URL:', embedUrl);
            
            // Set container size
            container.style.position = 'relative';
            container.style.width = '100%';
            container.style.paddingTop = '56.25%'; // 16:9 aspect ratio
            
            // Style iframe
            iframe.style.position = 'absolute';
            iframe.style.top = '0';
            iframe.style.left = '0';
            iframe.style.width = '100%';
            iframe.style.height = '100%';
            
            iframe.src = embedUrl;
            iframe.style.display = 'block';
            fallback.style.display = 'none';
        } else {
            console.warn(`No video available for day ${day} in ${lang}`);
            this.showFallback();
        }
    }

    showFallback() {
        const iframe = document.getElementById('youtube-video');
        const fallback = document.getElementById('video-fallback');
        iframe.src = '';
        iframe.style.display = 'none';
        fallback.style.display = 'block';
    }
}

// Initialize video loader when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing video loader...');
    window.videoLoader = new VideoLoader();
    window.videoLoader.init().catch(error => {
        console.error('Failed to initialize video loader:', error);
    });
});
