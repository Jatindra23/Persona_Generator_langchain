from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from src.utils import build_prompt, extract_citations, write_persona_file
from src.reddit_scraper import fetch_user_data
from typing import TypedDict
from src.logger import logging
from src.exception import PersonaException
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Step 1: Define the schema
class PersonaState(TypedDict):
    """Schema for the persona generation state."""
    username: str
    data: list
    persona: str
    citations: list

# Step 2: Define your node functions
def scrape_node(state: PersonaState) -> PersonaState:
    """Scrape Reddit user data."""
    try:
        state["data"] = fetch_user_data(state["username"])
        return state
    except Exception as e:
        logging.error(f"Error scraping data for {state['username']}: {e}")
        raise PersonaException(f"Failed to scrape data for {state['username']}", sys)

def generate_persona_node(state: PersonaState) -> PersonaState:
    """Generate a persona from the scraped data."""
    try:
        prompt = build_prompt(state["data"])
        state["persona"] = llm.invoke(prompt).content
        return state
    except Exception as e:
        logging.error(f"Error generating persona for {state['username']}: {e}")
        raise PersonaException(f"Failed to generate persona for {state['username']}", sys)  

def extract_citation_node(state: PersonaState) -> PersonaState:
    """Extract citations from the generated persona."""
    try:
        state["citations"] = extract_citations(state["persona"], state["data"])
        return state
    except Exception as e:
        logging.error(f"Error extracting citations for {state['username']}: {e}")
        raise PersonaException(f"Failed to extract citations for {state['username']}", sys)
    

def write_file_node(state: PersonaState) -> PersonaState:
    """Write the generated persona and citations to a file."""
    try:
        write_persona_file(state["username"], state["persona"], state["citations"])
        return state
    except Exception as e:
        logging.error(f"Error writing persona file for {state['username']}: {e}")
        raise PersonaException(f"Failed to write persona file for {state['username']}", sys)
    

# Step 3: Create the graph with schema
def create_persona_graph():
    """Create the state graph for persona generation."""
    logging.info("Creating persona generation graph")
    # Define the state graph with the PersonaState schema
    try:
        builder = StateGraph(PersonaState)  
        builder.add_node("scrape", scrape_node)
        builder.add_node("generate_persona", generate_persona_node)
        builder.add_node("extract_citations", extract_citation_node)
        builder.add_node("write_output", write_file_node)
    

        builder.set_entry_point("scrape")
        builder.add_edge("scrape", "generate_persona")
        builder.add_edge("generate_persona", "extract_citations")
        builder.add_edge("extract_citations", "write_output")
        builder.add_edge("write_output", END)

        return builder.compile()
    except Exception as e:
        logging.error(f"Error creating persona graph: {e}")
        raise PersonaException("Failed to create persona generation graph", sys)
