function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}





// Get the button
let mybutton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

function changeStyles(routes) {
  var links = document.querySelectorAll('a');
  var currentRoute = window.location.pathname;

  links.forEach(function (link) {
    var href = link.getAttribute('href');
    if (link.closest('.lang-list') && routes.some(function (route) { return currentRoute.startsWith(route); }) && currentRoute === href) {
      link.style.backgroundColor = 'white';
      link.style.color = 'black';
    }
  });
}

var routes = [
  "/top",
  "/india",
  "/world",
  "/politics",
  "/business",
  "/tech",
  "/sports",
  "/entertainment", "/",
]

changeStyles(routes)


window.addEventListener('load', function () {
  var loader = document.getElementById('loader');
  loader.style.display = 'none';
});

