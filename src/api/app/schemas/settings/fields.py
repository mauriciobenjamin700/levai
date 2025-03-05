from pydantic import Field


content_field:str = Field(
    title="Content",
    description="The content of the message.",
    examples=["why is the sky blue?"]
)
context_field: list = Field(
    title="Context",
    description="The context used to generate the response.",
    examples=[["build an AI that can generate text"]]
)
created_at_field: str = Field(
        title="Created At",
        description="The date and time when the response was created.",
        examples=["2021-07-27T20:00:00Z"]
)
done_field: bool = Field(
    title="Done",
    description="if the answer has been completed",
    examples=[True]
)
eval_count_field: int = Field(
    title="Eval Count",
    description="The number of evaluations of the response.",
    examples=[44]
)
eval_duration_field: int = Field(
    title="Eval Duration",
    description="The duration of evaluating the response in milliseconds.",
    examples=[736432000]
)
load_duration_field: int = Field(
    title="Load Duration",
    description="The duration of loading the model in milliseconds.",
    examples=[2559292]
)
messages: list = Field(
    title="Messages",
    description="The messages in the chat.",
    examples=[[{ "role": "user", "content": "why is the sky blue?" }]]
)
model_field: str = Field(
        default="deepseek-r1",
        title="Model",
        description="The model used to generate the response.",
        examples=["llava"]
)
prompt_eval_count_field: int = Field(
    title="Prompt Eval Count",
    description="The number of evaluations of the prompt.",
    examples=[1]
)
prompt_eval_duration_field: int = Field(
    title="Prompt Eval Duration",
    description="The duration of evaluating the prompt in milliseconds.",
    examples=[2195557000]
)
prompt_field: str = Field(
    title="Prompt",
    description="The prompt used to generate the response.",
    examples=["Build an AI that can generate text."]
)
response_field: str =  Field(
    title="Response",
    description="The response generated by the model.",
    examples=["I am a llama."]
)
total_duration_field: int = Field(
    title="Total Duration",
    description="The total duration of the request in milliseconds.",
    examples=[2938432250]
)
role_field: str = Field(
    title="Role",
    description="The role of the message.",
    examples=["user"]
)