/**
 * 		BotPi js module:
 * 			ajax.js
 *
 *		desc:
 * 			the BotPi AJAX JavaScript module.		
 * 		
 * 		requires:
 * 			jQuery
 */

var botpi = (function( app, $ ) {
	
	/* define new module */
	app.ajax = (function($){
		
		// private vars
		var _name = '';
			
		/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
		
		function _init() {

			$('a.ctrl').click(function(){
				// $(this).toggleClass('checked').siblings().removeClass('checked');
				$('a.ctrl.active').not(this).removeClass('active');
				$(this).toggleClass('active');
			});

			$('a.stp').click(function(){
				$('.jumbotron a.ctrl').removeClass('active');
			});			

			$('a.fwd').click(function(){
				$.post("/command", { command: "fwd" });
			});

			$('a.lft').click(function(){
				$.post("/command", { command: "lft" });			
			});

			$('a.stp').click(function(){
				$.post("/command", { command: "stp" });
			});

			$('a.rgt').click(function(){
				$.post("/command", { command: "rgt" });			
			});

			$('a.rev').click(function(){

				$.post("/command", { command: "rev" });
			});										
		}
		
		/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * /		
		
		/* return public-facing methods and/or vars */
		return {
			init : _init
		};
		
	}($));
	
	return app; /* return augmented app object */
	
}( botpi || {}, jQuery )); /* import app if exists, or create new; import jQuery */

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

// register this module for initialization
botpi.init.register( botpi.ajax.init );