// Check if 'mainBoardCanvas' is already declared
if (typeof mainBoardCanvas === 'undefined') {
    const mainBoardCanvas = document.getElementById('mainBoardChart');
    if (mainBoardCanvas) {
        const mainBoardCtx = mainBoardCanvas.getContext('2d');
        new Chart(mainBoardCtx, {
            type: 'doughnut',
            data: {
                labels: ['Upcoming', 'New Listed', 'Ongoing'],
                datasets: [{
                    data: [15, 25, 2],
                    backgroundColor: ['#6366f1', '#06b6d4', '#8b5cf6'],
                    borderWidth: 0,
                    cutout: '70%'
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
}

// Add hover effects to menu items
document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('mouseenter', () => {
        if (!item.classList.contains('active')) {
            item.style.backgroundColor = '#BFCFE7';
        }
    });

    item.addEventListener('mouseleave', () => {
        if (!item.classList.contains('active')) {
            item.style.backgroundColor = '';
        }
    });
});

// Add hover effects to quick links
document.querySelectorAll('.visit-link').forEach(link => {
    link.addEventListener('mouseenter', () => {
        link.style.color = '#6366f1';
    });

    link.addEventListener('mouseleave', () => {
        link.style.color = '#6b7280';
    });
});

// Load page function for sidebar links
function loadPage(page) {
    fetch(page)
        .then(response => response.text())
        .then(data => {
            document.getElementById('content').innerHTML = data;
        })
        .catch(error => console.log('Error loading page:', error));
}

// Event listeners for sidebar links
document.getElementById('dashboardLink').addEventListener('click', function () {
    loadPage('Dashboard.html');
});

document.getElementById('manageIpoLink').addEventListener('click', function () {
    loadPage('manage-ipo.html');
});

document.getElementById('ipoSubscriptionLink').addEventListener('click', function () {
    loadPage('ipo-subscription.html');
});
