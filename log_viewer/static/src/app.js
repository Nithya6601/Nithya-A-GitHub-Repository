// (function(){
//     'use strict';
//     angular.module('myApp', []);
// })();
// myApp.controller('MainLogViewerController', function($scope){
//     $scope.logs = [
//         {message: 'apache logs'},
//         {message: 'access logs'},
//         {message: 'error logs'},
//         {message: 'attack logs'},
//     ];
//     $scope.filterLogs = function(log){
//         if (!$scope.searchKeyword || $scope.searchKeyword.trim() === ''){
//             return true;
//         }
//         return log.message.toLowerCase().includes($scope.searchKeyword.toLowerCase());
//     };
// });

function loadLogs(service) {
    // Simulating log loading with a timeout
    document.getElementById('logs').innerHTML = 'Loading logs for ' + service + '...';
    setTimeout(function() {
        // Replace this with actual log loading logic
        let logs = getLogsForService(service);
        document.getElementById('logs').innerHTML = logs;
    }, 1000); // Adjust timeout as needed
}
function getLogsForService(service) {
    // Replace this with actual log retrieval logic
    if (service === 'apache') {
        return '<pre>Apache Logs</pre>';
    } else if (service === 'nginx') {
        return '<pre>Nginx logs...</pre>';
    } else {
        return 'No logs found for ' + service;
    }
}
