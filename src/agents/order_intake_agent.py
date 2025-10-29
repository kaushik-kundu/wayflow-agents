
from wayflowcore.agent import Agent
from wayflowcore.executors.executionstatus import (
    FinishedStatus,
    UserMessageRequestStatus,
)
from wayflowcore.tools import tool
from wayflowcore.models import OCIGenAIModel
from src.llm.oci_genai import initialize_llm
from src.system_prompts.order_intake_agent_prompts import prompt_order_intake_agent
from src.tools.vision_instruct_tools import test_image_to_text
import os

def order_intake():

    llm = initialize_llm()

    ###### Define Wayflow Tools- #########

    @tool(description_mode="only_docstring")
    def voice_to_text(query: str) -> str:
        """Tool that is invoked for a audio .mp3 file detailing the order, and returns the tool name.

        Parameters
        ----------
        query:
            file type

        Returns
        -------
            tool name

        """
        return 'voice_to_text'

    @tool(description_mode="only_docstring")
    def image_to_text(query: str) -> str:
        """Tool that is invoked for a image .jpg file detailing the order, and returns the tool name.

        Parameters
        ----------
        query:
            file type

        Returns
        -------
            tool name

        """
        return 'image_to_text'

    order_intake_agent_instructions = prompt_order_intake_agent.strip()

    assistant = Agent(
        custom_instruction=order_intake_agent_instructions,
        tools=[voice_to_text, image_to_text], 
        llm=llm
    )

    # print("What is the file name?")
    # filename = input()
    # Assume filename is orderhub_handwritten.jpg

    filename = "orderhub_handwritten.jpg"
    print(f"---\nfilename >>> {filename}\n---")

    root, extension = os.path.splitext(filename)
    # print(f"File extension: {extension}")

    conversation = assistant.start_conversation()

    conversation.append_user_message(extension)
    status = conversation.execute()
    if isinstance(status, UserMessageRequestStatus):
        assistant_reply = conversation.get_last_message()
        print(f"---\nOrder Intake Tool >>> {assistant_reply.content}\n---")
    else:
        print(f"Invalid execution status, expected UserMessageRequestStatus, received {type(status)}")


    if assistant_reply.content == 'image_to_text':
        # print("It is now image_to_text")
        response = test_image_to_text()
        print(response)

if __name__ == "__main__":
    order_intake()
