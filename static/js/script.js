$('.toast').toast('show');

const navSlide = () => {
    const burguer = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links')

    burguer.addEventListener("click", () => {
        nav.ClassList.toggle('nav-active');
    });
}

navSlide();