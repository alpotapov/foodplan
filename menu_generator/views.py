from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from menu_generator.generator import MenuGenerator
from main.serializers import RecipeSerializer
from user_profiles.models import User
#from user_profiles.models import User
#from user_profiles.serializers import UserSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def generate(request, user_id):
    #returns menu, format: {"day_name": {"meal_name": {pk, name, image_url, prep_time_seconds, price, is_vegetarian, is_lactose_intolerant}}}

    #user = User.objects.filter(pk=user_id)[0]
    #generator = MenuGenerator(lactose_intolerance_allowed=(not user.lactose_intolerance), vegetarian=user.vegetarian)
    generator = MenuGenerator(lactose_intolerance_allowed=True, vegetarian=False)
    week_menu = generator.generate_week_menu()
    return JSONResponse(week_menu)


def refresh_meal(request, user_id, day_name, meal_name):
    # returns single meal, format: {"day_name": {"meal_name": ...}}

    generator = MenuGenerator(lactose_intolerance_allowed=True, vegetarian=False)
    if meal_name == "breakfast":
        breakfast = True
    else:
        breakfast = False
    return JSONResponse(RecipeSerializer(generator.get_one_random_item(breakfast=breakfast)).data)