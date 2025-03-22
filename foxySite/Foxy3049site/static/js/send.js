$('#registration').on('submit', function() {
    const email = $('#email').val(); const nickname = $('#nickname').val(); const password = $('#password').val();
    const csrf = $('[name="csrfmiddlewaretoken"]').val();
    if(!email){
        alert("Введи свою почту пжпжпжпжпжпжпжп (мы её точно не сольём фбр)");
        return;
    }
    $.ajax({
        url: '/reg/',
        type: 'POST',
        data: {
            'nickname': nickname,
            'email': email,
            'password': password,
            "csrfmiddlewaretoken": csrf
        },
        dataType: 'json',

        success: function(data) {
            console.log("ЕМААА. БРАТАН, ДАННЫЕ ОТПРАВИЛИСЬ")
        },

        error: function(error) {
            console.error('Error: ', error.responseText)
        }
    })
});