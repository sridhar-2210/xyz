document.addEventListener('DOMContentLoaded', function () {
    // Handle login form submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            // Add your login validation here
            window.location.href = 'index.html'; // Redirect to home page after login
        });
    }
});
