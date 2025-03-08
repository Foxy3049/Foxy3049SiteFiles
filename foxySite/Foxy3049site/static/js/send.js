$('#buttonSubmit').click(function() {
    const email = $('#email').val(); const nickname = $('#nickname').val(); const password = $('#password').val();
    const csrf = $('[name="csrfmiddlewaretoken"]').val();
    let jsonString = JSON.stringify({nickname, email, password, csrf});
    console.log(jsonString);
    $.ajax({
        url: '/reg/',
        type: 'POST',
        data: jsonString,
        dataType: 'json',

        success: function(data) {
            console.log("ЕМААА. БРАТАН, ДАННЫЕ ОТПРАВИЛИСЬ")
        },

        error: function(error) {
            console.error('Error: ', error.responseText)
        }
    })
});