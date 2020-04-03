/* JS Document */

/******************************

 [Table of Contents]

 1. Vars and Inits
 4. Init Isotope


 ******************************/

$(document).ready(function () {
    "use strict";

    /*

    1. Vars and Inits

    */

    initIsotope();

    /*

    4. Init Isotope

    */

    function initIsotope() {
        let sortingButtons = $('.item_sorting_btn');

        if ($('.grid').length) {
            let grid = $('.grid').isotope({
                itemSelector: '.grid-item',
                percentPosition: true,
                masonry:
                    {
                        horizontalOrder: true
                    },
                getSortData:
                    {
                        price: function (itemElement) {
                            let priceEle = $(itemElement).find('.product_price').text().replace('$', '');
                            return parseFloat(priceEle);
                        },
                        name: '.tt_class_title'
                    }
            });

            // Filtering
            $('.item_filter_btn').on('click', function () {
                let buttons = $('.item_filter_btn');
                buttons.removeClass('active');
                $(this).addClass('active');
                let filterValue = $(this).attr('data-filter');
                grid.isotope({filter: filterValue});
            });
        }
    }

});