from utils.ai_helpers import generate_ai_response
import json

class Person:
    """
    Represents a villager in the simulation with various attributes and behaviors.
    This class is central to modeling individual actions and interactions within the village.
    """

    def __init__(self, name, age, occupation, personality, skills, relationships, backstory=None):
        # Initialize basic attributes of a person
        self.name = name
        self.age = age
        self.occupation = occupation
        self.personality = personality
        self.skills = skills
        self.relationships = relationships
        self.backstory = backstory
        
        # Initialize dynamic attributes that will change during the simulation
        self.goals = []
        self.knowledge = {}
        self.emotions = {}
        self.daily_action = None
        self.action_history = []

    def set_goals(self, goals):
        self.goals = goals

    def add_knowledge(self, key, value):
        self.knowledge[key] = value

    def update_emotion(self, emotion, intensity):
        self.emotions[emotion] = intensity

    def take_action(self, action):
        self.daily_action = action
        self.action_history.append(action)

    def review_goals(self):
        """
        Reviews and potentially updates the person's goals based on their current state and recent actions.
        Uses AI to generate a response that may modify goals or suggest the next action.
        """
        prompt = f"Review the goals for {self.name}, age {self.age}, occupation {self.occupation}, with personality {self.personality} and skills {self.skills}. Current goals: {self.goals}. Recent actions: {self.action_history[-5:]}. Current emotions: {self.emotions}. Revise the goals if needed. If they are not in need of revision, select an action for the next day."
        
        json_structure = {
            "goals": [
                {
                    "title": "string",
                    "actions": ["string"]
                }
            ],
            "next_action": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        if 'goals' in response:
            self.goals = response['goals']
        if 'next_action' in response:
            self.daily_action = response['next_action']

    def plan_next_action(self):
        """
        Plans the next day's action for the person based on their current state.
        Uses AI to generate a suitable action considering various factors.
        """
        prompt = f"Plan the next day's action for {self.name}, considering their goals: {self.goals}, personality: {self.personality}, skills: {self.skills}, and current emotions: {self.emotions}."
        
        json_structure = {
            "planned_action": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        self.daily_action = response.get("planned_action", "No action planned")

    def learn_from_experience(self, experience):
        """
        Updates the person's skills and knowledge based on a given experience.
        Uses AI to determine how the experience affects the person's attributes.
        """
        prompt = f"{self.name} just experienced: {experience}. How does this affect their skills or knowledge? Current skills: {self.skills}, Current knowledge: {self.knowledge}"
        
        json_structure = {
            "skill_changes": {"skill_name": "integer"},
            "new_knowledge": {"key": "value"}
        }
        
        response = generate_ai_response(prompt, json_structure)
        for skill, change in response.get('skill_changes', {}).items():
            self.skills[skill] = self.skills.get(skill, 0) + int(change)
        for key, value in response.get('new_knowledge', {}).items():
            self.add_knowledge(key, value)

    def interact_with(self, other_person):
        prompt = f"{self.name} is interacting with {other_person.name}. Their relationship is {self.relationships.get(other_person.name, 'neutral')}. {self.name}'s personality: {self.personality}, current emotions: {self.emotions}."
        
        json_structure = {
            "interaction": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("interaction", "No interaction occurred")

    def express_emotion(self, emotion):
        prompt = f"{self.name}, with personality {self.personality}, is expressing the emotion {emotion} with intensity {self.emotions.get(emotion, 0)}."
        
        json_structure = {
            "expression": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("expression", "No emotion expressed")

    def empathize(self, other_person):
        prompt = f"{self.name}, with personality {self.personality} and current emotions {self.emotions}, is trying to empathize with {other_person.name} who is feeling {other_person.emotions}."
        
        json_structure = {
            "empathetic_response": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("empathetic_response", "Unable to empathize")

    def make_decision(self):
        prompt = f"{self.name} needs to make a decision. Their goals: {self.goals}, knowledge: {self.knowledge}, personality: {self.personality}, skills: {self.skills}, current emotions: {self.emotions}."
        
        json_structure = {
            "decision": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("decision", "No decision made")

    def cooperate_with(self, other_person, goal):
        prompt = f"{self.name} is cooperating with {other_person.name} to achieve the goal: {goal}. {self.name}'s skills: {self.skills}, personality: {self.personality}. Their relationship: {self.relationships.get(other_person.name, 'neutral')}."
        
        json_structure = {
            "cooperation_action": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("cooperation_action", "No cooperation occurred")

    def compete_with(self, other_person, resource):
        prompt = f"{self.name} is competing with {other_person.name} for the resource: {resource}. {self.name}'s skills: {self.skills}, personality: {self.personality}. Their relationship: {self.relationships.get(other_person.name, 'neutral')}."
        
        json_structure = {
            "competition_strategy": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("competition_strategy", "No strategy devised")

    def form_relationship(self, other_person, relationship_type):
        old_relationship = self.relationships.get(other_person.name, "neutral")
        self.relationships[other_person.name] = relationship_type
        prompt = f"{self.name}'s relationship with {other_person.name} has changed from {old_relationship} to {relationship_type}. {self.name}'s personality: {self.personality}."
        
        json_structure = {
            "reaction": "string"
        }
        
        response = generate_ai_response(prompt, json_structure)
        return response.get("reaction", "No reaction to relationship change")

    def adapt_to_change(self, change):
        prompt = f"{self.name} needs to adapt to this change in the village: {change}. Their personality: {self.personality}, current goals: {self.goals}, skills: {self.skills}."
        
        json_structure = {
            "adaptation": "string",
            "new_goals": [
                {
                    "title": "string",
                    "actions": ["string"]
                }
            ]
        }
        
        response = generate_ai_response(prompt, json_structure)
        if 'new_goals' in response:
            self.goals.extend(response['new_goals'])
        return response.get("adaptation", "No significant adaptation needed")

    @classmethod
    def load_villagers(cls):
        """
        Class method to load villager data from a JSON file and create Person instances.
        Generates personality and skills for each villager using AI.
        """
        with open('data/people.json', 'r') as f:
            data = json.load(f)
        
        villagers = []
        for villager_data in data['villagers']:
            villager = cls(
                name=villager_data['name'],
                age=villager_data['age'],
                occupation=villager_data['occupation'],
                personality={},  # Will be generated with AI
                skills={},       # Will be generated with AI
                relationships={},
                backstory=villager_data.get('backstory')
            )
            villager.generate_personality_and_skills()
            villagers.append(villager)
        
        return villagers

    def generate_personality_and_skills(self):
        """
        Generates personality traits and skills for the person using AI.
        This method is called during the initialization of each villager.
        """
        prompt = f"Generate a personality and set of skills for {self.name}, a {self.age}-year-old {self.occupation}. Backstory: {self.backstory}"
        
        json_structure = {
            "personality": {
                "trait1": "description",
                "trait2": "description",
                "trait3": "description"
            },
            "skills": {
                "skill1": "integer (1-10)",
                "skill2": "integer (1-10)",
                "skill3": "integer (1-10)"
            }
        }
        
        response = generate_ai_response(prompt, json_structure)
        self.personality = response.get('personality', {})
        self.skills = {skill: int(level) for skill, level in response.get('skills', {}).items()}

    def __str__(self):
        """
        Returns a string representation of the person.
        """
        return f"{self.name}, {self.age} years old, {self.occupation}"