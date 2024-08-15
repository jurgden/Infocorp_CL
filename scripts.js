document.addEventListener("DOMContentLoaded", function() {
    const bannerContainer = document.getElementById('banner-slideshow');
    const jsonPath = 'assets/images/banner/banner_images.json'; // Path to your JSON file

    // Function to fetch image paths from JSON
    async function fetchImagePaths() {
        try {
            const response = await fetch(jsonPath);
            if (!response.ok) throw new Error('Network response was not ok');
            const imagePaths = await response.json();
            return imagePaths;
        } catch (error) {
            console.error('Error fetching image paths:', error);
            return [];
        }
    }

    // Function to create the slideshow
    function createSlideshow(images) {
        let currentIndex = 0;

        function showNextImage() {
            const imageElements = bannerContainer.getElementsByTagName('img');
            if (imageElements.length > 0) {
                imageElements[currentIndex].style.opacity = 0; // Fade out current image
                currentIndex = (currentIndex + 1) % images.length;
                imageElements[currentIndex].style.opacity = 1; // Fade in next image
            }
        }

        images.forEach((src, index) => {
            const img = document.createElement('img');
            img.src = src;
            img.style.position = 'absolute';
            img.style.top = '0';
            img.style.left = '0';
            img.style.width = '100%';
            img.style.height = '100%';
            img.style.transition = 'opacity 1s ease-in-out';
            img.style.opacity = index === 0 ? 1 : 0; // Show only the first image initially
            bannerContainer.appendChild(img);
        });

        setInterval(showNextImage, 5000); // Change image every 5 seconds
    }

    // Main function to load images and create the slideshow
    async function initBanner() {
        const imagePaths = await fetchImagePaths();
        if (imagePaths.length > 0) {
            createSlideshow(imagePaths);
        } else {
            console.error('No images found in JSON.');
        }
    }

    initBanner();
});
