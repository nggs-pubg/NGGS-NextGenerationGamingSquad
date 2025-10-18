const navTrigger = document.querySelector(".site-nav__trigger");
const navMenu = document.querySelector(".site-nav__menu");
const scrollButtonWrapper = document.querySelector(".scroll-to-top");
const scrollButton = scrollButtonWrapper?.querySelector("button");
const yearElement = document.getElementById("ano");
const contactForm = document.getElementById("contact-form");
const contactFormSubmit = contactForm?.querySelector('button[type="submit"]');
const contactFormFeedback = contactForm?.querySelector(".form-feedback");

function toggleMenu(forceOpen) {
  if (!navTrigger || !navMenu) return;

  const isOpen =
    typeof forceOpen === "boolean" ? !forceOpen : navTrigger.getAttribute("aria-expanded") === "true";
  const nextState = !isOpen;

  navTrigger.setAttribute("aria-expanded", String(nextState));
  navMenu.classList.toggle("is-open", nextState);
}

navTrigger?.addEventListener("click", () => toggleMenu());

navMenu?.addEventListener("click", (event) => {
  const target = event.target;
  if (target instanceof HTMLElement && target.tagName.toLowerCase() === "a") {
    toggleMenu(false);
  }
});

document.addEventListener("click", (event) => {
  if (!navTrigger || !navMenu) return;
  if (navMenu.contains(event.target) || navTrigger.contains(event.target)) return;

  if (navMenu.classList.contains("is-open")) {
    toggleMenu(false);
  }
});

if (scrollButtonWrapper && scrollButton) {
  const updateScrollButtonVisibility = () => {
    if (window.scrollY > window.innerHeight * 0.6) {
      scrollButtonWrapper.removeAttribute("hidden");
    } else {
      scrollButtonWrapper.setAttribute("hidden", "");
    }
  };

  window.addEventListener("scroll", updateScrollButtonVisibility, { passive: true });
  updateScrollButtonVisibility();

  scrollButton.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

if (yearElement) {
  yearElement.textContent = new Date().getFullYear().toString();
}

if (contactForm && contactFormSubmit && contactFormFeedback) {
  contactForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    contactFormFeedback.textContent = "Enviando...";
    contactFormFeedback.classList.remove("is-success", "is-error");
    contactFormSubmit.disabled = true;

    try {
      const formData = new FormData(contactForm);
      const response = await fetch(contactForm.action, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Não foi possível enviar sua mensagem.");
      }

      contactFormFeedback.textContent =
        "Mensagem enviada com sucesso! Em breve nossa equipe retorna o contato.";
      contactFormFeedback.classList.add("is-success");
      contactForm.reset();
    } catch (error) {
      console.error(error);
      contactFormFeedback.textContent =
        "Ops! Tente novamente em instantes ou fale conosco pelo Discord.";
      contactFormFeedback.classList.add("is-error");
    } finally {
      contactFormSubmit.disabled = false;
    }
  });
}

window.addEventListener("load", () => {
  if (typeof AOS !== "undefined") {
    AOS.init({
      once: true,
      duration: 700,
      easing: "ease-out",
      offset: 120,
    });
  }
});
