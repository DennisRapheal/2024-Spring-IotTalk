$(function () {
    var iottalk_url = window.location.origin;   
    //var mqtt_url = 'ws://' + window.location.hostname + ':8866/mqtt';        //unencrypted connections
    var mqtt_url = 'wss://' + window.location.hostname + ':8866/mqtts';    //encrypted connections
    var mqtt_user =  'iottalk';
    var mqtt_password = 'iottalk2023';

    var profile = {
        'dm_name': 'Bulb',
        'odf_list': [Luminance, Color_O],
        'd_name': undefined,
    }
    
    var r = 255 ;
    var g = 255;
    var b = 0;
    var lum = 100;

    function draw () {
        var rr = Math.floor((r * lum) / 100);
        var gg = Math.floor((g * lum) / 100);
        var bb = Math.floor((b * lum) / 100);
        $('.bulb-top, .bulb-middle-1, .bulb-middle-2, .bulb-middle-3, .bulb-bottom, .night').css(
            {'background': 'rgb('+ rr +', '+ gg +', '+ bb +')'}
        );
    }

    function test(){
        return Math.random();
    }

    function Luminance (data) {
        lum = data[0]
        draw();
    }

    function Color_O (data) {
        r = data[0];
        g = data[1];
        b = data[2];
        draw();
    }

    function ida_init (deviceId) {
        $('font')[0].innerText = profile.d_name;
        draw();
    }


    var ida = {
        'ida_init': ida_init,
        'iottalk_url': iottalk_url,
        'mqtt_url': mqtt_url,
        'mqtt_user': mqtt_user,
        'mqtt_password': mqtt_password,
    };

    dai(profile, ida);
});
