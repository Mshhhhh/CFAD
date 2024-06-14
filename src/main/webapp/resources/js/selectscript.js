const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
const totalSlides = slides.length;
let currentIndex = 1; // Start from the first real slide (index 1)

function updateSlides() {
    slides.forEach((slide, index) => {
        slide.classList.remove('active');
        if (index === currentIndex) {
            slide.classList.add('active');
        }
    });
    dots.forEach((dot, index) => {
        dot.classList.remove('active');
        if (index === (currentIndex - 1) % (totalSlides - 2)) {
            dot.classList.add('active');
        }
    });
    const offset = -(currentIndex * 500) + (2000 / 2 - 20); // Adjust the offset to show the partial view of the next slides
    slider.style.transform = `translateX(${offset}px)`;
}

function pretendTo(index) {
    setTimeout(() => {
        slider.style.transition = 'none';
        currentIndex = index;
        updateSlides();
        setTimeout(() => {
            slider.style.transition = 'transform 0.5s ease-in-out';
        }, 1);
    }, 0.5);
}

document.getElementById('next').addEventListener('click', () => {
    currentIndex++;
    updateSlides();
    if (currentIndex === totalSlides - 1) {
        pretendTo(1); // Move to the first real slide
    }
});

document.getElementById('prev').addEventListener('click', () => {
    currentIndex--;
    updateSlides();
    if (currentIndex === 0) {
        pretendTo(totalSlides - 3); // Move to the last real slide
    }
});

// Initial display
updateSlides();
