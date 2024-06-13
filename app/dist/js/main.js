$(function(){
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : 'Next',
            finish : 'Confirm',
            current : ''
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            var fullname = $('#first_name').val() + ' ' + $('#last_name').val();
            var room = $('#room').val();
            var day = $('#day').val();
            var time = $('#time').val();

            $('#fullname-val').text(fullname);
            $('#room-val').text(room);
            $('#day-val').text(day);
            $('#time-val').text(time);

            return true;
        }
    });
    $("#day").datepicker({
        dateFormat: "MM - DD - yy",
        showOn: "both",
        buttonText : '<i class="zmdi zmdi-chevron-down"></i>',
    });


    $('#getqr').click(function(){

        w_token=$('#w_token').val();
        w_end_point=$('#w_end_point').val();
        w_session=$('#w_session').val();
        const data = {
            w_token: w_token,
            w_end_point: w_end_point,
            w_session: w_session
        };

        $.ajax({
            url: 'api/sessions/set-session',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                console.log("Response:", response);
            },
            error: function(xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });



});
