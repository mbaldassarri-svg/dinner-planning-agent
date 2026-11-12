"""
tools.py - Strongly typed, descriptive tools for the Dinner Planning Agent.
"""
from typing import List, Dict, Any
import json

def generate_recipe_from_ingredients(ingredients: List[str], dietary_restrictions: List[str] = None) -> Dict[str, Any]:
    """
    Generates a personalized dinner recipe based on a specific list of available ingredients given by the user.

    Parameters:
    -----------
    ingredients : List[str]
        A list of ingredients currently available in the kitchen (e.g., ["chicken", "broccoli", "garlic"]).
    dietary_restrictions : List[str], optional
        Any dietary exclusions or preferences (e.g., ["vegetarian", "gluten-free"]). Defaults to None.

    Returns:
    --------
    Dict[str, Any]
        A structured dictionary containing:
        - "recipe_name": Name of the suggested dish
        - "prep_time": Prep time in minutes
        - "cook_time": Cook time in minutes
        - "instructions": Step-by-step directions
        - "missing_ingredients": Common pantry staples that might be needed
    """
    if not ingredients:
        # Guided Error Handling: Provide descriptive recovery instructions instead of crashing
        return {
            "error": "No ingredients were provided.",
            "recovery_instructions": "Please supply a non-empty list of available ingredients to plan your dinner."
        }
    
    # Process and build recipe (Mock or actual Gemini integration below)
    # Ensure returned JSON conforms strictly to schema expectations
    recipe = {
        "recipe_name": f"Savory Pan-Seared {' and '.join(ingredients[:2])}",
        "prep_time": 10,
        "cook_time": 15,
        "instructions": [
            f"Prep your {' and '.join(ingredients)} by washing and cutting into bite-sized pieces.",
            "Heat olive oil in a pan over medium heat.",
            "Sautée ingredients and season with salt and pepper to taste.",
            "Serve warm and enjoy!"
        ],
        "missing_ingredients": ["olive oil", "salt", "pepper"]
    }
    return recipe
