# Rule-Based AI Chatbot

Project 1 of my AI Internship at DecodeLabs.

## What I Built

A simple rule-based chatbot that responds to a fixed set of user phrases from the console. No machine learning here — just clean input handling and a lookup table — but it's a good starting point for understanding how conversational systems are structured before layering in NLP.

## Tech Stack

- Python (standard library only, no external dependencies)

## How It Works

1. User input is read from the console, lowercased, and stripped of extra whitespace
2. The bot checks whether any known keyword (e.g. `hello`, `help`) appears anywhere within the input, not just as an exact match — so "hello there" still matches on `hello`
3. The first keyword found is used to look up its response; if none match, the bot falls back to a default "I do not understand" message
4. The loop keeps running until the user types `exit`, `quit`, or `bye`

## Project Structure

```text
DecodeLabs_Chatbot/
├── chatbot.py     # Main chatbot script
└── README.md      # Project documentation
```

## Getting Started

No installation needed beyond Python itself.

```bash
python chatbot.py
```

Type a message at the `You:` prompt. Type `exit`, `quit`, or `bye` to end the conversation.

## What I Learned

Even a "simple" chatbot forces you to think about input normalization (case, whitespace) and graceful fallback handling — both of which matter a lot more once you move to real NLP-based bots.

## Author

Wireko Fosu Eric — AI Intern, DecodeLabs.
