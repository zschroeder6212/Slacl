var last_time = 0;

function update_chat() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const event_id = urlParams.get("event_id");

    $.post( "/api/chat/messages", { event_id:  event_id, after: last_time}, function(data){
        data.messages.forEach(function(message)
        {
            $("#messages").append("<div class='messagewrp'><span class='message'><span class='messagetxt'>"+message.body+"</span></span></div>");
        });

        if(data.messages.length > 0)
        {
            last_time = data.messages[data.messages.length - 1].time;
            $("#messages").scrollTop($("#messages")[0].scrollHeight);
        }
    } );
}

$(function() {
    update_chat();
    setInterval(update_chat, 3000);

    $("#send").click(function()
    {
        const body = $("#compose").val();
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        const event_id = urlParams.get("event_id");
        $.post( "/api/chat/send", { body: body, event_id:  event_id}, update_chat );
        $("#compose").val("");
    });
});