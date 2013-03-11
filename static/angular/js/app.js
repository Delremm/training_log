'use strict';


// Declare app level module which depends on filters, and services
//'myApp.filters', 'myApp.services', 'myApp.directives'


var myApp = angular.module('myApp',['$strap.directives',],function($routeProvider) {

    $routeProvider
        .when('/home',{templateUrl:'home.html'})
        .when('/appOne',{templateUrl:'appOne.html',controller:'oneCtrl'})
        .when('/appTwo',{templateUrl:'appTwo.html'})
        .when('/add_workout', {templateUrl:'add_workout.html', controller:'WorkoutAddCtrl'})
        .when('/add_workout/:wo_date', {templateUrl: 'add_workout.html', controller:'WorkoutAddCtrl'})
        .otherwise({redirectTo:'/add_workout'});

});
