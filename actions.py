# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionRespondCoroanStateCity(Action):
    def name(self):
        return "action_corona_state"

    def run(self, dispatcher, tracker, domain):
        # last_message = tracker.latest_message.get("text", "")

        response = requests.get(
            "https://api.covid19india.org/data.json").json()
        # print(response["statewise"])
        # print("Length ", len(response["statewise"]))
        message = "Please enter correct STATE name"

        entities = tracker.latest_message['entities']
        state = None
        for e in entities:
            if e['entity'] == "state":
                state = e['value']
        if state == "corona":
            state = "Total"
        if state == "india":
            state = "Total"

        # print("State ", state.title())
        message = "Please enter correct STATE name"
        if(state != None):
            message = "Please enter correct STATE name"
            for data in response["statewise"]:
                if data["state"] == state.title():
                    message = "Active: "+data["active"] + " Confirmed: " + data["confirmed"] + \
                        " Recovered: " + data["recovered"] + \
                        " On "+data["lastupdatedtime"]

        dispatcher.utter_message(message)

        return []


class ActionRespondDenmarkInfo(Action):
    def name(self):
        return "action_denmark_data"

    def run(self, dispatcher, tracker, domain):

        import json

        with open('data.json') as f:
            data = json.load(f)

        entities = tracker.latest_message['entities']
        year = None
        for e in entities:
            if e['entity'] == "year":
                year = e['value']
        if(year != None):
            message = "Please enter correct year name"
            for data in data:
                if data["Year"] == int(year):
                    message = f"Year: {data['Year']}" + "\n" + f"TotalPopulation: : {data['TotalPopulation']}" + "\n" + \
                        f"GrowthRate:{data['TotalPopulation']}" + "\n"+f"Density:{data['Density']}" + \
                        "\n" + \
                        f"TotalPopulationRank:{data['TotalPopulationRank']}"
        dispatcher.utter_message(message)

        return []
