from llm_utils.templates import generate_mock_chain
from llm_utils.templates import example
from models.Project import ProjectBase

def generate_mock_data(project: ProjectBase, nor: int):
    result = []
    required_rows = nor
    generated_rows = 0

    api_calls = 0

    chain_params = {
        'columns': project.jsonListString(),
        'nor': nor,
        'example_fields': example["fields"],
        'example_generated_answer': example["generated_answer"]

    }
    while 1 < required_rows + 1:
        generated_batch_string = generate_mock_chain.invoke(chain_params)
        api_calls += 1
        generated_batch_list = generated_batch_string.strip().split('<|eot_id|>')[0].strip().split('\n')[1:]
        print(len(generated_batch_list))
        required_rows -= len(generated_batch_list)
        chain_params['nor'] = required_rows
        result.extend([elem.split(',') for elem in generated_batch_list])
    
    print("API Calls: ", api_calls)
    field_names = project.getFieldNames()
    result.insert(0, field_names)
    return result



    