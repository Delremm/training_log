
var exercises = {
    '1': 'barbell deadlift',
    '2': 'squats',
    '3': 'bench press'
    };
get_exercise_name_by_id = function(id){
    return exercises[id]
    }

console.log(get_exercise_name_by_id(1));
var tt = _.exte
var workouts;
$(document).ready(function(){
    $.getJSON('/log/api/workouts/?format=json', function(workouts_data){
        workouts = workouts_data;
        for (var i in workouts){
            var kk = JSON.parse(workouts[i].data);
            $('.workouts_container').append(function(){
                return "<p>" + workouts[i].date + "</p>"
            });
            $('.workouts_container').append(function(){
                var $newul = $('<ul class="wo_container"></ul>');
                console.log($newul);
                var exrc_num = kk.length;
                for (var k in kk){
                    $newul.append(function(){
                    var $exrc = $("<li></li>");
                    console.log($exrc);
                    var exrc_name = kk[k][0];
                    console.log('exrc_name: ' + exrc_name);
                    $exrc.append(get_exercise_name_by_id(exrc_name));
                    $exrc.addClass("exercise_id" + exrc_name);
                    console.log($exrc);
                    return $exrc
                    });
                    $newul.append(function(){
                        var $exrc = $("<li></li>");
                        $exrc.append(function(){
                            console.log('priver');
                            var len = kk[k].length;
                            console.log('len: ' + len);
                            var $newul2 = $("<ul class='wr_list'></ul>");
                            for (var j = 1; j < len; j++){
                                $newul2.append(function(){
                                var $wr = $("<li class='wr_item'></li>");
                                    $wr.append(function(){
                                        return kk[k][j][0] + " kg x " + kk[k][j][1]
                                    });
                                    return $wr
                                });
                            }
                                console.log('wr: ' + $newul2);
                                return $newul2
                        });
                        return $exrc
                    });
                }
                return $newul
            });

            console.log(kk);
            $('h3:first').text(kk[0][1]);

        };
    });

});
