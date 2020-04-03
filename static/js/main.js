/* JS Document */

/******************************

 [Table of Contents]

 1. Vars and Inits
 2. Init Video
 3. Init Gallery

 ******************************/

$(document).ready(function () {
    "use strict";

    /*

    1. Vars and Inits

    */

    initVideo();
    initGallery();


    /*

    2. Init Video

    */

    function initVideo() {
        $(".vimeo").colorbox(
            {
                iframe: true,
                innerWidth: 640,
                innerHeight: 409,
                maxWidth: '90%'
            });
    }

    /*

    3. Init Gallery

    */

    function initGallery() {
        if ($('.gallery_slider').length) {
            let gallery = $('.gallery_slider');
            gallery.owlCarousel(
                {
                    autoplay: true,
                    loop: true,
                    smartSpeed: 1200,
                    nav: false,
                    dots: false,
                    center: true,
                    responsive:
                        {
                            0:
                                {
                                    items: 3
                                },
                            991:
                                {
                                    items: 5
                                }
                        }
                });
        }
    }

});