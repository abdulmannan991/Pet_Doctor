from agents import Agent
from my_config.gemini_confg import MODEL
from Dynamic_instruction.dynamic_instruction import dynamic_instructions
from guardrails.input import input_pet_Guardrail
from guardrails.output import output_pet_guardrail

Pet_Agent = Agent(
    name="pet Medical Assistant",
    instructions=dynamic_instructions,
    model=MODEL,
    output_guardrails=[output_pet_guardrail],
    input_guardrails=[input_pet_Guardrail]
  

   
)
