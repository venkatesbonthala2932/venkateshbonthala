user_prompt=input("what would you like me to do?")
if "hack" in user_prompt or "steal" in user_prompt or "illegal" in user_prompt:
    print("AI Guardrail Triggered: I cannot assist with illegal activities.")
else:
    print("Processing your request: ", user_prompt)
