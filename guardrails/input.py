from agents import RunContextWrapper, Agent, GuardrailFunctionOutput, input_guardrail, Runner
from pydantic import BaseModel
from my_config.gemini_confg import MODEL
# ✅ Define structure for checking if the input is valid
class InputCheck(BaseModel):
    is_related: bool
    reason: str

# ✅ Small helper agent that classifies user queries
input_guardrail_agent = Agent(
    name="Input Relevance Checker",
    instructions=(
       """
You are a guardrail that checks whether a user's question is related to pet health or care.
If the question is about animals, pets, or their health — mark it as VALID.
If it is not about pets, mark it as INVALID.

Output JSON strictly in this format:
{"is_pet_related": true or false}
"""

    ),
    output_type=InputCheck,
    model=MODEL
)

@input_guardrail
async def input_pet_Guardrail(ctx: RunContextWrapper, agent: Agent, inputMessage: str) -> GuardrailFunctionOutput:
    print("🧱 Input guardrail triggered with message:", inputMessage)

    result = await Runner.run(input_guardrail_agent, inputMessage, context=ctx.context)

    # If not related, tripwire triggers (stops main agent)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_related
    )
