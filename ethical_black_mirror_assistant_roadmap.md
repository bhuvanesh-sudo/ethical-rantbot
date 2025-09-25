# 🕶 Ethical Black Mirror Assistant – 1 Week Solo Roadmap

## 🎯 Goal by End of Week
A working chatbot where:
- You type something in.
- If it’s unethical → It refuses with a dramatic, verbose rant.
- If it’s normal → It gives a short normal response.
- UI looks clean enough to demo.

---

## 🗓 Daily Breakdown

### **Day 1 – Setup & Skeleton**
- [ ] Create GitHub repo.
- [ ] Setup frontend (React/Next.js) with a simple chat UI (textbox + chat bubble display).
- [ ] Setup backend (Flask/FastAPI) with a single `/chat` endpoint.
- [ ] Connect frontend → backend → return static response (“Hello, world”).
**Deliverable:** A working chat pipeline.

---

### **Day 2 – Refusal Logic Core**
- [ ] Implement keyword detection for unethical requests (dictionary of “hack,” “cheat,” “steal,” etc.).
- [ ] Write 3–5 refusal templates with verbose, rant-like text.
- [ ] Return rant if keyword detected, else return normal polite response.
**Deliverable:** Bot refuses selectively with dramatic text.

---

### **Day 3 – Rant Generator Flavor**
- [ ] Add randomized rant generator (shuffle phrases, metaphors).
- [ ] Add typing delay (simulate long thought process).
- [ ] Store refusal responses in JSON/text file for easy expansion.
**Deliverable:** Every refusal feels unique and dramatic.

---

### **Day 4 – Normal Mode**
- [ ] Add default safe responses (e.g., “Here’s a fun fact about cats…”).
- [ ] Create separation: normal mode vs rant mode.
- [ ] Add quick fallback for unknown inputs.
**Deliverable:** Assistant now behaves differently depending on request.

---

### **Day 5 – UI Enhancements**
- [ ] Improve frontend with chat bubbles and scrolling history.
- [ ] Add loading animation for typing delay.
- [ ] Style with dark, dystopian aesthetic (Black Mirror vibe).
**Deliverable:** It *feels* like a “Black Mirror” AI.

---

### **Day 6 – Extra Flavor**
- [ ] Add modes (Cynical Mode, Shakespearean Mode, Preacher Mode).
- [ ] Add history log (list of unethical requests + rants).
- [ ] Show “Morality Score” on screen.
**Deliverable:** Quirky, memorable extras.

---

### **Day 7 – Polish & Demo**
- [ ] Fix bugs (input clearing, text overlap, etc.).
- [ ] Clean UI (fonts, colors, layout).
- [ ] Record a short demo video (screen recording).
**Deliverable:** Finished MVP, demo-ready.

---

## 🚀 Tech Shortcuts
- Use keyword detection + rant templates first.
- If you have time: integrate GPT API for infinite variety in rants.
- TailwindCSS for quick styling.
- Focus on local demo before worrying about deployment.
