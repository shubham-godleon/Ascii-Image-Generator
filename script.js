async function uploadImage() {
    const fileInput = document.getElementById('uploadInput');
    const asciiArtDisplay = document.getElementById('asciiArtDisplay');

    if (!fileInput.files || fileInput.files.length === 0) {
        alert('Please select an image file.');
        return;
    }

    console.log(fileInput);

    const imageData = new FormData();
    imageData.append('image', fileInput.files[0]);

    console.log(imageData);

    try {
        const response = await fetch('https://godleon.pythonanywhere.com/upload', {
            method: 'POST',
            body: imageData
        });

        if (!response.ok) {
            throw new Error('Failed to upload image.');
        }
    
    // Expecting the server to respond with a file download
        const blob = await response.blob();

        // Create a temporary anchor element to trigger the download
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'ascii_art.txt'; // Specify the filename
        document.body.appendChild(a);
        a.click();

        // Clean up
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to process image.');
    }
}