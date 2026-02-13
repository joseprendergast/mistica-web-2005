// Photo Gallery Navigation Script
// This script adds keyboard and arrow navigation to photo pages

(function() {
    // Get current page filename (e.g., "7.htm")
    const currentFile = window.location.pathname.split('/').pop();
    const currentNum = parseInt(currentFile.replace('.htm', ''));
    
    // Get directory path to determine gallery
    const pathParts = window.location.pathname.split('/').filter(p => p);
    const currentIndex = pathParts.length - 1;
    const galleryPath = pathParts.slice(0, currentIndex).join('/');
    
    // Determine total number of photos in this gallery
    let totalPhotos = 20; // Default
    
    // Detect gallery type from path (handle both encoded and non-encoded)
    const pathStr = window.location.pathname;
    if (pathStr.includes('Concierto%2010_Junio_2005') || pathStr.includes('Concierto 10_Junio_2005')) {
        totalPhotos = 20;
    } else if (pathStr.includes('Concierto%202_Abril_2005') || pathStr.includes('Concierto 2_Abril_2005')) {
        totalPhotos = 7;
    } else if (pathStr.includes('Fotos_Grupo')) {
        totalPhotos = 15;
    }
    
    // Navigation functions
    function goToPhoto(num) {
        if (num >= 1 && num <= totalPhotos) {
            // Build the new path
            const newPath = galleryPath + '/' + num + '.htm';
            window.location.href = newPath;
        }
    }
    
    function goToNext() {
        if (currentNum < totalPhotos) {
            goToPhoto(currentNum + 1);
        }
    }
    
    function goToPrev() {
        if (currentNum > 1) {
            goToPhoto(currentNum - 1);
        }
    }
    
    // Keyboard event listener
    document.addEventListener('keydown', function(e) {
        // Only handle if not typing in an input field
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
            return;
        }
        
        if (e.key === 'ArrowLeft') {
            e.preventDefault();
            goToPrev();
        } else if (e.key === 'ArrowRight') {
            e.preventDefault();
            goToNext();
        }
    });
    
    // Make navigation functions available globally for button clicks
    window.photoNav = {
        next: goToNext,
        prev: goToPrev
    };
})();
