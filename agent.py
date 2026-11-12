"""
agent.py - Core Orchestration, Memory Compaction, and Strategic Routing.
"""
import os
import logging
from google import genai
from google.genai import types
from tools import generate_recipe_from_ingredients

# 4. Observability: Structured JSON Logging
logging.basicConfig(level=logging.INFO, format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
logger = logging.getLogger("dinner_agent")

class DinnerPlannerAgent:
    def __init__(self):
        # 5. Secure Secret Management: Leverage Secret Manager or injected environment variable
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("CRITICAL: GEMINI_API_KEY environment variable is missing.")
            
        self.client = genai.Client(api_key=self.api_key)
        self.model_flash = "gemini-1.5-flash" # Strategic model routing: Flash for fast processing
        self.model_pro = "gemini-1.5-pro"     # Pro for complex recipe planning
        self.conversation_history = []
        
        # 2. Context & Memory: Robust System Instruction (Constitution)
        self.system_instruction = (
            "You are an expert Concierge Culinary Agent specializing in creating outstanding dinner plans "
            "from limited household ingredients. You operate strictly within the bounds of safety, cleanliness, "
            "and health guidelines. Always be encouraging, brief, and structured. Ask the user for their "
            "daily ingredients and dietary preferences, and suggest creative dishes using only what they have "
            "plus standard pantry staples (like salt, pepper, oil)."
        )

    def compact_history_if_needed(self):
        """
        2. Context & Memory: History Compaction to manage context bloat.
        Truncates or summarizes the conversation history if it exceeds limit.
        """
        if len(self.conversation_history) > 10:
            logger.info("Context length exceeded limit. Initiating sliding window context compaction.")
            # Retain system boundaries and the last 4 turns
            self.conversation_history = self.conversation_history[-4:]

    def plan_dinner(self, user_input: str) -> str:
        self.compact_history_if_needed()
        
        # 4. Observability: Intent vs. Outcome Capture
        logger.info(f"Intent: Route query and process meal plan request for input: '{user_input}'")
        
        try:
            # Multi-Agent / Coordinator Pattern (Simulated routing based on complexity)
            chosen_model = self.model_pro if "dietary" in user_input.lower() or "allergy" in user_input.lower() else self.model_flash
            
            response = self.client.models.generate_content(
                model=chosen_model,
                contents=user_input,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.7,
                )
            )
            
            outcome = response.text
            logger.info("Outcome: Successfully generated recipe recommendations.")
            return outcome
            
        except Exception as e:
            logger.error(f"Error during execution: {str(e)}")
            return "I ran into an issue planning your meal. Could you list your ingredients again?"
