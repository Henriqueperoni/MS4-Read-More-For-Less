// Bootstrap Tabs
$('#myTab a').on('click', function (event) {
    event.preventDefault()
    $(this).tab('show')
});

// Plans Animation
if (window.matchMedia("(min-width: 1200px)").matches) {
    const priceAnim = gsap.timeline({ defaults: { ease: "power1.out" } });
    priceAnim.from("#pills-home > div:nth-child(2) > div" , { opacity: 0, duration: 1.8 }).delay(0.1);
    priceAnim.from("#pills-home > div:nth-child(1) > div", { x: 200, opacity: 0, duration: 1.2 }, "-=1.2");
    priceAnim.from("#pills-home > div:nth-child(3) > div", { x: -200, opacity: 0, duration: 1.2 }, "-=1.2");
};