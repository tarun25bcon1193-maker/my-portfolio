const themeToggle = document.getElementById("themeToggle");
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");
const projectSearch = document.getElementById("projectSearch");
const technologyFilter = document.getElementById("technologyFilter");
const projectCards = document.querySelectorAll(".project-card");
const noResults = document.getElementById("noResults");

// Light and dark mode
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  const darkMode = document.body.classList.contains("dark");
  themeToggle.textContent = darkMode ? "☀️" : "🌙";
  themeToggle.setAttribute(
    "aria-label",
    darkMode ? "Switch to light mode" : "Switch to dark mode"
  );
});

// Mobile navigation
menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("open");
});

navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => navLinks.classList.remove("open"));
});

// Search and filter projects
function filterProjects() {
  const query = projectSearch.value.toLowerCase().trim();
  const selectedTechnology = technologyFilter.value;
  let visibleCount = 0;

  projectCards.forEach((card) => {
    const searchableText =
      (card.innerText + " " + card.dataset.search).toLowerCase();
    const technologies = card.dataset.tech.split(" ");

    const matchesSearch = searchableText.includes(query);
    const matchesTechnology =
      selectedTechnology === "all" ||
      technologies.includes(selectedTechnology);

    const showCard = matchesSearch && matchesTechnology;
    card.hidden = !showCard;

    if (showCard) visibleCount++;
  });

  noResults.hidden = visibleCount !== 0;
}

projectSearch.addEventListener("input", filterProjects);
technologyFilter.addEventListener("change", filterProjects);

// Current year in footer
document.getElementById("year").textContent = new Date().getFullYear();