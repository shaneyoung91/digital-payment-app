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
        var dropdown_menu = $(".header-section .dropdown-menu");
        $(window).resize(function() {
            if ($(window).width() < 992) {
                dropdown_menu.removeClass('show');
            } else {
                dropdown_menu.addClass('show');
            }
        });
        if ($(window).width() < 992) {
            dropdown_menu.removeClass('show');
        } else {
            dropdown_menu.addClass('show');
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

        // language active
        var language = $(".language-content li");
        $(language).on('mouseover', function() {
            $(language).removeClass('active');
            $(this).addClass('active');
        });

        // checkbox active
        var checkbox = $(".checkbox-single");
        $(checkbox).on('mouseover', function() {
            $(checkbox).removeClass('active');
            $(this).addClass('active');
        });

        // Card Popup
        $('.card-popup .cancel').click(function() {
            $(".card-popup #limit-tab").click();
        });

        // Transactions Popup
        $('.transactions .cancel').click(function() {
            $(".card-popup #limit-tab").click();
        });

        // Confirm Popup
        $('.transfer-popup .confirm').click(function() {
            $(".transfer-popup #success-tab").click();
        });

        // transferMod Popup
        $('.transferMod').click(function() {
            if ($("#success").hasClass("active")) {
                $(".transfer-popup #transfer-tab").click();
            }
        });

        // User Active
        $('.header-section .sidebar-icon').on('click', function() {
            $('.sidebar-wrapper').toggleClass('active');
            $(".header-section").toggleClass("body-collapse");
            $(".dashboard-section").toggleClass("body-collapse");
        });

        // Sidebar Wrapper Close
        $(".sidebar-wrapper .close-btn").click(function() {
            $(".sidebar-wrapper").toggleClass("active");
            $(".header-section").toggleClass("body-collapse");
            $(".dashboard-section").toggleClass("body-collapse");
        });

        // sidebar body active
        var sidebar_wrapper = $(".sidebar-wrapper");
        var body_collapse = $(".header-section");
        $(window).resize(function() {
            if ($(window).width() > 1399) {
                sidebar_wrapper.removeClass('active');
                body_collapse.addClass('body-collapse');
            } else {
                sidebar_wrapper.addClass('active');
                body_collapse.removeClass('body-collapse');
            }
        });
        if ($(window).width() > 1399) {
            sidebar_wrapper.removeClass('active');
            body_collapse.addClass('body-collapse');
        } else {
            sidebar_wrapper.addClass('active');
            body_collapse.removeClass('body-collapse');
        }

        // Header Active
        $('.single-item .profile-area').on('click', function() {
            $('.user-content').toggleClass('active');
            $('.notifications-content').removeClass('active');
            $('.language-content').removeClass('active');
        });
        $('.single-item .notifications-btn').on('click', function() {
            $('.notifications-content').toggleClass('active');
            $('.user-content').removeClass('active');
            $('.language-content').removeClass('active');
        });
        $('.single-item .language-btn').on('click', function() {
            $('.language-content').toggleClass('active');
            $('.user-content').removeClass('active');
            $('.notifications-content').removeClass('active');
        });

        // Dropdown Active Remove
        $("section").click(function() {
            $('.user-content').removeClass('active');
            $('.notifications-content').removeClass('active');
            $('.language-content').removeClass('active');
        });

    });
});