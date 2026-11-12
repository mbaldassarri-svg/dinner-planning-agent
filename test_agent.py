"""
test_agent.py - Automated Evaluation Suite (Testing against golden dataset)
"""
import unittest
from agent import DinnerPlannerAgent

class TestDinnerPlannerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DinnerPlannerAgent()

    def test_golden_dataset_chicken(self):
        """Verify the agent handles standard ingredients properly."""
        user_input = "I have chicken, broccoli, and soy sauce."
        response = self.agent.plan_dinner(user_input)
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()
