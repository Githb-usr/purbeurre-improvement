/*!
* Start Bootstrap - Creative v7.0.2 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

});

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// AJAX for delete a user favourite
// const productCard = document.getElementById('authors');
// document.querySelector("#ajax-call").addEventListener("click", event => {
//     let formData = new FormData();
//     formData.append('a', document.querySelector("#a").value);
// })

let btn = $('form button');
let input = $('form input');

$.each((btn), function(){
  $(this).click(function(){
    //  console.log($(this).prev().value)
    let formData = new FormData();
    formData.append('substitute-id', $(this).prev().value);
  })
})

const request = new Request('{% url "delete_substitutes" %}', {method: 'POST', body: formData});

fetch(request)
.then(function(response) {
    if(response.ok) {
        response.json()
        .then(function(data) {

        })
    }
})
.catch(error => console.log('The fetch function does not work properly', error));


// function refleshPage() {
//     location.reload(true);
// }

// $(document).ready(function(){
//     $("button").click(function(){
//         location.reload(true);
//     });
//   });