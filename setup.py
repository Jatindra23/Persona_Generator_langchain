from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("-e .")]

setup(
    name="persona_generator_langchain",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="Reddit user persona generator using LangGraph and LangChain",
    packages=find_packages(),  # Automatically finds all packages with __init__.py
    include_package_data=True,
    install_requires=read_requirements(),
    
    python_requires='>=3.8',
)
