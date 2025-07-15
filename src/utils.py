import os

# ✅ Generate Persona Prompt
def build_prompt(data):
    examples = "\n\n".join([f"Type: {d['type']}, Content: {d.get('body', d.get('title', ''))}" for d in data])
    return f"""
You are an AI trained to analyze Reddit profiles. Generate a user persona based on the following data:

{examples}

Format your response using traits such as: Interests, Personality, Writing Style, Tone.
"""


def extract_citations(persona, data):
    citations = {
        "Interests": [data[0]['url']] if len(data) > 0 else [],
        "Personality": [data[1]['url']] if len(data) > 1 else [],
        "Writing Style": [data[1]['url']] if len(data) > 1 else [],
        "Tone": [data[0]['url'], data[2]['url']] if len(data) > 2 else []
    }
    return citations

def write_persona_file(username, persona, citations):
    """Writes the generated persona and citations to a file."""
    os.makedirs("output", exist_ok=True)
    filepath = f"output/{username}_persona.txt"
    with open(filepath, "w") as f:
        f.write(persona)
        f.write("\n\nSources:\n")
        for trait, links in citations.items():
            f.write(f"{trait}:\n")
            for link in links:
                f.write(f"- https://reddit.com{link}\n")
    return filepath