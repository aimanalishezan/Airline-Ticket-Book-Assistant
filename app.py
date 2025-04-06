import os 
from dotenv import load_dotenv
import ollama
import gradio as gr

load_dotenv()

model=os.getenv('mod')


MODEL=model


system_message="you are a helpful assistant for an airline called flighAI"
system_message+="give a short, courteous answer, no more then 1 sentence."
system_message+="Always be accurate . if you don't know the answer , say so ."

#function for the tool
ticket_price={"dhaka":"10000tK","thakurgaon":"5000tk","sylet":"7000tk","morocco":"40000"}
def get_ticket_price(destination_city):
    city=destination_city.lower()
    return ticket_price.get(city,"Unknown")
#there is a particular dictionary structure thats required to describe our function 
price_fun={
    "name":"get_ticket_price",
    "description":"Get the price of a return ticket to the festination city . call this whenver your need to know the ticket price, for ecample when a customer asks ' how much is a ticket to this city'",
    "parameters":{
        "type":"object",
        "prorperties":{
            "destination_city":{
                "type":"string",
                "destination":"the city that the customer wants to travel to ",
            },
        },
    },
        "required":["destination_city"],
        "additionalProperties":False
}