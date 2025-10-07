from agents import RunContextWrapper, Agent, GuardrailFunctionOutput, output_guardrail, Runner
from pydantic import BaseModel
# from my_agent.output_guardrail import output_guardrail_agent
from my_config.gemini_confg import MODEL

class MessageOutput(BaseModel):
    response: str


class OutputData(BaseModel):
    is_Output: bool   # True if allowed, False if flagged
    summary: str      # Summary or reason text


output_guardrail_agent = Agent(
    name="Guardrail Check",
    instructions="""You are an output guardrail for a veterinary assistant AI.

Check the assistant’s final message.  
If the response is:
- Relevant to pet health, animals, or veterinary guidance,
- Safe (no harmful advice or human medication for pets),
- And does NOT contain unrelated or math content,

Then output: {"is_Output": true}

Otherwise, if the answer is off-topic, unsafe, or irrelevant,
output: {"is_Output": false}

Respond ONLY in JSON — no explanations.
""",
    output_type=OutputData,
    model=MODEL
)


@output_guardrail
async def output_pet_guardrail(ctx: RunContextWrapper, agent: Agent, output_message: MessageOutput) -> GuardrailFunctionOutput:
    print("✅ Output guardrail triggered with:", output_message)

    result = await Runner.run(output_guardrail_agent, output_message, context=ctx.context)

    return GuardrailFunctionOutput(
    output_info=result.final_output,
    tripwire_triggered = not getattr(result.final_output, "is_Output", False)


)
