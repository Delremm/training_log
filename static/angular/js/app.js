'use strict';


// Declare app level module which depends on filters, and services
//'myApp.filters', 'myApp.services', 'myApp.directives'

angular.module('woList', []);

var myApp = angular.module('myApp',['$strap.directives'],function($routeProvider) {

    $routeProvider
        .when('/home',{templateUrl:'home.html'})
        .when('/appOne',{templateUrl:'appOne.html',controller:'oneCtrl'})
        .when('/appTwo',{templateUrl:'appTwo.html'})
        .when('/add_workout', {templateUrl:'add_workout.html', controller:'WorkoutAddCtrl'})
        .when('/add_workout/:wo_date', {templateUrl: 'add_workout.html', controller:'WorkoutAddCtrl'})
        .otherwise({redirectTo:'/add_workout'});

});

myApp.directive('logWr', function($compile){
    return {
        restrict: 'EAC',
        transclude: true,
        scope: {
            wr:'=wr',
            exercise: '=exercise',
            units: '=units'
        },
        replace: true,
        template: '<div>' +
            '<div ng-transclude></div>' +
            '<div></div>' +
            '</div>',
        // The linking function will add behavior to the template
        link: function(scope, element, attrs) {
            var wr_elem = angular.element(element.children()[1]);
            if (scope.exercise.type == 1){
                for (var i in scope.wr[0]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[0]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[0]['+i+'].unit" ng-options="u for u in units[1][0][0]" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
                wr_elem.append(' x ');
                for (var i in scope.wr[1]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[1]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[1]['+i+'].unit" ng-options="u for u in units[1][1][0]" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
            }
            else if (scope.exercise.type == 2){
                for (var i in scope.wr[0]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[0]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[0]['+i+'].unit" ng-options="u for u in units[2][0][0]" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
                wr_elem.append('<br>');
                for (var i in scope.wr[1]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[1]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[1]['+i+'].unit" ng-options="u for u in units[2][1]['+i+']" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
            }
            else if (scope.exercise.type == 3){
                for (var i in scope.wr[0]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[0]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[0]['+i+'].unit" ng-options="u for u in units[3][0][0]" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
                wr_elem.append('<br>');
                for (var i in scope.wr[1]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[1]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[1]['+i+'].unit" ng-options="u for u in units[3][1]['+i+']" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
            }
            else if (scope.exercise.type == 4){
                for (var i in scope.wr[0]){
                    var w_input = angular.element($compile('<input type="text" ng-model="wr[0]['+i+'].value" class="input-small">')(scope));
                    wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[0]['+i+'].unit" ng-options="u for u in units[4][0]['+i+']" class="btn btn-mini" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
                wr_elem.append('<br>');
                for (var i in scope.wr[1]){
                    //var w_input = angular.element($compile('<input type="text" ng-model="wr[1]['+i+'].value" class="input-small">')(scope));
                    //wr_elem.append(w_input);
                    var w_unit_t = '<select ng-model="wr[1]['+i+'].unit" ng-options="u for u in units[4][1][0]" class="btn btn-small" tabindex="-1">';
                    var w_unit = angular.element($compile(w_unit_t)(scope));
                    wr_elem.append(w_unit);
                }
            }
        }
    }
});