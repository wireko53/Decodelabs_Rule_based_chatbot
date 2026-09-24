def main():
    # Dictionary mapping key words to bot responses
    responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What would you like me to help you with?",
        "how are you": "I'm a bot, functioning perfectly! How about you?",
        "help": "I can assist you with some basic queries. Type 'exit' or 'bye' or 'quit' to close the conversation.",
        "who created you": "I was built as a rule-based AI chatbot by Wireko Fosu Eric, an intern for DecodeLabs."
    }

    print("--- Rule-Based AI Chatbot ---")
    print("Type 'exit' or 'bye' or 'quit' to end the conversation.\n")

    while True:
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # Stop condition
        if clean_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day.")
            break

        # Check for keyword containment
        matched_reply = None
        for keyword, reply in responses.items():
            if keyword in clean_input:
                matched_reply = reply
                break  # Stop at the first keyword match

        # Print matched response or fall back to default
        if matched_reply:
            print(f"Bot: {matched_reply}\n")
        else:
            print("Bot: I do not understand. Could you rephrase?\n")

if __name__ == "__main__":
    main()