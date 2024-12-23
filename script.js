(function() {
    let onpageLoad = localStorage.getItem("theme") || "";
    let element = document.body;
    element.classList.add(onpageLoad);
    document.getElementById("theme").textContent = localStorage.getItem("theme") || "light";
  })();
  
  function themeToggle() {
    let element = document.body;
    element.classList.toggle("dark-mode");
    let theme = localStorage.getItem("theme");
    if (theme && theme === "dark-mode") {
    localStorage.setItem("theme", "");
    console.log("light mode")
    } else {
    localStorage.setItem("theme", "dark-mode");
    console.log("dark mode")
    }
    
    document.getElementById("theme").textContent = localStorage.getItem("theme");
}