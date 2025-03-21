class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {supply:True for supply in supplies}
        recipe_idx = {recipe:index for index,recipe in enumerate(recipes)}
        def dfs(recipe):
            if recipe in can_cook:
                return can_cook[recipe]

            if recipe not in recipe_idx:
                return False
            can_cook[recipe] = False
            for nei in ingredients[recipe_idx[recipe]]:
                if not dfs(nei):
                    return False

            can_cook[recipe] = True

            return can_cook[recipe]

        sol = []
        for recipe in recipes:
            if dfs(recipe):
                sol.append(recipe)
        return sol
