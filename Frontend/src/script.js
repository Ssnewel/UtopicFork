// Простая анимация для плавного появления при загрузке
document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll('.forum-card');
    cards.forEach((card, index) => {
        card.style.opacity = 0;
        card.style.transform = "translateY(20px)";
        setTimeout(() => {
            card.style.transition = "opacity 0.6s ease, transform 0.6s ease";
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }, index * 200); // Задержка между появлением карточек
    });
});
