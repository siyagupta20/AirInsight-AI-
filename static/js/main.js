
document.addEventListener("DOMContentLoaded", function () {

    // Mobile navigation toggle
    const menuButton = document.getElementById("menuToggle");
    const navLinks = document.querySelector(".nav-links");

    if (menuButton && navLinks) {
        menuButton.addEventListener("click", function () {
            navLinks.classList.toggle("active");
        });
    }

    // Highlight active navigation link
    const currentPath = window.location.pathname;

    document.querySelectorAll(".nav-links a").forEach(function (link) {
        const linkPath = new URL(link.href).pathname;

        if (linkPath === currentPath) {
            link.classList.add("active");
        }
    });

});


// Display notification messages
function showNotification(message, type = "info") {

    const notification = document.createElement("div");

    notification.className = "notification " + type;
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(function () {
        notification.remove();
    }, 3500);
}


// Reusable API request function
async function fetchAPI(url) {

    try {

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Request failed: " + response.status);
        }

        return await response.json();

    } catch (error) {

        console.error("API Error:", error);

        showNotification(
            "Unable to load data. Please try again.",
            "error"
        );

        return null;
    }
}


// Show loading indicator
function showLoading(elementId) {

    const element = document.getElementById(elementId);

    if (element) {
        element.innerHTML = "<p>Loading data...</p>";
    }
}


// Hide or clear loading indicator
function clearLoading(elementId) {

    const element = document.getElementById(elementId);

    if (element) {
        element.innerHTML = "";
    }
}
