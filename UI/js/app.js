(function () {
'use strict';

angular.module('AWSApp', [])

.controller('AWSController',AWSController);
  AWSController.$inject=['$scope'];
  function AWSController($scope){
    $scope.languages = ["Node", "Python"];
  };
})();
