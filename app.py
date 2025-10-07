import chainlit as cl
from agents import Runner
from my_agent.pet_agent import Pet_Agent  

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Hello! I'm your **Pet Health Assistant**.\n\nHow can I assist you regarding your pet today? 🐶🐱"
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    await cl.Message(content=f"🧠 Processing: {user_input}").send()

    try:
        
        result = await Runner.run(Pet_Agent, user_input)
        final_output = getattr(result, "final_output", result)

       
        if hasattr(final_output, "response"):
            response_text = final_output.response
        elif isinstance(final_output, str):
            response_text = final_output
        else:
            response_text = str(final_output)

        await cl.Message(content=response_text).send()

    except Exception as e:
        error_msg = str(e).lower()

        # Custom friendly response for guardrail triggers
        if "guardrail" in error_msg or "tripwire" in error_msg:
            fallback = "⚠️ Sorry, I can’t respond to unrelated or restricted questions."
        else:
            fallback = f"❌ An unexpected error occurred: {str(e)}"

        await cl.Message(content=fallback).send()
