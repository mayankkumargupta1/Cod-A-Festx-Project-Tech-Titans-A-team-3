// -------------------------Typed Js-----------------------------
const typed = new Typed('.multiple-text', {
	strings: ['One Step Towards Healthy Life...', 'एक कदम मानवता की ओर...'],
	typeSpeed: 70,
	backSpeed: 70,
	backDelay: 1000,
	loop: true,
});

// ------------Content Logic---------

const content = document.querySelectorAll('.content'),
	dot = document.querySelectorAll('.dot');
let counter = 1;
slidefun(counter);

let timer = setInterval(autoSlide, 8000);
function autoSlide() {
	counter += 1;
	slidefun(counter);
}
function plusSlides(n) {
	counter += n;
	slidefun(counter);
	resetTimer();
}
function currentSlide(n) {
	counter = n;
	slidefun(counter);
	resetTimer();
}
function resetTimer() {
	clearInterval(timer);
	timer = setInterval(autoSlide, 6000);
}
function slidefun(n) {

	let i;
	for (i = 0; i < content.length; i++) {
		content[i].style.display = "none";
	}
	for (i = 0; i < dot.length; i++) {
		dot[i].className = dot[i].className.replace(' active', '');
	}
	if (n > content.length) {
		counter = 1;
	}
	if (n < 1) {
		counter = content.length;
	}
	content[counter - 1].style.display = "block";
	dot[counter - 1].className += " active";
}

ScrollReveal({
	distance: '20px',
	duration: 3000,
	delay: 800,
});
ScrollReveal().reveal('.box-container', { origin: 'right' });
ScrollReveal().reveal('.about-us', { origin: 'bottom' });
ScrollReveal().reveal('.goals-part', { origin: 'top' });




document.addEventListener('DOMContentLoaded', () => {
	const counters = document.querySelectorAll('.counter');

	counters.forEach(counter => {
		counter.innerText = '0';
		const updateCounter = () => {
			const target = +counter.getAttribute('data-count').replace(/,/g, '');
			const duration = 2000;
			const startTime = performance.now();

			const animate = (currentTime) => {
				const elapsedTime = currentTime - startTime;
				const progress = Math.min(elapsedTime / duration, 1);
				const currentCount = Math.floor(progress * target);

				if (currentCount >= 1000000) {
					counter.innerText = (currentCount / 1000000).toFixed(1);
				} else if (currentCount >= 1000) {
					counter.innerText = (currentCount / 1000).toFixed(1);
				} else {
					counter.innerText = currentCount.toLocaleString();
				}

				if (progress < 1) {
					requestAnimationFrame(animate);
				} else {
					counter.innerText = target.toLocaleString() + '+';
				}
			};

			requestAnimationFrame(animate);
		};

		updateCounter() + '+';
	});
});


let scrollContainer = document.querySelector(".gallery");
let backBtn = document.getElementById("backBtn");
let nextBtn = document.getElementById("nextBtn");

nextBtn.addEventListener("click", () => {
	scrollContainer.style.scrollBehaviour = 'smooth';
	scrollContainer.scrollLeft += 1200;
});

backBtn.addEventListener("click", () => {
	scrollContainer.style.scrollBehaviour = 'smooth';
	scrollContainer.scrollLeft -= 1200;
});