import sys
from src.persona_graph import create_persona_graph
from src.logger import logging
from src.exception import PersonaException

if __name__ == "__main__":
    logging.info("Starting Reddit Persona Generator")
    if len(sys.argv) < 2:
        logging.error("No Reddit profile URL provided.")
        raise PersonaException("Please provide a Reddit profile URL as an argument.", sys)
    try:
        logging.info(f"Processing Reddit profile: {sys.argv[1]}")
        if len(sys.argv) != 2:
            print("Usage: python main.py <reddit_profile_url>")
            sys.exit(1)

        reddit_url = sys.argv[1]
        username = reddit_url.strip("/").split("/")[-1]

        graph = create_persona_graph()
        final_state = graph.invoke({"username": username})
        logging.info(f"Persona generated for {username}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise PersonaException(f"An error occurred while generating persona: {e}", sys)

    print(f"Persona generated for {username} and saved to output/{username}_persona.txt")
