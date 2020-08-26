from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet

class ActionDefineTechnology(Action):

    def name(self) -> Text:
        return "action_define_technology"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        technology = tracker.get_slot("technology")
        if technology != None:
            definition = getattr(self, 'define_' + technology)                
            dispatcher.utter_message(text=definition())
        else:
            dispatcher.utter_message(template="utter_iamabot")

        return [SlotSet("technology", None)]

    def define_docker(self):
        return "It is a popular open-source project based on Linux container. It is basically\
          a container engine that uses the Linux kernel features like namespaces and control\
          groups to create containers on top of an operating system"
    
    def define_microservice(self):
        result = "also known as the microservice architecture - "
        result +=  "is an architectural style that structures an application as a collection"
        result +=  "of services that are. Highly maintainable and testable. Loosely coupled."
        result +=  " Independently deployable. Organized around business capabilities."
        return result

    