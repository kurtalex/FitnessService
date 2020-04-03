/* JS Document */

/******************************

 [Table of Contents]

 1. Vars and Inits
 2. Init Progress Bars

 ******************************/

$(document).ready(function () {
    "use strict";

    /*

    1. Vars and Inits

    */
    let ctrl = new ScrollMagic.Controller();

    initProgressBars();

    /*

    2. Init Progress Bars

    */

    function initProgressBars() {
        if ($('.skill_bars').length) {
            let eles = $('.skill_bars');

            eles.each(function (i) {
                let ele = $(this);
                let elePerc = ele.data('perc');
                let eleName = '#' + ele.data('name');

                let statsScene = new ScrollMagic.Scene({
                    triggerElement: this,
                    triggerHook: 'onEnter',
                    reverse: false
                })
                    .on('start', function () {
                        let pbar = new ProgressBar.Line(eleName,
                            {
                                strokeWidth: 4,
                                easing: 'easeInOut',
                                duration: 1400,
                                color: '#ff9711',
                                trailColor: 'transparent',
                                trailWidth: 1,
                                svgStyle: {width: '100%', height: '100%'},
                                text: {
                                    style: {
                                        // Text color.
                                        // Default: same as stroke color (options.color)
                                        color: '#717a85',
                                        position: 'absolute',
                                        right: '0',
                                        top: '-20px',
                                        padding: 0,
                                        margin: 0,
                                        transform: null
                                    },
                                    autoStyleContainer: false
                                },
                                from: {color: '#ff9711'},
                                to: {color: '#ff9711'},
                                step: function (state, bar) {
                                    bar.setText(Math.round(bar.value() * 100) + ' %');
                                }
                            });
                        pbar.animate(elePerc);
                    })
                    .addTo(ctrl);
            });
        }
    }

});