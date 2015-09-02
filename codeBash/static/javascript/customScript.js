var helloApp = angular.module( "helloApp", ['ui.bootstrap', 'ngRoute'] );
helloApp.controller('mainController', function($scope) {

    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

// create the controller and inject Angular's $scope
helloApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

helloApp.controller('aboutController', function($scope) {
    $scope.message = 'Look! I am an about page.';
});

helloApp.controller('contactController', function($scope) {
    $scope.message = 'Contact us! JK. This is just a demo.';
});
