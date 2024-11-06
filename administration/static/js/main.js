document.addEventListener('DOMContentLoaded', function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        if (currentPath === link.getAttribute('href')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});

function getCsrfToken() {
    let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}

function showToast(icon, title) {
    const Toast = Swal.mixin({
        toast: true,
        position: "bottom-end",
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didClose: () => {
            resolve(true);  // Resuelve siempre como true
        }
    });

    Toast.fire({
        icon: icon,
        title: title
    });
}