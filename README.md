# OTP Bomber

> **Safety notice:** This project is designed to automate repeated one-time-password (OTP) or SMS requests to third-party services. That can disrupt services and send unwanted messages to people. **Do not use it against real services, phone numbers, or people.** This README intentionally does not provide instructions for launching the live request workflow.

<img width="529" height="285" alt="Screenshot 2026-11-08 at 15 26 12" src="https://github.com/user-attachments/assets/bb150d93-63d9-4ba4-9755-cddb17f51bcd" />


## Project status

This repository is provided for code review and safety-focused maintenance. Its current implementation includes third-party request configurations and concurrent request logic; it is not a benign load-testing tool. The repository does not include a documented consent mechanism, a local-only mode, or a test suite. Treat it as unsafe to operate until those issues are addressed.

A safer direction for future development would be to remove live third-party integrations and replace them with a local mock server and a clearly bounded demonstration that cannot contact real services or recipients.

## What the code does

The Python command-line program prompts for a phone number and request settings. Its worker uses a thread pool to make repeated HTTP requests using configurations stored in `apidata.json`, then displays success and failure counts. The request configuration includes third-party services, and the program's success checks depend on response text. Such checks can become stale as services change and are not proof that a message was delivered or that a request was authorized.

This description is for understanding and safety review—not instructions for running the program.

## Repository layout

```text
.
├── main.py                 # Entrypoint that starts the interactive flow
├── apidata.json            # Request configuration; contains third-party integrations
├── requirements.txt        # Python package dependencies
└── functions/
    ├── askdetails.py       # Collects input and passes settings to the worker
    ├── phoneinfo.py        # Validates the entered phone-number format
    ├── workernode.py       # Coordinates concurrent work and progress reporting
    ├── provider.py         # Selects request configurations and issues HTTP requests
    ├── prettyprint.py      # Prints progress counters
    ├── decorators.py       # Colored terminal message formatting
    └── banner.py           # Terminal banner
```

## Technology

- **Language:** Python
- **Dependencies:** `requests` for HTTP, `colorama` for terminal colors, and their listed supporting packages
- **Configuration:** JSON in `apidata.json`

There is no package/build manifest, automated test suite, or documented CI workflow in the repository at present.

## Safety and responsible handling

- Do not use this project to send OTP requests, SMS messages, or other unsolicited traffic to real services or phone numbers.
- Do not add, refresh, or share third-party service endpoints, credentials, cookies, tokens, or request recipes.
- Do not commit personal data, secrets, or real recipient details. Treat existing request configuration as potentially sensitive and review it before distributing copies or derivatives.
- If you are assessing the code, prefer static review or tests against a local mock server that cannot forward traffic to the internet.
- A meaningful safe-maintenance change should disable/remove live integrations and add safeguards that make external requests impossible by default.

## Development and checks

You can create an isolated Python environment and install the listed dependencies for code review. **Do not launch `main.py` or otherwise execute the live request workflow.** For a non-networking syntax/configuration check, use:

```bash
python -m compileall -q main.py functions
python -m json.tool apidata.json > /dev/null
```

These checks only validate Python syntax and JSON formatting; they do not establish that the program is safe, authorized, or functional. The project currently has no automated tests.

## Contributing

Contributions should reduce risk or improve documentation—not expand the ability to contact real services or send unsolicited messages.

1. Open an issue describing the safety problem or proposed change. Do not include real targets, personal data, secrets, or working third-party request details.
2. Fork the repository and create a focused branch.
3. Make the smallest change that supports a local-only, non-networking, or defensive use case.
4. Run the static checks above. Any new tests must use local fixtures or a mock server and must not send requests to public services.
5. Update the documentation when behavior or safety assumptions change, then submit a pull request explaining the change and its safeguards.

Examples of appropriate contributions include removing third-party integrations, adding static validation, improving warnings, and documenting a local mock-only replacement. Changes that add targets, increase request volume or concurrency, bypass service protections, or enable sending to real recipients are not appropriate.

## License

No license file is present in this repository. Unless the maintainer adds a license, the code should not be assumed to be available for reuse, modification, or redistribution. Consider adding an explicit license before accepting or encouraging contributions.
