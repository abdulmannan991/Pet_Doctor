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
    instructions="Check if the output message includes any math expression. "
                 "If it does, set is_Output to False. Otherwise, True. "
                 "Provide a brief summary in one line.",
    output_type=OutputData,
    model=MODEL
)


@output_guardrail
async def output_pet_guardrail(ctx: RunContextWrapper, agent: Agent, output_message: MessageOutput) -> GuardrailFunctionOutput:
    print("✅ Output guardrail triggered with:", output_message)

    result = await Runner.run(output_guardrail_agent, output_message, context=ctx.context)

    return GuardrailFunctionOutput(
    output_info=result.final_output,
    tripwire_triggered=result.final_output.is_Output == False
)
