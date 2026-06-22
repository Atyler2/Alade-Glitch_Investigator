# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
1. Everytime I submitted a guess the game told me to go higher, even when the guess was at or above the threshold
2. I couldn't start a new game without keeping the final results of the previous one on the bottom
3. When I chose a new difficulty, I was still told to pick a number between one and a hundred regardless of the actualy threshold shown on the side bar.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |Accurate hints      "Too High" Hints
| | | | |working game creation
| | | | |

---

## 2. How did you use AI as a teammate?

- To solve the first error, I explained the original purpose of the program to my Copilot and then asked him to explain why the code was behaving the way it was. Afterwards I had the AI generate a few solution ideas and instructed it on how to fix the code based on the previous steps. Although the AI fixed the code correctly, However when utilizing the AI to generate pytests it mislead me to apply the pytest command without being cd into the correct folder.

---

## 3. Debugging and testing your fixes
  - In order to decide whether a bug was fixed or not, I would use the AI to generate pytest alongside running the code and utilizing the features that were broken. A major test that I performed was the pytest to test if the code performed correctly.

---

## 4. What did you learn about Streamlit and state?

- Streamlit re-executes the code everytime a user interacts with a button or widget. 
---

## 5. Looking ahead: your developer habits


- One habit I want to reuse from this project is double checking the results given by AI.
- One thing I would do differently is have the AI generate multiple solutions to the problem. 
- This project showed that I can use generated code without being relian on the AI