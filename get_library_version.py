import importlib.metadata
packages = [
    "beautifulsoup4",
    "fastapi",
    "html5lib",
    "jinja2",
    "langchain",
    "langchain-astradb",
    "langchain_core",
    "langchain-google-genai",
    "langchain-groq",
    "lxml",
    "python-dotenv",
    "python-multipart",
    "selenium",
    "streamlit",
    "undetected-chromedriver",
    "uvicorn",
    "structlog",
    "langgraph",
    "ragas",
    "langchain-mcp-adapters",
    "mcp",
    "ddgs",
    "langchain-openai"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")


with open("requirements.txt", "w") as f:
    for pkg in packages:
        try:
            version = importlib.metadata.version(pkg)
            f.write(f"{pkg}=={version}\n")
        except importlib.metadata.PackageNotFoundError:
            pass  # skip missing
