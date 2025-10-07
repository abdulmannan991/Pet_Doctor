from agents import Runner,set_tracing_disabled
from my_agent.pet_agent import Pet_Agent
set_tracing_disabled(True)

test_inputs = [
    "My dog has fever, what should I do?",
    "Calculate 5 + 7",
]

def run_test():
    for i, query in enumerate(test_inputs, 1):
        print(f"\n=== TEST {i}: '{query}' ===")

        try:
            result = Runner.run_sync(Pet_Agent, query)
            print("\n--- RESULT ---")
            print("Final Output:", result.final_output)
            print("----------------------------")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run_test()
