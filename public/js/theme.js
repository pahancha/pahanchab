(() => {
  // <stdin>
  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    updateIcon(theme);
  }
  function toggleTheme() {
    const currentTheme = localStorage.getItem("theme") || "light";
    const newTheme = currentTheme === "light" ? "dark" : "light";
    setTheme(newTheme);
  }
  function updateIcon(theme) {
    const lightIcon = document.getElementById("light-icon");
    const darkIcon = document.getElementById("dark-icon");
    if (theme === "light") {
      lightIcon.style.display = "none";
      darkIcon.style.display = "inline";
    } else {
      lightIcon.style.display = "inline";
      darkIcon.style.display = "none";
    }
  }
  document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    setTheme(savedTheme);
    const themeToggle = document.getElementById("theme-toggle");
    if (themeToggle) {
      themeToggle.addEventListener("click", toggleTheme);
    }
  });
})();
