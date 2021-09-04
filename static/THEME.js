 // function to set a given theme/color-scheme
 function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}
const SWITCH = document.getElementById("theme_selector");

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
        SWITCH.innerHTML = "Switch to Dark Theme"
    } else {
        setTheme('theme-dark');
        SWITCH.innerHTML = "Switch to Light Theme"

    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
        
    } else {
        setTheme('theme-light');
      document.getElementById('slider').checked = true;
      
    }
})();