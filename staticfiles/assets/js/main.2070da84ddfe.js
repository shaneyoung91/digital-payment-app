$(function($) {
    "use strict";

    jQuery(document).ready(function() {

        // preloader
        $("#preloader").delay(300).animate({
            "opacity": "0"
        }, 500, function() {
            $("#preloader").css("display", "none");
        });

        // Scroll Top
        var ScrollTop = $(".scrollToTop");
        $(window).on('scroll', function() {
            if ($(this).scrollTop() < 500) {
                ScrollTop.removeClass("active");
            } else {
                ScrollTop.addClass("active");
            }
        });
        $('.scrollToTop').on('click', function() {
            $('html, body').animate({
                scrollTop: 0
            }, 500);
            return false;
        });

        // Navbar Dropdown
        $(window).resize(function() {
            if ($(window).width() < 992) {
                $(".dropdown-menu").removeClass('show');
            } else {
                $(".dropdown-menu").addClass('show');
            }
        });
        if ($(window).width() < 992) {
            $(".dropdown-menu").removeClass('show');
        } else {
            $(".dropdown-menu").addClass('show');
        }

        // Sticky Header
        var fixed_top = $(".header-section");
        $(window).on("scroll", function() {
            if ($(window).scrollTop() > 50) {
                fixed_top.addClass("animated fadeInDown header-fixed");
            } else {
                fixed_top.removeClass("animated fadeInDown header-fixed");
            }
        });

        // Blog Reply btn
        var replybtn = $(".reply-btn");
        $(replybtn).on('click', function() {
            $(this).next().slideToggle('slow');
        });

    });
});