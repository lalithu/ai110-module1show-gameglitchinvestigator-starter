# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  When I first ran the game, it worked at a basic level but had several confusing and inconsistent behaviors. One major issue was that the hints were reversed — when my guess was too high, the game told me to go higher instead of lower. Another bug was that the secret number sometimes behaved inconsistently because it was being treated as both a string and an integer, which caused unpredictable comparisons. I also noticed that the attempt counter was off, and the difficulty settings didn’t match the actual range used in the game. Overall, the game felt unreliable and inconsistent.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT and Copilot as AI teammates during this project. One correct suggestion was refactoring the core logic into a separate logic_utils.py file, which made the code more modular and easier to test — I verified this by successfully importing the functions into my test file and running pytest. However, one misleading suggestion from the original AI-generated code was using a try/except block in the check_guess function to handle type errors instead of fixing the root cause. I verified this was unnecessary by removing the type inconsistency and confirming that the function worked correctly without exception handling. This showed me that AI suggestions need to be critically evaluated.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by both running the Streamlit app and verifying behavior manually, as well as writing pytest tests for core functions. For example, I wrote a test to check that a guess of 60 against a secret of 50 returns “Too High,” which confirmed that the hint logic was working correctly. I also tested input parsing with invalid values like “abc” to ensure proper error handling. AI helped me generate initial test cases, but I refined them to match the actual function outputs and edge cases. Running pytest and seeing all tests pass gave me confidence that my fixes were correct.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept behaving inconsistently because it was sometimes being converted into a string during the game logic, which broke comparisons. I also learned that Streamlit reruns the entire script every time a user interacts with the app, so without session state, values like the secret number would reset constantly. Session state acts like persistent memory that allows variables to survive across reruns. The key fix I made was ensuring the secret number was stored and consistently accessed from st.session_state without changing its type. This gave the game a stable and predictable secret value.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is writing tests alongside debugging, since it made it much easier to verify that fixes actually worked. In the future, I would be more cautious about blindly accepting AI-generated code and instead focus on understanding the underlying logic first. This project showed me that AI can be helpful for suggestions and structure, but it often produces flawed or incomplete solutions. I now see AI as a tool that needs validation rather than something to trust automatically.
