$(function($) {
    "use strict";

    jQuery(document).ready(function() {
        /* niceSelect */
        $("select").niceSelect();

        // counter Up
        if (document.querySelector('.counter') !== null) {
            $('.counter').counterUp({
                delay: 10,
                disableOn: 0,
                time: 2000
            });
        }

        // testimonials-carousel
        $(".testimonials-carousel").not('.slick-initialized').slick({
            infinite: true,
            autoplay: false,
            centerMode: true,
            centerPadding: "0px",
            focusOnSelect: false,
            speed: 1000,
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: true,
            prevArrow: "<button type='button' class='slick-prev pull-left'></button>",
            nextArrow: "<button type='button' class='slick-next pull-right'></button>",
            dots: false,
            dotsClass: 'section-dots',
            customPaging: function(slider, i) {
                var slideNumber = (i + 1),
                    totalSlides = slider.slideCount;
                return '<a class="dot" role="button" title="' + slideNumber + ' of ' + totalSlides + '"><span class="string">' + slideNumber + '/' + totalSlides + '</span></a>';
            },
            responsive: [{
                    breakpoint: 1199,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 676,
                    settings: {
                        slidesToShow: 1,
                        centerMode: false,
                    }
                }
            ]
        });

        /* Magnific Popup */
        if (document.querySelector('.popupvideo') !== null) {
            $('.popupvideo').magnificPopup({
                disableOn: 700,
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false,
            });
        }

        /* Wow js */
        new WOW().init();

    });
});