import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scripts.dispatcher import UKArchitectDispatcher  # noqa: E402


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input:
            return

        input_data = json.loads(raw_input)
        tool_name = input_data.get("tool")
        arguments = input_data.get("arguments", {})

        dispatcher = UKArchitectDispatcher()

        if tool_name == "load_sub_skill":
            result = dispatcher.load_sub_skill(arguments.get("skill_id"))
        elif tool_name in {"run_uk_calculator", "run_hk_calculator"}:
            result = dispatcher.run_uk_calculator(
                arguments.get("calc_type"),
                arguments.get("data"),
            )
        else:
            result = {"error": f"Unknown tool: {tool_name}"}

        sys.stdout.write(json.dumps(result))

    except Exception as e:
        sys.stdout.write(json.dumps({"error": f"Dispatcher Error: {str(e)}"}))


if __name__ == "__main__":
    main()
