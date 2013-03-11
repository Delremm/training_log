from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from models import *
from datetime import date
from forms import AddWorkoutForm, WeightRepsForm, AddGoalForm, CheckPointForm
from django.forms.formsets import formset_factory


class IndexView(generic.TemplateView):
    template_name = 'log/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        n = Workout.objects.count()
        recent_dict = {}
        for i, wo in enumerate(Workout.objects.all().order_by('-id')[0:4]):
            recent_dict[str(i)] = [wo, wo.set_set.all()]
        context['workouts_recent'] = sorted(recent_dict.iteritems())
        return context

class ExercisesView(generic.ListView):
    template_name = 'exercise_list.html'
    model = Exercise


class ExerciseDetailView(generic.DetailView):
    template_name = 'exercise_detail.html'
    model = Exercise
    context_object_name = 'exercise'
    def get_context_data(self, **kwargs):
        context = super(ExerciseDetailView, self).get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context

class WorkoutsView(generic.ListView, generic.edit.ProcessFormView):
    template_name = 'log/workouts.html'
    queryset = Workout.objects.all().order_by('-date').order_by('-id')
    context_object_name = 'objects_list'
    def post(self, request, **kwargs):
        if 'add' in request.POST:
            w = Workout()
            w.date = date.today()
            if not request.user.is_anonymous():
                w.user = request.user
            w.save()
            request.session['workout_id'] = w.id
            return HttpResponseRedirect('/choice_exercise/')
        return self.render_to_response()


class WorkoutDetailView(generic.DetailView):
    #template_name = 'log/workout_detail.html'
    model = Workout
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(WorkoutDetailView, self).get_context_data(**kwargs)
        context['sets'] = self.object.set_set.all()
        return context


class ChoiceExerciseView(generic.TemplateView):
    template_name = 'log/choice_exercise.html'
    redirect_to = '/weight_reps_add/'
    def get_context_data(self, **kwargs):
        context = super(ChoiceExerciseView, self).get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.all()
        context['redirect_to'] = self.redirect_to
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.session.has_key('workout_id'):
            context['workout_id'] = request.session['workout_id']
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.has_key('workout_id'):
            request.session['workout_id'] = request.POST['workout_id']
            context['workout_id'] = request.session['workout_id']
        return self.render_to_response(context)

class WeightRepsAddView(generic.TemplateView):
    template_name = 'log/add_weight_reps.html'
    WeightRepsFormset = formset_factory(WeightRepsForm)

    def get_context_data(self, **kwargs):
        context = super(WeightRepsAddView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def get_formset(self, data=None ):
        formset = self.WeightRepsFormset(data=data)
        return formset

    def post(self,request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.has_key('exercise_id'):
            request.session['exercise_id'] = request.POST['exercise_id']
            set = Set()
            set.workout = Workout.objects.get(id=request.session['workout_id'])
            set.exercise = Exercise.objects.get(id=request.session['exercise_id'])
            set.save()
            request.session['set'] = set
        if 'save' in request.POST:
            if request.session.has_key('set') and request.session.has_key('workout_id') :
                formset = self.get_formset(data=request.POST)
                if formset.is_valid():
                    data = formset.cleaned_data
                    context['data'] = data
                    #check if form is not empty
                    if data != [{}]:
                        for form in formset:
                            wr = WeightReps()
                            wr.set = request.session['set']
                            wr.weight = form.cleaned_data['weight']
                            wr.reps = form.cleaned_data['reps']
                            wr.save()
                            wr = None
                            #context['test']=form.cleaned_data
                        workout_id = request.session['workout_id']
                        request.session.clear()
                        #return self.render_to_response(context)
                        return HttpResponseRedirect("/workouts/%s/" % workout_id)
                    else:
                        context['formset'] = formset
                        return self.render_to_response(context)
                else:
                    context['formset'] = formset
                    return self.render_to_response(context)
            else:
                request.session.clear()
                return HttpResponseRedirect("/workouts/")


        return self.render_to_response(context)

class WorkoutDeleteView(generic.DeleteView):
    template_name = "log/workout_delete.html"
    success_url = '/workouts/'
    model = Workout

class WorkoutSetDeleteView(generic.DeleteView):
    success_url = '/workouts/'
    model = Set
    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.object_id)

    def post(self, *args, **kwargs):
        if 'set_id' in self.request.POST:
            self.object_id = self.request.POST['set_id']
            self.success_url += str(self.request.POST['workout_id'])
        return self.delete(self, **kwargs)

class ExerciseChangeView(ChoiceExerciseView):
    template_name = 'log/exercise_change.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.session.has_key('workout_id'):
            context['workout_id'] = request.session['workout_id']
        if request.session.has_key('set_id'):
            context['set_id'] = request.session['set_id']
            return self.render_to_response(context)
        return HttpResponseRedirect('/workouts/')

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.has_key('workout_id'):
            request.session['workout_id'] = request.POST['workout_id']
            context['workout_id'] = request.session['workout_id']
        if request.POST.has_key('set_id'):
            request.session['set_id'] = request.POST['set_id']
            context['set_id'] = request.session['set_id']
            return self.render_to_response(context)

        if 'exercise_id' in request.POST:
            set = Set.objects.get(id=request.session['set_id'])
            set.exercise = Exercise.objects.get(id=request.POST['exercise_id'])
            set.save()
            workout_id = request.session['workout_id']
            request.session.clear()
            return HttpResponseRedirect('/workouts/%s/' % workout_id)
        return HttpResponseRedirect('/workouts/')

class WeightRepsChangeView(generic.TemplateView):
    template_name = 'log/weight_reps_change.html'

    WeightRepsFormset = formset_factory(WeightRepsForm)

    def get_context_data(self, **kwargs):
        context = super(WeightRepsChangeView, self).get_context_data(**kwargs)
        return context

    def get_formset(self, data=None, initial=None ):
        if initial:
            WeightRepsFormsetExtra = formset_factory(WeightRepsForm, extra=0)
            return WeightRepsFormsetExtra(data=data, initial=initial)
        else:
            return self.WeightRepsFormset(data=data)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.session.has_key('workout_id'):
            context['workout_id'] = request.session['workout_id']
        if request.session.has_key('set_id'):
            context['set_id'] = request.session['set_id']
            context['formset'] = self.get_formset(initial=self.get_formset_initial(context['set_id']))
            return self.render_to_response(context)
        return HttpResponseRedirect('/workouts/')

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.has_key('workout_id'):
            request.session['workout_id'] = request.POST['workout_id']
            context['workout_id'] = request.session['workout_id']
        if request.POST.has_key('set_id'):
            request.session['set_id'] = request.POST['set_id']
            context['set_id'] = request.session['set_id']
            context['formset'] = self.get_formset(initial=self.get_formset_initial(context['set_id']))
            return self.render_to_response(context)

        if 'save' in request.POST:
            formset = self.get_formset(data=request.POST)
            if formset.is_valid():
                data = formset.cleaned_data
                context['data'] = data
                #check if form is not empty
                if data != [{}]:
                    set = Set.objects.get(id=request.session['set_id'])
                    if len(formset) > len(set.weight_reps.all()):
                        d = len(formset)-len(set.weight_reps.all())
                        form_data = []
                        if formset.cleaned_data != [{}]:
                            for f in formset:
                                form_data.append(f.cleaned_data)
                                if f.cleaned_data == {}:
                                    workout_id = request.session['workout_id']
                                    del request.session['workout_id']
                                    del request.session['set_id']
                                    return HttpResponseRedirect('/workouts/%s/' % workout_id)
                            for wr, form in zip(set.weight_reps.all(), formset):
                                wr.weight = form.cleaned_data['weight']
                                wr.reps = form.cleaned_data['reps']
                                wr.save()
                            for n in range(1, d + 1):
                                wr = WeightReps()
                                wr.set = set
                                wr.weight = form_data[-n]['weight']
                                wr.reps = form_data[-n]['reps']
                                wr.save()
                                wr = None
                            #for n in range(1,d + 1):
                    elif len(formset) == len(set.weight_reps.all()):
                        for wr, form in zip(set.weight_reps.all(), formset):
                            wr.weight = form.cleaned_data['weight']
                            wr.reps = form.cleaned_data['reps']
                            wr.save()
                    elif len(formset) < len(set.weight_reps.all()):
                        for wr in set.weight_reps.all():
                            wr.delete()
                        data = formset.cleaned_data
                        #check if form is not empty
                        if data != [{}]:
                            for form in formset:
                                wr = WeightReps()
                                wr.set = set
                                wr.weight = form.cleaned_data['weight']
                                wr.reps = form.cleaned_data['reps']
                                wr.save()
                                wr = None
                        else:
                            context['formset'] = formset
                            return self.render_to_response(context)
                        workout_id = request.session['workout_id']
                        request.session.clear()
                        #return self.render_to_response(context)
                        return HttpResponseRedirect("/workouts/%s/" % workout_id)
                    else:
                        context['formset'] = formset
                        return self.render_to_response(context)
                    workout_id = request.session['workout_id']
                    request.session.clear()
                    return HttpResponseRedirect('/workouts/%s/' % workout_id)
                else:
                    context['formset'] = formset
                    return self.render_to_response(context)


    def get_formset_initial(self, set_id):
        set = Set.objects.get(id=set_id)
        initial = []
        for wr in set.weight_reps.all():
            initial.append({'weight':wr.weight, 'reps':wr.reps})
        return initial

class GoalsView(generic.TemplateView):
    template_name = 'log/goals.html'

    def get_context_data(self, **kwargs):
        context = super(GoalsView, self).get_context_data(**kwargs)
        context['goals'] = Goal.objects.all()
        context['we'] = 'asdf'
        return context

class GoalChoiceExrc(ChoiceExerciseView):
    redirect_to = '/goals/add_goal/'

class AddGoalView(generic.TemplateView):
    template_name = 'log/add_goal.html'

    def get_context_data(self, **kwargs):
        context = super(AddGoalView, self).get_context_data(**kwargs)
        context['form'] = AddGoalForm()
        context['date'] = date.today()
        return context

    def post(self,request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.has_key('exercise_id'):
            request.session['exercise_id'] = request.POST['exercise_id']
        if 'save' in request.POST:
            if request.session.has_key('exercise_id'):
                form = AddGoalForm(data=request.POST)
                if form.is_valid():
                    goal = Goal()
                    goal.weight = form.cleaned_data['weight']
                    goal.reps = form.cleaned_data['reps']
                    goal.exercise = Exercise.objects.get(id=request.session['exercise_id'])
                    goal.date = date.today()
                    goal.user = request.user
                    goal.save()
                    del request.session['exercise_id']
                    return HttpResponseRedirect("/goals/")
                else:
                    context['form'] = form
                    return self.render_to_response(context)
            else:
                return HttpResponseRedirect("/goals/")
        return self.render_to_response(context)


class GoalDeleteView(generic.DeleteView):
    success_url = '/goals/'
    model = Goal

class CommonPhysPramsListView(generic.ListView): #move to profile
    template_name = 'log/common_phys_params_list.html'
    model = CommonPhysicalParams
    context_object_name = 'params'

class CommonPhysicalParamsView(generic.TemplateView): #del this
    template_name = 'log/common_phys_params.html'

class CheckPointListView(generic.ListView):
    template_name = 'log/check_point_list.html'
    model = CheckPointMovement

class CheckPointChoiceExrc(ChoiceExerciseView):
    redirect_to = '/check_points/add/'

class CheckPointAdd(generic.TemplateView):
    template_name = 'log/check_point_add.html'

    def get_context_data(self, **kwargs):
        context = super(CheckPointAdd, self).get_context_data(**kwargs)
        context['form'] = CheckPointForm()
        return context

    def post(self,request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.POST.has_key('exercise_id'):
            request.session['exercise_id'] = request.POST['exercise_id']
        if 'save' in request.POST:
            if request.session.has_key('exercise_id'):
                form = CheckPointForm(data=request.POST)
                if form.is_valid():
                    check_point = CheckPointMovement()
                    check_point.weight = form.cleaned_data['weight']
                    check_point.reps = form.cleaned_data['reps']
                    check_point.exercise = Exercise.objects.get(id=request.session['exercise_id'])
                    check_point.save()
                    del request.session['exercise_id']
                    return HttpResponseRedirect("/check_points/")
                else:
                    context['form'] = form
                    return self.render_to_response(context)
            else:
                return HttpResponseRedirect("/check_points/")
        return self.render_to_response(context)

class CheckPointDeleteView(generic.DeleteView):
    success_url = '/check_points/'
    model = CheckPointMovement


from django import http
from django.utils import simplejson as json

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
            content_type='application/json',
            **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class TestView(generic.TemplateView, JSONResponseMixin):
    template_name = 'test.html'

    def test_dayx(self):
        dayx = DayX(order='2 3')
        dayx.save()
        dayx.exercises.add(Exercise.objects.get(id=2))
        dayx.exercises.add(Exercise.objects.get(id=3))
        return dayx.get_exercises_in_order()

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['dayx'] = [x.to_dict() for x in Exercise.objects.all()]
        #context['request'] = self.request
        return context
    def render_to_response(self, context):
        if self.request.GET.get('format','html') == 'json':
            return JSONResponseMixin.render_to_response(self, context)
        else:
            return generic.TemplateView.render_to_response(self, context)



