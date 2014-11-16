from main.models import Recipe
from main.serializers import RecipeSerializer
import simplejson as json


class MenuGenerator:
    day_names = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    meal_names = ["breakfast", "lunch", "dinner"]

    def __init__(self, lactose_intolerance_allowed=True, vegetarian=False):
        self.lactose_intolerance_allowed = lactose_intolerance_allowed
        self.vegetarian = vegetarian

    def generate_week_menu(self):
        week_dict = {"mon": "", "tue": "", "wed": "", "thu": "", "fri": "", "sat": "", "sun": ""}
        menu = []
        for i in range(0,7):
            week_dict[self.day_names[i]] = self.generate_day_menu()

        return json.dumps(week_dict)

    def generate_day_menu(self):
        day_dict = {"breakfast": "", "lunch": "", "dinner": ""}
        day_dict["breakfast"] = RecipeSerializer(self.get_one_random_item(breakfast=True)).data
        day_dict["lunch"] = RecipeSerializer(self.get_one_random_item(breakfast=False)).data
        day_dict["dinner"] = RecipeSerializer(self.get_one_random_item(breakfast=False)).data

        return day_dict

    def get_one_random_item(self, breakfast=False):
        item = Recipe.objects.filter(is_breakfast=breakfast)
        if not self.lactose_intolerance_allowed:
            item = item.filter(is_lactose_intolerant=False)
        if self.vegetarian:
            item = item.filter(is_vegetarian=True)

        return item.order_by('?')[0]