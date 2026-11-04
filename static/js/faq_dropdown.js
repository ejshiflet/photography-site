document.addEventListener("DOMContentLoaded", () => {
    const faqQuestions = document.querySelectorAll(".faq-question");
  
    faqQuestions.forEach((question) => {
      question.addEventListener("click", () => {
        const isExpanded = question.getAttribute("aria-expanded") === "true";
  
        // OPTIONAL: Close all other open FAQ dropdowns before opening the new one
        faqQuestions.forEach((otherQuestion) => {
          if (otherQuestion !== question) {
            otherQuestion.setAttribute("aria-expanded", "false");
          }
        });
  
        // Toggle state of the clicked question
        question.setAttribute("aria-expanded", !isExpanded);
      });
    });
  });