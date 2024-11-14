
const sidebarLinks = document.querySelectorAll('.sidebar-links li a');

sidebarLinks.forEach(link => {
    link.addEventListener('click', function() {
        
        sidebarLinks.forEach(link => link.classList.remove('active'));
        this.classList.add('active');
    });
});
