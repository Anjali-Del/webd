$(document).ready(function() {
	
	$('form').on('submit', function(event) {
		event.preventDefault();

		var formdata = new FormData($('form')[0]);

		$.ajax({
			xhr : function() {
				var xhr = new window.XMLHttpRequest();
				xhr.upload.addEventListener('progress', function(e){
					if(e.lengthComputable) {
						var percentage = Math.round((e.loaded/e.total)*100);
						$('#progressbarid').attr('aria-valuenow', percentage).css('width', percentage+'%').text(percentage+'%')
					}
				});
				return xhr;
			},
			type: 'POST',
			url: './',
			data: formdata,
			processData: false,
			contentType: false,
			success: function() {
				window.location = "/img/success/"
			}
		});
	});
});