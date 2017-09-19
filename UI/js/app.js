$(document).delegate('#textbox', 'keydown', function(e) { 
  var keyCode = e.keyCode || e.which; 

  if (keyCode == 9) { 
    e.preventDefault(); 
    var start = $(this).get(0).selectionStart;
    var end = $(this).get(0).selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    $(this).val($(this).val().substring(0, start)
                + "\t"
                + $(this).val().substring(end));

    // put caret at right position again
    $(this).get(0).selectionStart = 
    $(this).get(0).selectionEnd = start + 1;
 } 
});

(function () {
'use strict';
angular.module('AWSApp', [])

.controller('AWSController',AWSController);
  AWSController.$inject=['$scope','$http'];
  function AWSController($scope,$http){
    $scope.languages = ["Node", "Python"];

	$scope.generatelambda = function(senddata){
	console.log("FUcntion call");
	console.log(senddata);
	$http({
                url: "http://10.103.3.186:8090/lambda/genarate",
                method: 'POST',
                headers: {
                        "Content-Type": "application/json",
                         "authorization": localStorage.getItem("Authoraization")
                 },
                data: JSON.stringify(senddata) 
        })
        .success( function (data,err) {
		console.log(typeof(data))
                alert(data.url);
        })
        .error( function (error) {
                alert(err)
        })

	}
  };
})();
