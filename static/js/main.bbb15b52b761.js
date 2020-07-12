$( document ).ready(function() {
	
	
	/* AJAX ON SEARCH */
	$( "#search-form" ).on( "submit", function(e) {
		e.preventDefault();

		
		if( !$("input[name='x']").val() ) {
			return false;
		}
		var x = $("input[name='x']").val();
		console.log(x);
		
        $.ajax({
            type: 'get',
            url: "/ninjify/ajax/getNinjify",
            data: {"x": x, "ajax": 1},
            success: function (response) {

				$(".section_result").remove();
				renderResultTable();
				renderResultNinjify(response["name"],response["result_id"]);
				$("html, body").animate({ scrollTop: $('.section-results').offset().top }, 1000);
				
				
               
            },
            error: function (response) {
                console.log(response)
            }
        })
	});


	/* GET HTLM FOR RESULT TABLE */
	function renderResultTable(){

		$.ajax({
            type: 'get',
            url: "/ninjify/ajax/getResultTable",
            success: function (response) {
				
				$(".section-result-table").html(response);
               
            },
            error: function (response) {
                console.log(response)
            }
        })

	}


	/* GET HTLM FOR NINJIFY RESULT */
	function renderResultNinjify(ninjify_name,result_id){

		$.ajax({
            type: 'get',
            url: "/ninjify/ajax/getResultNinjify",
            success: function (response) {
				
				$(".section-result-ninjify").html(response);
				$("#search-result").html(ninjify_name);
				$("#search-permalink").html("<span>Partager votre résultat!</span> <a target='_blank' href='/ninjify/resultat/" + result_id + "'>/ninjify/resultat/" + result_id + "</a>");

            },
            error: function (response) {
                console.log(response)
            }
        })

	}


});