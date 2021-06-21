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

var socket = io();

var queryString = window.location.search;
var urlParams = new URLSearchParams(queryString);
var event_id = urlParams.get("event_id");

$(() => {

    socket.on('connect', () => {
        socket.emit('join', {event_id: event_id});
    });

    socket.on('push message', (data) => {
        data.messages.forEach((message) => {
            $("#messages").append("<div class='messagewrp'><span class='message'><span class='messagetxt'>"+message.body+"</span></span></div>");
        });
        
        $("#messages").scrollTop($("#messages")[0].scrollHeight);
    });

    $("#send").click(() => {
        const body = $("#compose").val();

        socket.emit( "send message", { body: body, event_id: event_id} );
        $("#compose").val("");
    });
});