# Discurs.eu - AI-Assisted Rational Discourse Platform

## Overview
Discurs.eu is an AI-assisted platform designed to enhance rational discourse by providing fact-checking, logic analysis, and argument structure evaluation. The project is currently in its prototyping phase, using **Streamlit** for rapid development and deployment.

## Features
- **Chat-Based Interface**: Modeled after common messaging apps, providing an intuitive user experience.
- **Three AI Interventions**:
  - 🧐 **Fact-Check**: AI verifies statements against available sources.
  - 🧠 **Logic Check**: AI analyzes logical coherence and identifies fallacies.
  - 📖 **Argument Structure**: AI evaluates clarity, coherence, and completeness of statements.
- **AI Flagging System**:
  - AI passively marks potentially misleading statements.
  - Users can request an explanation for flagged content.
- **Discussion Modes**:
  - **Agora**: Open discussion with minimal AI moderation.
  - **Forum**: Structured, long-form discussions.
  - **Lab**: AI-assisted structured debate and synthesis.

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/discurs-eu.git
   cd discurs-eu
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Deployment
Discurs.eu can be deployed on **Streamlit Community Cloud**:
1. Push your project to GitHub.
2. Connect the repo to Streamlit Community Cloud.
3. Set environment variables (OpenAI API key).
4. Deploy and test the live app.

## Roadmap
- **Phase 1:** Basic chat functionality, AI interventions, and Streamlit deployment.
- **Phase 2:** Improve UI/UX, optimize AI responses, and introduce real-time updates.
- **Phase 3:** Expand language support, refine AI moderation logic, and integrate advanced discourse analytics.

## Contribution
Contributions are welcome! Please open an issue or submit a pull request to suggest improvements.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

