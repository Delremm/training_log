'use strict';

/* Controllers */
function MainCtrl($scope, $route, $routeParams, $location){
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
}

function FormController($scope) {
    var user = $scope.user = {
        name: 'John Smith',
        address:{line1: '123 Main St.', city:'Anytown', state:'AA', zip:'12345'},
        contacts:[{type:'phone', value:'1(234) 555-1212'}]
    };
    $scope.state = /^\w\w$/;
    $scope.zip = /^\d\d\d\d\d$/;

    $scope.addContact = function() {
        user.contacts.push({type:'email', value:''});
    };

    $scope.removeContact = function(contact) {
        for (var i = 0, ii = user.contacts.length; i < ii; i++) {
            if (contact === user.contacts[i]) {
                $scope.user.contacts.splice(i, 1);
            }
        }
    };
}
function ExercisesToList(exercises){
    var exrcs = [];
    var ss = exercises;
    for (var i in ss){
        alert(ss)
        exrcs.push(ss[i].name);
    }
    return exrcs
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var weekday=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

var monthNames = [ "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December" ];

function DatesBefore(date){
    var date_list = [];
    for (var i = 5; i>0; i--){
        var d = new Date(date);
        d.setDate(d.getDate()-i);
        date_list.push([d.toISOString().slice(0,10), '' + monthNames[d.getMonth()] + ' ' + d.getDate() + ' ' + weekday[d.getDay()]]);
    }
    return date_list
}
function DatesAfter(date){
    var date_list = [];
    for (var i = 1; i< 5; i++){
        var d = new Date(date);
        d.setDate(d.getDate()+i);
        date_list.push([d.toISOString().slice(0,10), '' + monthNames[d.getMonth()] + ' ' + d.getDate() + ' ' + weekday[d.getDay()]]);
    }
    return date_list
}
function WorkoutAddCtrl($scope, $http, $routeParams){

    //today
    var myDate = new Date();
    var today = new Date();
    var tzo = (myDate.getTimezoneOffset()/60)*(-1);
    myDate.setHours(myDate.getHours() + tzo);
    $scope.date = myDate;
    $scope.today = today;

    if ($routeParams.wo_date){
        var re = /^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$/;
        if (re.test($routeParams.wo_date)){
            var wo_date = $scope.wo_date = $routeParams.wo_date;
            myDate = Date(wo_date);
            console.log('gg:');
            console.log(myDate);
        }
        else {
            var wo_date = $scope.wo_date = myDate.toISOString().slice(0,10);
            //$routeParams.wo_date = wo_date;
        }
    }
    else {
        var wo_date = $scope.wo_date = myDate.toISOString().slice(0,10);
    }
    var d = new Date(wo_date);
    var wo_date_full = $scope.wo_date_full = '' + monthNames[d.getMonth()] + ' ' + d.getDate() + ' ' + weekday[d.getDay()];



    var date_b_list = $scope.date_b_list = DatesBefore(wo_date);
    for (var i in date_b_list){
        console.log(date_b_list[i]);
    }

    console.log(wo_date);
    var date_a_list = $scope.date_a_list = DatesAfter(wo_date);
    for (var i in date_a_list){
        console.log(date_a_list[i]);
    }



    //loading workout, json api
    $http.get("/log/api/workouts/" + wo_date + '/').success(function(data){
        $scope.workout = data;
        var ggg = $scope.workout.data;
        $scope.workout.data = JSON.parse(ggg);
        $scope.create_workout = false;

    }).error(function(data){
            $scope.create_workout = true;
            $scope.workout = {
                date: wo_date,
                data: []
            };
        });

    //saving workout, json api
    $scope.save_workout = function(){
        if ($scope.create_workout){
            $http.post('/log/api/workouts/', $scope.workout, {headers: {'X-CSRFToken': csrftoken}}).success(function(data){
                $scope.test = data;
            }).error(function(data){
                    $scope.test = data;
                });
            $scope.create_workout = false;
        }
        else {
            $http.put('/log/api/workouts/' + $scope.workout.date + '/', $scope.workout, {headers: {'X-CSRFToken': csrftoken}}).success(function(data){
                $scope.test = data;
            }).error(function(data){
                    $scope.test = data;
                });
        }
    }

    //date_to is used at calendar
    $scope.date_to = $scope.wo_date;
    $scope.rediredt_to_date = function(){
        //alert($scope.date_to);
        window.location.replace('/log/add_workout/#/add_workout/' + $scope.date_to);
    };

    //getting all exercises
    $http.get("/log/api/exercises/").success( function(data){
        $scope.exercises = data;
        $scope.cur_exercises = $scope.exercises;
        //$scope.typeahead = [];
        /*for (var i in data){
            $scope.typeahead.push(data[i].name);
        }*/
    }).error(function(data){
            $scope.exercises = "ggg";
        });
    $scope.exrc_order = true;

    //adding exercise to current workout
    $scope.add_exrc_to_cur_workout = function(exercise){
        var exrc = {
            name: exercise.name,
            id: exercise.pk,
            wrs: [["",""]]
        };
        if ($scope.workout){
            $scope.workout.data.push(exrc);
        }
        else {
            $scope.workout = {
                created: $scope.today,
                data: []
            };
            $scope.workout.data.push(exrc);
        };
        //scrolling to new exrc
        jQuery.fn.extend({
            scrollBottom: function(speed) {
                return this.each(function() {
                    var targetOffset = $(this).offset().top + $(this).height();
                    $('html').animate({scrollTop: targetOffset - $(window).height()},
                        speed);
                });
            }
        });
        $('.log-exercise:last').scrollBottom(2000);

    };

    $scope.typeaheadValue = 'Alabama';


    var states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Dakota","North Carolina","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"];
    states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Dakota","North Carolina","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"];


    var workout = {
        exercises: [
            {
                name: "Squats",
                id: 1,
                wrs: [
                    [222, 3],
                    [255, 4],
                    [555, 6]
                ]
            },
            {
                name: "Deads",
                id: 2,
                wrs: [
                    [555,3],
                    [222, 12]
                ]
            }
        ],
        created: "vchera"
    };
    $scope.workout = workout;

    $scope.addWR = function(exercise) {
        exercise.wrs.push(['','']);
    };
    $scope.removeWR = function(index, exercise){
        exercise.wrs.splice(index, 1);
    }

    $scope.addExercise = function(exercise){
        $scope.workout.data.push({name: exercise.name, id: exercise.id});
    }
    $scope.removeExrcise = function(exrc){
        $scope.workout.data.splice(exrc, 1);
    }
}

function HelloCntl($scope) {
    $scope.name = 'World';
}


function oneCtrl($scope) {
    $scope.name = 'World';
}