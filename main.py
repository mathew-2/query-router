# #!/usr/bin/env python3
# """CLI for the query router."""

from router import QueryRouter



def main():
    print("Initializing Query Router with Ollama...")
    
    try:
        router = QueryRouter()
    except Exception as e:
        print(f"Error: Failed to initialize router. Is Ollama running?")
        print(f"Details: {e}")
        return

    print("\nQuery Router CLI (powered by Ollama)")
    print("Type 'quit' to exit\n")

    while True:
        try:
            query = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if query.lower() == "quit":
            print("Goodbye!")
            break

        if not query:
            continue

        response = router.route(query)
        print(f"Response: {response}\n")


if __name__ == "__main__":
    main()