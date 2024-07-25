let device_id = null;
let _ENDPOINT =  'https://1.iottalk.tw';
let password = ''

function set_device_id(d_id){
    device_id = d_id;
    csmapi.set_endpoint(_ENDPOINT);   
}

function get_alias(device_id, df_name, callback){
    var alias;
    var ajax_obj = $.ajax({
        url: _ENDPOINT +'/get_alias/' + device_id+ '/' + df_name,
        type: 'GET',
        data: {alias},
    }).done(function(alias){
        if(typeof callback === 'function') callback(df_name, alias['alias_name'][0]);
    });
}

function update_alias(df_name, alias){
    if (alias!=undefined) $('.'+df_name)[0].innerText = alias;
}

function load_alias(device_id, df_main_name, count){
    for(var index=1; index<=count; index++){
	    get_alias(device_id, df_main_name+index.toString(), update_alias);
    }
}

function update_switch_state(data, exception, df_name){
    if (data.length != 0)
        if (data[0][1][0] == 1) $('#'+df_name).bootstrapToggle('on');
	else $('#'+df_name).bootstrapToggle('off');
}

function load_state(df_main_name, count, callback){
    for(var index=1; index<=count; index++){
        csmapi.pull(device_id, password, df_main_name+String(index), callback);
    }
}

function close_page(result){
    if (result){ console.log('Deregister successfully.');}
    else{ console.log('Failed to deregister!');}
    setTimeout("document.location.href=window.location.origin", 1000 )

}

function dereg(device_id) {
    var decision = confirm("Warning : Delete this Controller.\nAre you sure?");
    if (decision){ 
        console.log('Deregister this reomte control and close the page now.');
	csmapi.deregister(device_id, close_page);
    }
    else{
        console.log('Won\'t deregister.');
    }
}

//Switch
$(function () {
    $(document).on('click', '.toggle', function() {
	var self_id = $(this)[0].childNodes[0].id;
	var clicked = $(this).hasClass('btn-primary');
        csmapi.push(device_id, password, self_id, [clicked ? 1 : 0]);
    });
});


// Knob
$(function () {
    // Init vars
    var knobs = $('.knob-container');
    var knobVal = [];
    knobVal.length = knobs.length;

    // Init knob appearance
    knobs.knobKnob({
        startDeg: -45,
        degRange: 270,
        initVal: 0.0,
        numColorbar: 31,
    });

    // Check knob val updated or not
    function knobChecker() {
        // Check update
        for(var i=0; i<knobs.length; ++i)
            if( knobVal[i] !== $(knobs[i]).val() ) {
                knobVal[i] = $(knobs[i]).val().toString();
                csmapi.push($(knobs[i]).attr('deviceId'), password, $(knobs[i]).attr('dfName'), [parseFloat(knobVal[i])]);
            }
    }
    setInterval(knobChecker, 250);
});

// Keypad
$(function () {
    $(document).on('submit', '.keypad', function(e) {
		e.preventDefault();
		var self_id = this.id;
        csmapi.push(device_id, password, self_id, [parseFloat(e.originalEvent.submitter.value)]);
    });
});

// Button
$(function () {
    $(document).on('click', '.btn', function() {
		var self_id = $(this)[0].id;
        csmapi.push(device_id, password, self_id, [1]);
    });
});

// Color-I
$(function () {
    $(document).on('change', '.colorI', function() {
		var self_id = $(this)[0].id;
		let r = parseInt("0x" + this.value.slice(1, 3));
		let g = parseInt("0x" + this.value.slice(3, 5));
		let b = parseInt("0x" + this.value.slice(5, 7));
        csmapi.push(device_id, password, self_id, [r, g, b]);
    });
});

// $(function () {
//     console.log('RC JS has been successfully loaded.');
    
// });
