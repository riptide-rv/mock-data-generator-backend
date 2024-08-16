from langchain.prompts import PromptTemplate
from llm_utils.config import llm

example = {
    
    'fields':"""Generate 6(no of rows) mock csv data for given fields:
{{
    'name': 'Name',
    'Description':'Name of the student'
    'type':'String'
}},

{{
    'name': 'Rollno',
    'Description':'Roll no of the Student'
    'type':'Integer'
    'range':'10 to 20'
}},

{{
    'name': 'UUID',
    'Description':'A UUID value'
    'type':'String'
    'range':'UUID values'
}},

{{
    'name': 'Sex',
    'Description':'Sex of the student'
    'type':'ENUM'
    'range':'M, F, Other'
}},

{{
    'name': 'Age',
    'Description':'Age of the student'
    'type':'Integer'
    'range':'18 to 30'
}}""",
    
    'generated_answer':" \nName,Rollno,UUID,Sex,Age\nJohn Doe,11,123e4567-e89b-12d3-a456-426614174000,M,20\nJane Smith,14,223e4567-e89b-12d3-a456-426614174001,F,22\nAlice Johnson,18,323e4567-e89b-12d3-a456-426614174002,Female,25\nBob Brown,16,423e4567-e89b-12d3-a456-426614174003,Other,28\nCharlie Davis,13,523e4567-e89b-12d3-a456-426614174004,M,30\n"
}

prompt ="""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a AI Tool that takes in field names and no of rows as input and generates mock csv data as output. The result contains only the generated csv and no other words.Each field is specified in the following format:

{{
    'name': 'Name of the Field',
    'Description':'A small Description of the field'
    'type':'The type of field'
    'range':'The range of allowed values'
}}
<|eot_id|>
<|start_header_id|>user<|end_header_id|>
{example_fields}<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
The generated csv data: {example_generated_answer}<|eot_id|>
<|start_header_id|>user<|end_header_id|>
Generate {nor}(no of rows) mock csv data for given fields:

{columns}<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
The generated csv data:
"""
generate_mock_template = PromptTemplate.from_template(prompt)
generate_mock_chain = generate_mock_template | llm