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

			$('a.py-tst').click(function(){

				console.log('py-tst clicked.');
				$.post("/submit", { command: "test" },
					function(data) {
						console.log(data);
					});
			});	
		}
		
		/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */				
		
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