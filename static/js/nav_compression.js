const toggle = document.getElementById('nav-toggle');
const nav = document.getElementById('nav-bar');

toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen);
});