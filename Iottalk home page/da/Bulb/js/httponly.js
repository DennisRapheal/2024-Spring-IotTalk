var http = (function () {
    var _switch = undefined;
    function init(callback){
        _switch = callback;
        console.log('You can call http.only() in console to use HTTP only.');
    }
 
    function only(){
        if (!_switch){
            console.error('No HTTP switch function registered.');
            return '';
        }

        _switch();
        return 'Switch to HTTP only.';
    }

    return {
        'init': init,
        'only': only,
    };
})();
