document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("search-toggle");
    const modal  = document.getElementById("search-modal");

    if (toggle && modal) {
      toggle.addEventListener("change", () => {
        if (toggle.checked) {
          modal.classList.remove("hidden");
          modal.classList.add("flex");
        } else {
          modal.classList.remove("flex");
          modal.classList.add("hidden");
        }
      });
    }
  });