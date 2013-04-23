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
function ToProperDate(d){
    return d.toISOString().slice(0,10)
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
    /*
    for (var i in date_b_list){
        console.log(date_b_list[i]);
    }

    console.log(wo_date);
    */
    var date_a_list = $scope.date_a_list = DatesAfter(wo_date);
    /*
    for (var i in date_a_list){
        console.log(date_a_list[i]);
    }
    */



    //loading workout, json api
    $http.get("/log/api/workouts/" + wo_date + '/').success(function(data){
        $scope.workout = data;
        var ggg = $scope.workout.data;
        $scope.workout.data = JSON.parse(ggg);
        $scope.create_workout = false;
        $scope.master_workout = angular.copy($scope.workout);

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
                $scope.master_workout = angular.copy($scope.workout);
                $scope.saving_error = '';
            }).error(function(data){
                    $scope.saving_error = data;
                });
            $scope.create_workout = false;
        }
        else {
            $http.put('/log/api/workouts/' + $scope.workout.date + '/', $scope.workout, {headers: {'X-CSRFToken': csrftoken}}).success(function(data){
                $scope.test = data;
                $scope.master_workout = angular.copy($scope.workout);
                $scope.saving_error = '';
            }).error(function(data){
                    $scope.saving_error = data;
                });
        }
    }

    //date_to is used at calendar
    $scope.date_to = $scope.wo_date;
    $scope.rediredt_to_date = function(){
        //alert(ToProperDate($scope.date_to));
        window.location.replace('/log/add_workout/#/add_workout/' + ToProperDate($scope.date_to));
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

    //units
    $scope.units = [
        [[['']], [['']]],
        [[['кг', 'фунт']], [['раз(а)']]],
        [[['км', 'м', 'миль']], [['часы'],['мин'],['сек']]],
        [[['м', 'футы']], [['сек'], ['мсек']]],
        [[['часы'],['мин']], [['слабая интенсивность', 'средняя интенсивность', 'высокая интенсивность']]]
    ]


    function wrs_from_type(exrc_type){
        if (exrc_type == 1){
            return [[{value: '', unit: 'кг'}], [{value:'', unit: 'раз(а)'}]]
        }
        else if (exrc_type == 2){
            return [[{value: '', unit: 'м'}], [{value:'', unit: 'часы'}, {value:'', unit:'мин'}, {value:'',unit:'сек'}]]
        }
        else if (exrc_type == 3){
            return [[{value: '', unit: 'м'}], [{value:'',unit:'сек'}, {value:'', unit: 'мсек'}]]
        }
        else if (exrc_type == 4){
            return [[{value:'', unit: 'часы'}, {value:'', unit:'мин'}], [{value:'',unit:'средняя интенсивность'}]]
        }
    };


    //adding exercise to current workout
    $scope.add_exrc_to_cur_workout = function(exercise){
        var exrc = {
            name: exercise.name,
            id: exercise.pk,
            type: exercise.type,
            wrs: [[[{value: '', unit: ''}], [{value:'', unit: ''}]]],
            notes: [0, ""]
        };

        exrc.wrs = [wrs_from_type(exercise.type)];
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


    };



    $scope.addWR = function(exercise) {
        exercise.wrs.push(wrs_from_type(exercise.type));
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
    $scope.add_exercise_notes = function(exercise){
        exercise.notes[0] = 1;
    }
    $scope.remove_exercise_notes = function(exercise){
        exercise.notes[0] = 0;
        exercise.notes[1] = "";
    }



    $scope.show_exercise_description = function(exercise){
        $scope.exercise_description = exercise.description;
        $scope.exercise_description_name = exercise.name;
    }

    //search thro exercises by type
    $scope.cur_exercise_type_change = function(exrc_type){
        if (exrc_type==1){
            $scope.cur_exercise = 1;
        }
        else if (exrc_type==2){
            $scope.cur_exercise = 2;
        }
        else if (exrc_type==3){
            $scope.cur_exercise = 3;
        }
        else if (exrc_type==4){
            $scope.cur_exercise = 4;
        }
        else if (exrc_type==0){
            $scope.cur_exercise = '';
        }
        else {
            $scope.cur_exercise = exrc_type;
        }
    }

    //disabling save button when no changes
    $scope.noChanges = function(data){
        if (data==''){
            return true
        }
        else{
            if (angular.equals($scope.master_workout, $scope.workout)){
                return true
            }
            return false
        }
    }

}
// end of add_workout_ctrl




function woListCtrl($scope, $http) {

    //getting workouts list(paginated) , $scope.pages
    $http.get("/log/api/workouts/").success(function(data){
        $scope.pages = [data];
        //console.log(data)

        for (var i in $scope.pages[0].results){
            console.log('haha');
            console.log(JSON.parse($scope.pages[0].results[i].data));
            console.log('haha2');
            //var ggg = JSON.parse($scope.pages[0].results[i].data);
            $scope.pages[0].results[i].data = JSON.parse($scope.pages[0].results[i].data);;
        }
        //*/

    }).error(function(data){
            $scope.pages = [];
        });

    // adding more workouts to list
    $scope.more_workouts_state = true;
    $scope.more_workouts = function(){
        var page_addr = $scope.pages.slice(-1)[0].next;
        if (page_addr){
            $http.get(page_addr).success(function(data){
                var tmp = data;
                for (var i in tmp.results){
                    tmp.results[i].data = JSON.parse(tmp.results[i].data);
                }
                $scope.pages.push(tmp);
            });
        }
        else {
            $scope.more_workouts_state = false;
        }
        //$scope.pages.push();
    }
}


function oneCtrl($scope) {
    $scope.name = 'World';
}