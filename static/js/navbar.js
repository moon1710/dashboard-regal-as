document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.getElementById("sidebar");
  // Iniciar el sidebar colapsado
  sidebar.classList.add("collapsed");

  // Toggle al hacer click en el botón
  document.getElementById("expandBtn").addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
  });
});
