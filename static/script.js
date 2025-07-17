document.addEventListener('DOMContentLoaded', () => {
    const locationBtn = document.getElementById('locationBtn');
    const latitudeInput = document.getElementById('latitude');
    const longitudeInput = document.getElementById('longitude');
    const form = document.getElementById('dashboardForm');
    const submitBtn = document.getElementById('submitBtn');
    const spinner = document.getElementById('spinner');

    if (locationBtn) {
        locationBtn.addEventListener('click', () => {
            const originalText = locationBtn.innerHTML;
            locationBtn.innerHTML = 'Locating...';
            
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        latitudeInput.value = position.coords.latitude;
                        longitudeInput.value = position.coords.longitude;
                        locationBtn.innerHTML = '✅ Location Found';
                        setTimeout(() => {
                            locationBtn.innerHTML = originalText;
                        }, 2000);
                    },
                    (error) => {
                        alert("Error getting location: " + error.message);
                        locationBtn.innerHTML = originalText;
                    }
                );
            } else {
                alert("Geolocation is not supported by this browser.");
                locationBtn.innerHTML = originalText;
            }
        });
    }

    if (form) {
        form.addEventListener('submit', () => {
            if (submitBtn && spinner) {
                submitBtn.style.opacity = '0.8';
                submitBtn.style.pointerEvents = 'none';
                spinner.style.display = 'block';
            }
        });
    }

    // Leaflet map initialization
    const mapElement = document.getElementById('map');
    if (mapElement) {
        const lat = parseFloat(mapElement.getAttribute('data-lat'));
        const lon = parseFloat(mapElement.getAttribute('data-lon'));
        
        if (!isNaN(lat) && !isNaN(lon)) {
            const map = L.map('map').setView([lat, lon], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '© OpenStreetMap'
            }).addTo(map);
            L.marker([lat, lon]).addTo(map)
                .bindPopup('Selected Location')
                .openPopup();
        }
    }
});
