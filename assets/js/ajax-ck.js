/**
 * 		BotPi js module:
 * 			ajax.js
 *
 *		desc:
 * 			the BotPi AJAX JavaScript module.		
 * 		
 * 		requires:
 * 			jQuery
 */var botpi=function(e,t){e.ajax=function(e){function n(){e("a.ctrl").click(function(){e("a.ctrl.active").not(this).removeClass("active");e(this).toggleClass("active")});e("a.stp").click(function(){e(".jumbotron a.ctrl").removeClass("active")});e("a.fwd").click(function(){e.post("/command",{command:"fwd"})});e("a.lft").click(function(){e.post("/command",{command:"lft"})});e("a.stp").click(function(){e.post("/command",{command:"stp"})});e("a.rgt").click(function(){e.post("/command",{command:"rgt"})});e("a.rev").click(function(){e.post("/command",{command:"rev"})})}var t="";return{init:n}}(t);return e}(botpi||{},jQuery);botpi.init.register(botpi.ajax.init);