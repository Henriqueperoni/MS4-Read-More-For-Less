// Show Toast
$('.toast').toast('show');

// Burguer Navigation bar
// Burguer menu inspiration from: https://www.youtube.com/watch?v=gXkqy0b4M5g
const navSlide = () => {
    const burguer = document.querySelector(".burguer");
    const nav = document.querySelector(".nav-links");
    const navLinks = document.querySelectorAll(".nav-links li");
    
    // Active Burguer
    burguer.addEventListener("click", () => {
        nav.classList.toggle("nav-active");
    });
}
navSlide();

// Prevent submit forms more than once
let forms = document.getElementById('form');
forms.addEventListener('submit', function () {
    $('#submit-button').attr('disabled', true);
    console.log('hey')
});